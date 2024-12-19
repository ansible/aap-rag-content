#!/bin/bash

if [ "$#" -ne 3 ]
then
  echo "Usage: generate_changelog.sh <name> <gh_api_base_url> <changelogs_file>"
  exit 1
fi

REPO_NAME=$1
REPO_BASE_URL=$2
CHANGELOGS_FILE=$3

set -eou pipefail

REPO_URL_CONTENT=$(curl --silent ${REPO_BASE_URL})
REPO_TAG_NAME="$(echo ${REPO_URL_CONTENT} | jq -r '.tag_name')"
REPO_PUBLISHED="$(echo ${REPO_URL_CONTENT}| jq -r '.published_at')"
REPO_PUBLISHED_DATE="$(date -d "${REPO_PUBLISHED}"  '+%A, %B %d, %Y')"
#REPO_BODY="$(curl --silent ${REPO_BASE_URL} | jq -r '.body')"
echo "- ${REPO_NAME} Version ${REPO_TAG_NAME} Released on ${REPO_PUBLISHED_DATE}">> ${CHANGELOGS_FILE}
