---
title: "MyCompany Corp Inventory Management Policy"
url: "https://internal.mycompany.example.com/wiki/automation/inventory-policy"
---
# MyCompany Corp Inventory Management Policy

This document defines the mandatory conventions for structuring, naming, and maintaining Ansible inventories at MyCompany Corp. All automation teams must follow these conventions to ensure consistent pipeline behavior and to pass MyCompany CI validation.

---

## Inventory Group Naming

All inventory groups must follow a strict naming pattern that encodes the environment and infrastructure tier:

```
mycompany_<env>_<tier>
```

### Environment values

The `<env>` segment must be one of: `dev`, `staging`, `prod`.

### Tier values

Common tier values include `web`, `db`, `cache`, `worker`, `lb` (load balancer), and `mgmt` (management). New tiers must be approved by the Platform Team before use.

### Correct group name examples

- `mycompany_prod_web` — production web servers
- `mycompany_staging_db` — staging database servers
- `mycompany_dev_cache` — development cache nodes
- `mycompany_prod_lb` — production load balancers
- `mycompany_prod_worker` — production async worker nodes

### Incorrect group name examples (will fail CI validation)

- `production_web` — missing `mycompany_` prefix
- `mycompany_web_prod` — env and tier are reversed
- `webservers` — missing prefix and env segment

---

## Required Host Variables

### The `mycompany_env` variable

The variable `mycompany_env` is **mandatory** on every managed host. It must be set to exactly one of: `dev`, `staging`, `prod`.

Playbook runs will fail the pre-flight validation step if any host in the targeted inventory is missing this variable. There are no exceptions.

Set `mycompany_env` in `host_vars/<hostname>/main.yml`:

```yaml
mycompany_env: prod
```

Do not rely on group membership to infer the environment — the variable must be explicit on each host.

### Additional required variables

| Variable | Required on | Allowed values | Description |
| --- | --- | --- | --- |
| `mycompany_env` | All hosts | `dev`, `staging`, `prod` | Deployment environment |
| `mycompany_owner_team` | All hosts | Any valid team slug | Team responsible for this host |
| `mycompany_managed` | All hosts | `true`, `false` | Whether MyCompany automation manages this host |

---

## Variable File Structure

### Host-specific variables

All host-specific variables must be defined in:

```
host_vars/<hostname>/main.yml
```

Defining host-level variable overrides inside `group_vars` files is **prohibited**. This rule prevents hidden precedence bugs and makes host configuration auditable.

Additional host variable files (e.g., `host_vars/<hostname>/vault.yml` for dev/staging secrets) are permitted alongside `main.yml`.

### Group variables

Group-level variables belong in:

```
group_vars/<group_name>/main.yml
```

Each group must have its own directory; single-file `group_vars/<group_name>.yml` format is deprecated and will be rejected by the MyCompany CI validator after 2026-Q3.

---

## Inventory Source Registration

### Dynamic inventory sources

Before a dynamic inventory source (e.g., an AWX inventory plugin, a custom script, or a cloud provider plugin) can be used in any MyCompany pipeline, it must be registered in the **MyCompany Inventory Registry**:

```
https://inventory.mycompany.internal
```

Unregistered dynamic sources will be blocked at the pipeline level. Submit a registration request via the Registry web UI — approval from the Platform Team is required and typically completes within 2 business days.

The `mycompany.infrastructure.dynamic_cloud` inventory plugin is pre-approved and does not require registration.

### Static inventory files

Static inventory files must use one of the following extensions to be recognized by the MyCompany CI validator:

- `.mycompany.ini` — INI-format static inventories
- `.mycompany.yml` — YAML-format static inventories

Files with standard extensions (`.ini`, `.yml`, `.yaml`) will not be automatically discovered by MyCompany tooling and will produce a warning in CI.

---

## Inventory Validation

The `mycompany-inventory-validator` tool runs as part of every CI pipeline and checks:

1. All group names match the `mycompany_<env>_<tier>` pattern
2. All hosts define `mycompany_env` with an approved value
3. All hosts define `mycompany_owner_team`
4. No host-level overrides exist inside `group_vars`
5. Dynamic sources are registered in the MyCompany Inventory Registry (or are `mycompany.infrastructure.dynamic_cloud`)

To run the validator locally before pushing:

```bash
mycompany-inventory-validator --inventory-path ./inventory/
```

Failures in inventory validation block the pipeline and must be resolved before merge.