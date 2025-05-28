"""Utility script to generate embeddings."""
import argparse
import json
import os
import time
from typing import Callable, Dict
from pathlib import Path
import requests

from llama_stack_client.types.shared_params.document import Document as RAGDocument
from llama_stack.distribution.library_client import LlamaStackAsLibraryClient


UNREACHABLE_DOCS: int = 0
ADDITIONAL_DOCS_DIR = "additional_docs"

class SourceDocument:
    path: str
    metadata: Dict

    def __init__(self, path: str, metadata: Dict):
        self.path = path
        self.metadata = metadata


class DocumentIngestionTool:

    def __init__(self, folder, chunk, index, skip_ping=False):
        self.folder = folder
        self.chunk = chunk
        self.index = index
        self.skip_ping = skip_ping

        self.client = self.setup_llama_stack()

    def setup_llama_stack(self):
        client = LlamaStackAsLibraryClient(
            "./run.yaml",
            # provider_data is optional, but if you need to pass in any provider specific data, you can do so here.
            provider_data={},
        )
        client.initialize()

        vector_providers = [
            provider for provider in client.providers.list() if provider.api == "vector_io"
        ]
        provider_id = vector_providers[0].provider_id  # Use the first available vector provider

        # Register a vector database
        client.vector_dbs.register(
            vector_db_id=self.index,
            provider_id=provider_id,
            embedding_model="all-MiniLM-L6-v2",
            embedding_dimension=384,
        )
        return client

    def ping_url(self, url: str) -> bool:
        """Check if the URL parameter is live."""
        try:
            response = requests.get(url, timeout=30)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False


    def get_file_title(self, file_path: str) -> str:
        """Extract title from the plaintext doc file."""
        title = ""
        try:
            with open(file_path, encoding="utf8") as infile:
                title = infile.readline().rstrip("\n").lstrip("# ")
        except Exception:  # noqa: S110
            pass
        return title


    def file_metadata_func(
            self,
            file_path: str,
            docs_url_func: Callable[[str], str],
            docs_title_func: Callable[[str], str])-> Dict:
        """Populate the docs_url and title metadata elements with docs URL and the page's title.

        Args:
            file_path: str: file path in str
            docs_url_func: Callable[[str], str]: lambda for the docs_url
        """
        docs_url = docs_url_func(file_path)
        title = docs_title_func(file_path)
        msg = f"file_path: {file_path}, title: {title}, docs_url: {docs_url}"
        if not self.skip_ping and not self.ping_url(docs_url):
            global UNREACHABLE_DOCS
            UNREACHABLE_DOCS += 1
            msg += ", UNREACHABLE"
        print(msg)
        return {"docs_url": docs_url, "title": title}

    def aap_file_metadata_func(self, file_path: str) -> Dict:
        """Populate metadata for an AAP docs page.

        Args:
            file_path: str: file path in str
        """
        full_path = os.path.abspath(file_path)
        i = full_path.rindex("/")
        metadata_path = Path(full_path[:i]).joinpath(".metadata") \
            .joinpath(full_path[(i+1):].replace(".md", ".json"))
        with open(metadata_path, encoding="utf8") as f:
            metadata = json.load(f)
            docs_url = lambda x: metadata["url"]
            docs_title = lambda x: metadata["title"]
        return self.file_metadata_func(file_path, docs_url, docs_title)

    def additional_docs_metadata_func(self, file_path: str) -> Dict:
        """Populate metadata for additional docs.

        Args:
            file_path: str: file path in str
        """
        full_path = os.path.abspath(file_path)
        i = full_path.rindex("/")
        metadata_path = Path(full_path[:i]).joinpath(".metadata") \
            .joinpath(full_path[(i+1):].replace(".txt", ".json"))

        if metadata_path.exists():
            with open(metadata_path, encoding="utf8") as f:
                metadata = json.load(f)
                docs_url = lambda x: metadata["url"]
            return self.file_metadata_func(file_path, docs_url, self.get_file_title)

        AAP_RAG_CONTENT_BASE_URL = "https://github.com/ansible/aap-rag-content/blob/main/"
        docs_url = AAP_RAG_CONTENT_BASE_URL + str(file_path)

        title = self.get_file_title(file_path)
        msg = f"file_path: {file_path}, title: {title}, docs_url: {docs_url}"
        print(msg)
        return {"docs_url": docs_url, "title": title}

    def insert_documents(self, documents: list[SourceDocument], prefix: str):
        """
        Insert the documents into the vector database.
        :param documents:
        :param prefix:
        :return:
        """
        rag_documents = []
        count = 0
        batch_size = 100
        for i, doc in enumerate(documents):
            with open(doc.path) as f:
                content = f.read()
                rag_documents.append(
                    RAGDocument(
                        document_id=f"{prefix}-{i}",
                        content=content,
                        mime_type="text/plain",
                        metadata=doc.metadata,
                    )
                )
                if len(rag_documents) >= batch_size or len(rag_documents) + count == len(documents):
                    count += len(rag_documents)
                    print(f"count={count}")
                    self.client.tool_runtime.rag_tool.insert(
                        documents=rag_documents,
                        vector_db_id=self.index,
                        chunk_size_in_tokens=self.chunk,
                    )
                    rag_documents = []

    def run(self):
        """ Ingest product documentation and additional documents. """
        start_time = time.time()

        # Load documents
        input_files = list(Path(self.folder).rglob("*.md"))
        documents = [
            SourceDocument(f, self.aap_file_metadata_func(f))
            for f in input_files
        ]
        self.insert_documents(documents, "doc")

        additional_input_files = list((Path(self.folder) / "../additional_docs").rglob("*.txt"))
        additional_docs = [
            SourceDocument(f, self.additional_docs_metadata_func(f))
            for f in additional_input_files
        ]
        self.insert_documents(additional_docs, "additional_doc")

        if UNREACHABLE_DOCS > 0:
            print(
                "WARNING:\n"
                f"There were documents with {UNREACHABLE_DOCS} unreachable URLs, "
                "grep the log for UNREACHABLE.\n"
                "Please update the plain text."
            )

        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.2f} secs")

def main():
    parser = argparse.ArgumentParser(description="embedding cli for task execution")
    parser.add_argument("-f", "--folder", help="Plain text folder path")
    parser.add_argument("-c", "--chunk", type=int, default=380, help="Chunk size for embedding")
    parser.add_argument("-i", "--index", help="Product index")
    parser.add_argument("--skip-ping", action="store_true", help="Skip URL existence check")

    args = parser.parse_args()
    print(f"Arguments used: {args}")

    DocumentIngestionTool(args.folder, args.chunk,  args.index, args.skip_ping).run()


if __name__ == "__main__":
    main()