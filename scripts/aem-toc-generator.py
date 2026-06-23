# pylint: disable=invalid-name,duplicate-code
"""Generate TOC JSON from AEM-page HTML files.

AEM documentation archives use two structural patterns:

1. Nested articles: <article class="nested0/1/2/..."> with topictitle headings.
   The nesting level comes from the CSS class (nested0 = root, nested1 = chapter, etc.).

2. Flat sections: <section> or <div class="example"> with sectiontitle headings.
   These appear in simpler documents that lack nested article structure.

The parser handles both patterns, building a tree of AEMArticleNode objects.
Only elements whose container (<article>, <section>, or <div>) carries an id
attribute produce TOC entries; anonymous containers are skipped.
"""
import argparse
import json
import os
import re
from dataclasses import dataclass
from dataclasses import field
from html.parser import HTMLParser


@dataclass
class AEMArticleNode:
    """A node in the document tree representing a section or article."""

    id: str
    title: str = ""
    level: int = 0
    children: list = field(default_factory=list)


class AEMHTMLParser(HTMLParser):  # pylint: disable=too-many-instance-attributes
    """Parse AEM HTML into a tree of AEMArticleNode objects.

    Handles three kinds of content containers:
    - <article class="nested{N}">: primary structure in most AEM docs
    - <section>: used for subsections within or instead of nested articles
    - <div class="example">: used for named examples with sectiontitle headings

    Containers without an id attribute are tracked but do not produce TOC entries.
    When no nested0 article exists, the parser creates a fallback root from <body id>.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = None
        self.body_id = None

        # Nested article tracking
        self.article_stack = []  # stack of AEMArticleNode for open nested articles
        self.open_nested_depths = []  # parallel bool stack: True if article was nested

        # Section/example tracking (shared stack for <section> and <div class="example">)
        self.section_stack = []  # stack of AEMArticleNode (or None for non-matching)
        self.open_div_depths = []  # parallel bool stack: True if div was an example

        # Title collection state
        self.pending_title_node = None  # node awaiting its title from the next heading
        self.collecting_title = False
        self.title_text_parts = []

        self.nested_re = re.compile(r"nested(\d+)")
        self._wrapper_article = False
        self._wrapper_title = None

        # Nodes discovered before root is established (no nested0 article).
        # Attached to root in parse() after the fallback root is created.
        self.pending_sections = []
        self.pending_articles = []

    def handle_starttag(self, tag, attrs):  # pylint: disable=too-many-branches
        attr_dict = dict(attrs)

        if tag == "body" and "id" in attr_dict:
            self.body_id = attr_dict["id"]

        if tag == "article":
            cls = attr_dict.get("class", "")
            m = self.nested_re.search(cls)
            if m:
                level = int(m.group(1))
                node = AEMArticleNode(
                    id=attr_dict.get("id", ""),
                    level=level,
                )
                if level == 0:
                    self.root = node
                elif self.article_stack:
                    self.article_stack[-1].children.append(node)
                elif self.root:
                    self.root.children.append(node)
                else:
                    # No root yet (no nested0); defer attachment until parse()
                    self.pending_articles.append(node)

                self.article_stack.append(node)
                self.open_nested_depths.append(True)
                self.pending_title_node = node
            else:
                # Non-nested article (e.g. wrapper <article role="article">)
                self.open_nested_depths.append(False)
                if not self.root and "role" in attr_dict:
                    self._wrapper_article = True

        # <section> and <div class="example"> are handled identically
        if tag == "section" or (tag == "div" and "example" in attr_dict.get("class", "").split()):
            section_id = attr_dict.get("id", "")
            parent_level = self.article_stack[-1].level if self.article_stack else 0
            node = AEMArticleNode(id=section_id, level=parent_level + 1)
            self.section_stack.append(node)
            self.pending_title_node = node
            if tag == "div":
                self.open_div_depths.append(True)
                return

        if tag == "div":
            self.open_div_depths.append(False)

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            cls = attr_dict.get("class", "")
            if ("topictitle" in cls or "sectiontitle" in cls) and self.pending_title_node:
                self.collecting_title = True
                self.title_text_parts = []

    def handle_data(self, data):
        if self.collecting_title:
            self.title_text_parts.append(data)

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self.collecting_title:
            self.collecting_title = False
            # Only assign title if the container element has an id
            if self.pending_title_node and self.pending_title_node.id:
                self.pending_title_node.title = " ".join("".join(self.title_text_parts).split())
            self.pending_title_node = None

        # Closing </div>: pop the example-div tracker and treat as </section> if matched
        if tag == "div" and self.open_div_depths:
            is_example = self.open_div_depths.pop()
            if is_example:
                tag = "section"

        # Attach completed section nodes to their parent
        if tag == "section" and self.section_stack:
            node = self.section_stack.pop()
            if node and node.title:
                if self.article_stack:
                    self.article_stack[-1].children.append(node)
                elif self.root:
                    self.root.children.append(node)
                else:
                    self.pending_sections.append(node)

        if tag == "article" and self.open_nested_depths:
            is_nested = self.open_nested_depths.pop()
            if is_nested and self.article_stack:
                self.article_stack.pop()

    def get_root(self):
        """Return the root node, or construct one from wrapper article metadata."""
        if self.root:
            return self.root
        if self.body_id and hasattr(self, "_wrapper_title"):
            return AEMArticleNode(id=self.body_id, title=self._wrapper_title, level=0)
        return None

    def parse(self, html_content):
        """Parse HTML and return the root AEMArticleNode."""
        self.feed(html_content)

        # Fallback: create root from <body id> when no nested0 article exists
        if not self.root and self.body_id:
            self.root = AEMArticleNode(id=self.body_id, level=0)

        # Attach nodes that were discovered before root was established
        if self.root and self.pending_sections:
            self.root.children.extend(self.pending_sections)
            self.pending_sections = []

        if self.root and self.pending_articles:
            self.root.children.extend(self.pending_articles)
            self.pending_articles = []

        # Extract root title from the first h1.topictitle if not already set
        if self.root and not self.root.title:
            self._extract_root_title_fallback(html_content)

        return self.root

    def _extract_root_title_fallback(self, html_content):
        """Extract the document title from the first h1 with topictitle class."""
        m = re.search(
            r'<h1[^>]*class="[^"]*topictitle[^"]*"[^>]*>(.*?)</h1>',
            html_content,
            re.DOTALL,
        )
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1))
            self.root.title = " ".join(title.split())


class TOCGenerator:  # pylint: disable=too-few-public-methods
    """Convert an AEMArticleNode tree into a Mimir-compatible TOC JSON structure."""

    def generate(self, root_node):
        """Build the top-level TOC dict from the root node."""
        toc = {"version": "1.1", "sections": []}

        root_section = {
            "title": root_node.title,
            "visible": True,
            "weight": 1,
            "urlFragment": "index",
            "anchor": None,
            "singlePageAnchor": None,
        }

        if root_node.children:
            root_section["sections"] = []
            for i, child in enumerate(root_node.children):
                section = self._build_section(child, chapter_id=child.id)
                section["weight"] = i + 1
                root_section["sections"].append(section)

        toc["sections"].append(root_section)

        return toc

    def _build_section(self, node, chapter_id=None):
        """Recursively build a TOC section dict from a node.

        Args:
            node: The AEMArticleNode to convert.
            chapter_id: The id of the nearest level-1 ancestor, used as the
                urlFragment for deeper nodes so they link to the correct page.
        """
        if node.level <= 1:
            url_fragment = node.id
            anchor = None
        else:
            url_fragment = chapter_id or node.id
            anchor = node.id

        section = {
            "title": node.title,
            "visible": node.level < 4,
            "weight": 1,
            "urlFragment": url_fragment,
            "anchor": anchor,
            "singlePageAnchor": node.id,
        }

        if node.children:
            child_chapter_id = node.id if node.level == 1 else chapter_id
            section["sections"] = []
            for i, child in enumerate(node.children):
                child_section = self._build_section(child, chapter_id=child_chapter_id)
                child_section["weight"] = i + 1
                section["sections"].append(child_section)

        return section


def process_single(input_path, output_path):
    """Parse a single AEM HTML file and write the TOC JSON."""
    with open(input_path, encoding="utf-8") as f:
        html_content = f.read()

    parser = AEMHTMLParser()
    root = parser.parse(html_content)

    if not root:
        print(f"WARNING: Could not parse {input_path}, no root article found")
        return False

    generator = TOCGenerator()
    toc = generator.generate(root)

    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(toc, f, indent=2, ensure_ascii=False)

    print(f"Generated: {output_path} ({len(toc['sections'])} top-level sections)")
    return True


def process_batch(base_dir):
    """Process all aem-page directories under base_dir."""
    count = 0
    errors = 0

    for version_dir in sorted(os.listdir(base_dir)):
        version_path = os.path.join(base_dir, version_dir)
        if not os.path.isdir(version_path):
            continue

        for doc_dir in sorted(os.listdir(version_path)):
            doc_path = os.path.join(version_path, doc_dir)
            aem_dir = os.path.join(doc_path, "aem-page")
            if not os.path.isdir(aem_dir):
                continue

            html_files = [f for f in os.listdir(aem_dir) if f.endswith(".html")]
            if not html_files:
                continue

            input_path = os.path.join(aem_dir, html_files[0])
            toc_dir = os.path.join(doc_path, "toc")
            output_path = os.path.join(toc_dir, "toc.json")

            if process_single(input_path, output_path):
                count += 1
            else:
                errors += 1

    print(f"\nBatch complete: {count} generated, {errors} errors")


def main():
    """CLI entry point for single-file or batch TOC generation."""
    parser = argparse.ArgumentParser(description="Generate TOC JSON from AEM-page HTML files")
    parser.add_argument("--input", "-i", help="Path to input AEM HTML file")
    parser.add_argument("--output", "-o", help="Path to output TOC JSON file")
    parser.add_argument("--batch", action="store_true", help="Process all aem-page directories")
    parser.add_argument(
        "--base-dir",
        default="red_hat_content/documentation/red_hat_ansible_automation_platform",
        help="Base directory for batch processing",
    )
    args = parser.parse_args()

    if args.batch:
        process_batch(args.base_dir)
    elif args.input and args.output:
        process_single(args.input, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
