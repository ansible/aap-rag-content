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
"""Metadata handling for document nodes in vector database."""
import abc
import logging
import typing

import requests

LOG = logging.getLogger(__name__)


def check_url_reachable(url: str, retries: int = 3) -> bool:
    """Return True if the URL responds with HTTP 200.

    Retries the request when it fails or the status code is not 200.

    Args:
        url: URL to check.
        retries: Maximum number of GET attempts.

    Returns:
        True when the URL returns HTTP 200, otherwise False.
    """
    for trynum in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=30)
            if trynum < retries and response.status_code != 200:
                continue
            return response.status_code == 200
        except requests.exceptions.RequestException:
            if trynum < retries:
                continue
            return False
    return False


class MetadataProcessor:
    """Metadata processing callback.

    Projects should make their own metadata processors.
    Specifically, the `url_function` which is meant to derive URL
    from the name of a document, is not implemented.
    """

    def __init__(self, suppress_ping_url: bool = False):
        """Initialize MetadataProcessor.

        Args:
            suppress_ping_url: If True, skip URL reachability check and
                assume all URLs are reachable.
        """
        self.suppress_ping_url = suppress_ping_url

    def get_file_title(self, file_path: str) -> str:
        """Extract title from the plaintext doc file."""
        title = ""
        try:
            with open(file_path, encoding="utf-8") as file:
                title = file.readline().rstrip("\n").lstrip("# ")
        except Exception:  # noqa: S110 pylint: disable=broad-exception-caught
            pass
        return title

    def ping_url(self, url: str, retries: int = 3) -> bool:
        """Check if the URL parameter is live."""
        return check_url_reachable(url, retries=retries)

    def _resolve_url_reachable(self, url: str, file_path: str) -> bool:
        """Return whether the document URL is reachable.

        Args:
            url: Document URL to check.
            file_path: Path to the source document. Unused in the base
                implementation; subclasses may use it to read stored metadata.

        Returns:
            True when the URL is treated as reachable.
        """
        _ = file_path
        if self.suppress_ping_url:
            return True
        return self.ping_url(url)

    def populate(self, file_path: str) -> dict[str, typing.Any]:
        """Populate title and metadata with docs URL.

        Populate the docs_url, title and url_reachable metadata elements with docs URL,
        the page's title and if the url is reachable.

        Args:
            file_path: str: file path in str
        """
        doc_url = self.url_function(file_path)
        title = self.get_file_title(file_path)

        document = {
            "file_path": file_path,
            "title": title,
            "url": doc_url,
        }

        url_reachable = self._resolve_url_reachable(doc_url, file_path)
        if not url_reachable and not self.suppress_ping_url:
            LOG.warning(
                'URL not reachable: %(url)s (Title: "%(title)s", File path: %(file_path)s)',
                document,
            )

        LOG.debug(
            'Metadata populated for: "%(title)s" (URL: %(url)s, File path: %(file_path)s)',
            document,
        )

        return {"docs_url": doc_url, "title": title, "url_reachable": url_reachable}

    @abc.abstractmethod
    def url_function(self, file_path: str) -> str:
        """Derive URL to document source from given file path."""
        raise NotImplementedError
