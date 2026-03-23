"""Local replacement for llama_index dependencies.

This module provides minimal implementations of llama_index classes
needed by the document processor, without requiring the full llama_index library.
"""

from aap_rag_content.llama_index.core import (
    BaseReader,
    Document,
    SimpleDirectoryReader,
    TextNode,
)

__all__ = [
    "BaseReader",
    "Document",
    "SimpleDirectoryReader",
    "TextNode",
]