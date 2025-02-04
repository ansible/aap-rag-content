#!/bin/bash
MIMIR_DIR=./mimir
TARGET_DIRS=$(cat <<EOF
red_hat_content/documentation/ansible_on_clouds/2.x
 red_hat_content/documentation/red_hat_ansible_automation_platform/2.5
 red_hat_content/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest
EOF
)
echo $TARGET_DIRS

openssl enc -aes-256-cbc -d -pbkdf2 -pass pass:${MIMIR_ENC_SECRET} \
  -in ${MIMIR_DIR}/mimir-extracted-content-for-ai/mimir-extract-latest.tgz.enc \
  -out ${MIMIR_DIR}/mimir-extract-latest.tgz

tar xvzf ${MIMIR_DIR}/mimir-extract-latest.tgz ${TARGET_DIRS}
rm -f ${MIMIR_DIR}/mimir-extract-latest.tgz*