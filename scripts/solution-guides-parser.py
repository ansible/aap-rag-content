"""Download and parse solution guides for RAG DB ingestion."""

import argparse
import json
import os
import re
import time
import urllib.request
import urllib.error

SOLUTION_GUIDES_REPO_URL = "https://github.com/ansible-tmm/solution-guides/"
SOLUTION_GUIDES_WEB_PAGE = "https://ansible-tmm.github.io/solution-guides/"

SOURCE_FILES = [
    "README-AIOps.md",
    "README-EDB.md",
    "README-Instana-AIOps.md",
    "README-IA.md",
    "README-Intelligent-Assistant-RHAIIS.md",
    "README-AIOps-ServiceNow.md",
    "README-AIOps-Splunk-ITSI.md",
]


class SolutionGuidesParser:
    """Parse solution guide markdown files and generate metadata for RAG."""

    def __init__(self, repo_dir, out_dir):
        self.repo_dir = repo_dir
        self.out_dir = out_dir
        self.metadata_dir = os.path.join(self.out_dir, ".metadata")

        if not os.path.isdir(self.out_dir):
            os.makedirs(self.out_dir)
        if not os.path.isdir(self.metadata_dir):
            os.makedirs(self.metadata_dir)

    def _build_web_url(self, source_file):
        """Return the GitHub Pages URL for a source file."""
        slug = source_file.replace(".md", "")
        return f"{SOLUTION_GUIDES_WEB_PAGE}{slug}"

    def _extract_title(self, lines):
        """Return the first H1 heading, stripping HTML comments."""
        for line in lines:
            if line.startswith("# "):
                title = line.lstrip("# ").strip()
                title = re.sub(r"\s*<!--.*?-->", "", title)
                return title
        return None

    def _parse_file(self, source_file):
        """Copy a source file to out_dir (stripping images) and write metadata."""
        file_path = os.path.join(self.repo_dir, source_file)
        if not os.path.isfile(file_path):
            print(f"Warning: {file_path} not found, skipping.")
            return

        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()

        title = self._extract_title(lines)
        web_url = self._build_web_url(source_file)
        stem = source_file.replace(".md", "")

        out_file = os.path.join(self.out_dir, source_file)
        with open(out_file, "w", encoding="utf-8") as f:
            for line in lines:
                line = re.sub(r"<img\s[^>]*>", "", line)
                line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)
                f.write(line)

        metadata = {
            "title": title,
            "url": web_url,
            "path": source_file,
        }
        metadata_file = os.path.join(self.metadata_dir, f"{stem}.json")
        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

    def download_files(self):
        """Download only the SOURCE_FILES from the GitHub repository."""
        if not os.path.isdir(self.repo_dir):
            os.makedirs(self.repo_dir)

        raw_base_url = SOLUTION_GUIDES_REPO_URL.replace(
            "github.com", "raw.githubusercontent.com"
        ).rstrip("/") + "/main/"

        for source_file in SOURCE_FILES:
            url = raw_base_url + source_file
            dest = os.path.join(self.repo_dir, source_file)
            print(f"Downloading {source_file}...")
            try:
                urllib.request.urlretrieve(url, dest)
            except urllib.error.HTTPError as e:
                print(f"Warning: failed to download {source_file}: {e}")

    def run(self):
        for source_file in SOURCE_FILES:
            self._parse_file(source_file)


def main():
    start = time.time()
    try:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument(
            "-o", "--out-dir", default="solution-guides-plaintext"
        )
        arg_parser.add_argument(
            "-r", "--repo-dir", default="solution-guides"
        )
        arg_parser.add_argument(
            "--skip-download", action="store_true",
            help="Skip downloading source files from the repository",
        )
        args = arg_parser.parse_args()

        parser = SolutionGuidesParser(args.repo_dir, args.out_dir)
        if not args.skip_download:
            parser.download_files()
        parser.run()
    finally:
        print(f"Execution time: {(time.time() - start):.3f} secs")


if __name__ == "__main__":
    main()

