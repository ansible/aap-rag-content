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

import importlib
import sys
from pathlib import Path

import pytest

scripts_dir = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

_mod = importlib.import_module("download_embeddings_model")


@pytest.fixture
def snapshot_download_mock(mocker):
    """Mock huggingface_hub.snapshot_download before download_model imports it."""
    hub_mock = mocker.MagicMock()
    mocker.patch.dict(sys.modules, {"huggingface_hub": hub_mock})
    return hub_mock.snapshot_download


class TestDownloadModel:
    """Test cases for download_model()."""

    def _prepare_model_dir(self, model_dir):
        """Create the files/dirs download_model expects the snapshot to contain."""
        model_dir.mkdir(parents=True, exist_ok=True)
        (model_dir / "pytorch_model.bin").write_text("weights")
        (model_dir / "onnx").mkdir()
        (model_dir / "openvino").mkdir()

    def test_downloads_and_prepares_model(
        self, tmp_path, monkeypatch, snapshot_download_mock
    ):
        """The snapshot is downloaded and post-processed for offline use."""
        monkeypatch.chdir(tmp_path)
        self._prepare_model_dir(tmp_path / "model")

        result = _mod.download_model("model", "org/some-model")

        assert Path(result) == tmp_path / "model"
        snapshot_download_mock.assert_called_once_with(
            repo_id="org/some-model", local_dir=str(tmp_path / "model")
        )
        assert (tmp_path / "model" / "2_Normalize").is_dir()
        assert (tmp_path / "model" / "version.txt").read_text() == "1"
        assert not (tmp_path / "model" / "pytorch_model.bin").exists()
        assert not (tmp_path / "model" / "onnx").exists()
        assert not (tmp_path / "model" / "openvino").exists()

    def test_rejects_escaping_local_dir(
        self, tmp_path, monkeypatch, snapshot_download_mock
    ):
        """A local_dir escaping the working directory is rejected before download."""
        monkeypatch.chdir(tmp_path)

        with pytest.raises(ValueError, match="escapes the working directory"):
            _mod.download_model("../outside", "org/some-model")
        snapshot_download_mock.assert_not_called()

    def test_main_passes_cli_args(self, mocker, monkeypatch):
        """main() wires CLI arguments through to download_model()."""
        download_mock = mocker.patch.object(_mod, "download_model")
        monkeypatch.setattr(
            sys, "argv", ["prog", "-l", "model_dir", "-r", "org/some-model"]
        )

        _mod.main()

        download_mock.assert_called_once_with("model_dir", "org/some-model")
