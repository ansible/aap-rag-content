# Copyright 2026 Red Hat, Inc.
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
"""Tests for update_url_reachable module."""

# pylint: disable=C0415,import-error,protected-access
import importlib
import json
import sys
from pathlib import Path

import pytest

scripts_dir = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

_mod = importlib.import_module("update_url_reachable")


def _write_metadata(path: Path, payload: dict) -> None:
    """Write a metadata JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _read_metadata(path: Path) -> dict:
    """Read a metadata JSON file."""
    return json.loads(path.read_text(encoding="utf-8"))


class TestCanonicalUrl:
    """Test cases for canonical_url()."""

    def test_strips_fragment(self):
        """Fragments are removed so section URLs share a ping result."""
        assert (
            _mod.canonical_url("https://docs.example.com/guide#section")
            == "https://docs.example.com/guide"
        )

    def test_preserves_query_string(self):
        """Query strings are kept because they can change the resource."""
        assert (
            _mod.canonical_url("https://docs.example.com/guide?lang=en#section")
            == "https://docs.example.com/guide?lang=en"
        )


class TestFindMetadataFiles:
    """Test cases for find_metadata_files()."""

    def test_finds_only_metadata_json_files(self, tmp_path):
        """JSON files outside .metadata directories are ignored."""
        meta = tmp_path / "topic" / ".metadata" / "__index__.json"
        _write_metadata(meta, {"url": "https://example.com/a", "title": "A"})
        other = tmp_path / "topic" / "not-metadata.json"
        other.write_text("{}", encoding="utf-8")

        found = _mod.find_metadata_files(tmp_path)

        assert found == [meta]


class TestUpdateMetadataFiles:
    """Test cases for update_metadata_files()."""

    def test_adds_url_reachable_and_shares_fragment_pings(self, tmp_path, mocker):
        """Files that share a document URL are pinged once and all updated."""
        index = tmp_path / "topic" / ".metadata" / "__index__.json"
        section = tmp_path / "topic" / ".metadata" / "section.json"
        other = tmp_path / "other" / ".metadata" / "__index__.json"
        _write_metadata(
            index, {"url": "https://example.com/a", "title": "Index", "path": "a"}
        )
        _write_metadata(
            section,
            {
                "url": "https://example.com/a#section",
                "title": "Section",
                "path": "a#section",
            },
        )
        _write_metadata(
            other, {"url": "https://example.com/b", "title": "Other", "path": "b"}
        )
        ping = mocker.patch.object(
            _mod,
            "check_url_reachable",
            side_effect=lambda url, retries=3: url.endswith("/a"),
        )

        stats = _mod.update_metadata_files(tmp_path, workers=2)

        pinged_urls = [call.args[0] for call in ping.call_args_list]
        assert sorted(pinged_urls) == [
            "https://example.com/a",
            "https://example.com/b",
        ]
        assert stats.files_seen == 3
        assert stats.files_updated == 3
        assert stats.unique_urls == 2
        assert _read_metadata(index)["url_reachable"] is True
        assert _read_metadata(section)["url_reachable"] is True
        assert _read_metadata(other)["url_reachable"] is False
        assert stats.unreachable_urls == ["https://example.com/b"]

    def test_missing_url_is_marked_unreachable(self, tmp_path, mocker):
        """A metadata file without a URL is stored as not reachable."""
        path = tmp_path / "topic" / ".metadata" / "__index__.json"
        _write_metadata(path, {"title": "No URL", "path": "missing"})
        ping = mocker.patch.object(_mod, "check_url_reachable", return_value=True)

        stats = _mod.update_metadata_files(tmp_path)

        ping.assert_not_called()
        assert stats.missing_url == 1
        assert stats.files_updated == 1
        assert _read_metadata(path)["url_reachable"] is False

    def test_dry_run_does_not_write(self, tmp_path, mocker):
        """Dry-run reports updates without rewriting JSON files."""
        path = tmp_path / "topic" / ".metadata" / "__index__.json"
        original = {"url": "https://example.com/a", "title": "A", "path": "a"}
        _write_metadata(path, original)
        mocker.patch.object(_mod, "check_url_reachable", return_value=True)

        stats = _mod.update_metadata_files(tmp_path, dry_run=True)

        assert stats.files_updated == 1
        assert "url_reachable" not in _read_metadata(path)

    def test_skip_existing_leaves_stored_value(self, tmp_path, mocker):
        """Existing url_reachable values are not refreshed when skipping."""
        path = tmp_path / "topic" / ".metadata" / "__index__.json"
        _write_metadata(
            path,
            {
                "url": "https://example.com/a",
                "title": "A",
                "path": "a",
                "url_reachable": False,
            },
        )
        ping = mocker.patch.object(_mod, "check_url_reachable", return_value=True)

        stats = _mod.update_metadata_files(tmp_path, skip_existing=True)

        ping.assert_not_called()
        assert stats.files_skipped == 1
        assert stats.files_updated == 0
        assert _read_metadata(path)["url_reachable"] is False

    def test_unchanged_file_is_not_rewritten(self, tmp_path, mocker):
        """Files whose stored value already matches are left untouched."""
        path = tmp_path / "topic" / ".metadata" / "__index__.json"
        _write_metadata(
            path,
            {
                "url": "https://example.com/a",
                "title": "A",
                "path": "a",
                "url_reachable": True,
            },
        )
        mocker.patch.object(_mod, "check_url_reachable", return_value=True)
        write = mocker.patch.object(_mod, "write_metadata")

        stats = _mod.update_metadata_files(tmp_path)

        write.assert_not_called()
        assert stats.files_unchanged == 1
        assert stats.files_updated == 0

    def test_invalid_json_is_counted_as_failed(self, tmp_path, mocker):
        """Unreadable metadata files are reported and skipped."""
        path = tmp_path / "topic" / ".metadata" / "__index__.json"
        path.parent.mkdir(parents=True)
        path.write_text("{not json", encoding="utf-8")
        ping = mocker.patch.object(_mod, "check_url_reachable", return_value=True)

        stats = _mod.update_metadata_files(tmp_path)

        ping.assert_not_called()
        assert stats.files_failed == 1
        assert stats.files_updated == 0

    def test_non_object_json_is_counted_as_failed(self, tmp_path, mocker):
        """A JSON array is not a metadata object and is skipped."""
        path = tmp_path / "topic" / ".metadata" / "__index__.json"
        path.parent.mkdir(parents=True)
        path.write_text("[]", encoding="utf-8")
        mocker.patch.object(_mod, "check_url_reachable", return_value=True)

        stats = _mod.update_metadata_files(tmp_path)

        assert stats.files_failed == 1


class TestMain:
    """Test cases for the CLI entry point."""

    def test_arg_parser_defaults(self):
        """The CLI defaults to aap-product-docs-plaintext with 8 workers."""
        args = _mod.build_arg_parser().parse_args([])
        assert args.folder == "aap-product-docs-plaintext"
        assert args.workers == 8
        assert args.retries == 3
        assert args.dry_run is False
        assert args.skip_existing is False

    def test_main_writes_metadata(self, tmp_path, mocker, monkeypatch, capsys):
        """main() resolves the folder and writes url_reachable."""
        monkeypatch.chdir(tmp_path)
        path = tmp_path / "docs" / ".metadata" / "__index__.json"
        _write_metadata(path, {"url": "https://example.com/a", "title": "A"})
        mocker.patch.object(_mod, "check_url_reachable", return_value=True)

        _mod.main(["--folder", "docs", "--workers", "1"])

        assert _read_metadata(path)["url_reachable"] is True
        output = capsys.readouterr().out
        assert "Updated 1" in output

    def test_main_missing_folder(self, tmp_path, monkeypatch):
        """main() exits when the target folder does not exist."""
        monkeypatch.chdir(tmp_path)
        with pytest.raises(SystemExit, match="does not exist"):
            _mod.main(["--folder", "missing"])

    def test_main_exits_on_failed_files(self, tmp_path, mocker, monkeypatch):
        """main() exits non-zero when a metadata file cannot be parsed."""
        monkeypatch.chdir(tmp_path)
        path = tmp_path / "docs" / ".metadata" / "__index__.json"
        path.parent.mkdir(parents=True)
        path.write_text("{not json", encoding="utf-8")
        mocker.patch.object(_mod, "check_url_reachable", return_value=True)

        with pytest.raises(SystemExit) as exc_info:
            _mod.main(["--folder", "docs"])
        assert exc_info.value.code == 1

    def test_main_prints_unreachable_urls(self, tmp_path, mocker, monkeypatch, capsys):
        """Unreachable URLs are listed in the CLI summary."""
        monkeypatch.chdir(tmp_path)
        path = tmp_path / "docs" / ".metadata" / "__index__.json"
        _write_metadata(path, {"url": "https://example.com/missing", "title": "Gone"})
        mocker.patch.object(_mod, "check_url_reachable", return_value=False)

        _mod.main(["--folder", "docs"])

        output = capsys.readouterr().out
        assert "Unreachable URLs:" in output
        assert "https://example.com/missing" in output
