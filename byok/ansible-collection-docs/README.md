---
title: "Collection: mycompany.infrastructure"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/README.md"
---
# Collection: mycompany.infrastructure

**Version:** 1.4.2
**Supported ansible-core:** 2.14.0 or newer
**License:** GPL-3.0-or-later

## Description

The `mycompany.infrastructure` collection provides modules, lookup plugins, filter plugins, and inventory plugins for managing cloud and on-premises infrastructure resources, secrets, network configuration, and application deployments in enterprise environments.

This collection is maintained by the Platform Engineering team at MyCompany.

**Authors:**
- Alice Nguyen (@alice-n) — alice.nguyen@mycompany.example
- Bob Ramirez (@bob-r) — bob.ramirez@mycompany.example

**Links:**
- Issue Tracker: https://jira.mycompany.example/projects/INFRA
- Repository: https://github.mycompany.example/platform-eng/ansible-infrastructure
- Discussion: https://chat.mycompany.example/infra-automation

---

## Installation

```bash
ansible-galaxy collection install mycompany.infrastructure
```

Or via `requirements.yml`:

```yaml
collections:
  - name: mycompany.infrastructure
    version: ">=1.4.0"
```

---

## Plugin Index

### Modules

| Module | Description |
|---|---|
| [create_server](modules/create_server.md) | Create or update a virtual server instance |
| [manage_database](modules/manage_database.md) | Create, modify, or delete a managed database instance |
| [configure_network](modules/configure_network.md) | Configure VPC networks, subnets, and security groups |
| [deploy_application](modules/deploy_application.md) | Deploy or update an application on a target environment |

### Lookup Plugins

| Plugin | Description |
|---|---|
| [vault_secret](lookup/vault_secret.md) | Retrieve secrets from HashiCorp Vault or the internal secret store |
| [config_value](lookup/config_value.md) | Look up configuration values from the internal config service |

### Filter Plugins

| Plugin | Description |
|---|---|
| [to_cidr](filter/infrastructure_filters.md#to_cidr) | Convert an IP address and prefix length to CIDR notation |
| [parse_json_string](filter/infrastructure_filters.md#parse_json_string) | Parse a JSON string and return a Python object |
| [extract_tags](filter/infrastructure_filters.md#extract_tags) | Extract key-value tag pairs from a resource object |

### Inventory Plugins

| Plugin | Description |
|---|---|
| [dynamic_cloud](inventory/dynamic_cloud.md) | Build a dynamic inventory from multi-cloud provider APIs |

### Guides

| Guide | Description |
|---|---|
| [Authentication Guide](guides/authentication.md) | How to configure credentials for the collection |
| [Migration Guide 1.x → 2.x](guides/migration_1x_to_2x.md) | Breaking changes and upgrade steps |