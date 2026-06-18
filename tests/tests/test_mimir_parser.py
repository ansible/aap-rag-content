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
"""Tests for mimir-parser module."""
# pylint: disable=C0415,import-error,protected-access
import importlib
import json
import sys
from pathlib import Path

scripts_dir = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

_mod = importlib.import_module("mimir-parser")
DocFinder = _mod.DocFinder
MimirParser = _mod.MimirParser
PRODUCTS_TO_BE_INCLUDED = _mod.PRODUCTS_TO_BE_INCLUDED

SAMPLE_MD_HEADER = """\
+++
title = "Test Document"
path = "/docs/test"

[extra]
reference_url = "https://docs.example.com/test"
+++
"""

SAMPLE_KB_HEADER = """\
+++
title = "'''KB Article Title'''"
path = "/solutions/test"

[extra]
reference_url = "https://docs.example.com/solutions/test"
products = "["Red Hat Ansible Automation Platform"]"
+++
"""

SAMPLE_KB_HEADER_WRONG_PRODUCT = """\
+++
title = "'''Other Article'''"
path = "/solutions/other"

[extra]
reference_url = "https://docs.example.com/solutions/other"
products = "["Some Other Product"]"
+++
"""

SAMPLE_TOC = {
    "sections": [
        {
            "title": "Chapter One",
            "visible": True,
            "weight": 1,
            "urlFragment": "chapter-one",
            "anchor": "chapter-one",
            "singlePageAnchor": "chapter-one",
            "sections": [
                {
                    "title": "Section 1.1",
                    "visible": True,
                    "weight": 1,
                    "urlFragment": "section-1-1",
                    "anchor": "section-1-1",
                    "singlePageAnchor": "section-1-1",
                    "sections": [],
                }
            ],
        },
        {
            "title": "Chapter Two",
            "visible": True,
            "weight": 2,
            "urlFragment": "chapter-two",
            "anchor": "chapter-two",
            "singlePageAnchor": "chapter-two",
            "sections": [],
        },
    ]
}


def make_pantheon_tree(base, toc_data, md_content):
    """Create a Pantheon-format directory tree under base."""
    base = Path(base)
    toc_dir = base / "toc"
    toc_dir.mkdir(parents=True)
    (toc_dir / "toc.json").write_text(json.dumps(toc_data), encoding="utf-8")

    sp_dir = base / "single-page"
    sp_dir.mkdir()
    (sp_dir / "doc.md").write_text(md_content, encoding="utf-8")
    return str(base)


def make_aem_tree(base, md_content):
    """Create an AEM-format directory tree under base."""
    base = Path(base)
    aem_dir = base / "aem-page"
    aem_dir.mkdir(parents=True)
    (aem_dir / "doc.md").write_text(md_content, encoding="utf-8")
    return str(base)


class TestDocFinder:
    """Test cases for DocFinder."""

    def test_run_collects_subdirectories(self, tmp_path):
        """Subdirectories are collected, regular files are skipped."""
        target = tmp_path / "target"
        target.mkdir()
        (target / "doc_a").mkdir()
        (target / "doc_b").mkdir()
        (target / "not_a_dir.txt").write_text("x", encoding="utf-8")

        finder = DocFinder([str(target)])
        finder.run()

        assert len(finder.base_dirs) == 2
        names = [Path(d).name for d in finder.base_dirs]
        assert sorted(names) == ["doc_a", "doc_b"]

    def test_run_empty_target_dir(self, tmp_path):
        """Empty target directory produces no base_dirs."""
        target = tmp_path / "empty"
        target.mkdir()

        finder = DocFinder([str(target)])
        finder.run()

        assert finder.base_dirs == []


