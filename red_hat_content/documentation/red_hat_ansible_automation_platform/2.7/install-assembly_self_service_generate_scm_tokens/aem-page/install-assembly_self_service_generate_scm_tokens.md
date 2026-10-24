+++
template = "docs/aem-title.html"
title = "Generate Git personal access tokens - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_generate_scm_tokens"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_generate_scm_tokens/aem-page/install-assembly_self_service_generate_scm_tokens.html"
last_crumb = "Generate Git personal access tokens"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Generate Git personal access tokens"
oversized = "false"
page_slug = "install-assembly_self_service_generate_scm_tokens"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_generate_scm_tokens"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_generate_scm_tokens/toc/toc.json"
type = "aem-page"
+++

# Generate Git personal access tokens

If you are linking external Source Control Management (SCM) systems to Ansible automation portal, you must generate a Personal Access Token for authentication.

Ansible automation portal supports GitHub and GitLab SCM providers for discovering templates and collections.

Important:

Personal access tokens provide read access to Git repositories. If you plan to use the execution environment builder to save or push definitions to a GitHub repository, configure a GitHub OAuth App or GitHub App rather than a personal access token.

## Create a personal access token on GitHub

Create a GitHub personal access token (classic) to authenticate Ansible automation portal with your GitHub SCM.

### About this task

A GitHub personal access token provides read access for discovering templates and collections from GitHub repositories.

Important:

Personal access tokens cannot be used to push or save execution environment definitions to GitHub in newer portal versions. To enable pushing definitions, configure a GitHub OAuth App or GitHub App.

### Procedure

1. In a browser, log in to GitHub.
2. Click your profile picture and select Settings.
3. Select Developer settings.
4. Select Personal access tokens.
5. Click Generate new token> (and then)Generate new token (classic).
6. In the Select scopes section, enable the following:

  - `repo`
  - `read:org`
  - `workflow` (as needed)

7. Click Generate token.
8. Save the personal access token.

## Create a personal access token on GitLab

Create a GitLab personal access token to authenticate Ansible automation portal with your GitLab SCM.

### Procedure

1. In a browser, log in to GitLab and click your avatar.
2. Select Edit profile.
3. Select Access tokens.
4. Click Add new token.
5. Provide a name and expiration date for the token.
6. In the Scopes section, select the following:

  - `read_repository`
  - `api`

7. Click Create personal access token.
8. Save the personal access token.
