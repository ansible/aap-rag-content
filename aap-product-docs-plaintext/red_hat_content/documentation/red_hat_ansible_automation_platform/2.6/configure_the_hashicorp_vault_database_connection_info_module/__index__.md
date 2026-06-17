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
