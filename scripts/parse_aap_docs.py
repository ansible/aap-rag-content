"""
Parse Asciidoc files in the aap-docs repository to calculate the URLs on the product
documentation site
"""
# pylint: disable=C0103,R0902,R0912,R0913,R0917,R1732
import argparse
import copy
import json
import os
import re
import sys
from pathlib import Path

import requests


class ParseAAPDocs:
    """
    Parse the aap-docs repository and locate Red Hat product document URLs for each
    source Asciidoc file so that they can be used as referenced document links
    displayed on the chatbot UI.

    Reference: Modular documentation reference guide
    https://redhat-documentation.github.io/modular-docs/
    """

    def __init__(
        self, base_dir, project_document_path, files_to_skip, git_branch, do_validate=False
    ):
        """
        Initialize the ParseAAPDocs object

        :param base_dir: aap-docs local repository
        :param project_document_path: a relative path where Asciidoc sources are stored
        :param files_to_skip: a list of Ascii files paths to be ignored in the processing
        :param git_branch: a git branch of aap-docs repo that is used for the input source
        :param do_validate: whether a validation of URL is executed or not
        """
        self.base_dir = base_dir
        self.project_document_path = project_document_path
        self.files_to_skip = files_to_skip
        self.git_branch = git_branch
        self.do_validate = do_validate
        self.attributes_dict = {}
        self.title_dict = {}
        self.adocs_dict = {}

    def run(self):
        """
        Analyze the local aap-docs repository and calculate URLs for each Ascii file

        :return: None
        """
        self.parse_attributes()
        self.adocs_dict = self.get_dict()
        self.parse_doc_info_files()
        self.parse_include()
        self.parse_title_docs()

        has_url = list(filter(lambda x: self.adocs_dict[x]["url"] is not None, self.adocs_dict))
        print(f"has_url: {len(has_url)}")
        print(f"total: {len(self.adocs_dict)}")

    def validate(self, adoc):
        """
        Validate the URL given to a specified Asciidoc is a valid documentation URL

        :param adoc:
        :return: whether the URL is valid or not.
        """
        url = adoc["url"]
        try:
            response = requests.get(url, allow_redirects=False, timeout=10)
            if response.status_code == 200:
                return True
            print(f"INVALID: {url} status_code={response.status_code}")
            return False
        except requests.ConnectionError:
            print(f"INVALID: {url} ConnectionError")
            return False

    def parse_title_docs(self):
        """
        Parse title documents

        :return: None
        """
        title_docs = list(filter(lambda x: self.adocs_dict[x]["url"] is not None, self.adocs_dict))
        for title_doc in title_docs:
            if title_doc in self.files_to_skip:
                self.adocs_dict[title_doc]["url"] = None
                continue
            self.adocs_dict[title_doc]["url"] = self.adocs_dict[title_doc]["url"].replace(
                "/html/", "/html-single/"
            ).replace(
                "/ansible_on_clouds/2.x_latest/", "/ansible_on_clouds/2.x/"
            )
            print(title_doc, self.adocs_dict[title_doc]["url"])

            context = {
                "name": None,
                "url": self.adocs_dict[title_doc]["url"],
                "base_url": self.adocs_dict[title_doc]["url"],
            }
            self.adocs_dict[title_doc]["url"] = self.adocs_dict[title_doc]["url"] + "/index"
            self.simulate_includes(self.adocs_dict[title_doc], context)

    def simulate_includes(self, adoc, context):
        """
        Simulate Asciidoc include operation. Note that this code does not read files line by
        line like a real parser. So the results might be different from the ones obtained from
        a real Asciidoc parser.

        :param adoc: An Asciidoc to be parsed
        :param context: The current context
        :return: None
        """
        _id = None
        nesting_assembly = adoc["nesting_assembly"]
        context_save = copy.copy(context) if nesting_assembly else None

        if adoc["id"]:
            _id = adoc["id"]
            if "{context}" in _id:
                if context["name"] is None:
                    _id = _id.replace("_{context}", "")
                else:
                    _id = _id.replace("{context}", context["name"])
            if adoc["url"]:
                print(f"A URL is already set for {adoc['project_file_name']}")
            else:
                if context["url"] == context["base_url"]:
                    adoc["url"] = f"{context['url']}/index#{_id}"
                else:
                    adoc["url"] = f"{context['url']}#{_id}"
                if self.do_validate and not self.validate(adoc):
                    sys.exit(1)
                print(
                    f"A URL {adoc['url']} is set for {adoc['project_file_name']} context={context}"
                )

        if adoc["context"]:
            if not context["name"] and _id:
                context["url"] = f"{context['url']}/{_id}"
            context["name"] = adoc["context"]

        for include in adoc["includes"]:
            self.simulate_includes(self.adocs_dict[include], context)

        if context_save:
            context["name"] = context_save["name"]
            context["url"] = context_save["url"]

    def get_adocs(self):
        """
        Get the list of Ascii documents in the aap-docs local repo. Ignore files under
        /archive/ folder.

        :return:  None.
        """
        return list(
            filter(
                lambda x: "/archive/" not in str(x),
                Path(self.base_dir).joinpath(self.project_document_path).rglob("*.adoc"),
            )
        )

    def parse_doc_info_files(self):
        """
        Parse docinfo.xml file to get titles of title Ascii docs. Since Python ElementTree
        XML API did not work well, a simple regex is used and it seems good enough for our
        purpose.

        :return: None (self.adoc_dict is updated).
        """
        count = 0
        title_pattern = re.compile(r"^\s*<title>(.+)</title>\s*$")
        docinfo_files = list(
            filter(
                lambda x: "/archive/" not in str(x),
                Path(self.base_dir).joinpath(self.project_document_path).rglob("docinfo.xml"),
            )
        )
        for docinfo in docinfo_files:
            for line in open(docinfo, encoding="utf8"):
                m = title_pattern.match(line)
                if m:
                    title = m.group(1).strip()
                    if title in self.title_dict:
                        dir_name = str(docinfo.parents[0])
                        i = dir_name.index(f"{self.project_document_path}/")
                        master_adoc = f"{dir_name[i:]}/master.adoc"
                        if master_adoc not in self.adocs_dict:
                            print(f"NOT FOUND: {master_adoc}")
                        else:
                            url = self.attributes_dict["URL" + self.title_dict[title]]
                            self.adocs_dict[master_adoc]["url"] = url
                    else:
                        print(f"{title} IS NOT FOUND")
                    count += 1

    def parse_adoc(self, adoc_path):
        """
        Parse an Ascii document.
        :param adoc_path: A path to an Ascii document.
        :return: id, context, content_type, nesting_assembly
        """
        _id = None
        id_pattern = re.compile(r'\[id=["\']([^"\']+)["\']\]')
        context = None
        context_pattern = re.compile(r":context:\s*(.+)")
        #
        # Detect content type
        # https://github.com/redhat-documentation/vale-at-red-hat/issues/679
        #
        content_type = None
        content_type_pattern = re.compile(r":_mod-docs-content-type:\s*(.+)")
        #
        # Detect a pattern used for enabling nesting assemblies
        # https://redhat-documentation.github.io/modular-docs/#nesting-assemblies
        #
        nesting_assembly = False
        nesting_assembly_pattern = re.compile(r"ifdef::parent.+\[:context: {parent-context}\]")
        for line in open(adoc_path, encoding="utf8"):
            line = line.strip()
            m = id_pattern.match(line)
            if m:
                _id = m.group(1)
            m = context_pattern.match(line)
            if m:
                context = m.group(1)
            m = content_type_pattern.match(line)
            if m:
                content_type = m.group(1)
            m = nesting_assembly_pattern.match(line)
            if m:
                nesting_assembly = True

        return _id, context, content_type, nesting_assembly

    def get_dict(self):
        """
        Initialize a dict to store the information on Ascii docs.

        :return: A dict
        """
        d = {}
        for adoc in self.get_adocs():
            path_name = str(adoc)
            i = path_name.find(f"{self.project_document_path}/")
            project_file_name = path_name[i:]
            _id, context, content_type, nesting_assembly = self.parse_adoc(path_name)
            d[project_file_name] = {
                "project_file_name": project_file_name,
                "path_name": path_name,
                "includes": [],
                "url": None,
                "id": _id,
                "context": context,
                "content_type": content_type,
                "nesting_assembly": nesting_assembly,
            }
        return d

    def find_include_file(self, source, include_file):
        """
        Locate files included. aap-docs repository have symbolic links for organizing
        include files. This code uses Python File I/O function to resolve target
        directories pointed by symbolic links.

        :param source:
        :param include_file:
        :return: target file
        """
        base_path = Path(self.base_dir)
        parent_path = base_path.joinpath(Path(source).parents[0])
        include_file_path = parent_path.joinpath(include_file)
        include_file_path = os.path.realpath(include_file_path)
        i = include_file_path.find(f"{self.project_document_path}/")
        file_name = include_file_path[i:]
        if file_name not in self.adocs_dict:
            print(f"NOT FOUND: {include_file} (source: {source})")
            file_name = None
        return file_name

    def parse_include(self):
        """
        Parse include lines in Ascii files.

        :return: None (self.adocs_dict is updated).
        """
        include_pattern = re.compile(r"^\s*include::([\w\./\-_]+).*$")
        for k, v in self.adocs_dict.items():
            for line in open(v["path_name"], encoding="utf8"):
                m = include_pattern.match(line)
                if m:
                    include_file = m.group(1)
                    include_file = self.substitute_attributes(include_file)
                    file_name = self.find_include_file(k, include_file)
                    if file_name:
                        v["includes"].append(file_name)

    def substitute_attributes(self, line):
        """
        Substitude attributes in a line to the defined values.

        :param line: string to be parsed
        :return: Modified string
        """
        pattern = re.compile(r"{(\w+)}")
        attributes = pattern.findall(line)
        for attribute in attributes:
            if attribute in self.attributes_dict:
                line = line.replace(f"{{{attribute}}}", f"{self.attributes_dict[attribute]}")
            else:
                print(f"Attribute {attribute} is not found.")
        return line

    def parse_attributes(self):
        """
        Parse attributes.adoc

        :return: None (self.attributes_dict and self.title_dict are updated).
        """
        pattern = re.compile(r":(\w+):\s*(.+)$")
        menu_pattern = re.compile(r"^menu:([\w ]+)\[([\w >]+)\]$")
        attributes_adoc = (
            Path(self.base_dir)
            .joinpath(self.project_document_path)
            .joinpath("attributes")
            .joinpath("attributes.adoc")
        )

        def parse_line(line):
            line = line.strip()
            if len(line) == 0 or line.startswith("//"):
                return
            m = pattern.match(line)
            if m:
                key = m.group(1)
                value = self.substitute_attributes(m.group(2))
                m = menu_pattern.match(value)
                if m:
                    value = f"{m.group(1)} > {m.group(2)}"
                self.attributes_dict[key] = value
                if key.startswith("Title"):
                    self.title_dict[value] = key[len("Title") :]

        for line in open(attributes_adoc, encoding="utf8"):
            parse_line(line)

        # If the git_branch is "lightspeed-latest", parse additional lines
        # so that the tool can pickup the output URL. The information is not
        # included in the attributes.adoc in the lightspeed-latest branch.

        ADDITIONAL_LINES = """// Lightspeed branch titles/lightspeed-user-guide
:TitleLightspeedUserGuide: Red Hat Ansible Lightspeed with IBM watsonx Code Assistant User Guide
:URLLightspeedUserGuide: {BaseURL}/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide
:LinkLightspeedUserGuide: {URLLightspeedUserGuide}[{TitleLightspeedUserGuide}]"""  # noqa: E501
        if self.git_branch == "lightspeed-latest":
            for line in ADDITIONAL_LINES.split("\n"):
                parse_line(line)


def main():
    """
    Main routine
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--aap_docs_dir", "-i")
    parser.add_argument("--output_dir", "-o")
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--git-branch", "-b")

    args = parser.parse_args()

    project_document_path = "lightspeed" if args.git_branch == "lightspeed-latest" \
        else "aap-clouds" if args.git_branch == "aap-clouds-latest" else "downstream"

    # Parse Asciidoc files in a local aap_docs repo and calculate document URLs
    base_dir = args.aap_docs_dir
    files_to_skip = [
        "downstream/titles/aap-hardening/master.adoc",
        # "downstream/titles/upgrade/master.adoc",
        "downstream/titles/playbooks/playbooks-reference/master.adoc",
    ]
    parse_aap_docs = ParseAAPDocs(
        base_dir, project_document_path, files_to_skip, args.git_branch, do_validate=args.validate
    )
    parse_aap_docs.run()

    # Save parsed results as metadata.json
    with open(Path(args.output_dir).joinpath("metadata.json"), "w", encoding="utf8") as f:
        json.dump(parse_aap_docs.adocs_dict, f, indent=2)


if __name__ == "__main__":
    main()
