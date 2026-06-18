# Example for the hashicorp.vault.database_connection_info module

The following example shows a basic configuration for the `hashicorp.database_connection_inf`o module.

Example: List available database connections

```
- name: Read database connection mysql
hashicorp.vault.database_connection_info:
name: mysql

```
