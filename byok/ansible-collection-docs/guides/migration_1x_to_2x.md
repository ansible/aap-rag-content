---
title: "Migration Guide: 1.x to 2.x — mycompany.infrastructure"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/guides/migration_1x_to_2x.md"
---
# Migration Guide: 1.x to 2.x — mycompany.infrastructure

**Collection:** mycompany.infrastructure

---

## Overview

Version 2.0 of the `mycompany.infrastructure` collection introduces several breaking changes to module parameters, return values, and default behaviours. This guide explains what changed and how to update your playbooks.

---

## Breaking Changes

### Module: create_server

#### Renamed parameter: `type` → `instance_type`

The `type` parameter has been renamed to `instance_type`.

**Before (1.x):**
```yaml
- mycompany.infrastructure.create_server:
    name: web-prod-01
    provider: aws
    type: t3.medium
```

**After (2.x):**
```yaml
- mycompany.infrastructure.create_server:
    name: web-prod-01
    provider: aws
    instance_type: t3.medium
```

#### Changed default for `wait`

The default value of `wait` changed from `false` to `true`. Playbooks that relied on asynchronous creation without specifying `wait: false` will now block until the instance reaches `running` state.

If you need the old behaviour, add `wait: false` explicitly.

#### Return value renamed: `instance` → `server`

**Before (1.x):**
```yaml
- debug:
    msg: "{{ result.instance.instance_id }}"
```

**After (2.x):**
```yaml
- debug:
    msg: "{{ result.server.instance_id }}"
```

---

### Module: manage_database

#### Removed parameter: `apply_immediately`

The `apply_immediately` parameter has been removed. In 2.x, all mutable changes (`instance_class`, `storage_gb`, `backup_retention_days`) are always applied immediately.

If your 1.x playbooks used `apply_immediately: false` to defer changes to a maintenance window, you must now schedule the playbook run itself within the maintenance window.

---

### Module: configure_network

#### Subnets parameter format change

In 1.x, subnets were defined as a dictionary keyed by subnet name. In 2.x, they are a list of dicts, each with a `name` key.

**Before (1.x):**
```yaml
subnets:
  public-us-east-1a:
    cidr: "10.0.1.0/24"
    az: us-east-1a
    public: true
```

**After (2.x):**
```yaml
subnets:
  - name: public-us-east-1a
    cidr: "10.0.1.0/24"
    az: us-east-1a
    public: true
```

---

### Lookup Plugin: vault_secret

#### Changed default `kv_version`

The default KV version changed from `1` to `2`. If your Vault mount uses KV v1, pass `kv_version=1` explicitly.

**Before (1.x — implicitly KV v1):**
```yaml
"{{ lookup('mycompany.infrastructure.vault_secret', 'secret/myapp/db') }}"
```

**After (2.x — explicit KV v1):**
```yaml
"{{ lookup('mycompany.infrastructure.vault_secret',
           'secret/myapp/db',
           kv_version=1) }}"
```

---

### Inventory Plugin: dynamic_cloud

#### Renamed inventory filename pattern

The inventory source filename pattern changed from `*.mycompany.yml` to `*.mycompany_cloud.yml`. Rename your inventory source files accordingly.

#### Default `hostnames` changed

The default hostname resolution order changed from `["name", "private_ip"]` to `["private_dns", "private_ip"]`. If your playbooks rely on connecting via the instance `name` tag, add `name` back to the `hostnames` list in your inventory configuration.

---

## New Features in 2.x

| Feature | Plugin | Description |
|---|---|---|
| `purge_tags` parameter | `create_server` | Declarative tag management — removes tags not listed in `tags`. |
| `skip_final_snapshot` parameter | `manage_database` | Safe deletion workflow for staging environments. |
| `deploy_application` module | *(new)* | Previously only available as a role; now a full module. |
| `secret_version` parameter | `vault_secret` | Pin a specific KV v2 secret version. |
| `namespace` parameter | `vault_secret` | Vault Enterprise namespace support. |
| `config_value` lookup | *(new)* | Non-secret configuration retrieval from the internal config service. |
| Filter plugins | *(new)* | `to_cidr`, `parse_json_string`, `extract_tags` added. |

---

## Removed in 2.x (deprecated since 1.3.x)

| Removed item | Replacement |
|---|---|
| Module `mycompany.infrastructure.provision_vm` | `mycompany.infrastructure.create_server` |
| Lookup `mycompany.infrastructure.get_secret` | `mycompany.infrastructure.vault_secret` |
| Inventory `mycompany.infrastructure.cloud_inventory` | `mycompany.infrastructure.dynamic_cloud` |

---

## Upgrade Steps

1. **Update the collection:**
   ```bash
   ansible-galaxy collection install mycompany.infrastructure:>=2.0.0
   ```

2. **Find all usages of the collection in your codebase:**
   ```bash
   grep -r "mycompany.infrastructure" playbooks/ roles/ --include="*.yml" -l
   ```

3. **Apply the parameter and return-value renames** described in this guide to each file found.

4. **Rename inventory source files** from `*.mycompany.yml` to `*.mycompany_cloud.yml`.

5. **Update Vault lookups** that use KV v1 mounts to pass `kv_version=1`.

6. **Validate changes with check mode** before applying:
   ```bash
   ansible-playbook site.yml --check
   ```

---

## Getting Help

- Open a ticket: https://jira.mycompany.example/projects/INFRA
- Slack: `#infra-automation`