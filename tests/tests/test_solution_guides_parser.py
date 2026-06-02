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
"""Tests for solution_guides_parser module."""
# pylint: disable=C0415,import-error,protected-access
import importlib
import json
import sys
import urllib.error
from pathlib import Path
from unittest.mock import call
from unittest.mock import patch

import pytest

scripts_dir = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

# The module file uses hyphens (solution-guides-parser.py), so we need importlib
_mod = importlib.import_module("solution-guides-parser")
SolutionGuidesParser = _mod.SolutionGuidesParser
SOURCE_FILES = _mod.SOURCE_FILES
_urllib_request = _mod.urllib.request


class TestSolutionGuidesParserInit:
    """Test cases for SolutionGuidesParser initialization."""

    def test_init_creates_directories(self, tmp_path):
        """Test __init__ creates out_dir and .metadata when they don't exist."""
        out_dir = str(tmp_path / "output")
        repo_dir = str(tmp_path / "repo")
        parser = SolutionGuidesParser(repo_dir, out_dir)

        assert Path(out_dir).is_dir()
        assert Path(out_dir, ".metadata").is_dir()
        assert parser.repo_dir == repo_dir
        assert parser.out_dir == out_dir

    def test_init_existing_directories(self, tmp_path):
        """Test __init__ succeeds when directories already exist."""
        out_dir = tmp_path / "output"
        out_dir.mkdir()
        (out_dir / ".metadata").mkdir()
        repo_dir = str(tmp_path / "repo")

        parser = SolutionGuidesParser(repo_dir, str(out_dir))
        assert parser.out_dir == str(out_dir)


class TestBuildWebUrl:
    """Test cases for _build_web_url."""

    def test_build_web_url(self, tmp_path):
        """Test URL generation from a source filename."""
        parser = SolutionGuidesParser(str(tmp_path / "repo"), str(tmp_path / "out"))
        url = parser._build_web_url("README-AIOps.md")
        assert url == "https://ansible-tmm.github.io/solution-guides/README-AIOps"

    def test_build_web_url_different_file(self, tmp_path):
        """Test URL generation with a different filename."""
        parser = SolutionGuidesParser(str(tmp_path / "repo"), str(tmp_path / "out"))
        url = parser._build_web_url("README-EDB.md")
        assert url == "https://ansible-tmm.github.io/solution-guides/README-EDB"


class TestExtractTitle:
    """Test cases for _extract_title."""

    def test_extract_title_simple(self, tmp_path):
        """Test extracting a simple H1 title."""
        parser = SolutionGuidesParser(str(tmp_path / "repo"), str(tmp_path / "out"))
        title = parser._extract_title(["# My Title\n"])
        assert title == "My Title"

    def test_extract_title_strips_html_comment(self, tmp_path):
        """Test that HTML comments are stripped from titles."""
        parser = SolutionGuidesParser(str(tmp_path / "repo"), str(tmp_path / "out"))
        title = parser._extract_title(["# Title <!-- omit in toc -->\n"])
        assert title == "Title"

    def test_extract_title_no_heading(self, tmp_path):
        """Test that None is returned when no H1 heading exists."""
        parser = SolutionGuidesParser(str(tmp_path / "repo"), str(tmp_path / "out"))
        title = parser._extract_title(["No heading here\n", "Just text\n"])
        assert title is None

    def test_extract_title_skips_non_h1(self, tmp_path):
        """Test that non-H1 headings are skipped."""
        parser = SolutionGuidesParser(str(tmp_path / "repo"), str(tmp_path / "out"))
        title = parser._extract_title(["## H2 heading\n", "# H1 heading\n"])
        assert title == "H1 heading"


