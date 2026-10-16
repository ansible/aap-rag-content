"""Download and parse solution guides for RAG DB ingestion."""  # pylint: disable=invalid-name

import argparse
import json
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

SOLUTION_GUIDES_REPO_URL = "https://github.com/ansible-tmm/solution-guides/"
SOLUTION_GUIDES_WEB_PAGE = "https://ansible-tmm.github.io/solution-guides/"

SOURCE_FILES = [
    "README-AAP-HA-DR-OpenShift.md",
    "README-AAP-PostgreSQL-Autovacuum-Tuning.md",
    "README-AIOps-Azure-Service-Bus.md",
    "README-AIOps-LogicMonitor.md",
    "README-AIOps.md",
    "README-AIOps-ServiceNow.md",
    "README-AIOps-Splunk-ITSI.md",
    # "README-AIOps-Ticket-Enrichment.md",
    "README-AIOps-Use-Case-01-Incident-Ticket-Enrichment.md",
    "README-AIOps-Use-Case-02-Cost-Resource-Optimization.md",
    "README-AIOps-Use-Case-03-Intelligent-Capacity-Orchestration.md",
    "README-AIOps-Use-Case-04-Curated-Automation-Remediation.md",
    "README-AIOps-Use-Case-05-System-Drift-Policy-Enforcement.md",
    "README-AIOps-Use-Case-06-Self-Healing-Infrastructure.md",
    "README-AIOps-Windows-Cert-Rotation.md",
    "README-Ansible-DevSpaces.md",
    "README-Ansible-DevTools.md",
    "README-best-practices-implementation.md",
    "README-best-practices.md",
    "README-EDB.md",
    "README-Falco-runtime-mitigation.md",
    "README-Gluware-Network-Automation.md",
    "README-IA.md",
    "README-Instana-AIOps.md",
    "README-Intelligent-Assistant-RHAIIS.md",
    # "README.md",
    "README-NetBox-SoT-EDA-Config.md",
    "README-NetBox-WAN-EDA-Failover.md",
    "README-OpenShift-EDA-Kafka.md",
    "README-Patching-RHEL.md",
    "README-PQC-Discovery.md",
    "README-Satellite-CVE-Remediation.md",
    "README-ServiceNow-ITSM.md",
    "README-SQS.md",
    "README-ZTA.md",
]


