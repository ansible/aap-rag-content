+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_build_ee_from_catalog"
template = "docs/aem-title.html"
title = "Build an execution environment image from the catalog - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-build_execution_environments_with_the_automation_portal/", "Build execution environments with automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_build_ee_from_catalog/aem-page/develop-proc_build_ee_from_catalog.html"
last_crumb = "Build an execution environment image from the catalog"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Build an execution environment image from the catalog"
oversized = "false"
page_slug = "develop-proc_build_ee_from_catalog"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_build_ee_from_catalog"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_build_ee_from_catalog/toc/toc.json"
type = "aem-page"
+++

# Build an execution environment image from the catalog

Trigger a container image build on an existing execution environment definition from the catalog, independent of the creation workflow.

## Before you begin

- The execution environment definition was saved to a GitHub or GitLab repository.
- You can authenticate with your Git provider (GitHub or GitLab) through OAuth.
- Your AAP administrator has configured GitHub repository secrets or GitLab CI/CD variables for builds.

## Procedure

1.  From the execution environment catalog or definition detail page, click **Build**.
2.  In the build dialog, configure the following settings:

  - **Registry** -- private automation hub or a custom registry URL.

  - **Image Name** -- in `namespace/name` format.

  - **Image Tag**.

  - **Verify TLS certificates**. Clear this checkbox if the target registry's TLS certificates are not trusted by the CI runner executing the build.

3.  Click **Build**.
4.  Monitor the build from the **Actions** tab (GitHub) or the CI/CD Pipelines page (GitLab) on the repository where the definition was saved.
