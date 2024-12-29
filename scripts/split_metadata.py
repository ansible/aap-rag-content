import argparse
import json
from pathlib import Path


def process_metadata(base_dir, metadata):
    for k,v in metadata.items():
        i = k.index("/")
        j = k.rindex("/")
        txt_file = base_dir.joinpath(k[(i+1):].replace(".adoc", ".txt"))
        if txt_file.is_file():
            metadata_dir = base_dir.joinpath(k[(i+1):j]).joinpath('.metadata')
            if not metadata_dir.is_dir():
                metadata_dir.mkdir()
            metadata_file = metadata_dir.joinpath(k[(j+1):].replace(".adoc", ".json"))
            with open(metadata_file, "w", encoding="utf8") as f:
                json.dump(v, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="split metadata")
    parser.add_argument("-f", "--folder", help="Plain text folder path")
    parser.add_argument("-v", "--aap-version", help="AAP version")
    args = parser.parse_args()

    for sub_dir in [args.aap_version, "lightspeed-latest", "aap-clouds-latest"]:
        base_dir = Path(args.folder).joinpath(sub_dir)
        metadata_json = base_dir.joinpath("metadata.json")
        with open(metadata_json, encoding="utf8") as f:
            metadata = json.load(f)
        process_metadata(base_dir, metadata)
        metadata_json.unlink()


if __name__ == '__main__':
    main()
