+++
template = "docs/aem-title.html"
title = "Configure the hashicorp.vault.database_connection module - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-configure_the_hashicorp_vault_database_connection_module"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_introduction/", "Integrate with IBM HashiCorp Vault"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-configure_the_hashicorp_vault_database_connection_module/aem-page/integrate-configure_the_hashicorp_vault_database_connection_module.html"
last_crumb = "Configure the hashicorp.vault.database_connection module"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure the hashicorp.vault.database_connection module"
oversized = "false"
page_slug = "integrate-configure_the_hashicorp_vault_database_connection_module"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/integrate-configure_the_hashicorp_vault_database_connection_module"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-configure_the_hashicorp_vault_database_connection_module/toc/toc.json"
type = "aem-page"
+++

# Configure the hashicorp.vault.database_connection module

The hashicorp.vault.database_connection module performs **Create**, **Update**, **Delete**, and **Reset** operations on database connections for plug-ins.

## About this task

The corresponding community.hashi_vault modules are:

- `vault_database_connection_configure module`: Creates and updates the database connection.
- `vault_database_connection_delete module`: Delete a database connection.
- `vault_database_connection_reset module`: Closes a connection_name and its underlying plugin and restarts it with the configuration stored.

## Procedure

1.  Map the parameters from your existing `community.hashi_vault` modules to the corresponding `hashicorp.vault.database_connection` parameters.
  

```
---
module: database_connection
short_description: Manage database secrets engine connections in HashiCorp Vault.
version_added: 1.2.0
author: my-name
description:
  - This module manages (create, update, delete, and reset) the lifecycle of database
    connection configurations within the HashiCorp Vault Database secrets engine.

    options:
 state:
   description:
     - Goal state for the database connection.
     - Use V(present) to create or update the connection.
     - Use V(reset) to trigger a connection reset.
     - Use V(absent) to remove the connection configuration.
   choices: [present, absent, reset]
   default: present
   type: str
 database_mount_path:
   description: Database secret engine mount path.
   type: str
   default: database
   aliases: [vault_database_mount_path]
 name:
   description: The name of the database connection configuration.
   required: true
   type: str
   aliases: [connection_name]
 username:
   description:
     - The username to connect to the database.
   required: false
   type: str
   aliases: [connection_username]
 password:
   description:
     - The password to connect to the database.
   required: false
   type: str
   aliases: [connection_password]
 disable_escaping:
   description: Determines whether special characters in the username and password fields will be escaped.
   type: bool
   default: false
 connection_url:
   description: The connection string used to connect to the database.
   type: str
 plugin_name:
   description:
     - The name of the plugin to use for this connection.
     - Required when O(state=present).
   required: false
   type: str
 plugin_version:
   description:
     - The semantic version of the plugin to use for this connection.
   type: str
   required: false
 plugin_options:
   description:
     - Additional parameters specific to the plugin.
     - This should be a dictionary of options required by the specific database plugin.
   type: dict
 verify_connection:
   description: Specifies if the connection is verified during initial configuration.
   default: true
   type: bool
 allowed_roles:
   description: A list of roles authorized to use this connection.
   type: list
   elements: str
 root_rotation_statements:
   description:
     - Specifies the database statements to be executed to rotate the root user's credentials.
     - Refer to the specific Vault database plugin documentation for supported formatting.
   type: list
   elements: str
 password_policy:
   description:
     - The name of the password policy to use when generating passwords for this database.
     - If not specified, Vault uses a default policy (20 characters, mixed case, number, dash).
   type: str
extends_documentation_fragment:
 - hashicorp.vault.vault_auth.modules
```

2.  Configure the following parameters:

  - **Name**: The name of the database connection configuration. Alias: connection_name
  - **plugin_name**: If 0 (state=present) you must include the name of the plugin to use for this connection.

3.  Configure the [Parameters](https://console.redhat.com/ansible/automation-hub/collections/published/hashicorp/vault/documentation/module/database_connection?version=) for your `hashicorp.vault.database_connection` module.
