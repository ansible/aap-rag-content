"""Utility script to generate embeddings."""

import argparse
import json
import time
from pathlib import Path
from typing import Callable
from typing import Dict

import requests
from llama_stack.distribution.library_client import LlamaStackAsLibraryClient
from llama_stack_client.types.shared_params.document import Document as RAGDocument

PROVIDER_NAME = "vector_io"
UNREACHABLE_DOCS: int = 0


class SourceDocument:
    """Represents a source document with path and metadata."""

    def __init__(self, path: Path, metadata: Dict[str, str]):
        """Initialize SourceDocument with path and metadata.

        Args:
            path: Path to the source document file
            metadata: Dictionary containing document metadata
        """
        self.path: Path = path
        self.metadata: Dict[str, str] = metadata


def setup_llama_stack(index: str) -> LlamaStackAsLibraryClient:
    """Set up LlamaStack client and register vector database."""
    client = LlamaStackAsLibraryClient(
        "./run.yaml",
        # provider_data is optional, but if you need to pass in any provider
        # specific data, you can do so here.
        provider_data={},
    )
    client.initialize()

    vector_providers = [
        provider for provider in client.providers.list() if provider.api == PROVIDER_NAME
    ]
    provider_id = vector_providers[0].provider_id  # Use the first available vector provider

    # Register a vector database
    client.vector_dbs.register(
        vector_db_id=index,
        provider_id=provider_id,
        embedding_model="./embeddings_model",
        embedding_dimension=768,
    )
    return client


def ping_url(url: str) -> bool:
    """Check if the URL parameter is live."""
    try:
        response = requests.get(url, timeout=30)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def get_file_title(file_path: Path) -> str:
    """Extract title from the plaintext doc file."""
    if not file_path.exists():
        return ""
    content = file_path.read_text(encoding="utf8")
    if content:
        first_line = content.split("\n")[0]
        return first_line.rstrip("\n").lstrip("# ")
    return ""


def file_metadata_func(
    file_path: str,
    docs_url_func: Callable[[str], str],
    docs_title_func: Callable[[str], str],
    skip_ping: bool = False,
) -> Dict[str, str]:
    """Populate the docs_url and title metadata elements with docs URL and the page's title.

    Args:
        file_path: str: file path in str
        docs_url_func: Callable[[str], str]: lambda for the docs_url
        docs_title_func: Callable[[str], str]: lambda for the title
        skip_ping: bool: whether to skip URL ping check
    """
    docs_url = docs_url_func(file_path)
    title = docs_title_func(file_path)
    msg = f"{file_path=}, {title=}, {docs_url=}"
    if not skip_ping and not ping_url(docs_url):
        global UNREACHABLE_DOCS
        UNREACHABLE_DOCS += 1
        msg += ", UNREACHABLE"
    print(msg)
    return {"docs_url": docs_url, "title": title}


def aap_file_metadata_func(md_path: Path, skip_ping: bool = False) -> Dict[str, str]:
    """Populate metadata for an AAP docs page.

    Args:
        md_path: Path: path to the markdown file
        skip_ping: bool: whether to skip URL ping check
    """
    metadata_path = Path(md_path.parent / ".metadata" / f"{md_path.stem}.json")
    metadata = json.loads(metadata_path.read_text(encoding="utf8"))

    def docs_url(x: str) -> str:
        return metadata["url"]

    def docs_title(x: str) -> str:
        return metadata["title"]

    return file_metadata_func(str(md_path), docs_url, docs_title, skip_ping)


def additional_docs_metadata_func(file_path: Path, skip_ping: bool = False) -> Dict[str, str]:
    """Populate metadata for additional docs.

    Args:
        file_path: Path: path to the file
        skip_ping: bool: whether to skip URL ping check
    """
    metadata_path = file_path.parent / ".metadata"
    if metadata_path.exists() and metadata_path.is_file():
        metadata = json.loads(metadata_path.read_text(encoding="utf8"))

        def docs_url(x: str) -> str:
            return metadata["url"]

        def docs_title(x: str) -> str:
            return get_file_title(file_path)

        return file_metadata_func(str(file_path), docs_url, docs_title, skip_ping)

    aap_rag_content_base_url = "https://github.com/ansible/aap-rag-content/blob/main/"
    docs_url = aap_rag_content_base_url + str(file_path)

    title = get_file_title(file_path)
    print(f"{file_path=}, {title=}, {docs_url=}")
    return {"docs_url": docs_url, "title": title}


def insert_documents(
    client: LlamaStackAsLibraryClient,
    documents: list[SourceDocument],
    prefix: str,
    index: str,
    chunk: int,
) -> None:
    """Insert the documents into the vector database.

    Args:
        client: LlamaStack client instance
        documents: list of SourceDocument objects
        prefix: document ID prefix
        index: vector database index
        chunk: chunk size in tokens
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
        if len(rag_documents) >= batch_size or len(rag_documents) + count == len(documents):
            count += len(rag_documents)
            print(f"{count=}")
            client.tool_runtime.rag_tool.insert(
                documents=rag_documents,
                vector_db_id=index,
                chunk_size_in_tokens=chunk,
            )
            rag_documents = []


def run_document_ingestion(
    folder: Path,
    chunk: int,
    index: str,
    skip_ping: bool = False,
    additional_docs_folder: Path | None = None,
    extra_docs_folder: Path | None = None,
) -> None:
    """Ingest product documentation and additional documents.

    Args:
        folder: Path to the main documentation folder
        chunk: chunk size in tokens
        index: vector database index
        skip_ping: whether to skip URL ping check
        additional_docs_folder: Path to additional docs folder
        extra_docs_folder: Path to extra docs folder
    """
    start_time = time.time()

    # Setup LlamaStack client
    client = setup_llama_stack(index)

    # Load documents
    documents = [
        SourceDocument(f, aap_file_metadata_func(f, skip_ping)) for f in folder.rglob("*.md")
    ]
    insert_documents(client, documents, "doc", index, chunk)

    if additional_docs_folder:
        additional_docs = [
            SourceDocument(f, additional_docs_metadata_func(f, skip_ping))
            for f in additional_docs_folder.rglob("*.txt")
        ]
        insert_documents(client, additional_docs, "additional_doc", index, chunk)

    if extra_docs_folder:
        extra_docs = [
            SourceDocument(f, additional_docs_metadata_func(f, skip_ping))
            for f in extra_docs_folder.rglob("*.txt")
        ]
        insert_documents(client, extra_docs, "extra_doc", index, chunk)

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
    """Parse arguments and run document ingestion."""
    parser = argparse.ArgumentParser(description="embedding cli for task execution")
    parser.add_argument("-f", "--folder", type=Path, help="Plain text folder path")
    parser.add_argument(
        "--additional-docs-folder", type=Path, help="Addional_doc path", default=None
    )
    parser.add_argument("-c", "--chunk", type=int, default=380, help="Chunk size for embedding")
    parser.add_argument("-i", "--index", help="Product index")
    parser.add_argument("--skip-ping", action="store_true", help="Skip URL existence check")
    parser.add_argument(
        "--extra-docs-folder",
        type=Path,
        help="Folder that stores extra docs to be added to the existing DB",
        default=None,
    )

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

    run_document_ingestion(
        folder=args.folder,
        chunk=args.chunk,
        index=args.index,
        skip_ping=args.skip_ping,
        additional_docs_folder=args.additional_docs_folder,
        extra_docs_folder=args.extra_docs_folder,
    )


if __name__ == "__main__":
    main()
