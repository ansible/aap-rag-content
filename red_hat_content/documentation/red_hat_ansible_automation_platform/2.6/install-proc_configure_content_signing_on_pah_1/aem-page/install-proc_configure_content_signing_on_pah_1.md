+++
title = "Configure content signing on private automation hub - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_configure_content_signing_on_pah_1"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_platform_install_overview/", "Install RPM-based Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_configure_content_signing_on_pah_1/aem-page/install-proc_configure_content_signing_on_pah_1.html"
last_crumb = "Configure content signing on private automation hub"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure content signing on private automation hub"
oversized = "false"
page_slug = "install-proc_configure_content_signing_on_pah_1"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_configure_content_signing_on_pah_1"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_configure_content_signing_on_pah_1/toc/toc.json"
type = "aem-page"
+++

# Configure content signing on private automation hub

To successfully sign and publish Ansible Certified Content Collections, you must configure private automation hub for signing.

## Before you begin

- Your GnuPG key pairs have been securely set up and managed by your organization.
- Your public-private key pair has proper access for configuring content signing on private automation hub.

## About this task

## Procedure

1.  Create a signing script that accepts only a filename. Note:
      This script acts as the signing service and must generate an ascii-armored detached `gpg` signature for that file using the key specified through the `PULP_SIGNING_KEY_FINGERPRINT` environment variable.

    The script prints out a JSON structure with the following format.

```
{"file": "filename", "signature": "filename.asc"}
```
    All the file names are relative paths inside the current working directory. The file name must remain the same for the detached signature.

    **Example:** The following script produces signatures for content:

```shell
#!/usr/bin/env bash

    FILE_PATH=$1
SIGNATURE_PATH="$1.asc"

    ADMIN_ID="$PULP_SIGNING_KEY_FINGERPRINT"
PASSWORD="password"

    # Create a detached signature
gpg --quiet --batch --pinentry-mode loopback --yes --passphrase \
   $PASSWORD --homedir ~/.gnupg/ --detach-sign --default-key $ADMIN_ID \
   --armor --output $SIGNATURE_PATH $FILE_PATH

    # Check the exit status
STATUS=$?
if [ $STATUS -eq 0 ]; then
   echo {\"file\": \"$FILE_PATH\", \"signature\": \"$SIGNATURE_PATH\"}
else
   exit $STATUS
fi
```
    After you deploy a private automation hub with signing enabled to your Ansible Automation Platform cluster, new UI additions are displayed in collections.

2.  Review the Ansible Automation Platform installer inventory file for options that begin with `automationhub_*`.

```
[all:vars]
.
.
.
automationhub_create_default_collection_signing_service = True
automationhub_auto_sign_collections = True
automationhub_require_content_approval = True
automationhub_collection_signing_service_key = /abs/path/to/galaxy_signing_service.gpg
automationhub_collection_signing_service_script = /abs/path/to/collection_signing.sh
```
    The two new keys (**automationhub_auto_sign_collections** and **automationhub_require_content_approval**) indicate that the collections must be signed and approved after they are uploaded to private automation hub.
