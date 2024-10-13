#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "Usage: get_aap_plaintext_docs.sh aap_version"
  exit 1
fi

AAP_VERSION=$1
BASE_DIR=aap-product-docs-plaintext

set -eou pipefail

trap "rm -rf aap-docs" EXIT

if [ ! -d ${BASE_DIR} ]; then
    mkdir ${BASE_DIR}
fi

rm -rf ${BASE_DIR}/${AAP_VERSION}

git clone --single-branch --branch ${AAP_VERSION} https://github.com/ansible/aap-docs.git

python scripts/asciidoctor-text/convert-it-all-aap.py -i aap-docs \
    -o ${BASE_DIR}/${AAP_VERSION} -a aap-docs/downstream/attributes/attributes.adoc

python scripts/parse-aap-docs/parse-aap-docs.py -i aap-docs -o ${BASE_DIR}/${AAP_VERSION}

python scripts/filter-text-files.py -i ${BASE_DIR}/${AAP_VERSION}

rm -rf ${BASE_DIR}/${AAP_VERSION}/archive