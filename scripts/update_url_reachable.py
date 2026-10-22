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
"""Record URL reachability in product-docs metadata JSON files.

Downstream vector-DB builds may not have network access, so this script
pings each metadata URL while the network is available and stores the
result as ``url_reachable``. Run it after regenerating plaintext docs,
for example:

    PYTHONPATH=src uv run python3 scripts/update_url_reachable.py
"""

import argparse
import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from aap_rag_content.metadata_processor import check_url_reachable
from aap_rag_content.utils import resolve_output_path, setup_cli_logging

LOG = logging.getLogger(__name__)

DEFAULT_FOLDER = "aap-product-docs-plaintext"
DEFAULT_WORKERS = 8
DEFAULT_RETRIES = 3


@dataclass
class UpdateStats:
    """Summary of a metadata URL-reachability update run."""

    files_seen: int = 0
    files_updated: int = 0
    files_unchanged: int = 0
    files_skipped: int = 0
    files_failed: int = 0
    missing_url: int = 0
    unique_urls: int = 0
    unreachable_urls: list[str] = field(default_factory=list)


def canonical_url(url: str) -> str:
    """Return URL without a fragment so equivalent pages share a ping result."""
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, ""))


def find_metadata_files(folder: Path) -> list[Path]:
    """Return JSON files stored in ``.metadata`` directories under folder."""
    return sorted(
        path for path in folder.rglob("*.json") if path.parent.name == ".metadata"
    )


def load_metadata(path: Path) -> dict[str, Any] | None:
    """Load a metadata JSON object, or None when the file cannot be used."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        LOG.exception("Failed to read %s", path)
        return None
    if not isinstance(data, dict):
        LOG.error("Metadata file %s is not a JSON object", path)
        return None
    return data


def write_metadata(path: Path, data: dict[str, Any]) -> None:
    """Write metadata JSON with the same formatting as other generators."""
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")


def check_urls(
    urls: list[str],
    workers: int,
    retries: int,
) -> dict[str, bool]:
    """Return a mapping of canonical URL to reachability."""
    results: dict[str, bool] = {}
    if not urls:
        return results

    worker_count = max(1, workers)
    LOG.info("Checking %s unique URL(s) with %s worker(s)", len(urls), worker_count)

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        future_to_url = {
            executor.submit(check_url_reachable, url, retries): url for url in urls
        }
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            reachable = future.result()
            results[url] = reachable
            if not reachable:
                LOG.warning("URL not reachable: %s", url)
    return results


def _collect_urls_to_check(
    folder: Path,
    skip_existing: bool,
    stats: UpdateStats,
) -> tuple[list[tuple[Path, dict[str, Any], str | None]], list[str]]:
    """Load metadata files and collect unique URLs that need a ping."""
    pending: list[tuple[Path, dict[str, Any], str | None]] = []
    urls_to_check: list[str] = []
    seen_urls: set[str] = set()

    for path in find_metadata_files(folder):
        stats.files_seen += 1
        data = load_metadata(path)
        if data is None:
            stats.files_failed += 1
            continue
        if skip_existing and isinstance(data.get("url_reachable"), bool):
            stats.files_skipped += 1
            continue

        raw_url = data.get("url")
        url = raw_url.strip() if isinstance(raw_url, str) else None
        if not url:
            LOG.warning("Metadata file %s is missing a url", path)
            stats.missing_url += 1
            pending.append((path, data, None))
            continue

        pending.append((path, data, url))
        canonical = canonical_url(url)
        if canonical not in seen_urls:
            seen_urls.add(canonical)
            urls_to_check.append(canonical)

    return pending, urls_to_check


def update_metadata_files(
    folder: Path,
    workers: int = DEFAULT_WORKERS,
    retries: int = DEFAULT_RETRIES,
    dry_run: bool = False,
    skip_existing: bool = False,
) -> UpdateStats:
    """Ping metadata URLs and store ``url_reachable`` on each JSON file.

    Args:
        folder: Root directory that contains ``.metadata`` JSON files.
        workers: Number of concurrent URL checks.
        retries: Maximum GET attempts per unique URL.
        dry_run: When True, report changes without writing files.
        skip_existing: When True, leave files that already have url_reachable.

    Returns:
        Totals for files processed, updated, skipped, and unreachable URLs.
    """
    stats = UpdateStats()
    pending, urls_to_check = _collect_urls_to_check(folder, skip_existing, stats)
    stats.unique_urls = len(urls_to_check)
    reachability = check_urls(urls_to_check, workers=workers, retries=retries)
    stats.unreachable_urls = sorted(
        url for url, reachable in reachability.items() if not reachable
    )

    for path, data, url in pending:
        url_reachable = reachability[canonical_url(url)] if url else False
        if data.get("url_reachable") is url_reachable:
            stats.files_unchanged += 1
            continue
        data["url_reachable"] = url_reachable
        stats.files_updated += 1
        if dry_run:
            LOG.info(
                "Would set url_reachable=%s on %s",
                url_reachable,
                path,
            )
            continue
        write_metadata(path, data)

    return stats


def build_arg_parser() -> argparse.ArgumentParser:
    """Return the CLI parser for the metadata URL-reachability updater."""
    parser = argparse.ArgumentParser(
        description=(
            "Add url_reachable to metadata JSON files by pinging each URL. "
            "URL fragments are ignored so pages that share a document URL "
            "are checked once."
        )
    )
    parser.add_argument(
        "-f",
        "--folder",
        default=DEFAULT_FOLDER,
        help=f"Directory containing metadata JSON files (default: {DEFAULT_FOLDER})",
    )
    parser.add_argument(
        "-w",
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help=f"Number of concurrent URL checks (default: {DEFAULT_WORKERS})",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=DEFAULT_RETRIES,
        help=f"Number of ping attempts per unique URL (default: {DEFAULT_RETRIES})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check URLs and report changes without writing files",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Do not re-check files that already have url_reachable",
    )
    return parser


def format_summary(stats: UpdateStats, dry_run: bool) -> str:
    """Return a one-line summary of the update run."""
    action = "Would update" if dry_run else "Updated"
    return (
        f"Checked {stats.unique_urls} unique URL(s) across {stats.files_seen} "
        f"metadata file(s). {action} {stats.files_updated}, unchanged "
        f"{stats.files_unchanged}, skipped {stats.files_skipped}, failed "
        f"{stats.files_failed}, missing url {stats.missing_url}, unreachable "
        f"{len(stats.unreachable_urls)}."
    )


def main(argv: list[str] | None = None) -> None:
    """Parse CLI arguments and update metadata JSON files."""
    args = build_arg_parser().parse_args(argv)
    setup_cli_logging("update_url_reachable")
    folder = Path(resolve_output_path(args.folder))
    if not folder.is_dir():
        raise SystemExit(f"Folder does not exist: {folder}")

    stats = update_metadata_files(
        folder,
        workers=args.workers,
        retries=args.retries,
        dry_run=args.dry_run,
        skip_existing=args.skip_existing,
    )
    print(format_summary(stats, args.dry_run))
    if stats.unreachable_urls:
        print("Unreachable URLs:")
        for url in stats.unreachable_urls:
            print(f"  {url}")
    if stats.files_failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
