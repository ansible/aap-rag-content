#!/usr/bin/python

"""Utility script to convert AAP docs from adoc to plain text."""

import argparse
import os
import re
import subprocess
import sys

import yaml

from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This command converts the app-docs assemblies to plain text.",
        usage="convert-it-all-aap [options]",
    )

    parser.add_argument(
        "--input-dir",
        "-i",
        required=True,
        help="The input directory for the aap-docs repo",
    )
    parser.add_argument(
        "--output-dir", "-o", required=True, help="The output directory for text"
    )
    parser.add_argument(
        "--attributes", "-a", help="An optional file containing attributes"
    )

    args = parser.parse_args(sys.argv[1:])

    attribute_map = {}
    attribute_list: list = []   
    if args.attributes is not None:
        pattern = re.compile(r'^:(\w+):\s+(.+)\s*$')
        for line in open(args.attributes, "r"):
            line = line.strip()
            if len(line) == 0 or line.startswith('//'):
                continue
            m = pattern.match(line)
            if m:
                attribute_map[m.group(1)] = m.group(2)
        
        attribute_map_copy = attribute_map.copy()
        pattern2 = re.compile(r'^.*{(\w+)}.*$')
        for k,v in attribute_map.items():
            m = pattern2.match(v)
            if m:
                key = m.group(1)
                if key in attribute_map:
                    v = v.replace("{" + key + "}", attribute_map[key])
            attribute_map_copy[k] = v

        for k,v in attribute_map_copy.items():
            attribute_list = [*attribute_list, "-a", k + "=%s" % v]
        print(attribute_list)

    output_dir = os.path.normpath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    input_dir = os.path.normpath(args.input_dir)
    script_dir = os.path.dirname(os.path.realpath(__file__))

    mega_file_list: list = list(Path(".").joinpath(args.input_dir).rglob("*.adoc"))

    for filename in mega_file_list:
        input_file = str(filename)
        filename = input_file.replace(args.input_dir + '/downstream/', '').replace(".adoc", "")
        output_file = os.path.join(output_dir, filename + ".txt")
        print(f"{input_file} -> {output_file}")
        os.makedirs(os.path.dirname(os.path.realpath(output_file)), exist_ok=True)
        # input_file = os.path.join(input_dir, filename + ".adoc")
        converter_file = os.path.join(script_dir, "text-converter.rb")
        print("Processing: " + input_file)
        command = ["asciidoctor"]
        command = command + attribute_list
        command = [
            *command,
            "-r",
            converter_file,
            "-b",
            "text",
            "-o",
            output_file,
            "--trace",
            "--quiet",
            input_file,
        ]
        result = subprocess.run(command, check=False)  # noqa: S603
        if result.returncode != 0:
            print(result)
            print(result.stdout)
