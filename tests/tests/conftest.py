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

import sys
from types import ModuleType
from unittest.mock import MagicMock

try:
    import lightspeed_rag_content  # noqa: F401
except ImportError:
    # lightspeed_rag_content is only available inside the container image.
    # Install minimal stubs so tests can import custom_processor_aap.

    class _MetadataProcessor:
        def __init__(self, suppress_ping_url=False):
            self.suppress_ping_url = suppress_ping_url

        def ping_url(self, url):
            return True

        def populate(self, file_path):
            url = self.url_function(file_path)
            title = self.get_file_title(file_path)
            url_reachable = True if self.suppress_ping_url else self.ping_url(url)
            return {"docs_url": url, "title": title, "url_reachable": url_reachable}

    _utils_mod = MagicMock()
    _doc_proc_mod = MagicMock()
    _meta_proc_mod = ModuleType("lightspeed_rag_content.metadata_processor")
    _meta_proc_mod.MetadataProcessor = _MetadataProcessor  # type: ignore[attr-defined]

    _pkg = ModuleType("lightspeed_rag_content")
    _pkg.utils = _utils_mod  # type: ignore[attr-defined]
    _pkg.document_processor = _doc_proc_mod  # type: ignore[attr-defined]
    _pkg.metadata_processor = _meta_proc_mod  # type: ignore[attr-defined]

    sys.modules["lightspeed_rag_content"] = _pkg
    sys.modules["lightspeed_rag_content.utils"] = _utils_mod
    sys.modules["lightspeed_rag_content.document_processor"] = _doc_proc_mod
    sys.modules["lightspeed_rag_content.metadata_processor"] = _meta_proc_mod
