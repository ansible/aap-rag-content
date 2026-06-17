+++
template = "docs/aem-title.html"
title = "Build a bootc operating system image for Red Hat Edge Manager - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_build_bootc"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_build_bootc/aem-page/whats_new-con_edge_manager_build_bootc.html"
last_crumb = "Build a bootc operating system image for Red Hat Edge Manager"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Build a bootc operating system image for Red Hat Edge Manager"
oversized = "false"
page_slug = "whats_new-con_edge_manager_build_bootc"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_build_bootc"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_build_bootc/toc/toc.json"
type = "aem-page"
+++

# Build a *bootc* operating system image for Red Hat Edge Manager

With `bootc`, your operating system becomes a container image that lets your device be managed by the Red Hat Edge Manager.

To prepare your device to be managed by the Red Hat Edge Manager, build a `bootc` operating system image that has the Red Hat Edge Manager agent. Then build an operating system disk image for your devices.

## Prerequisites

See the following prerequisites for building a `bootc` operating system image:

- Install `podman` version 5.0 or later and `skopeo` version 1.14 or later.
- Install `bootc-image-builder`.

## Install the Red Hat Edge Manager CLI

To install the Red Hat Edge Manager CLI, complete the following steps:

### About this task

### Procedure

1.  Enable the subscription manager for the repository appropriate for your system by running the following command:
  

```bash
sudo subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms
```

2.  Install the `flightctl` CLI with your package manager by running the following command:
  

```bash
sudo dnf install flightctl
```
    If you [set up the OAuth application manually](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_set_up_oauth#edge-manager-oauth-manually "Manually set up an OAuth application within your Ansible Automation Platform instance. This is important for enabling token-based authentication and integrating external applications such as the Red Hat Edge Manager."), you also need to make sure that one utility `xdg-open`, `x-www-browser`, or `www-browser` is available, for example, by installing `xdg-utils`.

## Log in to the Red Hat Edge Manager through the CLI

How you log in the Red Hat Edge Manager depends on whether you choose the [automatic](/documentation/en-us/red_hat_ansible_automation_platform/2.6/proc-edge-manager-oauth-auto.html) or [manual](/documentation/en-us/red_hat_ansible_automation_platform/2.6/proc-edge-manager-oauth-manually.html) method when you initially set up the application.

### About this task

### Procedure

-  If you use the automatic setup you can create a personal access token, even only with Read scope (under the profile icon in the top right corner of your Ansible Automation Platform UI > **User details** > **Tokens** tab) and then use this token to log in directly through the CLI, with the following example syntax:
  

```bash
flightctl login https://<your-edge-manager-ip-or-domain>:3443 --token=<your-aap-oauth-token> --insecure-skip-tls-verify
```

-  If you use the manual setup, use the **Client ID** to log in through a web-based process, with the following example syntax:
  

```bash
flightctl login https://<your-edge-manager-ip-or-domain>:3443 --web --client-id=<your-aap-client-id> --insecure-skip-tls-verify
```
  * This opens in a web browser and asks you to approve. The `--insecure-skip-tls-verify` parameter is used only if you have not generated your own valid certificates.

### What to do next

Use the following commands to help you with the CLI:

- To output a list of available commands, use:

```bash
flightctl
```

- To output both the flightctl CLI version and the back-end Red Hat Edge Manager version, use:

```bash
flightctl version
```

Important:

To ensure supportability and proper functionality, the version of the flightctl CLI must match the version of the Red Hat Edge Manager in use. Mismatched versions are not supported.

## Optional: Request an enrollment certificate for early binding

If you want to include an agent configuration in the image, complete the following steps:

### About this task

### Procedure

1.  Log in to the flightctl CLI by following the steps in [Logging into the Red Hat Edge Manager through the CLI](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_build_bootc#edge-manager-log-into-CLI "How you log in the Red Hat Edge Manager depends on whether you choose the automatic or manual method when you initially set up the application."). Note:
      The CLI uses the certificate authority pool of the host to verify the identity of the Red Hat Edge Manager service. The verification can lead to a TLS verification error when using self-signed certificates, if you do not add your certificate authority certificate to the pool. You can bypass the server verification by adding the `--insecure-skip-tls-verify` flag to your command.

2.  Get the enrollment credentials in the format of an agent configuration file by running the following command:
  

```bash
flightctl certificate request --signer=enrollment --expiration=365d --output=embedded > config.yaml
```
  Note:

  - The `--expiration=365d` option specifies that the credentials are valid for a year.
  - The `--output=embedded` option specifies that the output is an agent configuration file with the enrollment credentials embedded.
    The returned `config.yaml` contains the URLs of the Red Hat Edge Manager service, the certificate authority bundle, and the enrollment client certificate and key for the agent. See the following example:

```yaml
enrollment-service:
  authentication:
    client-certificate-data: LS0tLS1CRUdJTiBD...
    client-key-data: LS0tLS1CRUdJTiBF...
  service:
    certificate-authority-data: LS0tLS1CRUdJTiBD...
    server: https://agent-api.flightctl.127.0.0.1.nip.io:7443
  enrollment-ui-endpoint: https://ui.flightctl.127.0.0.1.nip.io:8081
```

## Optional: Use image pull secrets

If your device relies on containers from a private repository, you must configure a pull secret for the registry. Complete the following steps:

### About this task

### Procedure

1.  Depending on the kind of container image you use, place the pull secret in one or both of the following system paths on the device:

  - Operating system images use the `/etc/ostree/auth.json` path.
  - Application container images use the `/root/.config/containers/auth.json` path. Important:
            The pull secret must exist on the device before the secret can be consumed.

2.  Ensure that the pull secrets use the following format:
  

```json
{
  "auths": {
    "registry.example.com": {
      "auth": "base64-encoded-credentials"
    }
  }
}
```
