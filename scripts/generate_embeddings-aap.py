"""Utility script to generate embeddings."""
# pylint: disable=C0103,C3001,E0401,E0606,W0603,W0718
import argparse
import json
import os
import time
import traceback
from pathlib import Path
from typing import Callable
from typing import Dict

import faiss
import requests
import torch
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.core.llms.utils import resolve_llm
from llama_index.core.schema import TextNode
from llama_index.core.storage.storage_context import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.vector_stores.postgres import PGVectorStore

# from llama_index.core.node_parser import MarkdownNodeParser

AAP_DOCS_ROOT_URL = "https://github.com/ansible/aap-docs/blob/"
AAP_DOCS_VERSION = "2.5"
UNREACHABLE_DOCS: int = 0

ADDITIONAL_DOCS_DIR = "additional_docs"


def ping_url(url: str) -> bool:
    """Check if the URL parameter is live."""
    try:
        response = requests.get(url, timeout=30)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def get_file_title(file_path: str) -> str:
    """Extract title from the plaintext doc file."""
    title = ""
    try:
        with open(file_path, encoding="utf8") as infile:
            title = infile.readline().rstrip("\n").lstrip("# ")
    except Exception:  # noqa: S110
        pass
    return title


def file_metadata_func(file_path: str, docs_url_func: Callable[[str], str], docs_title_func: Callable[[str], str])-> Dict:
    """Populate the docs_url and title metadata elements with docs URL and the page's title.

    Args:
        file_path: str: file path in str
        docs_url_func: Callable[[str], str]: lambda for the docs_url
    """
    docs_url = docs_url_func(file_path)
    title = docs_title_func(file_path)
    msg = f"file_path: {file_path}, title: {title}, docs_url: {docs_url}"
    if not ping_url(docs_url):
        global UNREACHABLE_DOCS
        UNREACHABLE_DOCS += 1
        msg += ", UNREACHABLE"
    print(msg)
    return {"docs_url": docs_url, "title": title}


def aap_file_metadata_func(file_path: str) -> Dict:
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
    return file_metadata_func(file_path, docs_url, docs_title)

def additional_docs_metadata_func(file_path: str) -> Dict:
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
        return file_metadata_func(file_path, docs_url, get_file_title)

    AAP_RAG_CONTENT_BASE_URL = "https://github.com/ansible/aap-rag-content/blob/main/"
    docs_url = AAP_RAG_CONTENT_BASE_URL + str(file_path)

    title = get_file_title(file_path)
    msg = f"file_path: {file_path}, title: {title}, docs_url: {docs_url}"
    print(msg)
    return {"docs_url": docs_url, "title": title}

def got_whitespace(text: str) -> bool:
    """Indicate if the parameter string contains whitespace."""
    for c in text:
        if c.isspace():
            return True
    return False


