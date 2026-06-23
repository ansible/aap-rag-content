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
"""Tests for aem-toc-generator module."""
# pylint: disable=C0415,import-error,protected-access,too-few-public-methods
import importlib
import json
import sys
from pathlib import Path

scripts_dir = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

_mod = importlib.import_module("aem-toc-generator")
AEMArticleNode = _mod.AEMArticleNode
AEMHTMLParser = _mod.AEMHTMLParser
TOCGenerator = _mod.TOCGenerator
process_single = _mod.process_single
process_batch = _mod.process_batch


NESTED_HTML = """\
<html>
<body>
<article role="article">
  <article class="nested0" id="doc-root">
    <h1 class="title topictitle1" id="ariaid-title1">Root Title</h1>
    <article class="topic task nested1" id="chapter-one">
      <h2 class="title topictitle2" id="ariaid-title2">Chapter One</h2>
    </article>
    <article class="topic concept nested1" id="chapter-two">
      <h2 class="title topictitle2" id="ariaid-title3">Chapter Two</h2>
    </article>
  </article>
</article>
</body>
</html>
"""

FLAT_HTML = """\
<html>
<body id="flat-doc">
<article role="article">
  <h1 class="title topictitle1" id="ariaid-title1">Flat Document</h1>
  <div class="body refbody">
    <section class="section" id="flat-doc___section-a">
      <h2 class="title sectiontitle">Section A</h2>
      <p>Content A.</p>
    </section>
    <section class="section" id="flat-doc___section-b">
      <h2 class="title sectiontitle">Section B</h2>
      <p>Content B.</p>
    </section>
  </div>
</article>
</body>
</html>
"""

MIXED_HTML = """\
<html>
<body>
<article role="article">
  <article class="nested0" id="mixed-root">
    <h1 class="title topictitle1" id="ariaid-title1">Mixed Document</h1>
    <article class="topic concept nested1" id="mixed-chapter">
      <h2 class="title topictitle2" id="ariaid-title2">Chapter With Sections</h2>
      <div class="body refbody">
        <section class="section" id="mixed-chapter___criteria">
          <h3 class="title sectiontitle">Criteria</h3>
          <p>Some criteria.</p>
        </section>
      </div>
    </article>
  </article>
</article>
</body>
</html>
"""

MINIMAL_HTML = """\
<html>
<body>
<div>
  <p>No articles or body id here.</p>
</div>
</body>
</html>
"""

DIV_EXAMPLE_HTML = """\
<html>
<body>
<article role="article">
  <article class="nested0" id="example-root">
    <h1 class="title topictitle1" id="ariaid-title1">Example Doc</h1>
    <article class="topic nested1" id="example-chapter">
      <h2 class="title topictitle2" id="ariaid-title2">A Chapter</h2>
      <div class="body refbody">
        <div class="example" id="example-chapter___demo">
          <h3 class="title sectiontitle">Demo Example</h3>
          <p>Example content.</p>
        </div>
      </div>
    </article>
  </article>
</article>
</body>
</html>
"""

NO_ID_SECTION_HTML = """\
<html>
<body>
<article role="article">
  <article class="nested0" id="noid-root">
    <h1 class="title topictitle1" id="ariaid-title1">No ID Sections</h1>
    <div class="body refbody">
      <section class="section">
        <h2 class="title sectiontitle">Anonymous Section</h2>
        <p>This section has no id.</p>
      </section>
      <section class="section" id="noid-root___named">
        <h2 class="title sectiontitle">Named Section</h2>
        <p>This section has an id.</p>
      </section>
    </div>
  </article>
</article>
</body>
</html>
"""

DEEP_NESTED_HTML = """\
<html>
<body>
<article role="article">
  <article class="nested0" id="deep-root">
    <h1 class="title topictitle1" id="ariaid-title1">Deep Doc</h1>
    <article class="topic nested1" id="level1">
      <h2 class="title topictitle2" id="ariaid-title2">Level 1</h2>
      <article class="topic nested2" id="level2">
        <h3 class="title topictitle3" id="ariaid-title3">Level 2</h3>
        <article class="topic nested3" id="level3">
          <h4 class="title topictitle4" id="ariaid-title4">Level 3</h4>
          <article class="topic nested4" id="level4">
            <h5 class="title topictitle5" id="ariaid-title5">Level 4</h5>
          </article>
        </article>
      </article>
    </article>
  </article>
</article>
</body>
</html>
"""


