"""Parse Mimir documentation archives into plaintext for RAG ingestion."""

# pylint: disable=invalid-name,duplicate-code
import argparse
import configparser
import json
import os
import re
import subprocess
import sys
import time
import traceback

# List of directories that are used as sources to generate RAG data.
# These should be found in the Mimir archive (mimir-extract-latest.tgz.enc).
SOURCE_DIRS = [
    "red_hat_content/documentation/ansible_on_clouds/2.x",
    "red_hat_content/documentation/red_hat_ansible_automation_platform/2.7",
    "red_hat_content/documentation"
    "/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest",
]
KNOWLEDGE_BASE_ARTICLES_DIR = "red_hat_content/solutions"
PRODUCTS_TO_BE_INCLUDED = {"Red Hat Ansible Automation Platform"}


class DocFinder:  # pylint: disable=too-few-public-methods
    """Locate document directories under the given target paths."""

    def __init__(self, target_dirs):
        self.target_dirs = target_dirs
        self.base_dirs = []

    def run(self):
        """Scan target directories and collect document base paths."""
        for target_dir in self.target_dirs:
            for doc_dir in os.listdir(target_dir):
                full_path = os.path.join(target_dir, doc_dir)
                if os.path.isdir(full_path):
                    self.base_dirs.append(os.path.join(target_dir, doc_dir))


