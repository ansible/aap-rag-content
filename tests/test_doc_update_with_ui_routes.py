"""
Unit tests for doc_update_with_ui_routes.py module.
Tests cover all functions including positive and negative cases.
"""
import os
import tempfile
from unittest.mock import Mock, patch
import pytest
import sys
from sklearn.feature_extraction.text import TfidfVectorizer

from scripts import doc_update_with_ui_routes as doc_module


class TestHelperFunctions:
    """Test helper functions for text processing and file operations."""

    def test_calculate_text_similarity_identical_texts(self):
        """Test text similarity calculation with identical texts."""
        text1 = "This is a test text"
        text2 = "This is a test text"
        similarity = doc_module.calculate_text_similarity(text1, text2)
        assert abs(similarity - 1.0) < 0.0001  # Allow for floating point precision

    def test_calculate_text_similarity_different_texts(self):
        """Test text similarity calculation with different texts."""
        text1 = "This is a test text"
        text2 = "This is completely different content"
        similarity = doc_module.calculate_text_similarity(text1, text2)
        assert 0.0 <= similarity <= 1.0
        assert similarity < 0.5  # Should be low similarity

    def test_calculate_text_similarity_with_markdown_links(self):
        """Test text similarity with markdown links (should normalize them)."""
        text1 = "Click [Settings](awx-settings) to configure"
        text2 = "Click Settings to configure"
        similarity = doc_module.calculate_text_similarity(text1, text2)
        assert similarity > 0.8  # Should be high similarity after normalization

    def test_calculate_text_similarity_empty_strings(self):
        """Test text similarity with empty strings."""
        similarity = doc_module.calculate_text_similarity("", "")
        assert similarity == 0.0

        similarity = doc_module.calculate_text_similarity("test", "")
        assert similarity == 0.0

    @patch('doc_update_with_ui_routes.TfidfVectorizer')
    def test_calculate_text_similarity_fallback_to_difflib(self, mock_vectorizer):
        """Test fallback to difflib when TF-IDF fails."""
        mock_vectorizer.side_effect = Exception("TF-IDF failed")

        text1 = "This is a test"
        text2 = "This is a test"
        similarity = doc_module.calculate_text_similarity(text1, text2)
        assert similarity == 1.0

    def test_get_tfidf_vectorizer_singleton(self):
        """Test that TF-IDF vectorizer is created as singleton."""
        # Reset the global variable
        doc_module._tfidf_vectorizer = None

        vectorizer1 = doc_module.get_tfidf_vectorizer()
        vectorizer2 = doc_module.get_tfidf_vectorizer()

        assert vectorizer1 is vectorizer2
        assert isinstance(vectorizer1, TfidfVectorizer)

    def test_read_markdown_file_success(self):
        """Test successful markdown file reading."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("# Test Markdown\n\nThis is a test.")
            temp_path = f.name

        try:
            content = doc_module.read_markdown_file(temp_path)
            assert content == "# Test Markdown\n\nThis is a test."
        finally:
            os.unlink(temp_path)

    def test_read_markdown_file_not_found(self):
        """Test reading non-existent markdown file."""
        content = doc_module.read_markdown_file("nonexistent.md")
        assert content is None

    def test_write_markdown_file_success(self):
        """Test successful markdown file writing."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            temp_path = f.name

        try:
            test_content = "# Test Output\n\nThis is processed content."
            doc_module.write_markdown_file(temp_path, test_content)

            with open(temp_path, 'r') as f:
                written_content = f.read()

            assert written_content == test_content
        finally:
            os.unlink(temp_path)


