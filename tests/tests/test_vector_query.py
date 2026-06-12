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
"""Vector query round-trip tests using real SentenceTransformer and FAISS."""
# pylint: disable=import-error,redefined-outer-name
import base64
import io
import json
import os
import sqlite3
from pathlib import Path

import faiss
import numpy as np
import pytest
from sentence_transformers import SentenceTransformer

pytestmark = pytest.mark.requires_model

EMBEDDING_DIM = 768
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MODEL_DIR = str(REPO_ROOT / "embeddings_model")

SAMPLE_DOCUMENTS = [
    "Ansible Automation Platform provides enterprise automation capabilities for IT teams",
    "Kubernetes is a container orchestration platform for deploying applications",
    "Python is a programming language commonly used for scripting and automation",
    "Red Hat Enterprise Linux is an operating system for servers and workstations",
    "Ansible playbooks define automation tasks in YAML format",
]

SOLUTION_GUIDE_URL_PREFIX = "ansible-tmm.github.io/solution-guides/"

SOLUTION_GUIDE_QUERIES = {
    "instana": {
        "query": "an issue with IBM Instana",
        "expected_url": SOLUTION_GUIDE_URL_PREFIX + "README-Instana-AIOps",
    },
    "servicenow": {
        "query": "AIOps with ServiceNow",
        "expected_url": SOLUTION_GUIDE_URL_PREFIX + "README-AIOps-ServiceNow",
    },
    "rhaiis": {
        "query": "Red Hat AI Inference Server",
        "expected_url": SOLUTION_GUIDE_URL_PREFIX + "README-Intelligent-Assistant-RHAIIS",
    },
}


def _find_vector_db_path():
    """Locate the built vector DB's faiss_store.db file."""
    candidates = [
        REPO_ROOT / "llama_stack_vector_db" / "faiss_store.db",
        REPO_ROOT / "rag" / "llama_stack_vector_db" / "faiss_store.db",
    ]
    for path in candidates:
        if path.is_file():
            return path
    return None


def _load_built_vector_db(db_path):
    """Load the FAISS index and chunk metadata from the built vector DB.

    The LlamaStack FAISS provider stores the index as a numpy uint8 array
    and chunk metadata as JSON strings inside a SQLite KV store.

    Returns (faiss_index, chunks_dict) where chunks_dict maps
    string index to parsed chunk metadata dict.
    """
    conn = sqlite3.connect(str(db_path))
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM kvstore WHERE key LIKE 'faiss_index:%'")
        row = cursor.fetchone()
        if row is None:
            return None, None

        data = json.loads(row[0])
        raw = np.load(io.BytesIO(base64.b64decode(data["faiss_index"])))
        index = faiss.deserialize_index(np.ascontiguousarray(raw))

        chunk_by_index = {}
        for key, value in data["chunk_by_index"].items():
            chunk_by_index[int(key)] = json.loads(value)

        return index, chunk_by_index
    finally:
        conn.close()


@pytest.fixture(scope="module")
def embedding_model():
    """Load the SentenceTransformer model once per test module."""
    model_dir = os.path.realpath(MODEL_DIR)
    if not os.path.isdir(model_dir):
        pytest.skip(f"Embeddings model not found at {model_dir}")
    old_hf_home = os.environ.get("HF_HOME")
    old_offline = os.environ.get("TRANSFORMERS_OFFLINE")
    os.environ["HF_HOME"] = model_dir
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    try:
        model = SentenceTransformer(model_dir)
        yield model
    finally:
        if old_hf_home is None:
            os.environ.pop("HF_HOME", None)
        else:
            os.environ["HF_HOME"] = old_hf_home
        if old_offline is None:
            os.environ.pop("TRANSFORMERS_OFFLINE", None)
        else:
            os.environ["TRANSFORMERS_OFFLINE"] = old_offline


@pytest.fixture(scope="module")
def populated_faiss_index(embedding_model):
    """Build a FAISS index from sample documents."""
    embeddings = embedding_model.encode(SAMPLE_DOCUMENTS)
    embeddings = np.array(embeddings, dtype=np.float32)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embeddings, SAMPLE_DOCUMENTS


@pytest.fixture(scope="module")
def built_vector_db():
    """Load the FAISS index built by custom_processor_aap.py."""
    db_path = _find_vector_db_path()
    if db_path is None:
        pytest.skip("Built vector DB (faiss_store.db) not found")

    index, chunks = _load_built_vector_db(db_path)
    if index is None:
        pytest.skip("No FAISS index found in the vector DB")

    has_solution_guides = any(
        SOLUTION_GUIDE_URL_PREFIX in c.get("metadata", {}).get("docs_url", "")
        for c in chunks.values()
    )
    if not has_solution_guides:
        pytest.skip(
            "Vector DB does not contain solution guide chunks "
            "(run custom_processor_aap.py to build a complete DB)"
        )

    return index, chunks