class MimirParser:  # pylint: disable=too-many-instance-attributes
    """Parse a single Mimir document directory into chunked plaintext."""

    def __init__(self, base_dir, out_dir, max_level, kb_article=False):
        self.base_dir = base_dir
        self.out_dir = out_dir
        self.max_level = max_level
        self.kb_article = kb_article
        self.metadata_dir = os.path.join(self.out_dir, ".metadata")
        self.doc_metadata = None

        if not os.path.isdir(self.out_dir):
            os.makedirs(self.out_dir)
        if not os.path.isdir(self.metadata_dir):
            os.makedirs(self.metadata_dir)

        self.aem = os.path.isdir(os.path.join(self.base_dir, "aem-page"))  # detect AEM format

        if not kb_article:
            self.sections = []
            self.toc = self.base_dir + "/toc/" + os.listdir(self.base_dir + "/toc")[0]
            md_dir = "aem-page" if self.aem else "single-page"
            self.md = (
                self.base_dir
                + f"/{md_dir}/"
                + next(
                    filter(lambda x: x.endswith(".md"), os.listdir(self.base_dir + f"/{md_dir}"))
                )
            )

    def process_section(self, section, level, parent_titles=None):
        """Recursively walk TOC sections up to max_level."""
        if parent_titles is None:
            parent_titles = []
        if level >= self.max_level:
            return

        section_title = None
        if "title" in section:
            section_title = section["title"]
            section["parent_titles"] = parent_titles
            self.sections.append(section)

        sections = section.get("sections", [])
        if sections:
            for s in sections:
                self.process_section(
                    s,
                    level + 1,
                    (parent_titles + [section_title]) if section_title else parent_titles,
                )

    def process_toc(self):
        """Load TOC JSON."""
        with open(self.toc, encoding="utf-8") as f:
            toc = json.loads(f.read())
        self.process_section(toc, -1)

    def process_md(
        self, md=None
    ):  # pylint: disable=too-many-locals,too-many-branches,too-many-statements
        """Parse a markdown file, split by TOC sections, and write output."""
        in_md_header = False
        in_example = False
        config = "[__default__]\n"
        link_to_section = re.compile(r"\]\((#[\w\-]+)\)")
        f = None
        section_index = 0
        base_url = ""

        if self.kb_article:
            md_file = os.path.join(self.base_dir, md)
        else:
            out_file = os.path.join(self.out_dir, "__index__.md")
            f = open(out_file, "w", encoding="utf-8")  # pylint: disable=consider-using-with
            md_file = self.md

        for line in open(md_file, encoding="utf-8"):  # pylint: disable=consider-using-with
            line = line.strip()

            if in_md_header:
                if line == "+++":
                    in_md_header = False
                    self.doc_metadata = configparser.ConfigParser()
                    self.doc_metadata.read_string(config)
                    if self.kb_article:
                        try:
                            products = json.loads(self.doc_metadata["extra"]["products"])
                        except KeyError:
                            products = []
                        except configparser.NoSectionError:
                            products = []

                        # If this is not an article for a product we want to include, skip it.
                        if len(PRODUCTS_TO_BE_INCLUDED.intersection(products)) == 0:
                            return

                        out_file = os.path.join(self.out_dir, md)
                        f = open(  # pylint: disable=consider-using-with
                            out_file, "w", encoding="utf-8"
                        )
                        metadata_file = os.path.join(self.metadata_dir, md.replace(".md", ".json"))
                    else:
                        metadata_file = os.path.join(self.metadata_dir, "__index__.json")

                    with open(metadata_file, "w", encoding="utf-8") as meta:
                        metadata = {
                            s: dict(self.doc_metadata.items(s))
                            for s in self.doc_metadata.sections()
                        }
                        metadata["url"] = self.doc_metadata["extra"]["reference_url"]
                        metadata["path"] = self.doc_metadata["__default__"]["path"]
                        if self.kb_article:
                            title = self.doc_metadata["__default__"]["title"].replace("'''", "")
                            title = "[Solution] " + title
                            print(f"# {title}\n", file=f)
                            metadata["title"] = title
                            metadata["products"] = products

                        json.dump(metadata, meta, indent=2)
                else:
                    line = re.sub(r"^(.+)\s*=\s*\"(.+)\"", r"\1 = \2", line)
                    config += line + "\n"
                continue
            if line == "+++":
                in_md_header = True
                continue

            if line.startswith("```"):
                in_example = not in_example

            if (
                not self.kb_article
                and not in_example
                and line.startswith("#")
                and section_index < len(self.sections)
            ):
                title = line.replace("\xa0", " ")
                title = re.sub(r"^#+\s*", "", title)
                title = re.sub(r"^Chapter\s*", "", title)
                section = self.sections[section_index]
                title_to_match = section["title"]
                single_page_anchor = section["singlePageAnchor"]
                if title == title_to_match and single_page_anchor == "":
                    # print(f"INFO: Skip: {md_file} - {title}")
                    section_index += 1
                elif title == title_to_match or single_page_anchor is None:
                    if single_page_anchor is None:
                        single_page_anchor = "__index__"
                    base_url = self.doc_metadata["extra"]["reference_url"]
                    section_index += 1

                    if f:
                        f.flush()
                        f.close()
                        f = None

                    metadata_file = os.path.join(self.metadata_dir, f"{single_page_anchor}.json")
                    with open(metadata_file, "w", encoding="utf-8") as meta:
                        metadata = {}
                        if single_page_anchor == "__index__":
                            metadata["url"] = f"{base_url}"
                        else:
                            metadata["url"] = f"{base_url}#{single_page_anchor}"
                        metadata["path"] = self.doc_metadata["__default__"]["path"]

                        if not self.kb_article:
                            # Remove the leading section/chapter number from titles
                            title = re.sub(r"^[\d\.]+ ", "", title)
                            metadata["title"] = title

                        json.dump(metadata, meta, indent=2)

                    out_file = os.path.join(self.out_dir, single_page_anchor + ".md")
                    f = open(out_file, "w", encoding="utf-8")  # pylint: disable=consider-using-with

                    for i, parent_title in enumerate(section["parent_titles"]):
                        print(f"{'#' * (i + 1)} {parent_title}", file=f)

            # Convert links to sections into links to full URLs
            line_copy = line
            for link in link_to_section.findall(line_copy):
                line = line.replace(link, base_url + link)

            if f:
                print(line, file=f)

        if f:
            f.flush()
            f.close()

    def run(self):
        """Process TOC and markdown for this document directory."""
        if self.kb_article:
            for f in filter(lambda x: x.endswith(".md"), os.listdir(self.base_dir)):
                self.process_md(f)
        else:
            self.process_toc()
            self.process_md()


