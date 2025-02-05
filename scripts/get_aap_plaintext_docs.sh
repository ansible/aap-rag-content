#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "Usage: get_aap_plaintext_docs.sh aap_version"
  exit 1
fi

AAP_VERSION=$1
LIGHTSPEED_LATEST=lightspeed-latest
AAP_CLOUDS_LATEST=aap-clouds-latest
AAP_DOCS_BASE_DIR=aap-product-docs-plaintext
CHANGELOGS_FILE=additional_docs/components_versions.txt

set -eou pipefail

trap "rm -rf aap-docs" EXIT

if [ ! -d ${AAP_DOCS_BASE_DIR} ]; then
    mkdir ${AAP_DOCS_BASE_DIR}
fi

# Changelog's
./scripts/generate_changelog.sh "Ansible Core (ansible-core)" \
  "https://api.github.com/repos/ansible/ansible/releases/latest" \
  "https://github.com/ansible/ansible" \
  "additional_docs/ansible-core.txt"

./scripts/generate_changelog.sh "Ansible Rulebook (ansible-rulebook)" \
  "https://api.github.com/repos/ansible/ansible-rulebook/releases/latest" \
  "https://github.com/ansible/ansible-rulebook" \
  "additional_docs/ansible-rulebook.txt"

for git_branch in ${AAP_VERSION}
do
  rm -rf ${AAP_DOCS_BASE_DIR}/${git_branch}
  git clone --single-branch --branch ${git_branch} https://github.com/ansible/aap-docs.git

  if [ "${git_branch}" == "${AAP_CLOUDS_LATEST}" ]; then
    # For some reasons, "AAP on Azure" has a different structure from others.
    # Following two lines are for correcting those differences.
    mv aap-docs/titles/aap-on-azure/aap-on-azure.asciidoc aap-docs/titles/aap-on-azure/master.adoc
    echo "<title>Red Hat Ansible Automation Platform on Microsoft Azure Guide</title>" > aap-docs/titles/aap-on-azure/docinfo.xml
    mv aap-docs aap-clouds
    mkdir aap-docs
    mv aap-clouds aap-docs
  fi

  python scripts/asciidoctor-text/convert-it-all-aap.py \
    -i aap-docs \
    -o ${AAP_DOCS_BASE_DIR}/${git_branch}  \
    -b ${git_branch}

  python scripts/parse_aap_docs.py \
    -i aap-docs \
    -o ${AAP_DOCS_BASE_DIR}/${git_branch} \
    -b ${git_branch}
  python scripts/filter_text_files.py \
    -i ${AAP_DOCS_BASE_DIR}/${git_branch} \
    -b ${git_branch}
  rm -rf ${AAP_DOCS_BASE_DIR}/${git_branch}/archive
  rm -rf aap-docs
done

python scripts/split_metadata.py \
  -f ${AAP_DOCS_BASE_DIR} \
  -v ${AAP_VERSION}