class TestParseFile:
    """Test cases for _parse_file."""

    def test_parse_file_strips_html_img(self, tmp_path):
        """Test that HTML img tags are removed from output."""
        repo_dir = tmp_path / "repo"
        out_dir = tmp_path / "out"
        repo_dir.mkdir()
        source = repo_dir / "test.md"
        source.write_text(
            '# Title\nBefore <img src="x.png" alt="y"> After\n',
            encoding="utf-8",
        )

        parser = SolutionGuidesParser(str(repo_dir), str(out_dir))
        parser._parse_file("test.md")

        result = (out_dir / "test.md").read_text(encoding="utf-8")
        assert "<img" not in result
        assert "Before  After" in result

    def test_parse_file_strips_markdown_image(self, tmp_path):
        """Test that markdown images ![alt](url) are removed from output."""
        repo_dir = tmp_path / "repo"
        out_dir = tmp_path / "out"
        repo_dir.mkdir()
        source = repo_dir / "test.md"
        source.write_text(
            "# Title\nSee ![alt text](https://example.com/img.png) here\n",
            encoding="utf-8",
        )

        parser = SolutionGuidesParser(str(repo_dir), str(out_dir))
        parser._parse_file("test.md")

        result = (out_dir / "test.md").read_text(encoding="utf-8")
        assert "![" not in result
        assert "See  here" in result

    def test_parse_file_strips_linked_image(self, tmp_path):
        """Test that linked images [![alt](img)](link) are removed."""
        repo_dir = tmp_path / "repo"
        out_dir = tmp_path / "out"
        repo_dir.mkdir()
        source = repo_dir / "test.md"
        source.write_text(
            "# Title\n[![diagram](img.png)](https://link.com)\n",
            encoding="utf-8",
        )

        parser = SolutionGuidesParser(str(repo_dir), str(out_dir))
        parser._parse_file("test.md")

        result = (out_dir / "test.md").read_text(encoding="utf-8")
        assert "[![" not in result
        assert "![" not in result

    def test_parse_file_writes_metadata_json(self, tmp_path):
        """Test that metadata JSON is written with correct title, url, path."""
        repo_dir = tmp_path / "repo"
        out_dir = tmp_path / "out"
        repo_dir.mkdir()
        source = repo_dir / "README-AIOps.md"
        source.write_text("# AIOps Guide\nContent here.\n", encoding="utf-8")

        parser = SolutionGuidesParser(str(repo_dir), str(out_dir))
        parser._parse_file("README-AIOps.md")

        metadata_file = out_dir / ".metadata" / "README-AIOps.json"
        assert metadata_file.exists()

        metadata = json.loads(metadata_file.read_text(encoding="utf-8"))
        assert metadata["title"] == "AIOps Guide"
        assert metadata["url"] == "https://ansible-tmm.github.io/solution-guides/README-AIOps"
        assert metadata["path"] == "README-AIOps.md"

    def test_parse_file_missing_source(self, tmp_path, capsys):
        """Test that a warning is printed for missing source files."""
        repo_dir = tmp_path / "repo"
        out_dir = tmp_path / "out"
        repo_dir.mkdir()

        parser = SolutionGuidesParser(str(repo_dir), str(out_dir))
        parser._parse_file("nonexistent.md")

        captured = capsys.readouterr()
        assert "Warning" in captured.out
        assert "nonexistent.md" in captured.out
        assert not (out_dir / "nonexistent.md").exists()
        assert not (out_dir / ".metadata" / "nonexistent.json").exists()

    def test_parse_file_preserves_non_image_content(self, tmp_path):
        """Test that non-image markdown content passes through unchanged."""
        repo_dir = tmp_path / "repo"
        out_dir = tmp_path / "out"
        repo_dir.mkdir()
        content = (
            "# Main Title\n"
            "## Section\n"
            "Regular paragraph text.\n"
            "[A link](https://example.com)\n"
            "- bullet point\n"
            "```python\ncode block\n```\n"
        )
        source = repo_dir / "test.md"
        source.write_text(content, encoding="utf-8")

        parser = SolutionGuidesParser(str(repo_dir), str(out_dir))
        parser._parse_file("test.md")

        result = (out_dir / "test.md").read_text(encoding="utf-8")
        assert result == content

    def test_run_calls_parse_for_all_source_files(self, tmp_path):
        """Test run() calls _parse_file once per entry in SOURCE_FILES."""
        parser = SolutionGuidesParser(str(tmp_path / "repo"), str(tmp_path / "out"))

        with patch.object(parser, "_parse_file") as mock_parse:
            parser.run()

            assert mock_parse.call_count == len(SOURCE_FILES)
            expected_calls = [call(f) for f in SOURCE_FILES]
            mock_parse.assert_has_calls(expected_calls, any_order=False)


