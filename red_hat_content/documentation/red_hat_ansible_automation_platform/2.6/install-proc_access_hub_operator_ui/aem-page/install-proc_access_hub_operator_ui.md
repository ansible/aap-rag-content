+++
title = "Finding the automation hub route - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_access_hub_operator_ui"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_access_hub_operator_ui/aem-page/install-proc_access_hub_operator_ui.html"
last_crumb = "Finding the automation hub route"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Finding the automation hub route"
oversized = "false"
page_slug = "install-proc_access_hub_operator_ui"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_access_hub_operator_ui"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_access_hub_operator_ui/toc/toc.json"
type = "aem-page"
+++

# Finding the automation hub route

You can access the automation hub through the platform gateway or through the following procedure.

## About this task

## Procedure

1.  Log into Red Hat OpenShift Container Platform.
2.  Navigate to Networking> (and then)Routes.
3.  Under **Location**, click on the URL for your automation hub instance.

## Results

The automation hub user interface launches where you can sign in with the administrator credentials specified during the operator configuration process.

Note:

If you did not specify an administrator password during configuration, one was automatically created for you. To locate this password, go to your project, select Workloads> (and then)Secrets and open controller-admin-password. From there you can copy the password and paste it into the Automation hub password field.

## Add a collection download count to automation hub

A collection download count can help you understand collection usage. To add a collection download count to automation hub, set the following configuration:

```
spec:
  pulp_settings:
    ansible_collect_download_count: true
```
When `ansible_collect_download_count` is enabled, automation hub will display a download count by the collection.

## Add allowed container registries

Before you can deploy a container image in automation hub, you must add the registry to the `allowedRegistries` in the automation controller image configuration. To do this you can copy and paste the following code into your automation controller image YAML.

### About this task

### Procedure

1.  Log in to **Red Hat OpenShift Container Platform**.
2.  Navigate to Home> (and then)Search.
3.  Select the **Resources** drop-down list and type "Image".
4.  Select **Image (config,openshift.io/v1)**.
5.  Click Cluster under the **Name** heading.
6.  Select the YAML tab.
7.  Paste in the following under spec value:
  

```
spec:
  registrySources:
    allowedRegistries:
    - quay.io
    - registry.redhat.io
    - image-registry.openshift-image-registry.svc:5000
    - <OpenShift Container Platform route for your automation hub>
```

8.  Click Save.

## Configure content signing for automation hub

As an automation administrator for your organization, you can configure Ansible Automation Platform Hub Operator for signing and publishing Ansible content collections from different groups within your organization.

### Before you begin

- A GPG key pair. If you do not have one, you can generate one using the `gpg --full-generate-key` command.
- Your public-private key pair has proper access for configuring content signing on Ansible Automation Platform Hub Operator.

### About this task

For additional security, automation creators can configure Ansible-Galaxy CLI to verify these collections to ensure that they have not been changed after they were uploaded to automation hub.

To successfully sign and publish Ansible Certified Content Collections, you must configure private automation hub for signing.

### Procedure

1.  Create a ConfigMap for signing scripts. The ConfigMap you create contains the scripts used by the signing service for collections and container images. Note:
      This script is used as part of the signing service and must generate an ascii-armored detached `gpg` signature for that file using the key specified through the `PULP_SIGNING_KEY_FINGERPRINT` environment variable.

    The script prints out a JSON structure with the following format.

```
{"file": "filename", "signature": "filename.asc"}
```
    All the file names are relative paths inside the current working directory. The file name must remain the same for the detached signature.

    **Example:** The following script produces signatures for content:

```shell
apiVersion: v1
kind: ConfigMap
metadata:
  name: signing-scripts
data:
  collection_sign.sh: |-
      #!/usr/bin/env bash

    FILE_PATH=$1
      SIGNATURE_PATH=$1.asc

    ADMIN_ID="$PULP_SIGNING_KEY_FINGERPRINT"
      PASSWORD="password"

    # Create a detached signature
      gpg --quiet --batch --pinentry-mode loopback --yes --passphrase \
        $PASSWORD --homedir /var/lib/pulp/.gnupg --detach-sign --default-key $ADMIN_ID \
        --armor --output $SIGNATURE_PATH $FILE_PATH

    # Check the exit status
      STATUS=$?
      if [ $STATUS -eq 0 ]; then
        echo {\"file\": \"$FILE_PATH\", \"signature\": \"$SIGNATURE_PATH\"}
      else
        exit $STATUS
      fi
  container_sign.sh: |-
    #!/usr/bin/env bash

    # galaxy_container SigningService will pass the next 4 variables to the script.
    MANIFEST_PATH=$1
    FINGERPRINT="$PULP_SIGNING_KEY_FINGERPRINT"
    IMAGE_REFERENCE="$REFERENCE"
    SIGNATURE_PATH="$SIG_PATH"

    # Create container signature using skopeo
    skopeo standalone-sign \
      $MANIFEST_PATH \
      $IMAGE_REFERENCE \
      $FINGERPRINT \
      --output $SIGNATURE_PATH

    # Optionally pass the passphrase to the key if password protected.
    # --passphrase-file /path/to/key_password.txt

    # Check the exit status
    STATUS=$?
    if [ $STATUS -eq 0 ]; then
      echo {\"signature_path\": \"$SIGNATURE_PATH\"}
    else
      exit $STATUS
    fi
```

2.  Create a secret for your GnuPG private key. This secret securely stores the GnuPG private key you use for signing.

```shell
gpg --export --armor <your-gpg-key-id> > signing_service.gpg

    oc create secret generic signing-galaxy --from-file=signing_service.gpg
```
    The secret must have a key named `signing_service.gpg`.

3.  Configure the AnsibleAutomationPlatform CR.

```shell
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: aap-hub-signing-sample
spec:
  hub:
    signing_secret: "signing-galaxy"
    signing_scripts_configmap: "signing-scripts"
```

### What to do next

 [Using content signing services in private automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.6/proc_using_content_signing_services_in_pah "After you have configured content signing on your private automation hub, you can manually sign a new collection or replace an existing signature with a new one.")
