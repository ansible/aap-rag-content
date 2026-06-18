# Configure KV2 modules

If you are using KV2 with `community.hashi_vault` collection, configure the corresponding modules in the `hashicorp.vault` collection.

## Configure the `hashicorp.vault.kv2_secret` module

The `hashicorp.vault.kv2_secret` module performs Create, Update, and Delete (CRUD) operations on KV2 secrets through a unified interface.

### Before you begin

- Install the Ansible Automation Platform certified `hashicorp.vault` collection.

### About this task

The corresponding `community.hashi_vault` modules are:

- **`community.hashi_vault.vault_kv2_write`** - Write KV2 secrets.
- **`community.hashi_vault.vault_kv2_delete`** - Delete KV2 secrets.

### Procedure

1.  Replicate your automation tasks from both of the `community.hashi_vault` modules to the following `hashicorp.vault.kv2_secret` parameters. The `hashicorp.vault.kv2_secret` parameters are similar to `community.hashi_vault`.

```
auth_method:
description: Authentication method to use
type: str
choices: [token, approle]
default: token
required: false

cas:
description: Perform a check-and-set operation.
type: int
required: false

data:
description: KV2 secret data to write.
type: dict
required: true

engine_mount_point:
description: The path where the secret backend is mounted.
type: str
default: secret
required: false
aliases: [secret_mount_path]

namespace:
description: Vault namespace where secrets reside.
type: str
default: admin
aliases: [vault_namespace]

path:
description: Vault KVv2 path to be written to.
type: str
required: true
aliases: [secret_path]

url:
description: URL of the Vault service
type: str
aliases: [vault_address]
required: true

versions:
description: One or more versions of the secret to delete.
type: list of int
required: false

state:
description: Desired state of the secret
type: str
choices: [present, absent]
default: present
```

2.  You must add the `state` parameter to the `hashicorp.vault.kv2_secret` module, as shown above. Valid options are:

- **`present`:** This is the equivalent of `create` or `update` in the `community.hashi_vault.vault_kv2` modules.
- **`absent`:** This is the equivalent of `delete secret` in the `community.hashi_vault.vault_kv2` modules.

### What to do next