class TestMimirParserInit:
    """Test cases for MimirParser initialization."""

    def test_creates_output_directories(self, tmp_path):
        """Output dir and .metadata are created when they don't exist."""
        base = make_pantheon_tree(tmp_path / "doc", SAMPLE_TOC, SAMPLE_MD_HEADER + "# Title\n")
        out_dir = tmp_path / "output"

        MimirParser(base, str(out_dir), max_level=3)

        assert out_dir.is_dir()
        assert (out_dir / ".metadata").is_dir()

    def test_detects_pantheon_format(self, tmp_path):
        """Pantheon format: aem=False, toc and md paths set correctly."""
        base = make_pantheon_tree(tmp_path / "doc", SAMPLE_TOC, SAMPLE_MD_HEADER + "# Title\n")
        out = str(tmp_path / "out")

        parser = MimirParser(base, out, max_level=3)

        assert parser.aem is False
        assert parser.toc.endswith("toc.json")
        assert parser.md.endswith("doc.md")
        assert "single-page" in parser.md

    def test_detects_aem_format(self, tmp_path):
        """AEM format: aem=True, toc=None, md in aem-page/."""
        base = make_aem_tree(tmp_path / "doc", SAMPLE_MD_HEADER + "# Title\n")
        out = str(tmp_path / "out")

        parser = MimirParser(base, out, max_level=3)

        assert parser.aem is True
        assert parser.toc is None
        assert parser.md.endswith("doc.md")
        assert "aem-page" in parser.md

    def test_kb_article_skips_format_detection(self, tmp_path):
        """KB article mode does not look for toc/ or single-page/ dirs."""
        base = tmp_path / "kb"
        base.mkdir()
        out = str(tmp_path / "out")

        parser = MimirParser(str(base), out, max_level=3, kb_article=True)

        assert parser.kb_article is True
        assert not hasattr(parser, "sections")


class TestProcessSection:
    """Test cases for MimirParser.process_section."""

    def _make_parser(self, tmp_path):
        base = make_pantheon_tree(tmp_path / "doc", SAMPLE_TOC, SAMPLE_MD_HEADER + "# Title\n")
        return MimirParser(base, str(tmp_path / "out"), max_level=10)

    def test_flat_section(self, tmp_path):
        """Single section with title is appended with empty parent_titles."""
        parser = self._make_parser(tmp_path)
        section = {"title": "Solo", "singlePageAnchor": "solo"}
        parser.process_section(section, 0)

        assert len(parser.sections) == 1
        assert parser.sections[0]["title"] == "Solo"
        assert parser.sections[0]["parent_titles"] == []

    def test_nested_sections(self, tmp_path):
        """Nested sections have parent_titles propagated correctly."""
        parser = self._make_parser(tmp_path)
        parser.process_section(SAMPLE_TOC, -1)

        titles = [s["title"] for s in parser.sections]
        assert titles == ["Chapter One", "Section 1.1", "Chapter Two"]
        assert parser.sections[1]["parent_titles"] == ["Chapter One"]

    def test_respects_max_level(self, tmp_path):
        """Sections beyond max_level are excluded."""
        base = make_pantheon_tree(tmp_path / "doc", SAMPLE_TOC, SAMPLE_MD_HEADER + "# Title\n")
        parser = MimirParser(base, str(tmp_path / "out"), max_level=1)
        parser.process_section(SAMPLE_TOC, -1)

        titles = [s["title"] for s in parser.sections]
        assert titles == ["Chapter One", "Chapter Two"]
        assert "Section 1.1" not in titles

    def test_no_title_key(self, tmp_path):
        """Section without title key does not crash, children still processed."""
        parser = self._make_parser(tmp_path)
        section = {"sections": [{"title": "Child", "singlePageAnchor": "child", "sections": []}]}
        parser.process_section(section, 0)

        assert len(parser.sections) == 1
        assert parser.sections[0]["title"] == "Child"
        assert parser.sections[0]["parent_titles"] == []


