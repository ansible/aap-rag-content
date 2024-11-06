"""
Rename unused text files by adding "__EXCLUDED__" extension so that they are not included in
the vector database
"""
import argparse
import json
import os
from pathlib import Path


def main():
    """
    Main routine
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-input_dir", "-i")
    parser.add_argument("--git-branch", "-b")

    args = parser.parse_args()
    project_document_path = "lightspeed" if args.git_branch == "lightspeed-latest" else "downstream"

    with open(Path(args.input_dir).joinpath("metadata.json"), encoding="utf8") as f:
        metadata = json.load(f)

    text_files = list(Path(args.input_dir).rglob("*.txt"))

    n = len(Path(args.input_dir).parts)

    found = 0
    not_found = 0
    for text_file in text_files:
        relative_path_name = "/".join(text_file.parts[n:])
        adoc_name = str(Path(project_document_path).joinpath(relative_path_name))
        adoc_name = adoc_name.replace(".txt", ".adoc")
        if adoc_name in metadata:
            url = metadata[adoc_name]["url"]
        else:
            url = None

        if url:
            found += 1
        else:
            not_found += 1
            os.rename(str(text_file), str(text_file) + ".__EXCLUDED__")

    print(f"found:{found} not_found:{not_found}")


if __name__ == "__main__":
    main()
