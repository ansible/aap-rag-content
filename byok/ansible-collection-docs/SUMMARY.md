---
title: "ansible-collection-docs-md — Summary"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/SUMMARY.md"
---
# ansible-collection-docs-md — Summary

Markdown export of the `mycompany.infrastructure` Ansible Collection documentation,
converted from RST (`ansible-collection-docs/`) into clean, RAG-injection-friendly Markdown.

---

## File Structure

```
ansible-collection-docs-md/
├── README.md                          ← collection overview + full plugin index
├── modules/
│   ├── create_server.md
│   ├── manage_database.md
│   ├── configure_network.md
│   └── deploy_application.md
├── lookup/
│   ├── vault_secret.md
│   └── config_value.md
├── filter/
│   └── infrastructure_filters.md     ← all 3 filters in one file (to_cidr, parse_json_string, extract_tags)
├── inventory/
│   └── dynamic_cloud.md
└── guides/
    ├── authentication.md
    └── migration_1x_to_2x.md
```

---

## Plugins Documented

### Modules

| Module | Description |
|---|---|
| `create_server` | Create or update a virtual server instance on AWS, Azure, GCP, or VMware |
| `manage_database` | Create, modify, or delete a managed PostgreSQL/MySQL/MariaDB instance |
| `configure_network` | Configure VPC networks, subnets, route tables, and security groups |
| `deploy_application` | Deploy containerised apps (ECS/AKS/GKE) or RPM/DEB packages to VMs |

### Lookup Plugins

| Plugin | Description |
|---|---|
| `vault_secret` | Fetch secrets from HashiCorp Vault KV v1/v2; supports Token, AppRole, AWS IAM auth |
| `config_value` | Retrieve non-secret configuration values from the internal config service |

### Filter Plugins

| Filter | Description |
|---|---|
| `to_cidr` | Convert an IP address and prefix length to CIDR notation |
| `parse_json_string` | Deserialise a JSON string into a Python object |
| `extract_tags` | Extract and normalise tag key-value pairs from cloud resource objects |

### Inventory Plugins

| Plugin | Description |
|---|---|
| `dynamic_cloud` | Build a dynamic inventory from AWS, Azure, GCP, and VMware APIs |

### Guides

| Guide | Description |
|---|---|
| `authentication.md` | Gateway token, IAM, Vault integration, and ansible.cfg configuration |
| `migration_1x_to_2x.md` | Breaking changes, removed parameters, and upgrade steps |

---

## RAG-Friendliness Design Decisions

- **One topic per file** — each file is a self-contained document; no RST cross-references or directives that break in plain text.
- **Consistent heading hierarchy** — every file opens with `# Plugin: <full FQCN>` plus a metadata block (collection, version), giving the retriever immediate context about the document subject.
- **Flat Markdown tables** instead of nested HTML — cleaner chunking boundaries and no parsing ambiguity.
- **`---` section dividers** — natural split points for chunk-size-aware text splitters.
- **Code blocks clearly fenced** with language hints (`yaml`, `bash`, `ini`) for better token handling.
- **Cross-references as relative links** — usable in rendered docs, but also readable as plain text when links are stripped.