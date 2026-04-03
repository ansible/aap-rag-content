# Copyright 2025 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""Tests for custom_processor_aap module."""
# pylint: disable=C0415
import sys
from pathlib import Path
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

# Add scripts directory to path
scripts_dir = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))


@pytest.fixture
def mock_args():
    """Mock command line arguments."""
    args = MagicMock()
    args.folder = "/fake/folder"
    args.model_dir = "embeddings_model"
    args.model_name = "test-model"
    args.chunk = 380
    args.overlap = 0
    args.workers = None
    args.vector_store_type = "faiss"
    args.manual_chunking = True
    args.index = "test-index"
    args.output = "/fake/output"
    args.suppress_ping_url = False
    return args


class TestAAPMetadataProcessor:
    """Test cases for AAPMetadataProcessor with suppress_ping_url support."""

    def test_init_default_suppress_ping_url(self):
        """Test AAPMetadataProcessor initializes with suppress_ping_url=False by default."""
        # Import here to avoid module-level import issues
        from custom_processor_aap import AAPMetadataProcessor

        processor = AAPMetadataProcessor()
        assert processor.suppress_ping_url is False

    def test_init_with_suppress_ping_url_true(self):
        """Test AAPMetadataProcessor initializes with suppress_ping_url=True when specified."""
        from custom_processor_aap import AAPMetadataProcessor

        processor = AAPMetadataProcessor(suppress_ping_url=True)
        assert processor.suppress_ping_url is True

    def test_init_with_suppress_ping_url_false(self):
        """Test AAPMetadataProcessor initializes with suppress_ping_url=False when specified."""
        from custom_processor_aap import AAPMetadataProcessor

        processor = AAPMetadataProcessor(suppress_ping_url=False)
        assert processor.suppress_ping_url is False

    @patch("custom_processor_aap.DocumentProcessor")
    @patch("custom_processor_aap.AAPMetadataProcessor")
    @patch("custom_processor_aap.utils.get_common_arg_parser")
    def test_main_suppress_ping_url_false(
        self, mock_parser, mock_processor_class, _mock_doc_processor
    ):
        """Test main instantiates AAPMetadataProcessor with suppress_ping_url=False."""
        from custom_processor_aap import main

        test_args = MagicMock()
        test_args.suppress_ping_url = False
        mock_parser_instance = MagicMock()
        mock_parser.return_value = mock_parser_instance
        mock_parser_instance.parse_args.return_value = test_args

        # Call main function
        main()

        # Verify AAPMetadataProcessor was called with correct parameter
        mock_processor_class.assert_called_once_with(suppress_ping_url=False)

    @patch("custom_processor_aap.DocumentProcessor")
    @patch("custom_processor_aap.AAPMetadataProcessor")
    @patch("custom_processor_aap.utils.get_common_arg_parser")
    def test_main_suppress_ping_url_true(
        self, mock_parser, mock_processor_class, _mock_doc_processor
    ):
        """Test main instantiates AAPMetadataProcessor with suppress_ping_url=True."""
        from custom_processor_aap import main

        test_args = MagicMock()
        test_args.suppress_ping_url = True
        mock_parser_instance = MagicMock()
        mock_parser.return_value = mock_parser_instance
        mock_parser_instance.parse_args.return_value = test_args

        # Call main function
        main()

        # Verify AAPMetadataProcessor was called with correct parameter
        mock_processor_class.assert_called_once_with(suppress_ping_url=True)

    def test_populate_with_suppress_ping_url(self, mocker):
        """Test that populate skips ping_url when suppress_ping_url=True."""
        from custom_processor_aap import AAPMetadataProcessor

        processor = AAPMetadataProcessor(suppress_ping_url=True)

        # Mock the methods
        mock_load_metadata = mocker.patch.object(processor, "_load_metadata")
        mock_load_metadata.return_value = {
            "url": "https://example.com",
            "title": "Test Title",
        }

        mock_ping_url = mocker.patch.object(processor, "ping_url")
        mocker.patch("builtins.open", mocker.mock_open(read_data="# Test Title\n"))

        result = processor.populate("/fake/path/test.md")

        # Verify ping_url was not called
        mock_ping_url.assert_not_called()

        # Verify result has url_reachable=True
        assert result["url_reachable"] is True
        assert result["docs_url"] == "https://example.com"
        assert result["title"] == "Test Title"

    def test_populate_without_suppress_ping_url(self, mocker):
        """Test that populate calls ping_url when suppress_ping_url=False."""
        from custom_processor_aap import AAPMetadataProcessor

        processor = AAPMetadataProcessor(suppress_ping_url=False)

        # Mock the methods
        mock_load_metadata = mocker.patch.object(processor, "_load_metadata")
        mock_load_metadata.return_value = {
            "url": "https://example.com",
            "title": "Test Title",
        }

        mock_ping_url = mocker.patch.object(processor, "ping_url")
        mock_ping_url.return_value = True
        mocker.patch("builtins.open", mocker.mock_open(read_data="# Test Title\n"))

        result = processor.populate("/fake/path/test.md")

        # Verify ping_url was called
        mock_ping_url.assert_called_once_with("https://example.com")

        # Verify result has url_reachable=True
        assert result["url_reachable"] is True
        assert result["docs_url"] == "https://example.com"
        assert result["title"] == "Test Title"
