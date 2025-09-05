"""Comprehensive test coverage for all functions in generate_embeddings-llama-stack.py."""

import argparse
import importlib.util
import json
import sys
import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import mock_open
from unittest.mock import patch


def import_module():
    """Helper function to import the module with dashes in filename, mocking dependencies."""
    # Mock the dependencies before importing
    mock_requests = MagicMock()
    mock_llama_stack_client = MagicMock()
    mock_llama_stack_lib = MagicMock()

    # Patch sys.modules to provide mocked dependencies
    sys.modules["requests"] = mock_requests
    sys.modules["llama_stack_client"] = mock_llama_stack_client
    sys.modules["llama_stack_client.types"] = MagicMock()
    sys.modules["llama_stack_client.types.shared_params"] = MagicMock()
    sys.modules["llama_stack_client.types.shared_params.document"] = MagicMock()
    sys.modules["llama_stack"] = mock_llama_stack_lib
    sys.modules["llama_stack.distribution"] = MagicMock()
    sys.modules["llama_stack.distribution.library_client"] = MagicMock()

    try:
        spec = importlib.util.spec_from_file_location(
            "generate_embeddings_llama_stack",
            Path(__file__).parent.parent / "scripts" / "generate_embeddings-llama-stack.py",
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        # Clean up mocked modules to avoid affecting other tests
        modules_to_remove = [
            "requests",
            "llama_stack_client",
            "llama_stack_client.types",
            "llama_stack_client.types.shared_params",
            "llama_stack_client.types.shared_params.document",
            "llama_stack",
            "llama_stack.distribution",
            "llama_stack.distribution.library_client",
        ]
        for module_name in modules_to_remove:
            if module_name in sys.modules:
                del sys.modules[module_name]


class TestPingUrl(unittest.TestCase):
    """Test cases for ping_url function."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.ping_url = self.module.ping_url

    def test_ping_url_success(self):
        """Test successful URL ping with status 200."""
        with patch.object(self.module, "requests") as mock_requests:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_requests.get.return_value = mock_response

            result = self.ping_url("https://example.com")

            self.assertTrue(result)
            mock_requests.get.assert_called_once_with("https://example.com", timeout=30)

    def test_ping_url_failure_non_200_status(self):
        """Test URL ping failure with non-200 status code."""
        with patch.object(self.module, "requests") as mock_requests:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_requests.get.return_value = mock_response

            result = self.ping_url("https://example.com/not-found")

            self.assertFalse(result)

    def test_ping_url_request_exception(self):
        """Test URL ping failure due to request exception."""
        with patch.object(self.module, "requests") as mock_requests:
            mock_requests.get.side_effect = self.module.requests.exceptions.RequestException(
                "Connection error"
            )

            result = self.ping_url("https://invalid-url.com")

            self.assertFalse(result)

    def test_ping_url_timeout(self):
        """Test URL ping failure due to timeout."""
        with patch.object(self.module, "requests") as mock_requests:
            mock_requests.get.side_effect = self.module.requests.exceptions.Timeout(
                "Request timeout"
            )

            result = self.ping_url("https://slow-website.com")

            self.assertFalse(result)

    def test_ping_url_various_status_codes(self):
        """Test URL ping with various HTTP status codes."""
        test_cases = [
            (200, True),
            (201, False),
            (301, False),
            (404, False),
            (500, False),
        ]

        for status_code, expected in test_cases:
            with self.subTest(status_code=status_code):
                with patch.object(self.module, "requests") as mock_requests:
                    mock_response = MagicMock()
                    mock_response.status_code = status_code
                    mock_requests.get.return_value = mock_response

                    result = self.ping_url(f"https://example.com/{status_code}")

                    self.assertEqual(result, expected)


class TestGetFileTitle(unittest.TestCase):
    """Test cases for get_file_title function."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.get_file_title = self.module.get_file_title

    def test_get_file_title_file_not_exists(self):
        """Test get_file_title when file doesn't exist."""
        non_existent_path = Path("/non/existent/file.md")

        result = self.get_file_title(non_existent_path)

        self.assertEqual(result, "")

    def test_get_file_title_empty_file(self):
        """Test get_file_title with empty file."""
        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.read_text", return_value=""),
        ):

            result = self.get_file_title(Path("empty.md"))

            self.assertEqual(result, "")

    def test_get_file_title_with_markdown_header(self):
        """Test get_file_title with markdown header."""
        content = "# This is a Title\nSome content here"

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.read_text", return_value=content),
        ):

            result = self.get_file_title(Path("test.md"))

            self.assertEqual(result, "This is a Title")

    def test_get_file_title_with_multiple_hashes(self):
        """Test get_file_title with multiple hash markdown headers."""
        content = "## Secondary Header\nContent follows"

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.read_text", return_value=content),
        ):

            result = self.get_file_title(Path("test.md"))

            self.assertEqual(result, "Secondary Header")

    def test_get_file_title_without_markdown_header(self):
        """Test get_file_title without markdown header."""
        content = "Plain text title\nMore content"

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.read_text", return_value=content),
        ):

            result = self.get_file_title(Path("test.txt"))

            self.assertEqual(result, "Plain text title")

    def test_get_file_title_with_trailing_newlines(self):
        """Test get_file_title with trailing newlines in first line."""
        content = "Title with newlines\n\n\nSecond line"

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.read_text", return_value=content),
        ):

            result = self.get_file_title(Path("test.md"))

            self.assertEqual(result, "Title with newlines")

    def test_get_file_title_encoding_error_handling(self):
        """Test get_file_title calls read_text with utf8 encoding."""
        content = "Test title"

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.read_text", return_value=content) as mock_read,
        ):

            self.get_file_title(Path("test.md"))

            mock_read.assert_called_once_with(encoding="utf8")