def main():  # pylint: disable=too-many-locals,too-many-branches,too-many-statements
    """Extract and parse Mimir archives into plaintext for RAG."""
    start = time.time()
    try:  # pylint: disable=too-many-nested-blocks
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-o", "--out-dir", default="aap-product-docs-plaintext")
        arg_parser.add_argument("-m", "--max-level", default=3)
        arg_parser.add_argument("--add-kb-articles", action=argparse.BooleanOptionalAction)
        arg_parser.add_argument(
            "--keep-html",
            action=argparse.BooleanOptionalAction,
            default=False,
            help="Keep HTML files after processing (default: False)",
        )

        args = arg_parser.parse_args()

        print("Following files are found in the mimir directory:")
        for f in os.listdir("mimir"):
            print(f"  - {f}")

        out_file = "mimir/mimir-extract-latest.tgz"
        in_file = out_file + ".enc"
        if os.path.exists(in_file):
            try:
                secret = os.getenv("MIMIR_ENC_SECRET")
                if not secret:
                    print("Envvar MIMIR_ENC_SECRET is not defined.")
                    sys.exit(1)
                openssl_cmd = (
                    f"openssl enc -aes-256-cbc -d -pbkdf2"
                    f" -pass pass:{secret}"
                    f" -in {in_file} -out {out_file}"
                )
                subprocess.run(
                    openssl_cmd.split(" "),
                    capture_output=True,
                    text=True,
                    check=True,
                )
                dirs = " ".join(SOURCE_DIRS)
                output = subprocess.run(
                    f"tar xvzf {out_file} {dirs}".split(" "),
                    capture_output=True,
                    text=True,
                    check=True,
                )
                print(output)
                print("Generating TOC files from AEM HTML files...")
                toc_script = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    "aem-toc-generator.py",
                )
                for source_dir in SOURCE_DIRS:
                    if not os.path.isdir(source_dir):
                        continue
                    for doc_name in sorted(os.listdir(source_dir)):
                        aem_dir = os.path.join(source_dir, doc_name, "aem-page")
                        if not os.path.isdir(aem_dir):
                            continue
                        html_files = [f for f in os.listdir(aem_dir) if f.endswith(".html")]
                        if not html_files:
                            continue
                        input_path = os.path.join(aem_dir, html_files[0])
                        output_path = os.path.join(source_dir, doc_name, "toc", "toc.json")
                        subprocess.run(
                            [
                                sys.executable,
                                toc_script,
                                "-i",
                                input_path,
                                "-o",
                                output_path,
                            ],
                            capture_output=True,
                            text=True,
                            check=True,
                        )
                print("TOC generation complete.")
                if args.add_kb_articles:
                    print("Extracting knowledge base articles...")
                    output = subprocess.run(
                        f"tar xzf {out_file} {KNOWLEDGE_BASE_ARTICLES_DIR}".split(" "),
                        capture_output=True,
                        text=True,
                        check=True,
                    )
                    print(output.stdout)
                    print(output.stderr)
                    print("done!")
                if args.keep_html:
                    print("Keeping html files")
                else:
                    print("Delete html files")
                    output = subprocess.run(
                        "find red_hat_content -name *.html -type f -delete".split(" "),
                        capture_output=True,
                        text=True,
                        check=True,
                    )
                    print(output)
            except subprocess.CalledProcessError:
                traceback.print_stack()
                sys.exit(2)
            finally:
                if os.path.exists(in_file):
                    os.unlink(in_file)
                if os.path.exists(out_file):
                    os.unlink(out_file)
        else:
            print(f"{in_file} is not found. Skip the file extraction step.")

        if args.add_kb_articles:
            MimirParser(
                KNOWLEDGE_BASE_ARTICLES_DIR,
                os.path.join(args.out_dir, KNOWLEDGE_BASE_ARTICLES_DIR),
                max_level=1,
                kb_article=True,
            ).run()

        doc_finder = DocFinder(SOURCE_DIRS)
        doc_finder.run()

        for base_dir in doc_finder.base_dirs:
            MimirParser(base_dir, os.path.join(args.out_dir, base_dir), int(args.max_level)).run()
    finally:
        print(f"Execution time: {(time.time() - start):.3f} secs")


if __name__ == "__main__":
    main()