if __name__ == "__main__":
    start_time = time.time()

    parser = argparse.ArgumentParser(description="embedding cli for task execution")
    parser.add_argument("-f", "--folder", help="Plain text folder path")
    parser.add_argument(
        "-md",
        "--model-dir",
        default="embeddings_model",
        help="Directory containing the embedding model",
    )
    parser.add_argument(
        "-mn",
        "--model-name",
        help="HF repo id of the embedding model",
    )
    parser.add_argument("-c", "--chunk", type=int, default=380, help="Chunk size for embedding")
    parser.add_argument("-l", "--overlap", type=int, default=0, help="Chunk overlap for embedding")
    parser.add_argument(
        "-em",
        "--exclude-metadata",
        nargs="+",
        default=None,
        help="Metadata to be excluded during embedding",
    )
    parser.add_argument("-o", "--output", help="Vector DB output folder")
    parser.add_argument("-i", "--index", help="Product index")
    parser.add_argument("-v", "--aap-version", help="AAP version")
    parser.add_argument(
        "--vector-store-type",
        default="faiss",
        choices=["faiss", "postgres"],
        help="vector store type to be used."
    )
    args = parser.parse_args()
    print(f"Arguments used: {args}")

    # OLS-823: sanitize directory
    PERSIST_FOLDER = os.path.normpath("/" + args.output).lstrip("/")
    if PERSIST_FOLDER == "":
        PERSIST_FOLDER = "."

    EMBEDDINGS_ROOT_DIR = os.path.abspath(args.folder)
    if EMBEDDINGS_ROOT_DIR.endswith("/"):
        EMBEDDINGS_ROOT_DIR = EMBEDDINGS_ROOT_DIR[:-1]

    AAP_DOCS_VERSION = args.aap_version

    os.environ["HF_HOME"] = args.model_dir
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    Settings.chunk_size = args.chunk
    Settings.chunk_overlap = args.overlap
    Settings.embed_model = HuggingFaceEmbedding(model_name=args.model_dir)
    Settings.llm = resolve_llm(None)

    embedding_dimension = len(Settings.embed_model.get_text_embedding("random text"))
    gpu_resource = None
    if args.vector_store_type == "faiss":
        faiss_index = faiss.IndexFlatIP(embedding_dimension)
        try:
            gpu_resource = faiss.StandardGpuResources()
    #       faiss_index = faiss.index_cpu_to_gpu(gpu_resource, 0, faiss_index)
            current_device = torch.cuda.current_device()
            print(f"current_device: {current_device}")
            faiss_index = faiss.index_cpu_to_gpu(gpu_resource, current_device, faiss_index)
        except (AttributeError, AssertionError, RuntimeError) as e:
            print("An error occurred. gpu_resource is set to None.")
            traceback.print_exc()
            gpu_resource = None
        vector_store = FaissVectorStore(faiss_index=faiss_index)
    elif args.vector_store_type == "postgres":
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        database = os.getenv("POSTGRES_DATABASE")

        table_name = args.index.replace("-", "_")

        vector_store = PGVectorStore.from_params(
            database=database,
            host=host,
            password=password,
            port=port,
            user=user,
            table_name=table_name,
            embed_dim=embedding_dimension,  # openai embedding dimension
        )
    else:
        raise RuntimeError(f"Unknown vector store type: {args.vector_store_type}")

    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Retrieve the number of CPUs
    cpu_count = os.cpu_count()
    print(f"CPU Count: {cpu_count}")

    # Load documents
    input_files = list(Path(args.folder).rglob("*.md"))
    documents = SimpleDirectoryReader(
        input_files=input_files,
        file_metadata=aap_file_metadata_func,
    ).load_data(num_workers=cpu_count)

    # Load additional documents
    additional_input_files = list(Path(ADDITIONAL_DOCS_DIR).rglob("*.txt"))
    if len(additional_input_files) > 0:
        additional_docs = SimpleDirectoryReader(
            input_files=additional_input_files,
            file_metadata=additional_docs_metadata_func,
        ).load_data(num_workers=cpu_count)
        documents.extend(additional_docs)

    # Split based on header/section
    # md_parser = MarkdownNodeParser()
    # documents = md_parser.get_nodes_from_documents(documents)

    # Create chunks/nodes
    nodes = Settings.text_splitter.get_nodes_from_documents(documents)

    # Filter out invalid nodes
    good_nodes = []
    for node in nodes:
        if isinstance(node, TextNode) and got_whitespace(node.text):
            # Exclude given metadata during embedding
            # if args.exclude_metadata is not None:
            #     node.excluded_embed_metadata_keys.extend(args.exclude_metadata)
            good_nodes.append(node)
        else:
            print("skipping node without whitespace: " + str(node))

    # Create & save Index
    index = VectorStoreIndex(
        good_nodes,
        storage_context=storage_context,
    )

    # If a GPU index is used, convert it into a CPU index before saving
    if gpu_resource is not None:
        vector_store._faiss_index = faiss.index_gpu_to_cpu(vector_store._faiss_index)

    index.set_index_id(args.index)
    index.storage_context.persist(persist_dir=PERSIST_FOLDER)

    _metadata: dict = {}
    _metadata["execution-time"] = time.time() - start_time
    _metadata["llm"] = "None"
    _metadata["embedding-model"] = args.model_name
    _metadata["index-id"] = args.index
    if args.vector_store_type == "faiss":
        _metadata["vector-db"] = "faiss.IndexFlatIP"
    elif args.vector_store_type == "postgres":
        _metadata["vector-db"] = "PGVectorStore"
    _metadata["embedding-dimension"] = embedding_dimension
    _metadata["chunk"] = args.chunk
    _metadata["overlap"] = args.overlap
    _metadata["total-embedded-files"] = len(documents)

    with open(os.path.join(PERSIST_FOLDER, "metadata.json"), "w", encoding="utf8") as file:
        file.write(json.dumps(_metadata))

    if UNREACHABLE_DOCS > 0:
        print(
            "WARNING:\n"
            f"There were documents with {UNREACHABLE_DOCS} unreachable URLs, "
            "grep the log for UNREACHABLE.\n"
            "Please update the plain text."
        )