class TestFileMetadataFunc(unittest.TestCase):
    """Test cases for file_metadata_func function."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.file_metadata_func = self.module.file_metadata_func
        # Reset the global counter before each test
        self.module.UNREACHABLE_DOCS = 0

    def test_file_metadata_func_skip_ping(self):
        """Test file_metadata_func with skip_ping=True."""
        docs_url_func = lambda x: f"https://docs.example.com/{x}"
        docs_title_func = lambda x: "Test Title"

        with patch("builtins.print") as mock_print:
            result = self.file_metadata_func(
                "test/file.md", docs_url_func, docs_title_func, skip_ping=True
            )

        expected_result = {
            "docs_url": "https://docs.example.com/test/file.md",
            "title": "Test Title",
        }
        self.assertEqual(result, expected_result)

        # Verify print was called with correct message
        expected_msg = "file_path='test/file.md', title='Test Title', docs_url='https://docs.example.com/test/file.md'"
        mock_print.assert_called_once_with(expected_msg)

        # Verify UNREACHABLE_DOCS counter wasn't incremented
        self.assertEqual(self.module.UNREACHABLE_DOCS, 0)

    def test_file_metadata_func_with_ping_success(self):
        """Test file_metadata_func with successful URL ping."""
        docs_url_func = lambda x: f"https://reachable.com/{x}"
        docs_title_func = lambda x: "Reachable Title"

        with (
            patch.object(self.module, "ping_url", return_value=True),
            patch("builtins.print") as mock_print,
        ):

            result = self.file_metadata_func(
                "valid/file.md", docs_url_func, docs_title_func, skip_ping=False
            )

        expected_result = {
            "docs_url": "https://reachable.com/valid/file.md",
            "title": "Reachable Title",
        }
        self.assertEqual(result, expected_result)

        # Verify print message doesn't contain UNREACHABLE
        expected_msg = "file_path='valid/file.md', title='Reachable Title', docs_url='https://reachable.com/valid/file.md'"
        mock_print.assert_called_once_with(expected_msg)

        # Verify UNREACHABLE_DOCS counter wasn't incremented
        self.assertEqual(self.module.UNREACHABLE_DOCS, 0)

    def test_file_metadata_func_with_ping_failure(self):
        """Test file_metadata_func with failed URL ping."""
        docs_url_func = lambda x: f"https://unreachable.com/{x}"
        docs_title_func = lambda x: "Unreachable Title"

        with (
            patch.object(self.module, "ping_url", return_value=False),
            patch("builtins.print") as mock_print,
        ):

            result = self.file_metadata_func(
                "broken/file.md", docs_url_func, docs_title_func, skip_ping=False
            )

        expected_result = {
            "docs_url": "https://unreachable.com/broken/file.md",
            "title": "Unreachable Title",
        }
        self.assertEqual(result, expected_result)

        # Verify print message contains UNREACHABLE
        expected_msg = "file_path='broken/file.md', title='Unreachable Title', docs_url='https://unreachable.com/broken/file.md', UNREACHABLE"
        mock_print.assert_called_once_with(expected_msg)

        # Verify UNREACHABLE_DOCS counter was incremented
        self.assertEqual(self.module.UNREACHABLE_DOCS, 1)

    def test_file_metadata_func_multiple_unreachable_urls(self):
        """Test file_metadata_func increments global counter for multiple unreachable URLs."""
        docs_url_func = lambda x: f"https://broken.com/{x}"
        docs_title_func = lambda x: "Title"

        with patch.object(self.module, "ping_url", return_value=False), patch("builtins.print"):

            # Call multiple times to test counter increment
            self.file_metadata_func("file1.md", docs_url_func, docs_title_func, skip_ping=False)
            self.file_metadata_func("file2.md", docs_url_func, docs_title_func, skip_ping=False)
            self.file_metadata_func("file3.md", docs_url_func, docs_title_func, skip_ping=False)

        # Verify UNREACHABLE_DOCS counter was incremented for each call
        self.assertEqual(self.module.UNREACHABLE_DOCS, 3)


class TestAAPFileMetadataFunc(unittest.TestCase):
    """Test cases for aap_file_metadata_func function."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.aap_file_metadata_func = self.module.aap_file_metadata_func

    def test_aap_file_metadata_func_success(self):
        """Test successful aap_file_metadata_func execution."""
        md_path = Path("/test/docs/example.md")
        metadata_content = {"url": "https://docs.example.com/example", "title": "Example Title"}

        with (
            patch("pathlib.Path.read_text", return_value=json.dumps(metadata_content)),
            patch.object(self.module, "file_metadata_func") as mock_file_metadata,
        ):

            mock_file_metadata.return_value = {"docs_url": "test_url", "title": "test_title"}

            result = self.aap_file_metadata_func(md_path, skip_ping=True)

            # Verify file_metadata_func was called with correct parameters
            self.assertEqual(mock_file_metadata.call_count, 1)
            call_args = mock_file_metadata.call_args[0]
            self.assertEqual(call_args[0], str(md_path))  # file_path
            self.assertEqual(call_args[3], True)  # skip_ping

            # Test the docs_url and docs_title functions
            docs_url_func = call_args[1]
            docs_title_func = call_args[2]
            self.assertEqual(docs_url_func("dummy"), "https://docs.example.com/example")
            self.assertEqual(docs_title_func("dummy"), "Example Title")

            self.assertEqual(result, {"docs_url": "test_url", "title": "test_title"})

    def test_aap_file_metadata_func_with_nested_path(self):
        """Test aap_file_metadata_func with nested directory structure."""
        md_path = Path("/docs/guide/installation/setup.md")
        metadata_content = {"url": "https://docs.example.com/setup", "title": "Setup Guide"}

        with (
            patch("pathlib.Path.read_text", return_value=json.dumps(metadata_content)),
            patch.object(self.module, "file_metadata_func") as mock_file_metadata,
        ):

            mock_file_metadata.return_value = {"docs_url": "setup_url", "title": "setup_title"}

            result = self.aap_file_metadata_func(md_path, skip_ping=False)

            # Verify the metadata path construction
            mock_file_metadata.assert_called_once()
            call_args = mock_file_metadata.call_args[0]
            self.assertEqual(call_args[0], str(md_path))
            self.assertEqual(call_args[3], False)  # skip_ping

    def test_aap_file_metadata_func_json_parsing(self):
        """Test aap_file_metadata_func correctly parses JSON metadata."""
        md_path = Path("/test/complex.md")
        metadata_content = {
            "url": "https://complex.example.com/docs",
            "title": "Complex Documentation Title",
            "version": "2.5",
            "category": "advanced",
        }

        with (
            patch("pathlib.Path.read_text", return_value=json.dumps(metadata_content)),
            patch.object(self.module, "file_metadata_func") as mock_file_metadata,
        ):

            mock_file_metadata.return_value = {"docs_url": "complex_url", "title": "complex_title"}

            self.aap_file_metadata_func(md_path)

            # Verify the internal functions extract correct values
            call_args = mock_file_metadata.call_args[0]
            docs_url_func = call_args[1]
            docs_title_func = call_args[2]

            self.assertEqual(docs_url_func("any_param"), "https://complex.example.com/docs")
            self.assertEqual(docs_title_func("any_param"), "Complex Documentation Title")