class TestProcessToc:
    """Test cases for MimirParser.process_toc."""

    def test_pantheon_loads_json(self, tmp_path):
        """TOC JSON is loaded and sections are populated."""
        base = make_pantheon_tree(tmp_path / "doc", SAMPLE_TOC, SAMPLE_MD_HEADER + "# Title\n")
        parser = MimirParser(base, str(tmp_path / "out"), max_level=10)
        parser.process_toc()

        assert len(parser.sections) == 3
        titles = [s["title"] for s in parser.sections]
        assert "Chapter One" in titles
        assert "Chapter Two" in titles
        assert "Section 1.1" in titles

    def test_aem_synthesizes_root(self, tmp_path):
        """AEM documents get a single synthetic root section."""
        base = make_aem_tree(tmp_path / "doc", SAMPLE_MD_HEADER + "# Title\n")
        parser = MimirParser(base, str(tmp_path / "out"), max_level=3)
        parser.process_toc()

        assert len(parser.sections) == 1
        root = parser.sections[0]
        assert root["title"] is None
        assert root["urlFragment"] == "index"
        assert root["singlePageAnchor"] is None
        assert root["parent_titles"] == []


class TestProcessMd:
    """Test cases for MimirParser.process_md."""

    def test_pantheon_writes_index_and_metadata(self, tmp_path):
        """Pantheon flow creates __index__.md and __index__.json."""
        md_content = SAMPLE_MD_HEADER + "# Chapter One\nSome content.\n"
        toc = {
            "sections": [
                {
                    "title": "Chapter One",
                    "visible": True,
                    "weight": 1,
                    "urlFragment": "chapter-one",
                    "anchor": "chapter-one",
                    "singlePageAnchor": None,
                    "sections": [],
                }
            ]
        }
        base = make_pantheon_tree(tmp_path / "doc", toc, md_content)
        out = tmp_path / "out"
        parser = MimirParser(base, str(out), max_level=3)
        parser.process_toc()
        parser.process_md()

        assert (out / "__index__.md").exists()
        meta = out / ".metadata" / "__index__.json"
        assert meta.exists()
        data = json.loads(meta.read_text(encoding="utf-8"))
        assert data["url"] == "https://docs.example.com/test"
        assert data["path"] == "/docs/test"

    def test_pantheon_splits_by_section(self, tmp_path):
        """Each TOC section produces a separate .md and .json output."""
        md_content = (
            SAMPLE_MD_HEADER
            + "# Introduction\nFirst chapter content.\n"
            + "# Configuration\nSecond chapter content.\n"
        )
        toc = {
            "sections": [
                {
                    "title": "Introduction",
                    "visible": True,
                    "weight": 1,
                    "urlFragment": "intro",
                    "anchor": "intro",
                    "singlePageAnchor": "introduction",
                    "sections": [],
                },
                {
                    "title": "Configuration",
                    "visible": True,
                    "weight": 2,
                    "urlFragment": "config",
                    "anchor": "config",
                    "singlePageAnchor": "configuration",
                    "sections": [],
                },
            ]
        }
        base = make_pantheon_tree(tmp_path / "doc", toc, md_content)
        out = tmp_path / "out"
        parser = MimirParser(base, str(out), max_level=3)
        parser.process_toc()
        parser.process_md()

        assert (out / "introduction.md").exists()
        assert (out / "configuration.md").exists()
        assert (out / ".metadata" / "introduction.json").exists()
        assert (out / ".metadata" / "configuration.json").exists()

    def test_pantheon_metadata_url_with_anchor(self, tmp_path):
        """Section metadata url includes #anchor for non-index sections."""
        md_content = SAMPLE_MD_HEADER + "# Introduction\nContent.\n"
        toc = {
            "sections": [
                {
                    "title": "Introduction",
                    "visible": True,
                    "weight": 1,
                    "urlFragment": "intro",
                    "anchor": "intro",
                    "singlePageAnchor": "introduction",
                    "sections": [],
                }
            ]
        }
        base = make_pantheon_tree(tmp_path / "doc", toc, md_content)
        out = tmp_path / "out"
        parser = MimirParser(base, str(out), max_level=3)
        parser.process_toc()
        parser.process_md()

        data = json.loads((out / ".metadata" / "introduction.json").read_text(encoding="utf-8"))
        assert data["url"] == "https://docs.example.com/test#introduction"

    def test_pantheon_link_rewriting(self, tmp_path):
        """Internal #anchor links are rewritten to full URLs."""
        md_content = SAMPLE_MD_HEADER + "# Chapter One\nSee [details](#some-anchor) for more.\n"
        toc = {
            "sections": [
                {
                    "title": "Chapter One",
                    "visible": True,
                    "weight": 1,
                    "urlFragment": "ch1",
                    "anchor": "ch1",
                    "singlePageAnchor": None,
                    "sections": [],
                }
            ]
        }
        base = make_pantheon_tree(tmp_path / "doc", toc, md_content)
        out = tmp_path / "out"
        parser = MimirParser(base, str(out), max_level=3)
        parser.process_toc()
        parser.process_md()

        content = (out / "__index__.md").read_text(encoding="utf-8")
        assert "https://docs.example.com/test#some-anchor" in content
        assert "(#some-anchor)" not in content

    def test_pantheon_section_number_stripped(self, tmp_path):
        """Leading section numbers like '2.1 ' are stripped from title."""
        md_content = SAMPLE_MD_HEADER + "# 2.1 Configuration\nContent.\n"
        toc = {
            "sections": [
                {
                    "title": "2.1 Configuration",
                    "visible": True,
                    "weight": 1,
                    "urlFragment": "config",
                    "anchor": "config",
                    "singlePageAnchor": "configuration",
                    "sections": [],
                }
            ]
        }
        base = make_pantheon_tree(tmp_path / "doc", toc, md_content)
        out = tmp_path / "out"
        parser = MimirParser(base, str(out), max_level=3)
        parser.process_toc()
        parser.process_md()

        data = json.loads((out / ".metadata" / "configuration.json").read_text(encoding="utf-8"))
        assert data["title"] == "Configuration"

    def test_aem_single_output(self, tmp_path):
        """AEM format produces a single output file."""
        md_content = (
            SAMPLE_MD_HEADER
            + "# Main Title\nFirst paragraph.\n"
            + "# Second Heading\nSecond paragraph.\n"
        )
        base = make_aem_tree(tmp_path / "doc", md_content)
        out = tmp_path / "out"
        parser = MimirParser(base, str(out), max_level=3)
        parser.process_toc()
        parser.process_md()

        assert (out / "__index__.md").exists()
        content = (out / "__index__.md").read_text(encoding="utf-8")
        assert "First paragraph." in content
        assert "Second paragraph." in content

    def test_aem_writes_metadata(self, tmp_path):
        """AEM metadata JSON has correct url and path."""
        md_content = SAMPLE_MD_HEADER + "# Title\nContent.\n"
        base = make_aem_tree(tmp_path / "doc", md_content)
        out = tmp_path / "out"
        parser = MimirParser(base, str(out), max_level=3)
        parser.process_toc()
        parser.process_md()

        meta = out / ".metadata" / "__index__.json"
        assert meta.exists()
        data = json.loads(meta.read_text(encoding="utf-8"))
        assert data["url"] == "https://docs.example.com/test"
        assert data["path"] == "/docs/test"

    def test_kb_article_included_product(self, tmp_path):
        """KB article with matching product is processed."""
        base = tmp_path / "kb"
        base.mkdir()
        (base / "article.md").write_text(
            SAMPLE_KB_HEADER + "Some article content.\n", encoding="utf-8"
        )
        out = tmp_path / "out"
        parser = MimirParser(str(base), str(out), max_level=3, kb_article=True)
        parser.process_md("article.md")

        assert (out / "article.md").exists()
        content = (out / "article.md").read_text(encoding="utf-8")
        assert content.startswith("# [Solution] KB Article Title")

        meta = out / ".metadata" / "article.json"
        assert meta.exists()
        data = json.loads(meta.read_text(encoding="utf-8"))
        assert data["title"] == "[Solution] KB Article Title"
        assert "Red Hat Ansible Automation Platform" in data["products"]

    def test_kb_article_excluded_product(self, tmp_path):
        """KB article with non-matching product produces no output."""
        base = tmp_path / "kb"
        base.mkdir()
        (base / "other.md").write_text(
            SAMPLE_KB_HEADER_WRONG_PRODUCT + "Content.\n", encoding="utf-8"
        )
        out = tmp_path / "out"
        parser = MimirParser(str(base), str(out), max_level=3, kb_article=True)
        parser.process_md("other.md")

        assert not (out / "other.md").exists()

    def test_kb_article_title_strips_triple_quotes(self, tmp_path):
        """Triple quotes are removed from KB article titles."""
        base = tmp_path / "kb"
        base.mkdir()
        (base / "article.md").write_text(SAMPLE_KB_HEADER + "Content.\n", encoding="utf-8")
        out = tmp_path / "out"
        parser = MimirParser(str(base), str(out), max_level=3, kb_article=True)
        parser.process_md("article.md")

        meta = out / ".metadata" / "article.json"
        data = json.loads(meta.read_text(encoding="utf-8"))
        assert "'''" not in data["title"]


