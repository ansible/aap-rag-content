+++
template = "docs/aem-title.html"
title = "Examples for the hashicorp.vault.database_connection module - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/examples_for_the_hashicorp_vault_database_connection_module"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/examples_for_the_hashicorp_vault_database_connection_module/aem-page/examples_for_the_hashicorp_vault_database_connection_module.html"
last_crumb = "Examples for the hashicorp.vault.database_connection module"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Examples for the hashicorp.vault.database_connection module"
oversized = "false"
page_slug = "examples_for_the_hashicorp_vault_database_connection_module"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/examples_for_the_hashicorp_vault_database_connection_module"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/examples_for_the_hashicorp_vault_database_connection_module/toc/toc.json"
type = "aem-page"
+++

# Examples for the hashicorp.vault.database_connection module

The following examples show basic configurations for the `hashicorp.vault.database_connection` module.

 **Example 1: Create a database connection with a PostgreSql plugin**

Before (`community.hashi_vault`):

```
- name: Example 1 - Create a database connection (PostgreSQL plugin, default database mount)
  community.hashi_vault.vault_database_connection_configure:
    url: https://vault.example.com:8200
    namespace: "{{ vault_namespace | default(omit) }}"
    auth_method: userpass
    username: "{{ vault_auth_username }}"
    password: "{{ vault_auth_password }}"
    connection_name: postgres-main
    plugin_name: postgresql-database-plugin
    connection_url:
postgresql://{{'{{username}}'}}:{{'{{password}}'}}@postgres.example.com:5432/appdb?sslmode=disable
    connection_username: "{{ db_static_user }}"
    connection_password: "{{ db_static_password }}"
    allowed_roles:
      - app-readonly
      - app-readwrite
  register: db_connection_result

```
After (`hashicorp.vault`):

```
- name: Create database connection with PostgreSQL plugin
  hashicorp.vault.database_connection:
    name: postgres-sample-connection
    plugin_name: "postgresql-database-plugin"
    allowed_roles:
      - "readonly"
    connection_url: "host=localhost port=5432 user='{{ username }}' password='{{ password }}'"
    plugin_options:
      max_open_connections: 5
      max_connection_lifetime: "5s"
    username: "admin_user"
    password: "secure_password"

```
 **Example 2: Update a database connection with MySQL**

Before (`community.hashi_vault`):

```
- name: Example 2 - Update an existing database connection (MySQL plugin)
  community.hashi_vault.vault_database_connection_configure:
    url: https://vault.example.com:8200
    namespace: "{{ vault_namespace | default(omit) }}"
    auth_method: token
    token: "{{ vault_token }}"
    connection_name: mysql-main
    plugin_name: mysql-database-plugin
    connection_url: "{{'{{username}}'}}:{{'{{password}}'}}@tcp(mysql.example.com:3306)/"
    connection_username: "{{ db_static_user }}"
    connection_password: "{{ db_static_password }}"
    allowed_roles:
      - readonly
      - readwrite
  register: mysql_connection_result

```
After (`hashicorp.vault`):

```
- name: Update a database connection with MySQL
  hashicorp.vault.database_connection:
    name: mysql-sample-connection
    state: present
    connection_url: "mysql://vaultuser:secretpassword@localhost:3306/mydb"
    verify_connection: true
    plugin_name: "mysql-database-plugin"
    database_mount_path: "database-conn-config-integration-tests"
    allowed_roles:
      - "readonly"
      - "readwrite"
    username: "vaultuser"
    password: "secretpassword"

```
 **Example 3: Reset a database connection**

Before (`community.hashi_vault`):

```
- name: Reset a Database Connection with the default mount point
 community.hashi_vault.vault_database_connection_reset:
   url: https://vault:8201
   auth_method: userpass
   username: '{{ user }}'
   password: '{{ passwd }}'
   connection_name: mysql-sample-connection
 register: result
```
After (`hashicorp.vault`):

```
- name: Reset a database connection
  hashicorp.vault.database_connection:
    name: mysql-sample-connection
    state: reset

```
 **Example 4: Delete a database connection**

Before (`community.hashi_vault`):

```
- name: Delete a Database Connection with the default mount point
 community.hashi_vault.vault_database_connection_delete:
   url: https://vault:8201
   auth_method: userpass
   username: '{{ user }}'
   password: '{{ passwd }}'
   connection_name: SomeName
 register: result

- name: Display the result of the operation
 ansible.builtin.debug:
   msg: "{{ result }}"
```
After (`hashicorp.vault`):

```
- name: Delete a database connection
  hashicorp.vault.database_connection:
    name: mysql-sample-connection
    state: absent

```
