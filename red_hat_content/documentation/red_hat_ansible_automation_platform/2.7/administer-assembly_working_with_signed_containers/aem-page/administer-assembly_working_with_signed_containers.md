+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_signed_containers"
title = "Secure your automation with container signing - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments/", "Define, create, and build execution environments"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_signed_containers/aem-page/administer-assembly_working_with_signed_containers.html"
last_crumb = "Secure your automation with container signing"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Secure your automation with container signing"
oversized = "false"
page_slug = "administer-assembly_working_with_signed_containers"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_signed_containers"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_signed_containers/toc/toc.json"
type = "aem-page"
+++

# Secure your automation with container signing

Add an extra layer of security to your content by enabling container signing in private automation hub.

## Deploy your system for container signing

For added security, set up your system for container signing.

### Before you begin

Automation content collection and container signing must be enabled.

### About this task

Note that installer looks for the script and key on the same server where installer is located.

### Procedure

1.  From a terminal, create a signing script, and pass the script path as an installer parameter. **Example**:

```
#!/usr/bin/env bash

    # pulp_container SigningService will pass the next 4 variables to the script.
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

2.  Review the Ansible Automation Platform installer inventory file for options for container signing that begin with `automationhub_*`.

```
[all:vars]
.
.
.

    automationhub_create_default_container_signing_service = True
automationhub_container_signing_service_key = /absolute/path/to/key/to/sign
automationhub_container_signing_service_script = /absolute/path/to/script/that/signs
```

3.  Once installation is complete, log in to Ansible Automation Platform and navigate to Automation Content> (and then)Signature Keys. Note:
      The `container-default` service is created by the Ansible Automation Platform installer.

### Results

Ensure that you have a key titled **container-default**, or **container**-*anyname*.

## Add and sign an execution environment

Push a signed execution environment to your private automation hub for added security.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Click Create execution environment and enter the relevant information in the fields that appear.   1.  The **Name** field displays the name of the execution environment on your local registry.
  2.  The **Upstream name** field is the name of the image on the remote server.
  3.  Under **Registry**, select the name of the registry from the drop-down menu.
  4.  Optional: Enter tags in the **Add tag(s) to include** field. If the field is blank, all the tags are passed. You must specify which repository-specific tags to pass.
  5.  Optional: Enter tags to exclude in the **Add tag(s) to exclude** field.
3.  Click Create execution environment. You should see your new execution environment in the list that appears.
4.  Sync and sign your new automation execution environment.   1.  Click the More Actions icon **⋮** and select **Sync execution environment**.
  2.  Click the More Actions icon **⋮** and select **Sign execution environment**.
5.  Click on your new execution environment. On the Details page, find the **Signed** label to determine that your execution environment has been signed.

## Push a signed execution environment from your local system

Sign an automation execution environment on a local system and push the signed execution environment to the automation hub registry.

### Procedure

1.  From a terminal, log in to Podman, or any container client currently in use, and pull the execution environment you want to sign.

```
podman pull <container-name>
```

2.  After the execution environment is pulled, add tags (for example: `latest`, `rc`, `beta`, or version numbers, such as `1.0`, `2.3`, and so on):
  

```
podman tag <container-name> <server-address>/<container-name>:<tag name>
```

3.  Sign the execution environment after changes have been made, and push it back up to the automation hub registry:
  

```
podman push <server-address>/<container-name>:<tag name> --tls-verify=false --sign-by <reference to the gpg key on your local>
```
    If the execution environment is not signed, it can only be pushed with any current signature embedded. Alternatively, you can use the following script to push the execution environment without signing it:

```
podman push <server-address>/<container-name>:<tag name> --tls-verify=false
```

4.  After the execution environment has been pushed, navigate to Automation Content> (and then)Execution Environments.
5.  To display the new execution environment, click the **Refresh** icon.
6.  Click the name of the image to view your pushed image.

### Results

After the execution environment is signed, the status changes to "signed".

The details page for each execution environment indicates whether it has been signed. If the details page indicates that an image is **Unsigned**, you can sign the execution environment from automation hub using the following steps:

1. Click the execution environment name to navigate to the details page.
2. Click the More Actions icon **⋮**. Three options are available:
  - **Sign execution environment**
  - **Use in Controller**
  - **Delete execution environment**
3. Click **Sign execution environment** from the drop-down menu.

## Confirm signatures are on your local environment

Podman and other image clients can use policies to ensure the validity of an image. To enable this capability, assign a policy to the signature.

### About this task

To ensure an execution environment is signed by specific signatures, the signatures must first be on your local environment.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Signature Keys.
2.  Click the Download key icon next to the signature that you are using. A new window should open to indicate you have downloaded the key.

## Configure a client to verify signatures

To ensure an execution environment pulled from the remote registry is properly signed, first configure the execution environment with the proper public key in a policy file.

### Before you begin

- The client must have sudo privileges configured to verify signatures.

### Procedure

1.  Open your terminal and use the following command:
  

```
sudo <name of editor> /etc/containers/policy.json
```
    The file that is displayed is similar to this:

```
{
  "default": [{"type": "reject"}],
  "transports": {
      "docker": {
        "quay.io": [{"type": "insecureAcceptAnything"}],
        "docker.io": [{"type": "insecureAcceptAnything"}],
        "<server-address>": [
          {
                  "type": "signedBy",
                  "keyType": "GPGKeys",
                  "keyPath": "/tmp/containersig.txt"
          }]
      }
  }
}
```
    This file shows that neither `quay.io`, or `docker.io` will perform the verification, because the type is `insecureAcceptAnything` which overrides the default type of `reject`. However, `<server-address>` will perform the verification, because the parameter `type` is set to `"signedBy"`.

  Note:
      The only `keyType` currently supported is GPG keys.

2.  Under the `<server-address>` entry, modify the `keyPath` <1> to include the name of your key file.

```
{
        "default": [{"type": "reject"}],
        "transports": {
            "docker": {
                "quay.io": [{"type": "insecureAcceptAnything"}],
                "docker.io": [{"type": "insecureAcceptAnything"}],
                "<server-address>": [{
                    "type": "signedBy",
                    "keyType": "GPGKeys",
                    "keyPath": "/tmp/<key file name>",
                    "signedIdentity": {
                        "type": "matchExact"
                    }
                  }]
            }
        }
}
```

3.  Save and close the file.

### Results

- Pull the file using Podman, or your client of choice:

```
podman pull <server-address>/<container-name>:<tag name> --tls-verify=false
```
This response verifies the execution environment has been signed with no errors. If the execution environment is not signed, the command fails.
