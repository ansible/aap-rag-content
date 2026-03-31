---
title: "Lookup Plugin: mycompany.infrastructure.vault_secret"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/lookup/vault_secret.md"
---
# Lookup Plugin: mycompany.infrastructure.vault_secret

**Short description:** Retrieve secrets from HashiCorp Vault or the internal secret store
**Collection:** mycompany.infrastructure
**Version added:** 1.0.0

---

## Synopsis

- Fetches secret values from HashiCorp Vault KV v1 or KV v2 secret engines, or from the MyCompany internal secret management service.
- Supports Token, AppRole, and AWS IAM authentication methods.
- Returns the full secret data dictionary or a specific field when `field` is specified.
- Multiple secret paths can be passed; results are returned as a list.

---

## Requirements

The following must be installed on the host executing this lookup:

- python >= 3.9
- hvac >= 1.0 *(not required when `use_gateway=true`)*
- requests >= 2.28

---

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `_terms` | list of strings | yes | | One or more Vault secret paths to retrieve (e.g. `secret/myapp/db_password`). For KV v2 mounts, omit the `data/` prefix — the lookup adds it automatically based on `kv_version`. |
| `field` | string | no | *(return full dict)* | When specified, return only this field from the secret data dictionary. If not set, the entire secret data dict is returned. |
| `url` | string | no | `$VAULT_ADDR` | URL of the Vault server or MyCompany secret gateway. Config: INI `[mycompany_infrastructure] vault_url`, env `VAULT_ADDR`, var `mycompany_vault_url`. |
| `token` | string | no | `$VAULT_TOKEN` | Vault token for Token authentication. Env `VAULT_TOKEN`, var `mycompany_vault_token`. |
| `auth_method` | string | no | `token` | Vault authentication method. Choices: `token`, `approle`, `aws_iam`. Config: INI `[mycompany_infrastructure] vault_auth_method`, env `MYCOMPANY_VAULT_AUTH_METHOD`, var `mycompany_vault_auth_method`. |
| `role_id` | string | no | | AppRole Role ID. Required when `auth_method=approle`. Env `VAULT_ROLE_ID`, var `mycompany_vault_role_id`. |
| `secret_id` | string | no | | AppRole Secret ID. Required when `auth_method=approle`. **no_log.** Env `VAULT_SECRET_ID`, var `mycompany_vault_secret_id`. |
| `kv_version` | integer | no | `2` | KV secrets engine version. Choices: `1`, `2`. |
| `secret_version` | integer | no | *(latest)* | Specific secret version to retrieve (KV v2 only). *(Added in 1.2.0)* |
| `namespace` | string | no | | Vault Enterprise namespace. Ignored for Community Edition. Env `VAULT_NAMESPACE`, var `mycompany_vault_namespace`. *(Added in 1.3.0)* |

---

## Notes

- Secrets retrieved by this lookup are marked `no_log` automatically in Ansible output, but callers should still avoid printing them in debug messages.
- When using `auth_method=aws_iam`, the control node must have an IAM role or instance profile with permission to call `sts:GetCallerIdentity`.
- Token renewal is handled automatically during long-running playbooks when the token's TTL drops below 30 seconds.
- To avoid leaking secrets in diffs or task output, combine this lookup with `no_log: true` on the task that uses the returned value.

> **Configuration priority (lowest to highest):** INI file → environment variable → Ansible variable → task parameter.

---

## See Also

- [config_value lookup](config_value.md) — Retrieve non-secret configuration values from the config service.
- [deploy_application module](../modules/deploy_application.md) — Pass Vault-retrieved credentials to application deployments.

---

## Examples

```yaml
# Retrieve a single field from a KV v2 secret
- name: Get database password
  ansible.builtin.set_fact:
    db_password: "{{ lookup('mycompany.infrastructure.vault_secret',
                            'secret/myapp/database',
                            field='password') }}"
  no_log: true

# Retrieve the entire secret data dictionary
- name: Get all database credentials
  ansible.builtin.set_fact:
    db_creds: "{{ lookup('mycompany.infrastructure.vault_secret',
                         'secret/myapp/database') }}"
  no_log: true

# Use AppRole authentication
- name: Get secret via AppRole
  ansible.builtin.set_fact:
    api_token: "{{ lookup('mycompany.infrastructure.vault_secret',
                          'secret/myapp/api_token',
                          field='value',
                          auth_method='approle',
                          role_id=vault_role_id,
                          secret_id=vault_secret_id) }}"
  no_log: true

# Retrieve a pinned secret version (KV v2)
- name: Get specific secret version
  ansible.builtin.set_fact:
    old_key: "{{ lookup('mycompany.infrastructure.vault_secret',
                        'secret/myapp/signing_key',
                        field='private_key',
                        secret_version=3) }}"
  no_log: true

# Retrieve multiple secrets at once (returns a list)
- name: Get multiple secrets
  ansible.builtin.set_fact:
    secrets: "{{ lookup('mycompany.infrastructure.vault_secret',
                        'secret/myapp/db',
                        'secret/myapp/cache',
                        wantlist=true) }}"
  no_log: true

# Use KV v1 mount explicitly
- name: Get secret from KV v1 mount
  ansible.builtin.set_fact:
    legacy_secret: "{{ lookup('mycompany.infrastructure.vault_secret',
                              'kv/myapp/old_secret',
                              kv_version=1,
                              field='value') }}"
  no_log: true
```

---

## Return Values

| Key | Description | Returned | Type |
|---|---|---|---|
| `_raw` | The secret value(s). A single string when `field` is specified; a dictionary of the full secret data otherwise. A list when multiple paths are passed. | success | any |

---

## Authors

- Alice Nguyen (@alice-n) — alice.nguyen@mycompany.example