class TestDownloadFiles:
    """Test cases for download_files."""

    def test_download_files_success(self, tmp_path):
        """Test urlopen is called for each SOURCE_FILES entry."""
        repo_dir = tmp_path / "repo"
        parser = SolutionGuidesParser(str(repo_dir), str(tmp_path / "out"))

        with patch.object(_urllib_request, "urlopen") as mock_urlopen:
            mock_urlopen.return_value.__enter__ = lambda s: s
            mock_urlopen.return_value.__exit__ = lambda s, *a: None
            mock_urlopen.return_value.read = lambda size=-1: b""
            with patch("builtins.open", create=True):
                with patch.object(_mod.shutil, "copyfileobj"):
                    parser.download_files()

            assert mock_urlopen.call_count == len(SOURCE_FILES)
            for source_file in SOURCE_FILES:
                expected_url = (
                    "https://raw.githubusercontent.com/ansible-tmm/solution-guides/main/"
                    + source_file
                )
                mock_urlopen.assert_any_call(expected_url, timeout=30)

    def test_download_files_http_error_aborts(self, tmp_path, capsys):
        """Test that download failures cause sys.exit(1)."""
        repo_dir = tmp_path / "repo"
        parser = SolutionGuidesParser(str(repo_dir), str(tmp_path / "out"))

        def side_effect(url, timeout=None):  # pylint: disable=unused-argument
            if "README-AIOps.md" in url:
                raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
            mock_resp = type(
                "Resp",
                (),
                {
                    "__enter__": lambda s: s,
                    "__exit__": lambda s, *a: None,
                    "read": lambda s, size=-1: b"",
                },
            )()
            return mock_resp

        with (
            patch.object(
                _urllib_request,
                "urlopen",
                side_effect=side_effect,
            ),
            patch.object(_mod.shutil, "copyfileobj"),
            pytest.raises(SystemExit, match="1"),
        ):
            parser.download_files()

        captured = capsys.readouterr()
        assert "ERROR" in captured.err
        assert "README-AIOps.md" in captured.err
        assert "Aborting" in captured.err

    def test_download_files_timeout_aborts(self, tmp_path, capsys):
        """Test that a timeout causes sys.exit(1)."""
        repo_dir = tmp_path / "repo"
        parser = SolutionGuidesParser(str(repo_dir), str(tmp_path / "out"))

        def side_effect(url, timeout=None):  # pylint: disable=unused-argument
            if "README-EDB.md" in url:
                raise TimeoutError("timed out")
            mock_resp = type(
                "Resp",
                (),
                {
                    "__enter__": lambda s: s,
                    "__exit__": lambda s, *a: None,
                    "read": lambda s, size=-1: b"",
                },
            )()
            return mock_resp

        with (
            patch.object(
                _urllib_request,
                "urlopen",
                side_effect=side_effect,
            ),
            patch.object(_mod.shutil, "copyfileobj"),
            pytest.raises(SystemExit, match="1"),
        ):
            parser.download_files()

        captured = capsys.readouterr()
        assert "ERROR" in captured.err
        assert "README-EDB.md" in captured.err

    def test_download_files_url_error_aborts(self, tmp_path, capsys):
        """Test that URLError (DNS/connection) causes sys.exit(1)."""
        repo_dir = tmp_path / "repo"
        parser = SolutionGuidesParser(str(repo_dir), str(tmp_path / "out"))

        def side_effect(url, timeout=None):
            raise urllib.error.URLError("Name resolution failed")

        with (
            patch.object(
                _urllib_request,
                "urlopen",
                side_effect=side_effect,
            ),
            pytest.raises(SystemExit, match="1"),
        ):
            parser.download_files()

        captured = capsys.readouterr()
        assert "ERROR" in captured.err
        assert f"{len(SOURCE_FILES)} download(s) failed" in captured.err

    def test_download_files_creates_repo_dir(self, tmp_path):
        """Test that repo_dir is created if it doesn't exist."""
        repo_dir = tmp_path / "new_repo"
        assert not repo_dir.exists()

        parser = SolutionGuidesParser(str(repo_dir), str(tmp_path / "out"))

        with patch.object(_urllib_request, "urlopen") as mock_urlopen:
            mock_urlopen.return_value.__enter__ = lambda s: s
            mock_urlopen.return_value.__exit__ = lambda s, *a: None
            with patch.object(_mod.shutil, "copyfileobj"):
                parser.download_files()

        assert repo_dir.is_dir()
