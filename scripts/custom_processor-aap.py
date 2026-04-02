import functools
import json
from pathlib import Path

from aap_rag_content.metadata_processor import MetadataProcessor
from aap_rag_content.document_processor import DocumentProcessor
from aap_rag_content import utils

# Folders where AAP product documentation markdown (.md) files are stored.
AAP_PRODUCT_DOCS = [
    "aap-product-docs-plaintext/red_hat_content/documentation/ansible_on_clouds",
    "aap-product-docs-plaintext/red_hat_content/documentation/red_hat_ansible_automation_platform/2.6",
    "aap-product-docs-plaintext/red_hat_content/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant",
]

# Folders where additional documents are stored as plain text (.txt) files.
ADDITIONAL_DOCS = [
    "additional_docs",
]


class AAPMetadataProcessor(MetadataProcessor):

    def __init__(self, suppress_ping_url: bool = False):
        super().__init__(suppress_ping_url=suppress_ping_url)

    @functools.lru_cache(maxsize=None)
    def _load_metadata(self, file_path_str: str) -> dict:
        # Return a dict that contains metadata for the specified source
        # document
        file_path = Path(file_path_str)
        metadata_path = Path(file_path.parent / ".metadata" / f"{file_path.stem}.json")
        if not metadata_path.exists():
            raise RuntimeError(f"Metadata JSON file {metadata_path} does not exist")
        metadata = json.loads(metadata_path.read_text(encoding="utf8"))
        return metadata

    def url_function(self, file_path: str) -> str:
        """
        Return a URL for the file, so it can be referenced when used
        in an answer
        """
        url = self._load_metadata(file_path).get("url")
        if not url:
            raise RuntimeError(f"URL is not found for {file_path}")
        return url

    def get_file_title(self, file_path: str) -> str:
        """
        If a title is find in the metadata JSON file, return it.
        Otherwise, extract title from the plaintext doc file.
        """
        title = self._load_metadata(file_path).get("title")
        if title:
            return title
        if not file_path.endswith(".txt"):
            raise RuntimeError(f"Title metadata is not found for the markdown file {file_path}")
        file_content = Path(file_path).read_text(encoding="utf8")
        return file_content.split("\n")[0].lstrip("# ")


if __name__ == "__main__":
    parser = utils.get_common_arg_parser()
    args = parser.parse_args()

    # Instantiate custom Metadata Processor
    metadata_processor = AAPMetadataProcessor(suppress_ping_url=args.suppress_ping_url)

    # Instantiate Document Processor
    document_processor = DocumentProcessor(
        chunk_size=args.chunk,
        chunk_overlap=args.overlap,
        model_name=args.model_name,
        embeddings_model_dir=args.model_dir,
        num_workers=args.workers,
        vector_store_type=args.vector_store_type,
        manual_chunking=args.manual_chunking,
    )

    # Load and embed the documents, this method can be called multiple times
    # for different sets of documents
    for document_folder in AAP_PRODUCT_DOCS:
        folder = Path(Path(args.folder) / document_folder)
        document_processor.process(
            folder,
            metadata=metadata_processor,
            required_exts=[".md"],
        )
    for document_folder in ADDITIONAL_DOCS:
        folder = Path(Path(args.folder) / document_folder)
        document_processor.process(
            folder,
            metadata=metadata_processor,
            required_exts=[".txt"],
        )

    # Save the new vector database to the output directory
    document_processor.save(args.index, args.output)
