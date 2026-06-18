+++
title = "Configure the hashicorp.vault.database_connection_info module - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure_the_hashicorp_vault_database_connection_info_module"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure_the_hashicorp_vault_database_connection_info_module/aem-page/configure_the_hashicorp_vault_database_connection_info_module.html"
last_crumb = "Configure the hashicorp.vault.database_connection_info module"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure the hashicorp.vault.database_connection_info module"
oversized = "false"
page_slug = "configure_the_hashicorp_vault_database_connection_info_module"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure_the_hashicorp_vault_database_connection_info_module"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure_the_hashicorp_vault_database_connection_info_module/toc/toc.json"
type = "aem-page"
+++

# Configure the hashicorp.vault.database_connection_info module

The `hashicorp.vault.database_connection_info` module lists the available database connections or reads the configuration for a specified connection.

## About this task

The corresponding `community.hashi_vault` modules are:

- `vault_database_connection_read module`: Returns the configuration settings for a connection_name.
- `vault_database_connections_list module`: Returns a list of available connections.

## Procedure

1.  Replicate the `community.hashi_vault` modules to the following `hashicorp.vault.database_connection_info` parameters.

```
---
module: database_connection_info
short_description: List available connections or read configuration for a specific connection.
version_added: 1.2.0
author: my-name
description:
  - This module retrieves configuration details for a specific Vault database connection.
  - When a connection name is provided, it returns its full settings; if the name is omitted,
    the module returns a comprehensive list of all available database connections within the specified mount path.
options:
  name:
    description: The name of the database connection to read.
    required: false
    type: str
  database_mount_path:
    description: Database secret engine mount path.
    type: str
    default: database
    aliases: [vault_database_mount_path]
extends_documentation_fragment:
  - hashicorp.vault.vault_auth.modules

```

2.  To retrieve the configuration details for a specific database connection, specify a name for the name parameter. If name is omitted, a list of available database connections is returned.
3.  Configure the [Parameters](https://console.redhat.com/ansible/automation-hub/collections/published/hashicorp/vault/documentation/module/database_connection?version=) for your `hashicorp.vault.database_connection_info` module.