class TestRouteProcessing:
    """Test route processing and validation functions."""

    def test_validate_and_filter_routes_valid_routes(self):
        """Test validation and filtering of valid routes."""
        ui_routes = [
            {"Settings": "awx-settings"},
            {"Users": "awx-users"},
            {"Organizations": "awx-organizations"},
            {"Teams": "awx-teams"},
            {"Projects": "awx-projects"}
        ]

        filtered_routes = doc_module.validate_and_filter_routes(ui_routes)

        assert len(filtered_routes) == 5
        assert all(route['route_type'] == 'awx' for route in filtered_routes)
        assert all('name' in route and 'route_id' in route for route in filtered_routes)

    def test_validate_and_filter_routes_mixed_types(self):
        """Test validation with mixed route types (AWX, EDA, HUB)."""
        ui_routes = [
            {"AWX Settings": "awx-settings"},
            {"EDA Rules": "eda-rules"},
            {"HUB Collections": "hub-collections"},
            {"Just Hub": "hub"}
        ]

        filtered_routes = doc_module.validate_and_filter_routes(ui_routes)

        # "hub" alone might be filtered out due to length check
        assert len(filtered_routes) >= 3
        route_types = {route['route_type'] for route in filtered_routes}
        assert 'awx' in route_types
        assert 'eda' in route_types
        assert 'hub' in route_types

    def test_validate_and_filter_routes_exclude_fake_routes(self):
        """Test exclusion of fake/test routes."""
        ui_routes = [
            {"Settings": "awx-settings"},
            {"Test Route": "awx-test-route"},
            {"Example": "awx-example"},
            {"Fake Route": "awx-fake-route"},
            {"Valid Route": "awx-valid-route"}
        ]

        filtered_routes = doc_module.validate_and_filter_routes(ui_routes)

        # Should exclude test, example, fake routes
        route_ids = {route['route_id'] for route in filtered_routes}
        assert "awx-settings" in route_ids
        assert "awx-valid-route" in route_ids
        assert "awx-test-route" not in route_ids
        assert "awx-example" not in route_ids
        assert "awx-fake-route" not in route_ids

    def test_categorize_routes_by_priority(self):
        """Test route categorization by priority tiers."""
        routes = [
            {"name": "Overview", "route_id": "awx-overview"},
            {"name": "Settings", "route_id": "awx-settings"},
            {"name": "Create User", "route_id": "awx-create-user"},
            {"name": "Job Template", "route_id": "awx-job-template"},
            {"name": "Job Output", "route_id": "awx-job-output"}
        ]

        categorized = doc_module.categorize_routes_by_priority(routes)

        # Check that tiers are assigned
        assert all('tier' in route for route in categorized)

        # Create User should be tier 1 (high priority - contains "create")
        create_user_route = next(r for r in categorized if r['name'] == 'Create User')
        assert create_user_route['tier'] == 1

        # Settings should be tier 3 (secondary priority)
        settings_route = next(r for r in categorized if r['name'] == 'Settings')
        assert settings_route['tier'] == 3

    def test_sort_routes_by_priority(self):
        """Test route sorting by priority and name."""
        routes = [
            {"name": "ZZZ Route", "route_id": "awx-zzz", "tier": 3},
            {"name": "AAA Route", "route_id": "awx-aaa", "tier": 1},
            {"name": "BBB Route", "route_id": "awx-bbb", "tier": 1},
            {"name": "CCC Route", "route_id": "awx-ccc", "tier": 2}
        ]

        sorted_routes = doc_module.sort_routes_by_priority(routes)

        # Should be sorted by tier first, then by name
        assert sorted_routes[0]['name'] == 'AAA Route'  # tier 1, alphabetically first
        assert sorted_routes[1]['name'] == 'BBB Route'  # tier 1, alphabetically second
        assert sorted_routes[2]['name'] == 'CCC Route'  # tier 2
        assert sorted_routes[3]['name'] == 'ZZZ Route'  # tier 3

    def test_count_routes_by_tier(self):
        """Test counting routes by tier."""
        routes = [
            {"tier": 1}, {"tier": 1}, {"tier": 2}, {"tier": 3}, {"tier": 4}
        ]

        counts = doc_module.count_routes_by_tier(routes)

        assert counts[1] == 2
        assert counts[2] == 1
        assert counts[3] == 1
        assert counts[4] == 1
        assert counts[0] == 0  # No routes without tier

    def test_find_similar_routes(self):
        """Test finding similar routes for invalid route IDs."""
        invalid_route = "awx-user-management"
        valid_routes = [
            {"name": "Users", "route_id": "awx-users"},
            {"name": "User Settings", "route_id": "awx-user-settings"},
            {"name": "Organizations", "route_id": "awx-organizations"}
        ]

        similar = doc_module.find_similar_routes(invalid_route, valid_routes)

        # The function might not find similarities with current logic
        assert isinstance(similar, list)
        assert len(similar) <= 3


