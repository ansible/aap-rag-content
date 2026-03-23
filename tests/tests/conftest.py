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


class RagMockEmbedding:
    """Mock class for HuggingFaceEmbedding."""

    def __init__(self, model_name="ABC", embed_dim=768):
        """Initialize the mock class."""
        self.model_name = model_name
        self.embed_dim = embed_dim

    def get_text_embedding(self, text):
        """Simulate the text embedding with the right size."""
        return "A" * self.embed_dim
