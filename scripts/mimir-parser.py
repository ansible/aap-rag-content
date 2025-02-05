import argparse
import configparser
import json
import os
import re
import time

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
    def __init__(self, base_dir, out_dir):
        self.base_dir = base_dir
        self.out_dir = out_dir
        self.metadata_dir = os.path.join(self.out_dir, ".metadata")

        if not os.path.isdir(self.out_dir):
            os.makedirs(self.out_dir)
        if not os.path.isdir(self.metadata_dir):
            os.makedirs(self.metadata_dir)

        self.sections = []
        self.toc = self.base_dir + "/toc/" + os.listdir(self.base_dir + "/toc")[0]
        self.md = self.base_dir + "/single-page/" + \
                  list(filter(lambda x: x.endswith(".md"),
                              os.listdir(self.base_dir + "/single-page")))[0]

    def process_section(self, section, level):
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


    def process_md(self):
        in_md_header = False
        config = "[__default__]\n"
        # Save Markdown files with .txt extension so that we can reuse the existing script
        out_file = os.path.join(self.out_dir, "__index__.txt")
        f = open(out_file, "w")
        section_index = 1

        for line in open(self.md, encoding="utf-8"):
            line = line.strip()

            if in_md_header:
                if line == "+++":
                    in_md_header = False
                    self.doc_metadata = configparser.ConfigParser()
                    self.doc_metadata.read_string(config)
                    metadata_file = os.path.join(self.metadata_dir, "__index__.json")
                    with open(metadata_file, "w") as meta:
                        metadata = {s:dict(self.doc_metadata.items(s)) for s in self.doc_metadata.sections()}
                        metadata["url"] = self.doc_metadata["extra"]["reference_url"]
                        metadata["path"] = self.doc_metadata["__default__"]["path"]
                        json.dump(metadata, meta, indent=2)
                else:
                    line = re.sub(r"^(.+)\s*=\s*\"(.+)\"", r"\1 = \2", line)
                    config += line + "\n"
                continue
            elif line == "+++":
                in_md_header = True
                continue

            if line.startswith("#"):
                title_to_match = self.sections[section_index]["title"]
                title = line.replace("\xa0", " ")
                title = re.sub(r"^#+\s*", "", title)
                title = re.sub(r"^Chapter\s*", "", title)
                if title == title_to_match:
                    base_url = self.doc_metadata["extra"]["reference_url"]
                    single_page_anchor = self.sections[section_index]['singlePageAnchor']
                    # print(f"[[ {base_url}#{single_page_anchor} ]]")
                    section_index += 1

                    if f:
                        f.flush()
                        f.close()
                        f = None

                    metadata_file = os.path.join(self.metadata_dir, f"{single_page_anchor}.json")
                    with open(metadata_file, "w") as meta:
                        metadata = dict()
                        metadata["url"] = f"{base_url}#{single_page_anchor}"
                        metadata["path"] = self.doc_metadata["__default__"]["path"]

                        # Remove the leading section/chapter number from titles
                        title = re.sub(r"^[\d\.]+ ", "", title)
                        metadata["title"] = title

                        json.dump(metadata, meta, indent=2)

                    # Save Markdown files with .txt extension so that we can reuse the existing script
                    out_file = os.path.join(self.out_dir, single_page_anchor + ".txt")
                    f = open(out_file, "w")

            # print(line)
            if f:
                print(line, file=f)

        if f:
            f.flush()
            f.close()
    def run(self):
        self.process_toc()
        self.process_md()


def main():
    start = time.time()
    try:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-o", "--out-dir", default="aap-product-docs-plaintext")
        args = arg_parser.parse_args()

        if "TARGET_DIRS" not in os.environ:
            # TEMPORARILY EXCLUDE AAP 2.5 DOCS AS MIMIR ARCHIVE DOES NOT CONTAIN THEM YET
            TARGET_DIRS="red_hat_content/documentation/ansible_on_clouds/2.x " + \
                        "red_hat_content/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest"
            # TARGET_DIRS="red_hat_content/documentation/ansible_on_clouds/2.x " + \
            #             "red_hat_content/documentation/red_hat_ansible_automation_platform/2.5 " + \
            #             "red_hat_content/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest"
        else:
            TARGET_DIRS = os.getenv("TARGET_DIRS")

        target_dirs = TARGET_DIRS.split()

        doc_finder = DocFinder(target_dirs)
        doc_finder.run()

        for base_dir in doc_finder.base_dirs:
            MimirParser(base_dir, os.path.join(args.out_dir, base_dir)).run()
    finally:
        print(f"Execution time: {(time.time() - start):.3f} secs")


if __name__ == '__main__':
    main()
