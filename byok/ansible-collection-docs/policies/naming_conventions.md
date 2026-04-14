---
title: "MyCompany Ansible Naming Conventions"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/policies/naming_conventions.md"
---
# MyCompany Ansible Naming Conventions

This document defines the mandatory naming standards for all Ansible automation assets at MyCompany Corp. All automation contributors must follow these conventions before submitting any playbook, role, or inventory for review.

---

## Roles

### Naming Standard

All custom Ansible roles **must** use the `mycompany_` prefix followed by a descriptive lowercase name with underscores separating words.

**Pattern:** `mycompany_<descriptive_name>`

**Examples:**

| Correct | Incorrect |
|---------|-----------|
| `mycompany_webserver` | `webserver` |
| `mycompany_database_backup` | `db-backup` |
| `mycompany_monitoring_agent` | `monitoring` |
| `mycompany_deploy_app` | `deploy` |

The `mycompany_` prefix is required because:
- It prevents naming collisions with community Galaxy roles
- It signals that the role is owned and maintained by MyCompany Corp
- It is enforced by the Platform Team's automated linting pipeline

### Initializing a Role

Use `ansible-galaxy` to scaffold a new role with the correct name:

```bash
ansible-galaxy role init mycompany_<descriptive_name>
```

Example:

```bash
ansible-galaxy role init mycompany_monitoring_agent
```

This creates the standard role directory structure under `roles/mycompany_monitoring_agent/`.

### Role Directory Structure

```
roles/
└── mycompany_monitoring_agent/
    ├── defaults/
    │   └── main.yml
    ├── files/
    ├── handlers/
    │   └── main.yml
    ├── meta/
    │   └── main.yml
    ├── tasks/
    │   └── main.yml
    ├── templates/
    ├── tests/
    │   ├── inventory
    │   └── test.yml
    └── vars/
        └── main.yml
```

The `meta/main.yml` file **must** include the `galaxy_info.namespace` key set to `mycompany`.

---

## Inventory Groups

### Naming Standard

All Ansible inventory groups **must** follow the `mycompany_<env>_<tier>` pattern, where:

- `<env>` identifies the deployment environment: `prod`, `staging`, `dev`, `qa`
- `<tier>` identifies the infrastructure tier: `web`, `app`, `db`, `cache`, `worker`, `mgmt`

**Pattern:** `mycompany_<env>_<tier>`

**Examples:**

| Group Name | Meaning |
|-----------|---------|
| `mycompany_prod_web` | Production web servers |
| `mycompany_prod_db` | Production database servers |
| `mycompany_staging_app` | Staging application servers |
| `mycompany_dev_worker` | Development worker nodes |
| `mycompany_qa_cache` | QA cache layer |
| `mycompany_prod_mgmt` | Production management/bastion hosts |

### Why This Pattern

The `mycompany_<env>_<tier>` pattern provides:
- **Consistency** — all groups are unambiguous at a glance
- **Filterability** — you can target all production groups with `--limit 'mycompany_prod_*'`
- **Collision avoidance** — the `mycompany_` prefix prevents conflicts with upstream community inventories

### Group Variables

Group variable files must follow the same pattern: `group_vars/mycompany_<env>_<tier>.yml`.

```
inventory/
├── hosts.yml
└── group_vars/
    ├── mycompany_prod_web.yml
    ├── mycompany_prod_db.yml
    └── mycompany_staging_app.yml
```

---

## Playbooks

Playbook filenames should reflect their purpose and target environment:

**Pattern:** `<action>_<component>[_<env>].yml`

**Examples:**
- `deploy_application_prod.yml`
- `configure_database.yml`
- `provision_server_staging.yml`

---

## Collections

All internal MyCompany collections are namespaced under `mycompany.<collection_name>`.

**Examples:**
- `mycompany.infrastructure` — infrastructure provisioning and secrets
- `mycompany.networking` — network configuration

---

## Enforcement

Naming convention compliance is checked automatically by:
- **Pre-commit hooks** in the GitLab CI pipeline
- **Platform Team lint gate** during playbook review (see [Playbook Review Process](playbook_review.md))

Submissions that do not follow these conventions will be rejected at the lint gate and must be corrected before the review SLA clock starts.

---

## References

- Starter role templates: [https://gitlab.mycompany.internal/ansible/templates](https://gitlab.mycompany.internal/ansible/templates)
- Playbook review process: [playbook_review.md](playbook_review.md)
- Platform Team contact: `#platform-ops` on Slack