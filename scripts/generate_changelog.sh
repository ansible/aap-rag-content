#!/bin/bash

if [ "$#" -ne 4 ]
then
  echo "Usage: generate_changelog.sh <name> <gh_api_base_url> <gh_base_url> <changelogs_file>"
  exit 1
fi

REPO_NAME=$1
REPO_API_BASE_URL=$2
REPO_BASE_URL=$3
CHANGELOGS_FILE=$4

METADATA_DIR=`echo ${CHANGELOGS_FILE}|sed 's/\(.*\)\/\(.*\)txt/\1\/.metadata/'`
METADATA_FILE=`echo ${CHANGELOGS_FILE}|sed 's/\(.*\)\/\(.*\)txt/\1\/.metadata\/\2json/'`

echo ${METADATA_DIR}
echo ${METADATA_FILE}

set -eou pipefail

REPO_URL_CONTENT=$(curl --silent ${REPO_API_BASE_URL})
REPO_TAG_NAME="$(echo ${REPO_URL_CONTENT} | jq -r '.tag_name')"
REPO_PUBLISHED="$(echo ${REPO_URL_CONTENT}| jq -r '.published_at')"
REPO_PUBLISHED_DATE="$(date -d "${REPO_PUBLISHED}"  '+%A, %B %d, %Y')"
#REPO_BODY="$(curl --silent ${REPO_API_BASE_URL} | jq -r '.body')"
echo -e "# ${REPO_NAME} Versions\n\nHere is the most recent update for ${REPO_NAME}:\n" > ${CHANGELOGS_FILE}
echo "- ${REPO_NAME} Version ${REPO_TAG_NAME} Released on ${REPO_PUBLISHED_DATE}">> ${CHANGELOGS_FILE}

if [ ! -d "${METADATA_DIR}" ]; then
  mkdir -p ${METADATA_DIR}
fi
echo "{ \"url\":\"${REPO_BASE_URL}\" }"> ${METADATA_FILE}