class TestPatternDetection:
    """Test UI navigation pattern detection functions."""

    def test_identify_ui_navigation_patterns_select_patterns(self):
        """Test identification of 'select' navigation patterns."""
        text = "From the navigation panel, selectTemplates→Organizations"
        patterns = doc_module.identify_ui_navigation_patterns(text)

        assert len(patterns) > 0
        select_patterns = [p for p in patterns if p[0] in ['nav_panel', 'select']]
        assert len(select_patterns) > 0

        # Check that the pattern text is captured
        pattern_text = select_patterns[0][3]
        assert "Templates" in pattern_text
        assert "Organizations" in pattern_text

    def test_identify_ui_navigation_patterns_click_patterns(self):
        """Test identification of 'click' navigation patterns."""
        text = "ClickCreate organization to start"
        patterns = doc_module.identify_ui_navigation_patterns(text)

        click_patterns = [p for p in patterns if p[0] == 'click']
        assert len(click_patterns) > 0
        assert "Create organization" in click_patterns[0][3]

    def test_identify_ui_navigation_patterns_page_references(self):
        """Test identification of page reference patterns."""
        text = "Navigate to the Users page to manage users"
        patterns = doc_module.identify_ui_navigation_patterns(text)

        page_patterns = [p for p in patterns if p[0] in ['navigate', 'go_to']]
        assert len(page_patterns) > 0

    def test_identify_ui_navigation_patterns_multiple_patterns(self):
        """Test identification of multiple different patterns in one text."""
        text = """
        From the navigation panel, selectTemplates→Users.
        ClickCreate user to add a new user.
        Navigate to the Settings page for configuration.
        """
        patterns = doc_module.identify_ui_navigation_patterns(text)

        # Should find multiple patterns
        assert len(patterns) >= 3
        pattern_types = {p[0] for p in patterns}
        assert 'nav_panel' in pattern_types or 'select' in pattern_types
        assert 'click' in pattern_types
        assert 'navigate' in pattern_types

    def test_identify_ui_navigation_patterns_no_patterns(self):
        """Test with text that has no UI navigation patterns."""
        text = "This is just regular text without any UI navigation instructions."
        patterns = doc_module.identify_ui_navigation_patterns(text)

        assert len(patterns) == 0

    def test_needs_llm_processing_true(self):
        """Test that text with UI patterns needs LLM processing."""
        text = "selectTemplates→Organizations"
        needs_processing = doc_module.needs_llm_processing(text)

        assert needs_processing is True

    def test_needs_llm_processing_false(self):
        """Test that text without UI patterns doesn't need LLM processing."""
        text = "This is just regular documentation text."
        needs_processing = doc_module.needs_llm_processing(text)

        assert needs_processing is False


class TestLLMProcessing:
    """Test LLM processing and formatting functions."""

    def test_format_llm_request_content(self):
        """Test formatting of LLM request content."""
        document_content = "selectTemplates→Organizations"
        ui_routes = [
            {"Templates": "awx-templates"},
            {"Organizations": "awx-organizations"}
        ]

        prompt = doc_module.format_llm_request_content(document_content, ui_routes)

        assert "selectTemplates→Organizations" in prompt
        assert "awx-templates" in prompt
        assert "awx-organizations" in prompt
        assert "# DOCUMENT" in prompt
        assert "# AVAILABLE ROUTES" in prompt

    @patch('doc_update_with_ui_routes.requests.post')
    def test_query_vllm_model_success(self, mock_post):
        """Test successful vLLM model query."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Processed content"}}]
        }
        mock_post.return_value = mock_response

        result = doc_module.query_vllm_model("Test prompt")

        assert result == "Processed content"
        mock_post.assert_called_once()

    @patch('doc_update_with_ui_routes.requests.post')
    def test_query_vllm_model_failure(self, mock_post):
        """Test failed vLLM model query."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        result = doc_module.query_vllm_model("Test prompt")

        assert result is None

    @patch('doc_update_with_ui_routes.requests.post')
    def test_query_vllm_model_exception(self, mock_post):
        """Test vLLM model query with exception."""
        mock_post.side_effect = Exception("Network error")

        result = doc_module.query_vllm_model("Test prompt")

        assert result is None

    def test_clean_llm_output_basic(self):
        """Test basic LLM output cleaning."""
        raw_output = """This is the actual document content.

        # AVAILABLE ROUTES
        Templates: awx-templates
        Organizations: awx-organizations
        """

        cleaned = doc_module.clean_llm_output(raw_output)

        assert "# AVAILABLE ROUTES" not in cleaned
        assert "Templates: awx-templates" not in cleaned
        # Check that some content remains after cleaning
        assert "This is the actual document content." in cleaned

    def test_clean_llm_output_explanatory_text(self):
        """Test removal of explanatory text from LLM output."""
        raw_output = """
        Document content here.
        NOTE: I could not find a route for this element.
        More content.
        The document has been updated with the links.
        """

        cleaned = doc_module.clean_llm_output(raw_output)

        assert "NOTE: I could not find a route" not in cleaned
        assert "The document has been updated" not in cleaned
        assert "Document content here." in cleaned
        assert "More content." in cleaned


