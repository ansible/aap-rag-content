+++
title = "Configure a Personal Access Token for GitHub content discovery - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_pat_ee_builder"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder/", "Configure a GitHub App for content discovery"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_pat_ee_builder/aem-page/develop-proc_configure_pat_ee_builder.html"
last_crumb = "Configure a Personal Access Token for GitHub content discovery"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure a Personal Access Token for GitHub content discovery"
oversized = "false"
page_slug = "develop-proc_configure_pat_ee_builder"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_configure_pat_ee_builder"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_pat_ee_builder/toc/toc.json"
type = "aem-page"
+++

# Configure a Personal Access Token for GitHub content discovery

Create and store a GitHub Personal Access Token (PAT) so that execution environment builder can scan repositories for Ansible collections.

## Before you begin

- You have a GitHub account with access to the repositories automation portal needs to scan.

## About this task

PATs provide a simpler setup with user-scoped access. If you are already using PATs for automation portal, you can continue using them. Choose this option or a GitHub App for content discovery. GitHub App and PAT are mutually exclusive.

## Procedure

1.  Create a GitHub PAT with the following scopes:

  - `repo`
  - `read:org`
  - `workflow` (required for the CI activity tab to display workflow run status)

2.  Store the PAT.
      **OpenShift — CLI:**

```
$ oc create secret generic secrets-scm \
  --from-literal=github-token=<your_github_pat> \
  -n <namespace>
```
    **OpenShift — web console:**

  1. Navigate to **Workloads > Secrets > Create > Key/value secret**.
  2. Set the name to `secrets-scm`.
  3. Add key `github-token` with your PAT value.
    **RHEL appliance:**

```
$ echo -n '<your_github_pat>' | sudo podman secret create portal_github_token -
```
  Note:
      If you configured a GitHub personal access token during RHEL appliance installation (via cloud-init), the `portal_github_token` secret already exists and is active for content discovery. Running the command above updates the existing secret with a new value.

## Results

Note:

If you already have PAT-based GitHub integration configured from a previous AAP release, those instructions remain valid. This guide documents both authentication methods.