class TestAdditionalDocsMetadataFunc(unittest.TestCase):
    """Test cases for additional_docs_metadata_func function."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.additional_docs_metadata_func = self.module.additional_docs_metadata_func

    def test_additional_docs_metadata_func_with_metadata_file(self):
        """Test additional_docs_metadata_func when .metadata file exists."""
        file_path = Path("/docs/additional/test.txt")
        metadata_content = {"url": "https://additional.example.com/test"}

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.is_file", return_value=True),
            patch("pathlib.Path.read_text", return_value=json.dumps(metadata_content)),
            patch.object(self.module, "get_file_title", return_value="Test File Title"),
            patch.object(self.module, "file_metadata_func") as mock_file_metadata,
        ):

            mock_file_metadata.return_value = {"docs_url": "meta_url", "title": "meta_title"}

            result = self.additional_docs_metadata_func(file_path, skip_ping=True)

            # Verify file_metadata_func was called
            mock_file_metadata.assert_called_once()
            call_args = mock_file_metadata.call_args[0]
            self.assertEqual(call_args[0], str(file_path))
            self.assertEqual(call_args[3], True)  # skip_ping

            # Test the internal functions
            docs_url_func = call_args[1]
            docs_title_func = call_args[2]
            self.assertEqual(docs_url_func("dummy"), "https://additional.example.com/test")
            self.assertEqual(docs_title_func("dummy"), "Test File Title")

    def test_additional_docs_metadata_func_without_metadata_file(self):
        """Test additional_docs_metadata_func when .metadata file doesn't exist."""
        file_path = Path("docs/additional/test.txt")

        with (
            patch("pathlib.Path.exists", return_value=False),
            patch.object(self.module, "get_file_title", return_value="Fallback Title"),
            patch("builtins.print") as mock_print,
        ):

            result = self.additional_docs_metadata_func(file_path)

            expected_result = {
                "docs_url": "https://github.com/ansible/aap-rag-content/blob/main/docs/additional/test.txt",
                "title": "Fallback Title",
            }
            self.assertEqual(result, expected_result)

            # Verify print was called with fallback URL
            print_calls = [str(call[0][0]) for call in mock_print.call_args_list]
            expected_url = (
                "https://github.com/ansible/aap-rag-content/blob/main/docs/additional/test.txt"
            )
            expected_title = "Fallback Title"

            # Check that the print call contains the expected components
            self.assertTrue(
                any(expected_url in call and expected_title in call for call in print_calls),
                f"Expected URL and title not found in print calls: {print_calls}",
            )

    def test_additional_docs_metadata_func_metadata_is_directory(self):
        """Test additional_docs_metadata_func when .metadata exists but is a directory."""
        file_path = Path("docs/test.txt")

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.is_file", return_value=False),
            patch.object(self.module, "get_file_title", return_value="Directory Test"),
            patch("builtins.print") as mock_print,
        ):

            result = self.additional_docs_metadata_func(file_path)

            expected_result = {
                "docs_url": "https://github.com/ansible/aap-rag-content/blob/main/docs/test.txt",
                "title": "Directory Test",
            }
            self.assertEqual(result, expected_result)

    def test_additional_docs_metadata_func_path_construction(self):
        """Test additional_docs_metadata_func constructs GitHub URL correctly."""
        test_cases = [
            Path("simple.txt"),
            Path("folder/file.txt"),
            Path("deep/nested/folder/document.txt"),
        ]

        for file_path in test_cases:
            with self.subTest(file_path=file_path):
                with (
                    patch("pathlib.Path.exists", return_value=False),
                    patch.object(self.module, "get_file_title", return_value="Test"),
                    patch("builtins.print"),
                ):

                    result = self.additional_docs_metadata_func(file_path)

                    expected_url = (
                        f"https://github.com/ansible/aap-rag-content/blob/main/{file_path}"
                    )
                    self.assertEqual(result["docs_url"], expected_url)