- [Configure the `hashicorp.vault.kv2_secret_info` module](/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_kv2_modules#vault-configuring-kv2-secret-info "The hashicorp.vault.kv2_secret_info module reads KV2 secrets.").

## Configure the `hashicorp.vault.kv2_secret_info` module

The `hashicorp.vault.kv2_secret_info` module reads KV2 secrets.

### About this task

The corresponding `community.hashi_vault` module is:

- **`community.hashi_vault.vault_kv2_get`:** Gets secrets from the HashiCorp Vault KV version 2 secret store.

### Procedure

1.  Replicate the `community.hashi_vault` modules to the following `hashicorp.vault.kv2_secret_info` parameters.

```
engine_mount_point:
description: KV secrets engine mount point.
default: secret
type: str
aliases: [secret_mount_path]
path:
description: Path to the secret.
required: true
type: str
aliases: [secret_path]
version:
description: The version to retrieve.
type: int
extends_documentation_fragment:
- hashicorp.vault.vault_auth.modules
```

2.  Configure the required parameters:

- **`path`:** The path where the secret is located in the community.`hashi_vault.hashi_vault` modules. **Alias:**`secret_path`
- **`url`:** Maps to `url` in the `community.hashi_vault.hashi_vault` modules. Uses the same aliases as `vault_address`.

3.  If needed, configure the optional parameters.

### What to do next

- [Configure the `hashicorp.vault.kv2_secret_get` lookup plugin](/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_kv2_modules#vault-configuring-kv2-secret-get-lookup "The hashicorp.vault.kv2_secret_get lookup plugin module reads KV2 secrets.").

## Configure the `hashicorp.vault.kv2_secret_get` lookup plugin

The `hashicorp.vault.kv2_secret_get` lookup plugin module reads KV2 secrets.

### About this task

The corresponding `community.hashi_vault` modules are:

- **`community.hashi_vault.hashi_vault`:** Retrieves secrets from HashiCorp Vault.
- **`community.hashi_vault.vault_kv2_get` lookup:** Gets secrets from the HashiCorp Vault KV version 2 secret store.

### Procedure

1.  Replicate the `community.hashi_vault` modules to the following `hashicorp.vault.kv2_secret_get` parameters.

```
auth_method:
description: Authentication method to use
type: str
choices: [token, approle]
default: token
required: false

mount_point:
description: Vault mount point
type: str
required: false
aliases: [secret_mount_path]

namespace:
description: Vault namespace where secrets reside.
type: str
default: admin
aliases: [vault_namespace]
secret:
description: Vault path to the secret being requested in the format path[:field]
type: str
required: true
aliases: [secret_path]

url:
description: URL of the Vault service
type: str
aliases: [vault_address]
required: true

version:
description: Specifies the version to return. If not set the latest is returned.
type: int
required: false
```

2.  Use the following guidance to configure the `hashicorp.vault.kv2_secret_get` parameters:

- **`auth_method`:** Maps identically to `auth_method` in the `community.hashi_vault.hashi_vault` modules.
- **`mount_point`:** Maps to `mount_point` in the `community.hashi_vault.hashi_vault` modules. **Alias:**`secret_mount_path`.
- **`namespace`:** Maps to `namespace` in the `community.hashi_vault.hashi_vault` modules. **Alias:**`vault_namespace`.
- **`secret`:** Maps to `secret` in the `community.hashi_vault.hashi_vault` modules.
- **`url`:** Maps to `url` in the `community.hashi_vault.hashi_vault` modules. Uses the same aliases as `vault_address`.
- **`version`:** Maps identically to `version` in the `community.hashi_vault.hashi_vault` modules.

### What to do next

-  [Create a credential type](/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_authenticating#vault-creating-credential-type "As an admin, you create a secure credential type in Ansible Automation Platform, which is used to authenticate to Vault.")

## Examples: `hashicorp.vault.kv2_secret` module

The following migration examples show basic before and after configurations for the `hashicorp.vault.kv2_secret` module.

Note:

KV2 delete operations are `soft-delete`.

**Example 1: Basic Secret Write/Create**

Before (`community.hashi_vault`):

```
- name: Write/create a secret
community.hashi_vault.vault_kv2_write:
url: https://vault:8200
path: hello
data:
foo: bar
```
After (`hashicorp.vault`):

```
- name: Write/create a secret
hashicorp.vault.kv2_secret:
url: https://vault:8200
path: hello
data:
foo: bar
```
**Example 2: Basic Secret Delete**

Before (`community.hashi_vault`):

```
- name: Delete the latest version of the secret/mysecret secret.
community.hashi_vault.vault_kv2_delete:
url: https://vault:8201
path: secret/mysecret
```
After (`hashicorp.vault`):

```
- name: Delete the latest version of the secret/mysecret secret.
hashicorp.vault.kv2_secret:
url: https://vault:8201
path: secret/mysecret
state: absent
```
**Example 3: Secret Delete - specific version**

Before (`community.hashi_vault`):

```
- name: Delete versions 1 and 3 of the secret/mysecret secret.
community.hashi_vault.vault_kv2_delete:
url: https://vault:8201
path: secret/mysecret
versions: [1, 3]
```
After (`hashicorp.vault`):

```
- name: Delete versions 1 and 3 of the secret/mysecret secret.
hashicorp.vault.kv2_secret:
url: https://vault:8201
path: secret/mysecret
versions: [1, 3]
state: absent
```

## Examples: `hashicorp.vault.kv2_secret_info` module

The following migration examples show before and after configurations for the `hashicorp.vault.kv2_secret_info` module.

**Example 1: Read a secret with token authentication**

Before (community.hashi_vault)

```
- name: Read the latest version of a kv2 secret from Vault  community.hashi_vault.vault_kv2_get:
url: https://vault.example.com:8200
token: "{{ vault_token }}"
path: myapp/config
register: response
```
After (hashicorp.vault)

```
- name: Read a secret with token authentication
hashicorp.vault.kv2_secret_info:
url: https://vault.example.com:8200
token: "{{ vault_token }}"
path: myapp/config
```
**Example 2: Read a secret with a specific version**

Before (community.hashi.vault)

```
- name: Read version 5 of a secret from kv2
community.hashi_vault.vault_kv2_get:
url: https://vault.example.com:8200
path: myapp/config
version: 5
```
After (hashicorp.vault)

```
- name: Read a secret with a specific version
hashicorp.vault.kv2_secret_info:
url: https://vault.example.com:8200
path: myapp/config
version: 1
```

## Examples: `hashicorp.vault.kv2_secret_get` lookup

The following migration example shows the KV2 secret get lookup for retrieving the latest version.

**Example:**

Before (`community.hashi_vault`)

```
- name: Return latest KV v2 secret from path
ansible.builtin.debug:
msg: "{{ lookup('community.hashi_vault.hashi_vault', 'secret=secret/data/hello
token=my_vault_token
url=http://myvault_url:8200') }}"
```
After (`hashicorp.vault`)

```
name: Return latest KV v2 secret from path
ansible.builtin.debug:
msg: "{{ lookup('hashicorp.vault.kv2_secret_get', 'secret=secret/data/hello
url=http://myvault_url:8200') }}"
```
