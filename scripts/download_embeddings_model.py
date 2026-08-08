"""Utility script to download models from HuggingFace."""

import argparse
import os
import shutil

from aap_rag_content.utils import resolve_within_cwd

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Script to download models from HuggingFace"
    )
    parser.add_argument(
        "-l", "--local-dir", required=True, help="Directory to download model to"
    )
    parser.add_argument("-r", "--hf-repo-id", required=True, help="Model repo id")
    args = parser.parse_args()

    os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"

    from huggingface_hub import snapshot_download

    # OLS-823: validate local directory stays under the working directory
    local_directory = resolve_within_cwd(args.local_dir)

    snapshot_download(repo_id=args.hf_repo_id, local_dir=local_directory)

    # workaround for https://github.com/UKPLab/sentence-transformers/pull/2460
    os.makedirs(os.path.join(local_directory, "2_Normalize"), exist_ok=True)

    # pretend local_dir is HF cache
    with open(os.path.join(local_directory, "version.txt"), "w", encoding="utf-8") as f:
        f.write("1")

    # remove pytorch_model.bin, load the model from model.safetensors
    os.remove(os.path.join(local_directory, "pytorch_model.bin"))

    shutil.rmtree(os.path.join(local_directory, "onnx"))
    shutil.rmtree(os.path.join(local_directory, "openvino"))