class TestRun:
    """Test cases for MimirParser.run."""

    def test_full_pantheon_flow(self, tmp_path):
        """End-to-end: Pantheon TOC + md produces split output files."""
        md_content = (
            SAMPLE_MD_HEADER
            + "# Introduction\nFirst content.\n"
            + "# Configuration\nSecond content.\n"
        )
        toc = {
            "sections": [
                {
                    "title": "Introduction",
                    "visible": True,
                    "weight": 1,
                    "urlFragment": "intro",
                    "anchor": "intro",
                    "singlePageAnchor": "introduction",
                    "sections": [],
                },
                {
                    "title": "Configuration",
                    "visible": True,
                    "weight": 2,
                    "urlFragment": "config",
                    "anchor": "config",
                    "singlePageAnchor": "configuration",
                    "sections": [],
                },
            ]
        }
        base = make_pantheon_tree(tmp_path / "doc", toc, md_content)
        out = tmp_path / "out"

        MimirParser(base, str(out), max_level=3).run()

        assert (out / "introduction.md").exists()
        assert (out / "configuration.md").exists()
        assert (out / ".metadata" / "introduction.json").exists()
        assert (out / ".metadata" / "configuration.json").exists()

    def test_full_aem_flow(self, tmp_path):
        """End-to-end: AEM md produces single output."""
        md_content = SAMPLE_MD_HEADER + "# Title\nAEM content here.\n"
        base = make_aem_tree(tmp_path / "doc", md_content)
        out = tmp_path / "out"

        MimirParser(base, str(out), max_level=3).run()

        assert (out / "__index__.md").exists()
        content = (out / "__index__.md").read_text(encoding="utf-8")
        assert "AEM content here." in content

    def test_kb_article_iterates_md_files(self, tmp_path):
        """KB article mode processes each .md file, skips non-.md files."""
        base = tmp_path / "kb"
        base.mkdir()
        (base / "art1.md").write_text(SAMPLE_KB_HEADER + "Article 1.\n", encoding="utf-8")
        (base / "art2.md").write_text(SAMPLE_KB_HEADER + "Article 2.\n", encoding="utf-8")
        (base / "readme.txt").write_text("not markdown", encoding="utf-8")
        out = tmp_path / "out"

        MimirParser(str(base), str(out), max_level=3, kb_article=True).run()

        assert (out / "art1.md").exists()
        assert (out / "art2.md").exists()
        assert not (out / "readme.txt").exists()
