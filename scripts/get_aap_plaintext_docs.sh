#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "Usage: get_aap_plaintext_docs.sh aap_version"
  exit 1
fi

AAP_VERSION=$1
LIGHTSPEED_LATEST=lightspeed-latest
AAP_CLOUDS_LATEST=aap-clouds-latest
BASE_DIR=aap-product-docs-plaintext

set -eou pipefail

trap "rm -rf aap-docs" EXIT

if [ ! -d ${BASE_DIR} ]; then
    mkdir ${BASE_DIR}
fi

for git_branch in ${AAP_VERSION} ${LIGHTSPEED_LATEST} ${AAP_CLOUDS_LATEST}
do
  rm -rf ${BASE_DIR}/${git_branch}
  git clone --single-branch --branch ${git_branch} https://github.com/ansible/aap-docs.git

  if [ "${git_branch}" == "${AAP_CLOUDS_LATEST}" ]; then
    mv aap-docs aap-clouds
    mkdir aap-docs
    mv aap-clouds aap-docs
  fi

  python scripts/asciidoctor-text/convert-it-all-aap.py \
    -i aap-docs \
    -o ${BASE_DIR}/${git_branch}  \
    -b ${git_branch}

  python scripts/parse_aap_docs.py \
    -i aap-docs \
    -o ${BASE_DIR}/${git_branch} \
    -b ${git_branch}
  python scripts/filter_text_files.py \
    -i ${BASE_DIR}/${git_branch} \
    -b ${git_branch}
  rm -rf ${BASE_DIR}/${git_branch}/archive
  rm -rf aap-docs
done