class TestVectorQueryRoundTrip:
    """Test the embed -> FAISS index -> query round-trip."""

    def test_faiss_index_creation_from_embeddings(self, populated_faiss_index):
        """Verify a FAISS index is built with correct document count and dimension."""
        index, embeddings, docs = populated_faiss_index
        assert index.ntotal == len(docs)
        assert index.d == EMBEDDING_DIM
        assert embeddings.shape == (len(docs), EMBEDDING_DIM)

    def test_query_returns_semantically_relevant_result(
        self, embedding_model, populated_faiss_index
    ):
        """Verify the top result for an Ansible query is Ansible-related."""
        index, _, docs = populated_faiss_index
        query = "How do I automate infrastructure with Ansible?"
        query_embedding = np.array(embedding_model.encode([query]), dtype=np.float32)
        _, indices = index.search(query_embedding, k=len(docs))

        top_idx = indices[0][0]
        assert top_idx in (0, 4), (
            f"Expected top result to be an Ansible doc (index 0 or 4), "
            f"got index {top_idx}: '{docs[top_idx]}'"
        )
        assert top_idx not in (1, 3), (
            f"Top result should not be Kubernetes (1) or RHEL (3), "
            f"got index {top_idx}: '{docs[top_idx]}'"
        )

    def test_query_returns_correct_number_of_results(self, embedding_model, populated_faiss_index):
        """Verify the query returns exactly k results."""
        index, _, _ = populated_faiss_index
        query_embedding = np.array(embedding_model.encode(["automation tasks"]), dtype=np.float32)
        _, indices_3 = index.search(query_embedding, k=3)
        assert indices_3.shape == (1, 3)

        _, indices_1 = index.search(query_embedding, k=1)
        assert indices_1.shape == (1, 1)

    def test_embedding_dimension_matches_faiss_index(self, embedding_model, populated_faiss_index):
        """Verify encoded embeddings have the correct dimension for the index."""
        index, _, _ = populated_faiss_index
        dim = embedding_model.get_sentence_embedding_dimension()
        assert dim == EMBEDDING_DIM
        assert dim == index.d

        single_embedding = embedding_model.encode(["test document"])
        assert single_embedding.shape == (1, dim)

    def test_duplicate_documents_both_returned(self, embedding_model):
        """Verify duplicate documents are indexed and returned with identical distances."""
        doc = "Ansible is an open source automation tool"
        docs = [doc, doc, "unrelated text about cooking recipes"]
        embeddings = np.array(embedding_model.encode(docs), dtype=np.float32)

        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)

        query_embedding = np.array(embedding_model.encode([doc]), dtype=np.float32)
        distances, indices = index.search(query_embedding, k=3)

        assert set(indices[0][:2]) == {0, 1}
        assert np.isclose(distances[0][0], distances[0][1], atol=1e-6)


class TestSolutionGuidesQuery:
    """Verify queries against the built vector DB return chunks from expected solution guides."""

    TOP_K = 5

    def _query_top_urls(self, embedding_model, built_vector_db, query):
        """Return the docs_url values for the top-k chunks matching query."""
        index, chunks = built_vector_db
        query_embedding = np.array(embedding_model.encode([query]), dtype=np.float32)
        _, indices = index.search(query_embedding, k=self.TOP_K)
        return [chunks[idx].get("metadata", {}).get("docs_url", "") for idx in indices[0]]

    def test_instana_query_returns_instana_guide(self, embedding_model, built_vector_db):
        """Verify an IBM Instana query returns chunks from the Instana solution guide."""
        urls = self._query_top_urls(
            embedding_model,
            built_vector_db,
            SOLUTION_GUIDE_QUERIES["instana"]["query"],
        )
        expected = SOLUTION_GUIDE_QUERIES["instana"]["expected_url"]
        assert any(expected in url for url in urls), (
            f"Expected a chunk from {expected} in top {self.TOP_K} results, " f"got URLs: {urls}"
        )

    def test_servicenow_query_returns_servicenow_guide(self, embedding_model, built_vector_db):
        """Verify an AIOps ServiceNow query returns chunks from the ServiceNow guide."""
        urls = self._query_top_urls(
            embedding_model,
            built_vector_db,
            SOLUTION_GUIDE_QUERIES["servicenow"]["query"],
        )
        expected = SOLUTION_GUIDE_QUERIES["servicenow"]["expected_url"]
        assert any(expected in url for url in urls), (
            f"Expected a chunk from {expected} in top {self.TOP_K} results, " f"got URLs: {urls}"
        )

    def test_rhaiis_query_returns_rhaiis_guide(self, embedding_model, built_vector_db):
        """Verify a Red Hat AI Inference Server query returns chunks from the RHAIIS guide."""
        urls = self._query_top_urls(
            embedding_model,
            built_vector_db,
            SOLUTION_GUIDE_QUERIES["rhaiis"]["query"],
        )
        expected = SOLUTION_GUIDE_QUERIES["rhaiis"]["expected_url"]
        assert any(expected in url for url in urls), (
            f"Expected a chunk from {expected} in top {self.TOP_K} results, " f"got URLs: {urls}"
        )