class TestInsertDocuments(unittest.TestCase):
    """Test cases for insert_documents function."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.insert_documents = self.module.insert_documents
        self.SourceDocument = self.module.SourceDocument

    def test_insert_documents_single_batch(self):
        """Test insert_documents with documents fitting in a single batch."""
        mock_client = MagicMock()

        # Create test documents
        documents = []
        for i in range(3):
            doc_path = MagicMock()
            doc_path.read_text.return_value = f"Content of document {i}"
            doc = self.SourceDocument(
                doc_path, {"title": f"Doc {i}", "url": f"http://example.com/{i}"}
            )
            documents.append(doc)

        with (
            patch.object(self.module, "RAGDocument") as mock_rag_doc,
            patch("builtins.print") as mock_print,
        ):

            # Configure RAGDocument mock to return objects with expected attributes
            mock_rag_instances = []
            for i in range(3):
                mock_instance = MagicMock()
                mock_instance.document_id = f"test-{i}"
                mock_instance.content = f"Content of document {i}"
                mock_instance.mime_type = "text/plain"
                mock_instance.metadata = {"title": f"Doc {i}", "url": f"http://example.com/{i}"}
                mock_rag_instances.append(mock_instance)

            mock_rag_doc.side_effect = mock_rag_instances

            self.insert_documents(mock_client, documents, "test", "test_index", 500)

        # Verify client.tool_runtime.rag_tool.insert was called once
        mock_client.tool_runtime.rag_tool.insert.assert_called_once()

        # Verify the call arguments
        call_kwargs = mock_client.tool_runtime.rag_tool.insert.call_args[1]
        self.assertEqual(call_kwargs["vector_db_id"], "test_index")
        self.assertEqual(call_kwargs["chunk_size_in_tokens"], 500)
        self.assertEqual(len(call_kwargs["documents"]), 3)

        # Verify RAGDocument was called with correct parameters
        self.assertEqual(mock_rag_doc.call_count, 3)
        for i in range(3):
            call_args = mock_rag_doc.call_args_list[i][1]
            self.assertEqual(call_args["document_id"], f"test-{i}")
            self.assertEqual(call_args["content"], f"Content of document {i}")
            self.assertEqual(call_args["mime_type"], "text/plain")
            self.assertEqual(
                call_args["metadata"], {"title": f"Doc {i}", "url": f"http://example.com/{i}"}
            )

    def test_insert_documents_multiple_batches(self):
        """Test insert_documents with documents requiring multiple batches."""
        mock_client = MagicMock()

        # Create 150 documents (should trigger multiple batches with batch_size=100)
        documents = []
        for i in range(150):
            doc_path = MagicMock()
            doc_path.read_text.return_value = f"Content {i}"
            doc = self.SourceDocument(doc_path, {"title": f"Title {i}"})
            documents.append(doc)

        with patch("builtins.print") as mock_print:
            self.insert_documents(mock_client, documents, "batch", "batch_index", 200)

        # Verify client.tool_runtime.rag_tool.insert was called twice
        self.assertEqual(mock_client.tool_runtime.rag_tool.insert.call_count, 2)

        # Verify first batch (100 documents)
        first_call_kwargs = mock_client.tool_runtime.rag_tool.insert.call_args_list[0][1]
        self.assertEqual(len(first_call_kwargs["documents"]), 100)

        # Verify second batch (50 documents)
        second_call_kwargs = mock_client.tool_runtime.rag_tool.insert.call_args_list[1][1]
        self.assertEqual(len(second_call_kwargs["documents"]), 50)

        # Verify print output shows progress
        print_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertIn("count=100", print_calls)
        self.assertIn("count=150", print_calls)

    def test_insert_documents_empty_list(self):
        """Test insert_documents with empty document list."""
        mock_client = MagicMock()

        with patch("builtins.print"):
            self.insert_documents(mock_client, [], "empty", "empty_index", 300)

        # Verify no calls were made to the client
        mock_client.tool_runtime.rag_tool.insert.assert_not_called()

    def test_insert_documents_file_read_error(self):
        """Test insert_documents handles file read errors gracefully."""
        mock_client = MagicMock()

        doc_path = MagicMock()
        doc_path.read_text.side_effect = FileNotFoundError("File not found")
        doc = self.SourceDocument(doc_path, {"title": "Error Doc"})

        with self.assertRaises(FileNotFoundError):
            self.insert_documents(mock_client, [doc], "error", "error_index", 100)

    def test_insert_documents_encoding_parameter(self):
        """Test insert_documents calls read_text with utf8 encoding."""
        mock_client = MagicMock()

        doc_path = MagicMock()
        doc_path.read_text.return_value = "Test content"
        doc = self.SourceDocument(doc_path, {"title": "Encoding Test"})

        with patch("builtins.print"):
            self.insert_documents(mock_client, [doc], "encoding", "encoding_index", 100)

        # Verify read_text was called with utf8 encoding
        doc_path.read_text.assert_called_once_with(encoding="utf8")


class TestRunDocumentIngestion(unittest.TestCase):
    """Test cases for run_document_ingestion function."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.run_document_ingestion = self.module.run_document_ingestion

        # Reset global counter
        self.module.UNREACHABLE_DOCS = 0

    def test_run_document_ingestion_basic_workflow(self):
        """Test basic run_document_ingestion workflow."""
        folder = Path("/test/docs")

        # Mock dependencies
        with (
            patch.object(self.module, "setup_llama_stack") as mock_setup,
            patch.object(self.module, "aap_file_metadata_func") as mock_aap_metadata,
            patch.object(self.module, "insert_documents") as mock_insert,
            patch("pathlib.Path.rglob") as mock_rglob,
            patch.object(self.module, "time") as mock_time,
            patch("builtins.print"),
        ):

            # Setup mocks
            mock_client = MagicMock()
            mock_setup.return_value = mock_client

            mock_files = [Path("doc1.md"), Path("doc2.md")]
            mock_rglob.return_value = mock_files

            mock_aap_metadata.side_effect = [
                {"title": "Doc 1", "url": "http://example.com/1"},
                {"title": "Doc 2", "url": "http://example.com/2"},
            ]

            mock_time.time.side_effect = [0.0, 5.5]  # start_time, end_time

            # Call function
            self.run_document_ingestion(folder, 400, "test_index", skip_ping=True)

            # Verify setup_llama_stack was called
            mock_setup.assert_called_once_with("test_index")

            # Verify rglob was called to find markdown files
            mock_rglob.assert_called_once_with("*.md")

            # Verify metadata functions were called for each file
            self.assertEqual(mock_aap_metadata.call_count, 2)
            mock_aap_metadata.assert_any_call(Path("doc1.md"), True)
            mock_aap_metadata.assert_any_call(Path("doc2.md"), True)

            # Verify insert_documents was called
            mock_insert.assert_called_once()
            call_args = mock_insert.call_args[0]
            self.assertEqual(call_args[0], mock_client)  # client
            self.assertEqual(len(call_args[1]), 2)  # documents list
            self.assertEqual(call_args[2], "doc")  # prefix
            self.assertEqual(call_args[3], "test_index")  # index
            self.assertEqual(call_args[4], 400)  # chunk

    def test_run_document_ingestion_with_additional_docs(self):
        """Test run_document_ingestion with additional docs folder."""
        folder = Path("/test/docs")
        additional_folder = Path("/test/additional")

        with (
            patch.object(self.module, "setup_llama_stack") as mock_setup,
            patch.object(self.module, "aap_file_metadata_func") as mock_aap_metadata,
            patch.object(self.module, "additional_docs_metadata_func") as mock_additional_metadata,
            patch.object(self.module, "insert_documents") as mock_insert,
            patch("pathlib.Path.rglob") as mock_rglob,
            patch.object(self.module, "time") as mock_time,
            patch("builtins.print"),
        ):

            # Setup mocks
            mock_client = MagicMock()
            mock_setup.return_value = mock_client

            # Mock file discovery
            def rglob_side_effect(pattern):
                if pattern == "*.md":
                    return [Path("main.md")]
                elif pattern == "*.txt":
                    return [Path("additional.txt")]
                return []

            mock_rglob.side_effect = rglob_side_effect

            mock_aap_metadata.return_value = {"title": "Main", "url": "http://main.com"}
            mock_additional_metadata.return_value = {
                "title": "Additional",
                "url": "http://additional.com",
            }

            mock_time.time.side_effect = [0.0, 10.0]

            # Call function with additional docs
            self.run_document_ingestion(
                folder, 300, "combined_index", additional_docs_folder=additional_folder
            )

            # Verify insert_documents was called twice (main docs + additional docs)
            self.assertEqual(mock_insert.call_count, 2)

            # Verify first call (main docs)
            first_call = mock_insert.call_args_list[0][0]
            self.assertEqual(first_call[2], "doc")  # prefix

            # Verify second call (additional docs)
            second_call = mock_insert.call_args_list[1][0]
            self.assertEqual(second_call[2], "additional_doc")  # prefix

    def test_run_document_ingestion_with_extra_docs(self):
        """Test run_document_ingestion with extra docs folder."""
        folder = Path("/test/docs")
        extra_folder = Path("/test/extra")

        with (
            patch.object(self.module, "setup_llama_stack") as mock_setup,
            patch.object(self.module, "aap_file_metadata_func") as mock_aap_metadata,
            patch.object(self.module, "additional_docs_metadata_func") as mock_extra_metadata,
            patch.object(self.module, "insert_documents") as mock_insert,
            patch("pathlib.Path.rglob") as mock_rglob,
            patch.object(self.module, "time") as mock_time,
            patch("builtins.print"),
        ):

            # Setup mocks
            mock_client = MagicMock()
            mock_setup.return_value = mock_client

            def rglob_side_effect(pattern):
                if pattern == "*.md":
                    return [Path("main.md")]
                elif pattern == "*.txt":
                    return [Path("extra.txt")]
                return []

            mock_rglob.side_effect = rglob_side_effect

            mock_aap_metadata.return_value = {"title": "Main", "url": "http://main.com"}
            mock_extra_metadata.return_value = {"title": "Extra", "url": "http://extra.com"}

            mock_time.time.side_effect = [0.0, 7.3]

            # Call function with extra docs
            self.run_document_ingestion(folder, 250, "extra_index", extra_docs_folder=extra_folder)

            # Verify insert_documents was called twice
            self.assertEqual(mock_insert.call_count, 2)

            # Verify second call uses "extra_doc" prefix
            second_call = mock_insert.call_args_list[1][0]
            self.assertEqual(second_call[2], "extra_doc")

    def test_run_document_ingestion_unreachable_docs_warning(self):
        """Test run_document_ingestion prints warning for unreachable docs."""
        folder = Path("/test/docs")

        # Set global counter to simulate unreachable docs
        self.module.UNREACHABLE_DOCS = 5

        with (
            patch.object(self.module, "setup_llama_stack"),
            patch.object(self.module, "aap_file_metadata_func"),
            patch.object(self.module, "insert_documents"),
            patch("pathlib.Path.rglob", return_value=[]),
            patch.object(self.module, "time") as mock_time,
            patch("builtins.print") as mock_print,
        ):

            mock_time.time.side_effect = [0.0, 3.0]

            self.run_document_ingestion(folder, 100, "warning_index")

            # Verify warning was printed
            print_calls = [str(call) for call in mock_print.call_args_list]
            warning_found = any(
                "WARNING" in call and "unreachable URLs" in call for call in print_calls
            )
            self.assertTrue(
                warning_found, "Expected unreachable docs warning not found in print calls"
            )

    def test_run_document_ingestion_elapsed_time_printing(self):
        """Test run_document_ingestion prints elapsed time."""
        folder = Path("/test/docs")

        with (
            patch.object(self.module, "setup_llama_stack"),
            patch.object(self.module, "aap_file_metadata_func"),
            patch.object(self.module, "insert_documents"),
            patch("pathlib.Path.rglob", return_value=[]),
            patch.object(self.module, "time") as mock_time,
            patch("builtins.print") as mock_print,
        ):

            mock_time.time.side_effect = [100.0, 142.75]  # 42.75 second difference

            self.run_document_ingestion(folder, 100, "timing_index")

            # Verify elapsed time was printed
            print_calls = [str(call) for call in mock_print.call_args_list]
            elapsed_found = any("Elapsed time: 42.75 secs" in call for call in print_calls)
            self.assertTrue(elapsed_found, "Expected elapsed time message not found")


