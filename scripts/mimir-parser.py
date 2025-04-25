import argparse
import configparser
import json
import os
import re
import subprocess
import time
import traceback

# List of directories that are used as sources to generate RAG data.
# These should be found in the Mimir archive (mimir-extract-latest.tgz.enc).
SOURCE_DIRS = [
    "red_hat_content/documentation/ansible_on_clouds/2.x",
    "red_hat_content/documentation/red_hat_ansible_automation_platform/2.5",
    "red_hat_content/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest",
]
KNOWLEDGE_BASE_ARTICLES_DIR = "red_hat_content/solutions"
PRODUCTS_TO_BE_INCLUDED = set([
    "Red Hat Ansible Automation Platform"
])

class DocFinder:
    def __init__(self, target_dirs):
        self.target_dirs = target_dirs
        self.base_dirs = []

    def run(self):
        for target_dir in self.target_dirs:
            for doc_dir in os.listdir(target_dir):
                full_path = os.path.join(target_dir, doc_dir)
                if os.path.isdir(full_path):
                    self.base_dirs.append(os.path.join(target_dir, doc_dir))


class MimirParser:
    def __init__(self, base_dir, out_dir, max_level, kb_article = False):
        self.base_dir = base_dir
        self.out_dir = out_dir
        self.max_level = max_level
        self.kb_article = kb_article
        self.metadata_dir = os.path.join(self.out_dir, ".metadata")

        if not os.path.isdir(self.out_dir):
            os.makedirs(self.out_dir)
        if not os.path.isdir(self.metadata_dir):
            os.makedirs(self.metadata_dir)

        if not kb_article:
            self.sections = []
            self.toc = self.base_dir + "/toc/" + os.listdir(self.base_dir + "/toc")[0]
            self.md = self.base_dir + "/single-page/" + \
                      list(filter(lambda x: x.endswith(".md"),
                                  os.listdir(self.base_dir + "/single-page")))[0]

    def process_section(self, section, level):
        if level >= self.max_level:
            return

        if "title" in section:
            self.sections.append(section)

        sections = section.get("sections", [])
        if sections:
            for s in sections:
                self.process_section(s, level + 1)

    def process_toc(self):
        with open(self.toc, encoding="utf-8") as f:
            toc = json.loads(f.read())
        self.process_section(toc, -1)


    def process_md(self, md=None):
        in_md_header = False
        config = "[__default__]\n"
        link_to_section = re.compile(r'\]\((#[\w\-_]+)\)')

        if self.kb_article:
            md_file = os.path.join(self.base_dir, md)
        else:
            out_file = os.path.join(self.out_dir, "__index__.md")
            f = open(out_file, "w")
            section_index = 0
            md_file = self.md

        for line in open(md_file, encoding="utf-8"):
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
                        f = open(out_file, "w")
                        metadata_file = os.path.join(self.metadata_dir, md.replace(".md", ".json"))
                    else:
                        metadata_file = os.path.join(self.metadata_dir, "__index__.json")

                    with open(metadata_file, "w") as meta:
                        metadata = {s:dict(self.doc_metadata.items(s)) for s in self.doc_metadata.sections()}
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
            elif line == "+++":
                in_md_header = True
                continue

            if not self.kb_article and line.startswith("#"):
                title_to_match = self.sections[section_index]["title"]
                title = line.replace("\xa0", " ")
                title = re.sub(r"^#+\s*", "", title)
                title = re.sub(r"^Chapter\s*", "", title)
                single_page_anchor = self.sections[section_index]['singlePageAnchor']
                if title == title_to_match or single_page_anchor == None:
                    if single_page_anchor == None:
                        single_page_anchor = "__index__"
                    base_url = self.doc_metadata["extra"]["reference_url"]
                    section_index += 1

                    if f:
                        f.flush()
                        f.close()
                        f = None

                    metadata_file = os.path.join(self.metadata_dir, f"{single_page_anchor}.json")
                    with open(metadata_file, "w") as meta:
                        metadata = dict()
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
                    f = open(out_file, "w")

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
        if self.kb_article:
            for f in filter(lambda x: x.endswith(".md"), os.listdir(self.base_dir)):
                self.process_md(f)
        else:
            self.process_toc()
            self.process_md()


def main():
    start = time.time()
    try:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-o", "--out-dir", default="aap-product-docs-plaintext")
        arg_parser.add_argument("-m", "--max-level", default=3)
        arg_parser.add_argument("--add-kb-articles", action=argparse.BooleanOptionalAction)

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
                    exit(1)
                subprocess.run(f"openssl enc -aes-256-cbc -d -pbkdf2 -pass pass:{secret} -in {in_file} -out {out_file}".split(" "),
                               capture_output=True, text=True, check=True)
                dirs = " ".join(SOURCE_DIRS)
                output = subprocess.run(f"tar xvzf {out_file} {dirs}".split(" "), capture_output=True, text=True, check=True)
                print(output)
                if args.add_kb_articles:
                    print("Extracting knowledge base articles...")
                    output = subprocess.run(f"tar xzf {out_file} {KNOWLEDGE_BASE_ARTICLES_DIR}".split(" "), capture_output=True, text=True,
                                            check=True)
                    print(output.stdout)
                    print(output.stderr)
                    print("done!")
            except subprocess.CalledProcessError:
                traceback.print_stack()
                exit(2)
            finally:
                if os.path.exists(in_file):
                    os.unlink(in_file)
                if os.path.exists(out_file):
                    os.unlink(out_file)
        else:
            print(f"{in_file} is not found. Skip the file extraction step.")

        if args.add_kb_articles:
            MimirParser(KNOWLEDGE_BASE_ARTICLES_DIR, os.path.join(args.out_dir, KNOWLEDGE_BASE_ARTICLES_DIR),
                        max_level=1, kb_article=True).run()

        doc_finder = DocFinder(SOURCE_DIRS)
        doc_finder.run()

        for base_dir in doc_finder.base_dirs:
            MimirParser(base_dir, os.path.join(args.out_dir, base_dir), int(args.max_level)).run()
    finally:
        print(f"Execution time: {(time.time() - start):.3f} secs")


if __name__ == '__main__':
    main()
