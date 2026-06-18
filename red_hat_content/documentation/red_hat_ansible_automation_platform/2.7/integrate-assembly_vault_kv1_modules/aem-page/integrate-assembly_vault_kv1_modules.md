+++
template = "docs/aem-title.html"
title = "Configure KV1 modules - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_vault_kv1_modules"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_vault_introduction/", "Integrate with IBM HashiCorp Vault"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-assembly_vault_kv1_modules/aem-page/integrate-assembly_vault_kv1_modules.html"
last_crumb = "Configure KV1 modules"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure KV1 modules"
oversized = "false"
page_slug = "integrate-assembly_vault_kv1_modules"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-assembly_vault_kv1_modules"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-assembly_vault_kv1_modules/toc/toc.json"
type = "aem-page"
+++

# Configure KV1 modules

If you are using KV1 with `community.hashi_vault` collection, configure the corresponding modules in the `hashicorp.vault` collection.

## Configure the `hashicorp.vault.kv1_secret` module

Configuring this module is not required, but you can configure the defaults if needed after the migration.

### Procedure

 Configuring this module is not required for migration because there are no corresponding modules in `community.hashi_vault`. However, you might want to configure something other than the defaults for `auth_method` and `state` after the migration. You can use the examples on Ansible automation hub for reference.

## Configure the `hashicorp.vault.kv1_secret_info` module

The `hashicorp.vault.kv1_secret_info` module reads KV1 secrets.

### About this task

The corresponding community.hashi_vault modules are:

- **`community.hashi_vault.vault_kv1_get`:** Retrieves secrets from the HashiCorp Vault KV version 1 secret store.
- **`community.hashi_vault.vault_kv1_get lookup`:** Retrieves secrets from the HashiCorp Vault KV version 1 secret store.

### Procedure

1.  Replicate the `community.hashi_vault modules` to the following `hashicorp.vault.kv1_secret_secret_info` parameters.

```
  engine_mount_point:
    description: KV secrets engine mount point.
    default: secret
    type: str
    aliases: [secret_mount_path]
  path:
    description:
      - Specifies the path of the secret.
    required: true
    type: str
    aliases: [secret_path]
extends_documentation_fragment:
  - hashicorp.vault.vault_auth.modules
```

2.  (Required) Configure the `path` parameter. This is the path to the secret in the `community.hashi_vault.hashi_vault` modules. **Alias:**`secret_path`
3.  If needed, configure the optional parameters.

### What to do next

- [Configure the `hashicorp.vault.kv1_secret_get` lookup plugin](/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_vault_kv1_modules#vault-configuring-kv1-secret-get-lookup "The hashicorp.vault.kv1_secret_get lookup plugin module reads KV1 secrets.").

## Configure the `hashicorp.vault.kv1_secret_get` lookup plugin

The `hashicorp.vault.kv1_secret_get` lookup plugin module reads KV1 secrets.

### About this task

The corresponding `community.hashi_vault` modules are:

- **`community.hashi_vault.hashi_vault`:** Retrieves secrets from HashiCorp Vault.
- **`community.hashi_vault.vault_kv1_get lookup`:** Gets secrets from the HashiCorp Vault KV version 1 secret store.

### Procedure

1.  Replicate `the community.hashi_vault` modules to the following `hashicorp.vault.kv1_secret_get` parameters.

```
auth_method:
  description: Authentication method to use.
  choices: ['token', 'approle']
  default: token
  type: str
engine_mount_point:
  description:
    - The KV secrets engine mount point.
  default: secret
  type: str
  aliases: ['mount_point', 'secret_mount_path']
secret:
  description:
    - The Vault path to the secret being requested.
  required: true
  type: str
  aliases: ['secret_path']
```

2.  (Required) Configure the secret parameter. This maps to secret in the `community.hashi_vault.hashi_vault` modules. **Alias:**`secret_path`
3.  If needed, configure the optional parameters.

### What to do next

-  [Create a credential type](/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_vault_authenticating#vault-creating-custom-credential "Vault users must create a custom credential to use with job templates in Ansible Automation Platform.")

## Example: `hashicorp.vault.kv1_secret_info` module

The following migration example shows before and after configurations for the `hashicorp.vault.kv1_secret_info` module.

 **Example:**

Before (community.hashi_vault)

```
- name: Read a kv1 secret from Vault (community collection)
  community.hashi_vault.vault_kv1_get:
    url: https://vault:8201
    token: "{{ vault_token }}"
    path: hello
  register: response
```
After (hashicorp.vault)

```
- name: Read a kv1 secret from Vault (hashicorp.vault collection)
  hashicorp.vault.kv1_secret_info:
    url: https://vault.example.com:8201
    token: "{{ vault_token }}"
    path: sample
```

## Example: `hashicorp.vault.kv1_secret_get` lookup

The following migration example shows the KV1 secret get lookup.

 **Example:**

Before (community.hashi_vault)

```
- name: Retrieve a secret from the Vault
  ansible.builtin.debug:
    msg: "{{ lookup('community.hashi_vault.vault_kv1_get', 'hello', url='https://vault:8201') }}"
```
After (hashicorp.vault)

```
- name: Retrieve a secret from the Vault
  ansible.builtin.debug:
    msg: "{{ lookup('hashicorp.vault.kv1_secret_get',
                    secret='hello',
                    url='https://myvault_url:8201') }}"
```