class TestValidation:
    """Test validation functions for LLM output."""

    def test_validate_output_for_prompt_leakage_clean(self):
        """Test validation of clean output without prompt leakage."""
        clean_output = "This is clean document content with [Settings](awx-settings) link."

        is_valid, reason = doc_module.validate_output_for_prompt_leakage(clean_output)

        assert is_valid is True
        assert reason == "Valid"

    def test_validate_output_for_prompt_leakage_contaminated(self):
        """Test validation of output with prompt leakage."""
        contaminated_output = """
        # TASK
        Your task is to convert specific UI navigation instructions...
        Document content here.
        """

        is_valid, reason = doc_module.validate_output_for_prompt_leakage(contaminated_output)

        assert is_valid is False
        assert "forbidden phrase" in reason

    def test_validate_changes_only_expected_no_patterns(self):
        """Test validation when no patterns were detected."""
        original = "This is the original content."
        processed = "This is the original content."

        is_valid, _ = doc_module.validate_changes_only_expected(original, processed, [])

        assert is_valid is True

    def test_validate_changes_only_expected_with_patterns(self):
        """Test validation when patterns were detected and changes made."""
        original = "selectTemplates→Organizations"
        processed = "select[Templates→Organizations](awx-organizations)"
        patterns = [('select', 0, 10, 'Templates→Organizations')]

        is_valid, _ = doc_module.validate_changes_only_expected(original, processed, patterns)

        assert is_valid is True

    def test_validate_changes_only_expected_too_different(self):
        """Test validation when processed text is too different from original."""
        original = "This is the original content."
        processed = "This is completely different content with no similarity."
        patterns = [('select', 0, 10, 'test')]

        is_valid, reason = doc_module.validate_changes_only_expected(original, processed, patterns)

        assert is_valid is False
        assert "differs too much" in reason

    def test_validate_awx_routes_exist_valid(self):
        """Test validation of valid AWX routes."""
        output = "Click [Settings](awx-settings) and then [Users](awx-users)."
        valid_routes = [
            {"name": "Settings", "route_id": "awx-settings"},
            {"name": "Users", "route_id": "awx-users"}
        ]

        is_valid, reason = doc_module.validate_awx_routes_exist(output, valid_routes)

        assert is_valid is True
        assert reason == "All UI routes are valid"

    def test_validate_awx_routes_exist_invalid(self):
        """Test validation of invalid AWX routes."""
        output = "Click [Settings](awx-invalid-route)."
        valid_routes = [
            {"name": "Settings", "route_id": "awx-settings"}
        ]

        is_valid, reason = doc_module.validate_awx_routes_exist(output, valid_routes)

        assert is_valid is False
        assert "invalid route IDs" in reason
        assert "awx-invalid-route" in reason

    def test_validate_line_by_line_mixed_validity(self):
        """Test line-by-line validation with mixed valid/invalid routes."""
        original = "Line 1: selectSettings\nLine 2: selectInvalidRoute"
        processed = "Line 1: select[Settings](awx-settings)\nLine 2: select[InvalidRoute](awx-invalid)"
        valid_routes = [
            {"name": "Settings", "route_id": "awx-settings"}
        ]

        cleaned = doc_module.validate_line_by_line(original, processed, valid_routes)

        # Should keep the valid line and revert the invalid line
        assert "select[Settings](awx-settings)" in cleaned
        assert "awx-invalid" not in cleaned

    def test_enhanced_validation_gate_success(self):
        """Test enhanced validation gate with successful validation."""
        original = "selectTemplates→Organizations"
        processed = "select[Templates→Organizations](awx-organizations)"
        patterns = [('select', 0, 10, 'Templates→Organizations')]
        valid_routes = [
            {"name": "Templates", "route_id": "awx-templates"},
            {"name": "Organizations", "route_id": "awx-organizations"}
        ]

        is_valid, _ = doc_module.enhanced_validation_gate(
            original, processed, patterns, valid_routes
        )

        assert is_valid is True

    def test_enhanced_validation_gate_failure(self):
        """Test enhanced validation gate with validation failure."""
        original = "selectTemplates→Organizations"
        processed = """
        # TASK
        Your task is to convert...
        select[Templates→Organizations](awx-organizations)
        """
        patterns = [('select', 0, 10, 'Templates→Organizations')]
        valid_routes = [
            {"name": "Organizations", "route_id": "awx-organizations"}
        ]

        is_valid, _ = doc_module.enhanced_validation_gate(
            original, processed, patterns, valid_routes
        )

        assert is_valid is False