class TestAEMArticleNode:
    """Test cases for AEMArticleNode dataclass."""

    def test_default_fields(self):
        """Dataclass defaults: empty title, level=0, empty children."""
        node = AEMArticleNode(id="test-id")
        assert node.id == "test-id"
        assert node.title == ""
        assert node.level == 0
        assert node.children == []


class TestAEMHTMLParser:
    """Test cases for AEMHTMLParser."""

    def test_nested_articles(self):
        """Pattern 1: nested0/nested1 articles produce correct tree."""
        parser = AEMHTMLParser()
        root = parser.parse(NESTED_HTML)

        assert root is not None
        assert root.id == "doc-root"
        assert root.title == "Root Title"
        assert root.level == 0
        assert len(root.children) == 2
        assert root.children[0].id == "chapter-one"
        assert root.children[0].title == "Chapter One"
        assert root.children[0].level == 1
        assert root.children[1].id == "chapter-two"
        assert root.children[1].title == "Chapter Two"

    def test_flat_sections(self):
        """Pattern 2: flat sections with sectiontitle produce children from body id."""
        parser = AEMHTMLParser()
        root = parser.parse(FLAT_HTML)

        assert root is not None
        assert root.id == "flat-doc"
        assert root.title == "Flat Document"
        assert len(root.children) == 2
        assert root.children[0].id == "flat-doc___section-a"
        assert root.children[0].title == "Section A"
        assert root.children[1].id == "flat-doc___section-b"
        assert root.children[1].title == "Section B"

    def test_mixed_content(self):
        """Pattern 3: nested articles containing sections."""
        parser = AEMHTMLParser()
        root = parser.parse(MIXED_HTML)

        assert root is not None
        assert root.id == "mixed-root"
        assert len(root.children) == 1
        chapter = root.children[0]
        assert chapter.id == "mixed-chapter"
        assert chapter.title == "Chapter With Sections"
        assert len(chapter.children) == 1
        assert chapter.children[0].id == "mixed-chapter___criteria"
        assert chapter.children[0].title == "Criteria"

    def test_section_without_id_skipped(self):
        """Sections without id produce no TOC entry."""
        parser = AEMHTMLParser()
        root = parser.parse(NO_ID_SECTION_HTML)

        assert root is not None
        assert root.id == "noid-root"
        assert len(root.children) == 1
        assert root.children[0].id == "noid-root___named"
        assert root.children[0].title == "Named Section"

    def test_div_example_with_sectiontitle(self):
        """<div class="example"> with sectiontitle is treated like a section."""
        parser = AEMHTMLParser()
        root = parser.parse(DIV_EXAMPLE_HTML)

        assert root is not None
        chapter = root.children[0]
        assert chapter.id == "example-chapter"
        assert len(chapter.children) == 1
        example = chapter.children[0]
        assert example.id == "example-chapter___demo"
        assert example.title == "Demo Example"

    def test_fallback_root_from_body_id(self):
        """No nested0: root created from <body id>."""
        parser = AEMHTMLParser()
        root = parser.parse(FLAT_HTML)

        assert root is not None
        assert root.id == "flat-doc"
        assert root.level == 0

    def test_root_title_fallback(self):
        """Root title extracted from first h1.topictitle via regex."""
        html = """\
<html>
<body id="fallback-doc">
<article role="article">
  <h1 class="title topictitle1" id="ariaid-title1">Fallback Title</h1>
  <div class="body refbody">
    <p>Content.</p>
  </div>
</article>
</body>
</html>
"""
        parser = AEMHTMLParser()
        root = parser.parse(html)

        assert root is not None
        assert root.title == "Fallback Title"

    def test_no_root_returns_none(self):
        """HTML with no nested articles and no body id returns None."""
        parser = AEMHTMLParser()
        root = parser.parse(MINIMAL_HTML)

        assert root is None


