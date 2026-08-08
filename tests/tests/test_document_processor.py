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

import os
from unittest import mock

import pytest

from aap_rag_content import document_processor
from tests.tests.conftest import RagMockEmbedding


class TestConfig:
    """Test cases for the _Config class in document_processor module."""

    def test_config(self):
        """Test that _Config class properly initializes and stores configuration values."""
        config = document_processor._Config(
            chunk_size=380,
            chunk_overlap=0,
            model_name="sentence-transformers/all-mpnet-base-v2",
            embeddings_model_dir="./embeddings_model",
        )
        assert config.chunk_size == 380
        assert config.chunk_overlap == 0
        assert config.model_name == "sentence-transformers/all-mpnet-base-v2"
        assert config.embeddings_model_dir == "./embeddings_model"


@pytest.fixture
def mock_processor(mocker):
    """Fixture to mock dependencies for DocumentProcessor tests."""
    log = mocker.patch.object(document_processor, "LOG")
    llamadb = mocker.patch.object(document_processor, "_LlamaStackDB")
    yield {
        "log": log,
        "llamadb": llamadb,
        "params": {
            "chunk_size": 380,
            "chunk_overlap": 0,
            "model_name": "sentence-transformers/all-mpnet-base-v2",
            "embeddings_model_dir": "embeddings_model",
            "num_workers": 10,
            "doc_type": "text",
        },
    }


