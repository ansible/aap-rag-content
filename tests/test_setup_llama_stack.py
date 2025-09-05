"""Test coverage for setup_llama_stack function."""

import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock
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


class TestSetupLlamaStack(unittest.TestCase):
    """Test class for setup_llama_stack function."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.setup_llama_stack = self.module.setup_llama_stack

        # Set up common mocks that will be used across tests
        self.client_patcher = patch.object(self.module, "LlamaStackAsLibraryClient")
        self.mock_client_class = self.client_patcher.start()
        self.mock_client = MagicMock()
        self.mock_client_class.return_value = self.mock_client

    def tearDown(self):
        """Clean up after each test."""
        self.client_patcher.stop()

    def create_mock_provider(self, api_type, provider_id):
        """Helper method to create mock providers."""
        mock_provider = MagicMock()
        mock_provider.api = api_type
        mock_provider.provider_id = provider_id
        return mock_provider

    def setup_providers(self, provider_configs):
        """Helper method to set up mock providers from a list of (api, provider_id) tuples."""
        providers = [self.create_mock_provider(api, pid) for api, pid in provider_configs]
        self.mock_client.providers.list.return_value = providers
        return providers

    def assert_standard_calls(self, index_name):
        """Helper method to assert the standard sequence of calls."""
        self.mock_client_class.assert_called_once_with("./run.yaml", provider_data={})
        self.mock_client.initialize.assert_called_once()
        self.mock_client.providers.list.assert_called_once()

    def assert_vector_db_registration(self, index_name, provider_id):
        """Helper method to assert vector database registration."""
        self.mock_client.vector_dbs.register.assert_called_once_with(
            vector_db_id=index_name,
            provider_id=provider_id,
            embedding_model="./embeddings_model",
            embedding_dimension=768,
        )

    def test_setup_llama_stack_success(self):
        """Test successful setup_llama_stack execution."""
        # Set up providers with mixed types, vector_io providers should be filtered
        self.setup_providers(
            [
                ("some_other_api", "other_provider"),
                ("vector_io", "vector_provider_123"),
                ("vector_io", "vector_provider_456"),
            ]
        )

        # Call the function
        result = self.setup_llama_stack("test_index")

        # Verify standard call sequence
        self.assert_standard_calls("test_index")

        # Verify vector database registration with first matching provider
        self.assert_vector_db_registration("test_index", "vector_provider_123")

        # Verify return value
        self.assertEqual(result, self.mock_client)

    def test_setup_llama_stack_no_vector_providers(self):
        """Test setup_llama_stack when no vector_io providers are found."""
        # Set up providers with no vector_io types
        self.setup_providers(
            [("some_other_api", "other_provider"), ("another_api", "another_provider")]
        )

        # Call the function and expect IndexError
        with self.assertRaises(IndexError):
            self.setup_llama_stack("test_index")

        # Verify that providers.list was called
        self.mock_client.providers.list.assert_called_once()

        # Verify that vector_dbs.register was not called
        self.mock_client.vector_dbs.register.assert_not_called()

    def test_setup_llama_stack_empty_providers_list(self):
        """Test setup_llama_stack when providers list is empty."""
        # Set up empty providers list
        self.setup_providers([])

        # Call the function and expect IndexError
        with self.assertRaises(IndexError):
            self.setup_llama_stack("test_index")

    def test_setup_llama_stack_client_initialization_failure(self):
        """Test setup_llama_stack when client initialization fails."""
        # Set up client to fail on initialization
        self.mock_client.initialize.side_effect = Exception("Initialization failed")

        # Call the function and expect the exception to propagate
        with self.assertRaises(Exception) as context:
            self.setup_llama_stack("test_index")

        self.assertEqual(str(context.exception), "Initialization failed")

        # Verify that initialize was called
        self.mock_client.initialize.assert_called_once()

    def test_setup_llama_stack_providers_list_failure(self):
        """Test setup_llama_stack when providers.list() fails."""
        # Set up providers.list to fail
        self.mock_client.providers.list.side_effect = Exception("Failed to list providers")

        # Call the function and expect the exception to propagate
        with self.assertRaises(Exception) as context:
            self.setup_llama_stack("test_index")

        self.assertEqual(str(context.exception), "Failed to list providers")

    def test_setup_llama_stack_vector_db_registration_failure(self):
        """Test setup_llama_stack when vector database registration fails."""
        # Set up a single vector_io provider
        self.setup_providers([("vector_io", "vector_provider_123")])

        # Make vector_dbs.register fail
        self.mock_client.vector_dbs.register.side_effect = Exception("Registration failed")

        # Call the function and expect the exception to propagate
        with self.assertRaises(Exception) as context:
            self.setup_llama_stack("test_index")

        self.assertEqual(str(context.exception), "Registration failed")

        # Verify that registration was attempted
        self.mock_client.vector_dbs.register.assert_called_once()

    def test_setup_llama_stack_with_different_index_names(self):
        """Test setup_llama_stack with various index names."""
        # Set up a single vector_io provider
        self.setup_providers([("vector_io", "test_provider")])

        # Test different index names
        test_indices = [
            "simple_index",
            "index-with-dashes",
            "index_with_underscores",
            "INDEX_UPPERCASE",
            "123numeric_index",
            "special.chars@index",
        ]

        for index_name in test_indices:
            with self.subTest(index=index_name):
                # Reset mock calls for each iteration
                self.mock_client.vector_dbs.register.reset_mock()

                # Call function
                result = self.setup_llama_stack(index_name)

                # Verify the index name was passed correctly
                self.assert_vector_db_registration(index_name, "test_provider")

                # Verify return value
                self.assertEqual(result, self.mock_client)

    def test_setup_llama_stack_with_multiple_vector_providers(self):
        """Test that setup_llama_stack uses the first vector_io provider when multiple exist."""
        # Set up multiple providers with vector_io providers first
        self.setup_providers(
            [
                ("vector_io", "first_vector_provider"),
                ("vector_io", "second_vector_provider"),
                ("other_api", "other_provider"),
            ]
        )

        # Call the function
        result = self.setup_llama_stack("test_index")

        # Verify it uses the first vector_io provider
        self.assert_vector_db_registration("test_index", "first_vector_provider")

        # Verify return value
        self.assertEqual(result, self.mock_client)

    def test_setup_llama_stack_fixed_parameters(self):
        """Test that setup_llama_stack uses correct fixed parameters."""
        # Set up a single vector_io provider
        self.setup_providers([("vector_io", "test_provider")])

        # Call the function
        self.setup_llama_stack("any_index")

        # Verify client was created with correct parameters
        self.assert_standard_calls("any_index")

        # Verify vector database registration uses correct fixed parameters
        self.assert_vector_db_registration("any_index", "test_provider")

    def test_setup_llama_stack_empty_index_name(self):
        """Test setup_llama_stack with empty index name."""
        # Set up a single vector_io provider
        self.setup_providers([("vector_io", "test_provider")])

        # Call the function with empty index name
        result = self.setup_llama_stack("")

        # Verify empty string is passed through
        self.assert_vector_db_registration("", "test_provider")

        # Verify return value
        self.assertEqual(result, self.mock_client)


class TestSetupLlamaStackIntegration(unittest.TestCase):
    """Integration-style tests for setup_llama_stack (with minimal mocking)."""

    def setUp(self):
        """Set up test fixtures."""
        self.module = import_module()
        self.setup_llama_stack = self.module.setup_llama_stack

        # Set up common mocks for integration tests
        self.client_patcher = patch.object(self.module, "LlamaStackAsLibraryClient")
        self.mock_client_class = self.client_patcher.start()
        self.mock_client = MagicMock()
        self.mock_client_class.return_value = self.mock_client

    def tearDown(self):
        """Clean up after each test."""
        self.client_patcher.stop()

    def create_realistic_providers(self):
        """Create realistic mock providers for integration testing."""
        providers = [
            type("Provider", (), {"api": "text_generation", "provider_id": "text_gen_1"})(),
            type("Provider", (), {"api": "vector_io", "provider_id": "vector_db_primary"})(),
            type("Provider", (), {"api": "embedding", "provider_id": "embed_1"})(),
            type("Provider", (), {"api": "vector_io", "provider_id": "vector_db_secondary"})(),
        ]
        self.mock_client.providers.list.return_value = providers
        return providers

    def test_setup_llama_stack_complete_workflow(self):
        """Test the complete workflow of setup_llama_stack."""
        # Set up realistic providers
        self.create_realistic_providers()

        # Call the function
        result = self.setup_llama_stack("production_index")

        # Verify the entire workflow
        self.mock_client_class.assert_called_once_with("./run.yaml", provider_data={})
        self.mock_client.initialize.assert_called_once()
        self.mock_client.providers.list.assert_called_once()
        self.mock_client.vector_dbs.register.assert_called_once_with(
            vector_db_id="production_index",
            provider_id="vector_db_primary",
            embedding_model="./embeddings_model",
            embedding_dimension=768,
        )

        self.assertEqual(result, self.mock_client)


if __name__ == "__main__":
    unittest.main()