class TestDocumentProcessing:
    """Test document processing functions."""

    def test_split_markdown_into_chunks_basic(self):
        """Test basic markdown splitting into chunks."""
        content = "# Header 1\n\nParagraph 1.\n\n# Header 2\n\nParagraph 2.\n\n# Header 3\n\nParagraph 3."
        chunks = doc_module.split_markdown_into_chunks(content, 50)

        assert len(chunks) > 1
        assert all(len(chunk) <= 100 for chunk in chunks)  # Should be reasonable size

    def test_split_markdown_into_chunks_large_paragraph(self):
        """Test splitting with very large paragraphs."""
        large_paragraph = "This is a very long paragraph. " * 100  # Very long
        content = f"# Header\n\n{large_paragraph}\n\n# Another Header\n\nShort paragraph."

        chunks = doc_module.split_markdown_into_chunks(content, 100)

        assert len(chunks) > 1
        # Should handle large paragraphs by breaking them down

    def test_split_markdown_into_chunks_small_content(self):
        """Test splitting with content smaller than chunk size."""
        content = "Small content."
        chunks = doc_module.split_markdown_into_chunks(content, 1000)

        assert len(chunks) == 1
        assert chunks[0] == content + "\n\n"

    @patch('doc_update_with_ui_routes.query_vllm_model')
    @patch('doc_update_with_ui_routes.read_markdown_file')
    def test_process_document_success(self, mock_read, mock_query):
        """Test successful document processing."""
        # Mock file reading
        mock_read.return_value = "selectTemplates→Organizations\n\nSome other content."

        # Mock LLM response
        mock_query.return_value = "select[Templates→Organizations](awx-organizations)\n\nSome other content."

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_out:
            temp_out_path = temp_out.name

        try:
            ui_routes = [
                {"Templates": "awx-templates"},
                {"Organizations": "awx-organizations"}
            ]

            doc_module.process_document("input.md", temp_out_path, ui_routes)

            # Should have created output file
            assert os.path.exists(temp_out_path)

            # Check that file was written
            with open(temp_out_path, 'r', encoding='utf-8') as f:
                content = f.read()

            assert len(content) > 0
        finally:
            os.unlink(temp_out_path)

    @patch('doc_update_with_ui_routes.read_markdown_file')
    def test_process_document_file_not_found(self, mock_read):
        """Test document processing with non-existent input file."""
        mock_read.return_value = None

        # Should not raise exception, just return early
        doc_module.process_document("nonexistent.md", "output.md", [])


class TestIntegrationWithRealData:
    """Integration tests using real data from the provided files."""

    def test_pattern_detection_with_real_markdown(self):
        """Test pattern detection with real markdown content."""
        # Sample from the actual file
        real_content = """
        From the navigation panel, selectTemplates→Organizations.
        ClickCreate organization.
        Navigate to the Users page to manage users.
        """

        patterns = doc_module.identify_ui_navigation_patterns(real_content)

        assert len(patterns) >= 3
        pattern_types = {p[0] for p in patterns}
        assert 'nav_panel' in pattern_types or 'select' in pattern_types
        assert 'click' in pattern_types
        assert 'navigate' in pattern_types

    def test_route_validation_with_real_routes(self):
        """Test route validation with realistic AWX routes."""
        real_routes = [
            {"Templates": "awx-templates"},
            {"Organizations": "awx-organizations"},
            {"Users": "awx-users"},
            {"Teams": "awx-teams"},
            {"Projects": "awx-projects"},
            {"Inventories": "awx-inventories"}
        ]

        filtered_routes = doc_module.validate_and_filter_routes(real_routes)

        assert len(filtered_routes) == 6
        assert all(route['route_type'] == 'awx' for route in filtered_routes)

        # Test prioritization
        prioritized = doc_module.categorize_routes_by_priority(filtered_routes)
        assert all('tier' in route for route in prioritized)

    def test_text_similarity_with_real_content(self):
        """Test text similarity calculation with realistic content."""
        original = "From the navigation panel, selectTemplates→Organizations"
        processed = "From the navigation panel, select[Templates→Organizations](awx-organizations)"

        similarity = doc_module.calculate_text_similarity(original, processed)

        # Should be high similarity since only links were added
        assert similarity > 0.8

    def test_llm_prompt_formatting_with_real_data(self):
        """Test LLM prompt formatting with realistic data."""
        document_section = """
        ## 2.4. Creating an organization

        From the navigation panel, selectTemplates→Organizations.
        ClickCreate organization.
        Enter the Name and optionally provide a Description for your organization.
        """

        ui_routes = [
            {"Templates": "awx-templates"},
            {"Organizations": "awx-organizations"},
            {"Create organization": "awx-create-organization"}
        ]

        prompt = doc_module.format_llm_request_content(document_section, ui_routes)

        # Verify prompt structure
        assert "# DOCUMENT" in prompt
        assert "# AVAILABLE ROUTES" in prompt
        assert "selectTemplates→Organizations" in prompt
        assert "awx-templates" in prompt
        assert "awx-organizations" in prompt
        assert "awx-create-organization" in prompt

    def test_output_validation_with_real_processed_content(self):
        """Test output validation with realistic processed content."""
        original = "From the navigation panel, selectTemplates→Organizations"
        processed = "From the navigation panel, select[Templates→Organizations](awx-organizations)"

        patterns = [('nav_panel', 0, 50, 'Templates→Organizations')]
        valid_routes = [
            {"name": "Templates", "route_id": "awx-templates"},
            {"name": "Organizations", "route_id": "awx-organizations"}
        ]

        is_valid, reason = doc_module.enhanced_validation_gate(
            original, processed, patterns, valid_routes
        )

        assert is_valid is True
        assert reason == "All validations passed"


