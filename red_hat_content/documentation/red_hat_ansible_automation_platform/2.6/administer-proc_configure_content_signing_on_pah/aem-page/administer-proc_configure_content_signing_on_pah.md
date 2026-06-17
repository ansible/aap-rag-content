+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_configure_content_signing_on_pah"
title = "Configure content signing on private automation hub - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-manage_your_organization_s_automation_content/", "Manage your organization's automation content"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_configure_content_signing_on_pah/aem-page/administer-proc_configure_content_signing_on_pah.html"
last_crumb = "Configure content signing on private automation hub"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure content signing on private automation hub"
oversized = "false"
page_slug = "administer-proc_configure_content_signing_on_pah"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-proc_configure_content_signing_on_pah"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-proc_configure_content_signing_on_pah/toc/toc.json"
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

## Download signature public keys

After you sign and approve collections, download the signature public keys from the Ansible Automation Platform UI.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Signature Keys. The Signature Keys dashboard displays a list of multiple keys: collections and container images.   - To verify collections, download the key prefixed with `collections-`.
  - To verify container images, download the key prefixed with `container-`.

3.  Choose one of the following methods to download your public key:

  - Click the Download Key icon to download the public key.
  - Click the Copy to clipboard next to the public key you want to copy.

### Results

Use the public key that you copied to verify the content collection that you are installing.

## Configure Ansible-Galaxy CLI to verify collections

You can configure Ansible-Galaxy CLI to verify collections. This ensures that downloaded collections are approved by your organization and have not been changed after they were uploaded to automation hub.

### Before you begin

- Public key for verification has been added to the local system keyring.
- Signed collections are available in automation hub to verify signature.
- Certified collections can be signed by approved roles within your organization.

### About this task

If a collection has been signed by automation hub, the server provides ASCII armored, GPG-detached signatures to verify the authenticity of `MANIFEST.json` before using it to verify the collection’s contents. First you must opt into signature verification by configuring a keyring for `ansible-galaxy` or providing the path with the `--keyring` option.

### Procedure

1.  To import a public key into a non-default keyring for use with `ansible-galaxy`, run the following command.

```
gpg --import --no-default-keyring --keyring ~/.ansible/pubring.kbx my-public-key.asc
```
  Note:
      In addition to any signatures provided by automation hub, signature sources can also be provided in the requirements file and on the command line. Signature sources should be URIs.

2.  To verify the collection name provided on the CLI with an additional signature, run the following command:
  

```
ansible-galaxy collection install namespace.collection
--signature https://examplehost.com/detached_signature.asc
--signature file:///path/to/local/detached_signature.asc --keyring ~/.ansible/pubring.kbx
```
    You can use this option multiple times to provide multiple signatures.

3.  Confirm that the collections in a requirements file list any additional signature sources following the collection’s signatures key, as in the following example.

```yaml
# requirements.yml
collections:
  - name: ns.coll
    version: 1.0.0
    signatures:
      - https://examplehost.com/detached_signature.asc
      - file:///path/to/local/detached_signature.asc

    ansible-galaxy collection verify -r requirements.yml --keyring ~/.ansible/pubring.kbx
```
    When you install a collection from automation hub, the signatures provided by the server are saved along with the installed collections to verify the collection’s authenticity.

4.  (Optional) If you need to verify the internal consistency of your collection again without querying the Ansible Galaxy server, run the same command you used previously using the `--offline` option.