class SolutionGuidesParser:
    """Parse solution guide markdown files and generate metadata for RAG."""

    def __init__(self, repo_dir, out_dir):
        # repo_dir is a read-only source location and may legitimately live
        # outside the working directory; only the output dir is contained.
        self.repo_dir = repo_dir
        self.out_dir = resolve_output_path(out_dir)
        self.metadata_dir = os.path.join(self.out_dir, ".metadata")

        if not os.path.isdir(self.out_dir):
            os.makedirs(self.out_dir)
        if not os.path.isdir(self.metadata_dir):
            os.makedirs(self.metadata_dir)

    def _build_web_url(self, source_file):
        """Return the GitHub Pages URL for a source file."""
        slug = source_file.replace(".md", "")
        return f"{SOLUTION_GUIDES_WEB_PAGE}{slug}"

    def _strip_leading_raw_tag(self, lines):
        """Return lines without a leading Jinja '{% raw %}' line."""
        if lines and lines[0].strip() == "{% raw %}":
            return lines[1:]
        return lines

    def _is_markdown_heading(self, line):
        """Return True if line is an ATX markdown heading."""
        return bool(re.match(r"#{1,6}\s", line.lstrip()))

    def _html_block_end(self, lines, start, tag):
        """Return the index of the closing tag for an opening tag at start.

        Returns None when the line at start is not that tag or no closing tag
        is found.
        """
        if start >= len(lines) or not re.match(
            rf"<{tag}\b", lines[start].lstrip(), flags=re.IGNORECASE
        ):
            return None
        close = re.compile(rf"</{tag}>", flags=re.IGNORECASE)
        end = start
        while end < len(lines):
            if close.search(lines[end]):
                return end
            end += 1
        return None

    def _preamble_block_end(self, lines, start):
        """Return (tag, end_index) for a preamble HTML block opening at start."""
        for tag in ("div", "style", "a"):
            end = self._html_block_end(lines, start, tag)
            if end is not None:
                return tag, end
        return None, None

    def _strip_preamble_html(self, lines):
        """Remove preamble HTML blocks before the first markdown heading.

        Drops leading <div>, <style>, and <a> blocks. Returns
        (first_div_html, remaining_lines). first_div_html is None when no
        preamble <div> is present.
        """
        remaining = []
        first_div = None
        idx = 0
        while idx < len(lines):
            if self._is_markdown_heading(lines[idx]):
                remaining.extend(lines[idx:])
                break
            tag, end = self._preamble_block_end(lines, idx)
            if end is not None:
                if tag == "div" and first_div is None:
                    first_div = "".join(lines[idx : end + 1])
                idx = end + 1
                continue
            remaining.append(lines[idx])
            idx += 1
        return first_div, remaining

    def _strip_leading_blank_lines(self, lines):
        """Return lines without a leading run of blank lines."""
        idx = 0
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
        return lines[idx:]

    def _strip_html_comments(self, text):
        """Remove HTML comments from text."""
        while "<!--" in text:
            comment_start = text.find("<!--")
            comment_end = text.find("-->", comment_start + 4)
            if comment_end == -1:
                break
            text = (text[:comment_start] + text[comment_end + 3 :]).strip()
        return text

    def _title_from_h1(self, html):
        """Return the text of the first HTML <h1>, or None."""
        match = re.search(
            r"<h1\b[^>]*>(.*?)</h1>",
            html,
            flags=re.DOTALL | re.IGNORECASE,
        )
        if not match:
            return None
        title = self._strip_html_comments(match.group(1))
        title = re.sub(r"<[^>]+>", "", title)
        title = re.sub(r"\s+", " ", title).strip()
        return title or None

    def _extract_markdown_title(self, lines):
        """Return the first markdown H1 heading, stripping HTML comments."""
        for line in lines:
            if line.startswith("# "):
                title = self._strip_html_comments(line.lstrip("# ").strip())
                return title or None
        return None

    def _extract_title(self, lines):
        """Return the document title from a leading HTML h1 or markdown H1."""
        lines = self._strip_leading_raw_tag(lines)
        first_div, remaining = self._strip_preamble_html(lines)
        if first_div:
            title = self._title_from_h1(first_div)
            if title:
                return title
            lines = remaining
        return self._extract_markdown_title(lines)

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
        _, body_lines = self._strip_preamble_html(self._strip_leading_raw_tag(lines))
        body_lines = self._strip_leading_blank_lines(body_lines)

        out_file = os.path.join(self.out_dir, source_file)
        with open(out_file, "w", encoding="utf-8") as f:
            for line in body_lines:
                line = re.sub(r"<img\s[^>]*>", "", line)
                # Strip linked images ([![...](...)](#...)) before plain images
                line = re.sub(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)", "", line)
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
            f.write("\n")

    def _check_url(self, url):
        """Return None if url is reachable, otherwise a description of the failure."""
        if urllib.parse.urlparse(url).scheme in {"http", "https"}:
            try:
                with urllib.request.urlopen(url, timeout=30) as response:  # noqa: S310
                    if 200 <= response.status < 400:
                        return None
                    return f"{url} (HTTP {response.status})"
            except urllib.error.HTTPError as e:
                return f"{url} (HTTP {e.code})"
            except OSError as e:
                return f"{url} ({e})"
        return f"{url} (unsupported scheme)"

    def _verify_metadata_urls(self):
        """Abort if any generated metadata URL is unreachable."""
        unreachable = []
        for source_file in SOURCE_FILES:
            stem = source_file.replace(".md", "")
            metadata_file = os.path.join(self.metadata_dir, f"{stem}.json")
            if not os.path.isfile(metadata_file):
                continue
            with open(metadata_file, encoding="utf-8") as f:
                metadata = json.load(f)
            url = metadata.get("url")
            if not url:
                unreachable.append(f"{metadata_file}: missing url")
                continue
            print(f"Verifying {url}...")
            error = self._check_url(url)
            if error:
                unreachable.append(error)

        if unreachable:
            print(
                "ERROR: unreachable metadata URL(s):",
                file=sys.stderr,
            )
            for item in unreachable:
                print(f"  {item}", file=sys.stderr)
            sys.exit(1)

    def download_files(self):
        """Download only the SOURCE_FILES from the GitHub repository."""
        if not os.path.isdir(self.repo_dir):
            os.makedirs(self.repo_dir)

        raw_base_url = (
            SOLUTION_GUIDES_REPO_URL.replace("github.com", "raw.githubusercontent.com").rstrip("/")
            + "/main/"
        )

        failures = []
        for source_file in SOURCE_FILES:
            url = raw_base_url + source_file
            dest = os.path.join(self.repo_dir, source_file)
            print(f"Downloading {source_file}...")
            try:
                with (
                    urllib.request.urlopen(url, timeout=30) as response,
                    open(dest, "wb") as out,
                ):
                    shutil.copyfileobj(response, out)
            except OSError as e:
                print(
                    f"ERROR: failed to download {source_file}: {e}",
                    file=sys.stderr,
                )
                failures.append(source_file)

        if failures:
            print(
                f"\n{len(failures)} download(s) failed: {', '.join(failures)}",
                file=sys.stderr,
            )
            print(
                "Aborting to avoid producing an incomplete corpus.",
                file=sys.stderr,
            )
            sys.exit(1)

    def run(self):
        """Parse all source files and write plaintext output with metadata."""
        for source_file in SOURCE_FILES:
            self._parse_file(source_file)
        self._verify_metadata_urls()


def main():
    """Entry point for the solution guides parser CLI."""
    start = time.time()
    try:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-o", "--out-dir", default="solution-guides-plaintext")
        arg_parser.add_argument("-r", "--repo-dir", default="solution-guides")
        arg_parser.add_argument(
            "--skip-download",
            action="store_true",
            help="Skip downloading source files from the repository",
        )
        args = arg_parser.parse_args()

        parser = SolutionGuidesParser(args.repo_dir, args.out_dir)
        if not args.skip_download:
            parser.download_files()
        parser.run()
    finally:
        print(f"Execution time: {(time.time() - start):.3f} secs")


def resolve_output_path(path: str) -> str:
    """Validate a CLI-supplied output path, rejecting relative ``..`` escapes.

    An absolute path is honored as explicit operator intent and only
    lexically normalized — it is NOT contained. A relative path is
    anchored at the current working directory and must stay within it
    *lexically*: ``../`` escapes are rejected, while symlinks inside the
    tree are deliberately not resolved, so a symlinked output directory
    (e.g. ``./output`` pointing at a scratch disk) keeps working. For
    strict, symlink-resolving containment of input paths, use
    :func:`resolve_within_cwd` instead.

    Args:
        path: A path provided via a CLI argument or config value.

    Returns:
        The absolute, lexically normalized path.

    Raises:
        ValueError: If a relative path lexically escapes the working
            directory.
    """
    if os.path.isabs(path):
        return os.path.normpath(path)
    base = os.getcwd()
    resolved = os.path.normpath(os.path.join(base, path))
    if resolved != base and not resolved.startswith(base + os.sep):
        raise ValueError(f"Path escapes the working directory: {path}")
    return resolved


if __name__ == "__main__":
    main()