class TestMain(unittest.TestCase):
    """Test cases for main function."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.main = self.module.main

    def test_main_argument_parsing(self):
        """Test main function argument parsing."""
        test_args = [
            "script_name",
            "-f",
            "/test/folder",
            "--additional-docs-folder",
            "/test/additional",
            "-c",
            "500",
            "-i",
            "test_index",
            "--skip-ping",
            "--extra-docs-folder",
            "/test/extra",
        ]

        with (
            patch("sys.argv", test_args),
            patch("pathlib.Path.is_dir", return_value=True),
            patch.object(self.module, "run_document_ingestion") as mock_run,
            patch("builtins.print"),
        ):

            self.main()

            # Verify run_document_ingestion was called with correct arguments
            mock_run.assert_called_once_with(
                folder=Path("/test/folder"),
                chunk=500,
                index="test_index",
                skip_ping=True,
                additional_docs_folder=Path("/test/additional"),
                extra_docs_folder=Path("/test/extra"),
            )

    def test_main_missing_folder_validation(self):
        """Test main function validates folder existence."""
        test_args = ["script_name", "-f", "/nonexistent", "-i", "test_index"]

        with (
            patch("sys.argv", test_args),
            patch("pathlib.Path.is_dir", return_value=False),
            patch("builtins.print") as mock_print,
            patch("builtins.exit") as mock_exit,
            patch.object(self.module, "run_document_ingestion"),
        ):

            self.main()

            # Verify error message and exit
            mock_print.assert_any_call("--folder must point on a valid directory")
            mock_exit.assert_called_with(1)

    def test_main_invalid_additional_docs_folder(self):
        """Test main function validates additional docs folder."""
        test_args = [
            "script_name",
            "-f",
            "/test/folder",
            "--additional-docs-folder",
            "/invalid/additional",
            "-i",
            "test_index",
        ]

        def mock_is_dir(self):
            path_str = str(self)
            if path_str == "/test/folder":
                return True
            elif path_str == "/invalid/additional":
                return False
            return True

        with (
            patch("sys.argv", test_args),
            patch("pathlib.Path.is_dir", mock_is_dir),
            patch("builtins.print") as mock_print,
            patch("builtins.exit") as mock_exit,
            patch.object(self.module, "run_document_ingestion"),
        ):

            self.main()

            # Verify error message and exit
            mock_exit.assert_called_with(1)

    def test_main_invalid_extra_docs_folder(self):
        """Test main function validates extra docs folder."""
        test_args = [
            "script_name",
            "-f",
            "/test/folder",
            "--extra-docs-folder",
            "/invalid/extra",
            "-i",
            "test_index",
        ]

        def mock_is_dir(self):
            path_str = str(self)
            if path_str == "/test/folder":
                return True
            elif path_str == "/invalid/extra":
                return False
            return True

        with (
            patch("sys.argv", test_args),
            patch("pathlib.Path.is_dir", mock_is_dir),
            patch("builtins.print") as mock_print,
            patch("builtins.exit") as mock_exit,
            patch.object(self.module, "run_document_ingestion"),
        ):

            self.main()

            # Verify error message and exit
            mock_print.assert_any_call("--extra-docs-folder must point on a valid directory")
            mock_exit.assert_called_with(1)

    def test_main_default_values(self):
        """Test main function uses correct default values."""
        test_args = ["script_name", "-f", "/test/folder", "-i", "default_index"]

        with (
            patch("sys.argv", test_args),
            patch("pathlib.Path.is_dir", return_value=True),
            patch.object(self.module, "run_document_ingestion") as mock_run,
            patch("builtins.print"),
        ):

            self.main()

            # Verify default values
            call_kwargs = mock_run.call_args[1]
            self.assertEqual(call_kwargs["chunk"], 380)  # default chunk size
            self.assertEqual(call_kwargs["skip_ping"], False)  # default skip_ping
            self.assertIsNone(call_kwargs["additional_docs_folder"])  # default None
            self.assertIsNone(call_kwargs["extra_docs_folder"])  # default None

    def test_main_no_additional_docs_folder_message(self):
        """Test main function prints message when additional-docs-folder not set."""
        test_args = ["script_name", "-f", "/test/folder", "-i", "test_index"]

        with (
            patch("sys.argv", test_args),
            patch("pathlib.Path.is_dir", return_value=True),
            patch.object(self.module, "run_document_ingestion"),
            patch("builtins.print") as mock_print,
        ):

            self.main()

            # Verify message about missing additional-docs-folder
            mock_print.assert_any_call("--additional-docs-folder was not set")


if __name__ == "__main__":
    unittest.main()