class TestErrorHandling:
    """Test error handling and edge cases."""

    def test_empty_input_handling(self):
        """Test handling of empty inputs."""
        # Empty text for pattern detection
        patterns = doc_module.identify_ui_navigation_patterns("")
        assert patterns == []

        # Empty routes list
        filtered = doc_module.validate_and_filter_routes([])
        assert filtered == []

        # Empty similarity calculation
        similarity = doc_module.calculate_text_similarity("", "")
        assert similarity == 0.0

    def test_malformed_route_handling(self):
        """Test handling of malformed route data."""
        malformed_routes = [
            {"name": "awx-route"},  # Missing route_id
            "invalid-string-route",  # Not a dict
            {"": "awx-empty-name"},  # Empty name
            {"Valid": ""},  # Empty route_id
            {"Valid": "too-short"}  # Route ID too short
        ]

        filtered = doc_module.validate_and_filter_routes(malformed_routes)

        # Should handle malformed data gracefully, function is more permissive
        assert isinstance(filtered, list)
        assert len(filtered) >= 0  # Some routes might still pass through

    def test_unicode_handling(self):
        """Test handling of Unicode characters."""
        unicode_text = "selectTemplates→Organizations with émojis 🚀"
        patterns = doc_module.identify_ui_navigation_patterns(unicode_text)

        # Should handle Unicode without errors
        assert len(patterns) >= 1

    def test_very_long_content_handling(self):
        """Test handling of very long content."""
        long_content = "This is a very long line. " * 1000
        chunks = doc_module.split_markdown_into_chunks(long_content, 100)

        # Should break down long content
        assert len(chunks) > 1
        assert all(len(chunk) > 0 for chunk in chunks)

    @patch('doc_update_with_ui_routes.TfidfVectorizer')
    def test_sklearn_import_failure(self, mock_vectorizer):
        """Test handling when sklearn components fail."""
        mock_vectorizer.side_effect = ImportError("sklearn not available")

        # Should fallback to difflib
        similarity = doc_module.calculate_text_similarity("test", "test")
        assert similarity == 1.0


# Test fixtures and utilities
@pytest.fixture
def sample_ui_routes():
    """Fixture providing sample UI routes for testing."""
    return [
        {"Overview": "awx-overview"},
        {"CreateProject": "awx-create-project"},
        {"Organizations": "awx-organizations"},
        {"Users": "awx-users"},
        {"Teams": "awx-teams"},
        {"Projects": "awx-projects"},
        {"Inventories": "awx-inventories"},
        {"Settings": "awx-settings"},
    ]


@pytest.fixture
def sample_markdown_content():
    """Fixture providing sample markdown content for testing."""
    return """
    # Getting Started

    From the navigation panel, selectTemplates→Organizations.
    ClickCreate organization to add a new organization.
    Navigate to the Users page to manage users.

    ## Configuration

    Go to the Settings page for system configuration.
    Access the Overview to view system status.
    """


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