class TestTOCGenerator:
    """Test cases for TOCGenerator."""

    def test_root_only(self):
        """Single root node with no children."""
        root = AEMArticleNode(id="root", title="Root", level=0)
        gen = TOCGenerator()
        toc = gen.generate(root)

        assert toc["version"] == "1.1"
        assert len(toc["sections"]) == 1
        root_section = toc["sections"][0]
        assert root_section["title"] == "Root"
        assert root_section["urlFragment"] == "index"
        assert root_section["singlePageAnchor"] is None
        assert root_section["anchor"] is None
        assert "sections" not in root_section

    def test_with_children(self):
        """Root + children: checks urlFragment, anchor, singlePageAnchor, weight."""
        child1 = AEMArticleNode(id="ch1", title="Chapter 1", level=1)
        child2 = AEMArticleNode(id="ch2", title="Chapter 2", level=1)
        root = AEMArticleNode(id="root", title="Root", level=0, children=[child1, child2])

        gen = TOCGenerator()
        toc = gen.generate(root)

        root_section = toc["sections"][0]
        assert len(root_section["sections"]) == 2

        s1 = root_section["sections"][0]
        assert s1["title"] == "Chapter 1"
        assert s1["urlFragment"] == "ch1"
        assert s1["anchor"] is None
        assert s1["singlePageAnchor"] == "ch1"
        assert s1["weight"] == 1

        s2 = root_section["sections"][1]
        assert s2["title"] == "Chapter 2"
        assert s2["weight"] == 2

    def test_deep_nesting(self):
        """Level 2+ nodes get chapter_id as urlFragment and their own id as anchor."""
        subsection = AEMArticleNode(id="sub", title="Subsection", level=2)
        chapter = AEMArticleNode(id="ch1", title="Chapter", level=1, children=[subsection])
        root = AEMArticleNode(id="root", title="Root", level=0, children=[chapter])

        gen = TOCGenerator()
        toc = gen.generate(root)

        ch_section = toc["sections"][0]["sections"][0]
        sub_section = ch_section["sections"][0]

        assert sub_section["urlFragment"] == "ch1"
        assert sub_section["anchor"] == "sub"
        assert sub_section["singlePageAnchor"] == "sub"

    def test_visibility_level4_hidden(self):
        """Nodes at level >= 4 have visible=false."""
        parser = AEMHTMLParser()
        root = parser.parse(DEEP_NESTED_HTML)

        gen = TOCGenerator()
        toc = gen.generate(root)

        root_section = toc["sections"][0]
        assert root_section["visible"] is True

        l1 = root_section["sections"][0]
        assert l1["visible"] is True

        l2 = l1["sections"][0]
        assert l2["visible"] is True

        l3 = l2["sections"][0]
        assert l3["visible"] is True

        l4 = l3["sections"][0]
        assert l4["visible"] is False


class TestProcessSingle:
    """Test cases for process_single."""

    def test_writes_toc_json(self, tmp_path):
        """Generates valid JSON output from HTML file."""
        html_file = tmp_path / "doc.html"
        html_file.write_text(NESTED_HTML, encoding="utf-8")
        out_file = tmp_path / "toc.json"

        result = process_single(str(html_file), str(out_file))

        assert result is True
        assert out_file.exists()
        toc = json.loads(out_file.read_text(encoding="utf-8"))
        assert toc["version"] == "1.1"
        assert len(toc["sections"]) == 1
        assert toc["sections"][0]["title"] == "Root Title"

    def test_creates_output_directory(self, tmp_path):
        """Output dir is created if missing."""
        html_file = tmp_path / "doc.html"
        html_file.write_text(NESTED_HTML, encoding="utf-8")
        out_file = tmp_path / "subdir" / "toc.json"

        result = process_single(str(html_file), str(out_file))

        assert result is True
        assert out_file.exists()

    def test_returns_false_on_unparseable(self, tmp_path):
        """Returns False for HTML with no root."""
        html_file = tmp_path / "bad.html"
        html_file.write_text(MINIMAL_HTML, encoding="utf-8")
        out_file = tmp_path / "toc.json"

        result = process_single(str(html_file), str(out_file))

        assert result is False
        assert not out_file.exists()


class TestProcessBatch:
    """Test cases for process_batch."""

    def test_processes_aem_directories(self, tmp_path):
        """Batch mode finds and processes aem-page dirs."""
        # Create structure: base_dir/version/doc_name/aem-page/file.html
        version_dir = tmp_path / "2.7"
        doc_dir = version_dir / "some-doc"
        aem_dir = doc_dir / "aem-page"
        aem_dir.mkdir(parents=True)
        (aem_dir / "some-doc.html").write_text(NESTED_HTML, encoding="utf-8")

        process_batch(str(tmp_path))

        toc_file = doc_dir / "toc" / "toc.json"
        assert toc_file.exists()
        toc = json.loads(toc_file.read_text(encoding="utf-8"))
        assert toc["version"] == "1.1"
