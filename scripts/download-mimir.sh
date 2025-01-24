#!/bin/bash

if [[ -z "${MIMIR_ENC_SECRET}" ]]; then
  echo Environment variable MIMIR_ENC_SECRET is not defined.
  exit 1
fi

if [[ -z "${TARGET_DIRS}" ]]; then
  echo Environment variable TARGET_DIRS is not defined.
  exit 1
fi

OUT_DIR=/tmp/mimir_work
trap "rm -rf ${OUTDIR}" EXIT

mkdir -pv ${OUTDIR}

git clone git@gitlab.cee.redhat.com:jsprague/mimir-extracted-content-for-ai.git ${OUT_DIR}/mimir-extracted-content-for-ai
openssl enc -aes-256-cbc -d -pbkdf2 -pass pass:${MIMIR_ENC_SECRET} \
  -in ${OUT_DIR}/mimir-extracted-content-for-ai/mimir-extract-latest.tgz.enc \
  -out ${OUT_DIR}/mimir-extract-latest.tgz
tar xvzf ${OUT_DIR}/mimir-extract-latest.tgz ${TARGET_DIRS}