class TestDocumentProcessor:
    """Test cases for the DocumentProcessor class in document_processor module."""

    def test_init_default(self, mock_processor):
        """Test DocumentProcessor initialization with default vector store type (llamastack-faiss)."""
        params = mock_processor["params"].copy()
        params["vector_store_type"] = "llamastack-faiss"
        doc_processor = document_processor.DocumentProcessor(**params)

        mock_processor["log"].warning.assert_not_called()
        mock_processor["llamadb"].assert_called_once_with(doc_processor.config)

        assert doc_processor is not None

        expected_params = params.copy()
        expected_params.update(  # Add default values
            embedding_dimension=None,  # Not calculated because class is mocked
            manual_chunking=True,
            table_name=None,
        )
        assert expected_params == doc_processor.config._Config__attributes
        assert doc_processor._num_embedded_files == 0

        assert expected_params["embeddings_model_dir"] == os.environ["HF_HOME"]
        assert os.environ["TRANSFORMERS_OFFLINE"] == "1"
        os.environ.pop("TRANSFORMERS_OFFLINE", None)

    @pytest.mark.parametrize(
        "vector_store_type", ["llamastack-faiss", "llamastack-sqlite-vec"]
    )
    def test_init_llama_stack(self, vector_store_type, mock_processor):
        """Test DocumentProcessor initialization with LlamaStack-compatible vector store types."""
        params = mock_processor["params"].copy()
        params["vector_store_type"] = vector_store_type

        doc_processor = document_processor.DocumentProcessor(**params)
        mock_processor["log"].warning.assert_not_called()
        mock_processor["llamadb"].assert_called_once_with(doc_processor.config)

        assert doc_processor is not None

        params.update(  # Add default values
            embedding_dimension=None,  # Not calculated because class is mocked
            manual_chunking=True,
            table_name=None,
        )
        assert params == doc_processor.config._Config__attributes
        assert doc_processor._num_embedded_files == 0

        assert params["embeddings_model_dir"] == os.environ["HF_HOME"]
        assert os.environ["TRANSFORMERS_OFFLINE"] == "1"
        os.environ.pop("TRANSFORMERS_OFFLINE", None)

    def test_process(self, mock_processor, mocker):
        """Test the document processing that reads and adds them to the database."""
        params = mock_processor["params"].copy()
        params["vector_store_type"] = "llamastack-faiss"
        doc_processor = document_processor.DocumentProcessor(**params)

        metadata = mocker.Mock()
        docs = list(range(5))

        reader_mock = mocker.patch.object(document_processor, "SimpleDirectoryReader")
        reader_mock.return_value.load_data.return_value = docs

        doc_processor.process(
            mock.sentinel.docs_dir,
            metadata,
            mock.sentinel.required_exts,
            mock.sentinel.file_extractor,
        )

        reader_mock.assert_called_once_with(
            str(mock.sentinel.docs_dir),
            recursive=True,
            file_metadata=metadata.populate,
            required_exts=mock.sentinel.required_exts,
            file_extractor=mock.sentinel.file_extractor,
        )

        doc_processor.db.add_docs.assert_called_once_with(docs)
        assert len(docs) == doc_processor._num_embedded_files

    def _make_processor_with_docs(self, mock_processor, mocker, docs):
        """Build a DocumentProcessor whose reader.load_data() returns the given docs."""
        params = mock_processor["params"].copy()
        params["vector_store_type"] = "llamastack-faiss"
        doc_processor = document_processor.DocumentProcessor(**params)

        reader_mock = mocker.patch.object(document_processor, "SimpleDirectoryReader")
        reader_mock.return_value.load_data.return_value = docs
        return doc_processor

    def test_process_unreachable_warn_keeps_all_docs(self, mock_processor, mocker):
        """unreachable_action='warn' (default) keeps unreachable docs untouched."""
        docs = [
            mocker.Mock(metadata={"title": "a", "url_reachable": True}),
            mocker.Mock(metadata={"title": "b", "url_reachable": False}),
        ]
        doc_processor = self._make_processor_with_docs(mock_processor, mocker, docs)

        doc_processor.process(mock.sentinel.docs_dir, mocker.Mock())

        doc_processor.db.add_docs.assert_called_once_with(docs)
        assert doc_processor._num_embedded_files == len(docs)

    def test_process_fail_raises_on_unreachable(self, mock_processor, mocker):
        """unreachable_action='fail' raises RuntimeError when any doc is unreachable."""
        docs = [
            mocker.Mock(metadata={"title": "a", "url_reachable": True}),
            mocker.Mock(metadata={"title": "b", "url_reachable": False}),
        ]
        doc_processor = self._make_processor_with_docs(mock_processor, mocker, docs)
        metadata = mocker.Mock()

        with pytest.raises(RuntimeError, match="unreachable"):
            doc_processor.process(
                mock.sentinel.docs_dir, metadata, unreachable_action="fail"
            )
        doc_processor.db.add_docs.assert_not_called()

    def test_process_fail_passes_when_all_reachable(self, mock_processor, mocker):
        """unreachable_action='fail' does not raise when every doc is reachable."""
        docs = [
            mocker.Mock(metadata={"title": "a", "url_reachable": True}),
            mocker.Mock(metadata={"title": "b", "url_reachable": True}),
        ]
        doc_processor = self._make_processor_with_docs(mock_processor, mocker, docs)

        doc_processor.process(
            mock.sentinel.docs_dir, mocker.Mock(), unreachable_action="fail"
        )
        doc_processor.db.add_docs.assert_called_once_with(docs)

    def test_process_drop_removes_unreachable_docs(self, mock_processor, mocker):
        """unreachable_action='drop' removes unreachable docs before saving."""
        reachable = mocker.Mock(metadata={"title": "a", "url_reachable": True})
        unreachable = mocker.Mock(metadata={"title": "b", "url_reachable": False})
        docs = [reachable, unreachable]
        doc_processor = self._make_processor_with_docs(mock_processor, mocker, docs)

        doc_processor.process(
            mock.sentinel.docs_dir, mocker.Mock(), unreachable_action="drop"
        )

        doc_processor.db.add_docs.assert_called_once_with([reachable])
        assert doc_processor._num_embedded_files == 1

    def test_process_drop_keeps_ignore_listed_docs(self, mock_processor, mocker):
        """unreachable_action='drop' keeps docs whose title is in ignore_list even if unreachable."""
        reachable = mocker.Mock(metadata={"title": "a", "url_reachable": True})
        ignored_unreachable = mocker.Mock(
            metadata={"title": "b", "url_reachable": False}
        )
        dropped_unreachable = mocker.Mock(
            metadata={"title": "c", "url_reachable": False}
        )
        docs = [reachable, ignored_unreachable, dropped_unreachable]
        doc_processor = self._make_processor_with_docs(mock_processor, mocker, docs)

        doc_processor.process(
            mock.sentinel.docs_dir,
            mocker.Mock(),
            unreachable_action="drop",
            ignore_list=["b"],
        )

        saved_docs = doc_processor.db.add_docs.call_args[0][0]
        assert set(saved_docs) == {reachable, ignored_unreachable}
        assert dropped_unreachable not in saved_docs

    def test_save(self, mock_processor):
        """Test saving the document processor's database to disk."""
        params = mock_processor["params"].copy()
        params["vector_store_type"] = "llamastack-faiss"
        doc_processor = document_processor.DocumentProcessor(**params)

        doc_processor.save(mock.sentinel.index, mock.sentinel.output_dir)
