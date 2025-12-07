"""Utility script to generate embeddings."""

import argparse
import json
import os
import time
from typing import Callable, Dict
from pathlib import Path
import requests

from llama_stack_client.types.shared_params.document import Document as RAGDocument
from llama_stack.core.library_client import LlamaStackAsLibraryClient


PROVIDER_NAME = "vector_io"
UNREACHABLE_DOCS: int = 0


class SourceDocument:
    path: str
    metadata: Dict

    def __init__(self, path: Path, metadata: Dict):
        self.path = path
        self.metadata = metadata


class DocumentIngestionTool:

    def __init__(
        self,
        folder: Path,
        chunk,
        index,
        vector_db_id_file_name: str,
        skip_ping=False,
        additional_docs_folder: Path | None = None,
        extra_docs_folder: Path | None = None,
    ):
        self.folder = folder
        self.additional_docs_folder = additional_docs_folder
        self.chunk = chunk
        self.index = index
        self.skip_ping = skip_ping
        self.extra_docs_folder = extra_docs_folder

        self.client, self.vector_dbs_identifier = self.setup_llama_stack()
        with open(vector_db_id_file_name, "w") as fp:
            fp.write(str(self.vector_dbs_identifier))

    def setup_llama_stack(self):
        client = LlamaStackAsLibraryClient(
            "./run.yaml",
            # provider_data is optional, but if you need to pass in any provider specific data, you can do so here.
            provider_data={},
        )
        client.initialize()

        vector_providers = [
            provider
            for provider in client.providers.list()
            if provider.api == PROVIDER_NAME
        ]
        provider_id = vector_providers[
            0
        ].provider_id  # Use the first available vector provider

        # Register a vector database
        result = client.vector_dbs.register(
            vector_db_id=self.index,
            provider_id=provider_id,
            embedding_model="sentence-transformers/embeddings_model",
            embedding_dimension=768,
        )

        return client, result.identifier

    def ping_url(self, url: str) -> bool:
        """Check if the URL parameter is live."""
        try:
            response = requests.get(url, timeout=30)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def get_file_title(self, file_path: Path) -> str:
        """Extract title from the plaintext doc file."""
        if not file_path.exists():
            return ""
        file_content = file_path.read_text(encoding="utf8")
        return file_content.split("\n")[0].lstrip("# ")

    def file_metadata_func(
        self,
        file_path: str,
        docs_url_func: Callable[[str], str],
        docs_title_func: Callable[[str], str],
    ) -> Dict:
        """Populate the docs_url and title metadata elements with docs URL and the page's title.

        Args:
            file_path: str: file path in str
            docs_url_func: Callable[[str], str]: lambda for the docs_url
        """
        docs_url = docs_url_func(file_path)
        title = docs_title_func(file_path)
        msg = f"{file_path=}, {title=}, {docs_url=}"
        if not self.skip_ping and not self.ping_url(docs_url):
            global UNREACHABLE_DOCS
            UNREACHABLE_DOCS += 1
            msg += ", UNREACHABLE"
        print(msg)
        return {"docs_url": docs_url, "title": title}

    def aap_file_metadata_func(self, md_path: Path) -> Dict:
        """Populate metadata for an AAP docs page.

        Args:
            file_path: str: file path in str
        """
        metadata_path = Path(md_path.parent / ".metadata" / f"{md_path.stem}.json")
        metadata = json.loads(metadata_path.read_text(encoding="utf8"))
        docs_url = lambda x: metadata["url"]
        docs_title = lambda x: metadata["title"]
        return self.file_metadata_func(md_path, docs_url, docs_title)

    def additional_docs_metadata_func(self, file_path: Path) -> Dict:
        """Populate metadata for additional docs.

        Args:
            file_path: str: file path in str
        """
        metadata_path = file_path.parent / ".metadata" / f"{file_path.stem}.json"
        if metadata_path.exists():
            metadata = json.loads(metadata_path.read_text(encoding="utf8"))
            docs_url = lambda x: metadata["url"]
            return self.file_metadata_func(file_path, docs_url, self.get_file_title)

        AAP_RAG_CONTENT_BASE_URL = (
            "https://github.com/ansible/aap-rag-content/blob/main/"
        )
        docs_url = AAP_RAG_CONTENT_BASE_URL + str(file_path)

        title = self.get_file_title(file_path)
        print(f"{file_path=}, {title=}, {docs_url=}")
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
            content = doc.path.read_text(encoding="utf8")
            rag_documents.append(
                RAGDocument(
                    document_id=f"{prefix}-{i}",
                    content=content,
                    mime_type="text/plain",
                    metadata=doc.metadata,
                )
            )
            if len(rag_documents) >= batch_size or len(rag_documents) + count == len(
                documents
            ):
                count += len(rag_documents)
                print(f"{count=}")
                self.client.tool_runtime.rag_tool.insert(
                    documents=rag_documents,
                    vector_db_id=self.vector_dbs_identifier,
                    chunk_size_in_tokens=self.chunk,
                )
                rag_documents = []

    def run(self):
        """Ingest product documentation and additional documents."""
        start_time = time.time()

        # Load documents
        documents = [
            SourceDocument(f, self.aap_file_metadata_func(f))
            for f in self.folder.rglob("*.md")
        ]
        self.insert_documents(documents, "doc")

        if self.additional_docs_folder:
            additional_docs = [
                SourceDocument(f, self.additional_docs_metadata_func(f))
                for f in self.additional_docs_folder.rglob("*.txt")
            ]
            self.insert_documents(additional_docs, "additional_doc")

        if self.extra_docs_folder:
            extra_docs = [
                SourceDocument(f, self.additional_docs_metadata_func(f))
                for f in self.extra_docs_folder.rglob("*.txt")
            ]
            self.insert_documents(extra_docs, "extra_doc")

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
    parser.add_argument("-f", "--folder", type=Path, help="Plain text folder path")
    parser.add_argument(
        "--additional-docs-folder", type=Path, help="Addional_doc path", default=None
    )
    parser.add_argument(
        "-c", "--chunk", type=int, default=380, help="Chunk size for embedding"
    )
    parser.add_argument("-i", "--index", help="Product index")
    parser.add_argument(
        "--skip-ping", action="store_true", help="Skip URL existence check"
    )
    parser.add_argument(
        "--extra-docs-folder",
        type=Path,
        help="Folder that stores extra docs to be added to the existing DB",
        default=None,
    )
    parser.add_argument("-v", "--vector-db-id-file-path", type=Path, help="Plain provider_vector_db_id file name")

    args = parser.parse_args()
    print(f"Arguments used: {args}")
    if not args.folder.is_dir():
        print("--folder must point on a valid directory")
        exit(1)
    if not args.additional_docs_folder:
        print("--additional-docs-folder was not set")
    if args.additional_docs_folder and not args.additional_docs_folder.is_dir():
        print(f"{args.additional_docs_folder=} doesn't exist!")
        exit(1)
    if args.extra_docs_folder and not args.extra_docs_folder.is_dir():
        print("--extra-docs-folder must point on a valid directory")
        exit(1)

    DocumentIngestionTool(
        args.folder, args.chunk, args.index, args.vector_db_id_file_path, args.skip_ping, args.additional_docs_folder, args.extra_docs_folder
    ).run()


if __name__ == "__main__":
    main()
