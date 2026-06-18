+++
title = "Example for the hashicorp.vault.database_connection_info module - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/example_for_the_hashicorp_database_connection_info_module"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/example_for_the_hashicorp_database_connection_info_module/aem-page/example_for_the_hashicorp_database_connection_info_module.html"
last_crumb = "Example for the hashicorp.vault.database_connection_info module"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Example for the hashicorp.vault.database_connection_info module"
oversized = "false"
page_slug = "example_for_the_hashicorp_database_connection_info_module"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/example_for_the_hashicorp_database_connection_info_module"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/example_for_the_hashicorp_database_connection_info_module/toc/toc.json"
type = "aem-page"
+++

# Example for the hashicorp.vault.database_connection_info module

The following example shows a basic configuration for the `hashicorp.database_connection_inf`o module.

Example: List available database connections

```
- name: Read database connection mysql
  hashicorp.vault.database_connection_info:
    name: mysql

```
