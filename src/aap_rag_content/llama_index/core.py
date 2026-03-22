"""Core classes for document processing without llama_index dependency.

This module provides llama-index compatible classes without importing all
llama-index dependencies. These lightweight implementations offer the same
interface as their llama-index counterparts, allowing code to work with
familiar patterns while minimizing external dependencies.
"""

import logging
import uuid
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable, Optional

LOG = logging.getLogger(__name__)


class Document:
    """A document with text content and metadata."""

    def __init__(
        self,
        text: str = "",
        metadata: Optional[dict[str, Any]] = None,
        doc_id: Optional[str] = None,
    ):
        """Initialize a Document.

        Args:
            text: The text content of the document
            metadata: Dictionary of metadata about the document
            doc_id: Unique identifier for the document. Generated if not provided.
        """
        self.text = text
        self.metadata = metadata or {}
        self.doc_id = doc_id or str(uuid.uuid4())

    def __repr__(self) -> str:
        return f"Document(doc_id='{self.doc_id}', text_length={len(self.text)})"


class TextNode:
    """A text node with content and metadata (used for chunked documents)."""

    def __init__(
        self,
        text: str = "",
        metadata: Optional[dict[str, Any]] = None,
        id_: Optional[str] = None,
        ref_doc_id: Optional[str] = None,
    ):
        """Initialize a TextNode.

        Args:
            text: The text content of the node
            metadata: Dictionary of metadata about the node
            id_: Unique identifier for the node. Generated if not provided.
            ref_doc_id: Reference to the parent document ID
        """
        self.text = text
        self.metadata = metadata or {}
        self.id_ = id_ or str(uuid.uuid4())
        self.ref_doc_id = ref_doc_id or str(uuid.uuid4())

    def __repr__(self) -> str:
        return f"TextNode(id_='{self.id_}', text_length={len(self.text)})"


class BaseReader(ABC):
    """Abstract base class for document readers."""

    @abstractmethod
    def load_data(self, *args: Any, **kwargs: Any) -> list[Document]:
        """Load data and return a list of Documents.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        Returns:
            List of Document objects
        """
        pass


class SimpleDirectoryReader(BaseReader):
    """Reads documents from a directory."""

    def __init__(
        self,
        input_dir: str,
        recursive: bool = True,
        file_metadata: Optional[Callable[[str], dict[str, Any]]] = None,
        required_exts: Optional[list[str]] = None,
        file_extractor: Optional[dict[str, BaseReader]] = None,
    ):
        """Initialize the directory reader.

        Args:
            input_dir: Directory to read files from
            recursive: Whether to recursively search subdirectories
            file_metadata: Optional callback function that takes a file path
                          and returns metadata dict
            required_exts: Optional list of required file extensions (e.g., ['.txt', '.md'])
            file_extractor: Optional dict mapping file extensions to custom readers
        """
        self.input_dir = Path(input_dir)
        self.recursive = recursive
        self.file_metadata = file_metadata
        self.required_exts = required_exts
        self.file_extractor = file_extractor or {}

        if not self.input_dir.exists():
            raise ValueError(f"Directory does not exist: {input_dir}")
        if not self.input_dir.is_dir():
            raise ValueError(f"Path is not a directory: {input_dir}")

    def _get_files(self) -> list[Path]:
        """Get list of files to process based on settings."""
        if self.recursive:
            pattern = "**/*"
        else:
            pattern = "*"

        files = []
        for path in self.input_dir.glob(pattern):
            if path.is_file():
                # Check if file extension is in required list
                if self.required_exts:
                    if path.suffix in self.required_exts:
                        files.append(path)
                else:
                    files.append(path)

        return files

    def _read_file(self, file_path: Path) -> Optional[Document]:
        """Read a single file and return a Document.

        Args:
            file_path: Path to the file to read

        Returns:
            Document object or None if reading failed
        """
        try:
            # Check if there's a custom reader for this file type
            if file_path.suffix in self.file_extractor:
                reader = self.file_extractor[file_path.suffix]
                docs = reader.load_data(str(file_path))
                if docs:
                    return docs[0]  # Return first document
                return None

            # Default: read as text file
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            # Get metadata if callback provided
            metadata = {}
            if self.file_metadata:
                metadata = self.file_metadata(str(file_path))

            # Add file path to metadata
            metadata["file_path"] = str(file_path)
            metadata["file_name"] = file_path.name

            doc_id = str(uuid.uuid4())
            return Document(text=text, metadata=metadata, doc_id=doc_id)

        except Exception as e:
            LOG.error("Failed to read file %s: %s", file_path, e)
            return None

    def load_data(self, num_workers: Optional[int] = 0) -> list[Document]:
        """Load all documents from the directory.

        Args:
            num_workers: Number of worker threads for parallel processing.
                        If 0 or None, process sequentially.

        Returns:
            List of Document objects
        """
        files = self._get_files()
        LOG.info("Found %d files to process", len(files))

        documents = []

        if num_workers and num_workers > 0:
            # Parallel processing
            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                future_to_file = {
                    executor.submit(self._read_file, file_path): file_path
                    for file_path in files
                }

                for future in as_completed(future_to_file):
                    doc = future.result()
                    if doc:
                        documents.append(doc)
        else:
            # Sequential processing
            for file_path in files:
                doc = self._read_file(file_path)
                if doc:
                    documents.append(doc)

        LOG.info("Successfully loaded %d documents", len(documents))
        return documents