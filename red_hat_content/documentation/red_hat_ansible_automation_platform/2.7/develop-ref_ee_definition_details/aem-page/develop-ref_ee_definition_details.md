+++
template = "docs/aem-title.html"
title = "Execution environment definition detail page - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_definition_details"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_ee_catalog_overview/", "Discover and manage execution environments and collections"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_ee_definition_details/aem-page/develop-ref_ee_definition_details.html"
last_crumb = "Execution environment definition detail page"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Execution environment definition detail page"
oversized = "false"
page_slug = "develop-ref_ee_definition_details"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_ee_definition_details"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_ee_definition_details/toc/toc.json"
type = "aem-page"
+++

# Execution environment definition detail page

The execution environment definition detail page displays metadata, defined content, and available actions for a registered definition in the catalog.

## Detail page sections

Open an execution environment definition from the catalog to view its detail page. The detail page includes the following sections:

| Section             | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| **About**           | Metadata, owner, tags, and lifecycle status.                                |
| **Defined Content** | Parsed YAML showing the base image, collections, packages, and build steps. |
| **Readme**          | Documentation for the execution environment definition.                     |
| **Resources**       | Links to related documentation.                                             |

## Available actions

The following actions are available from the detail page:

| Action                | Description                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------- |
| **Build**             | Trigger a new container image build from the definition.                                           |
| **Edit definition**   | Open the source in your Git provider.                                                              |
| **View in source**    | Navigate to the source repository.                                                                 |
| **Download EE files** | Download the definition as a `.tar` archive (available for definitions not saved to a repository). |
| **Delete**            | Unregister the definition from the catalog.                                                        |
