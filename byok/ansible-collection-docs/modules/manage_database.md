---
title: "Module: mycompany.infrastructure.manage_database"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/modules/manage_database.md"
---
# Module: mycompany.infrastructure.manage_database

**Short description:** Create, modify, or delete a managed database instance
**Collection:** mycompany.infrastructure
**Version added:** 1.0.0

---

## Synopsis

- Creates, modifies, or deletes a managed relational database instance on supported cloud providers (AWS RDS, Azure Database, GCP Cloud SQL).
- Supports PostgreSQL, MySQL, and MariaDB engines.
- When `state=present` and the database already exists, mutable attributes such as `instance_class`, `storage_gb`, and `tags` are updated in-place.
- Immutable attributes (`engine`, major `engine_version`, `db_name`) cannot be changed after creation and will cause a task failure if they differ from the existing instance.

---

## Requirements

The following must be installed on the host executing this module:

- python >= 3.9
- boto3 >= 1.26 *(for `provider=aws`)*
- azure-mgmt-rdbms >= 10.0 *(for `provider=azure`)*
- google-cloud-sql >= 1.9 *(for `provider=gcp`)*

---

## Parameters

| Parameter | Type | Required | Default | Choices | Description |
|---|---|---|---|---|---|
| `db_identifier` | string | yes | | | Unique identifier for the database instance. 1–63 characters, lowercase letters, digits, and hyphens. |
| `provider` | string | yes | | `aws`, `azure`, `gcp` | Cloud provider managing the database. |
| `engine` | string | no | `postgres` | `postgres`, `mysql`, `mariadb` | Database engine. Cannot be changed after creation. |
| `engine_version` | string | no | `15` (postgres), `8.0` (mysql/mariadb) | | Engine version (e.g. `15.4`). Minor version upgrades are applied automatically during the maintenance window. |
| `instance_class` | string | no | `db.t3.medium` | | Compute class for the database instance. AWS: e.g. `db.r6g.large`. GCP: e.g. `db-n1-standard-2`. Azure: e.g. `GP_Gen5_2`. |
| `storage_gb` | integer | no | `20` | | Allocated storage in gigabytes. Can only be increased, not decreased after creation. |
| `db_name` | string | no | `appdb` | | Name of the initial database. Cannot be changed after creation. |
| `master_username` | string | no | `dbadmin` | | Master username for the database instance. |
| `master_password` | string | no | | | Master password. Required when creating a new instance. **no_log.** Use Vault to avoid plaintext passwords. |
| `multi_az` | boolean | no | `false` | `true`, `false` | Enable multi-AZ deployment for high availability. |
| `backup_retention_days` | integer | no | `7` | | Days to retain automated backups. Set to `0` to disable. |
| `skip_final_snapshot` | boolean | no | `false` | `true`, `false` | When `state=absent`, skip creating a final snapshot before deletion. Set to `false` in production. |
| `state` | string | no | `present` | `present`, `absent` | Desired state of the database instance. |
| `region` | string | no | | | Cloud region where the database is deployed. Env var: `MYCOMPANY_REGION`. |
| `tags` | dictionary | no | `{}` | | Key/value tags applied to the database instance. |

---

## Attributes

| Attribute | Support | Description |
|---|---|---|
| check_mode | full | Runs without making changes; reports what would change. |
| diff_mode | partial | Returns diff for mutable attributes only (`instance_class`, `storage_gb`, `backup_retention_days`, `tags`). |
| platform | all | No target-host OS dependencies. |

---

## Notes

- Database deletion is irreversible. Set `skip_final_snapshot: false` in production to retain a snapshot.
- Storage can only be scaled up, not down.
- For PostgreSQL, the `postgres` engine maps to `aurora-postgresql` on AWS if `multi_az=true` and the region supports Aurora.
- Minor version upgrades happen automatically. To control the exact version, pin `engine_version` to a minor version such as `15.4`.

---

## See Also

- [create_server](create_server.md) — Create application servers that connect to this database.
- [vault_secret lookup](../lookup/vault_secret.md) — Retrieve the master password securely from Vault.

---

## Examples

```yaml
# Create a PostgreSQL RDS instance on AWS
- name: Create production database
  mycompany.infrastructure.manage_database:
    db_identifier: myapp-prod-postgres
    provider: aws
    region: us-east-1
    engine: postgres
    engine_version: "15"
    instance_class: db.r6g.large
    storage_gb: 100
    db_name: appdb
    master_username: dbadmin
    master_password: "{{ lookup('mycompany.infrastructure.vault_secret', 'secret/db/master_password') }}"
    multi_az: true
    backup_retention_days: 14
    tags:
      environment: production
      team: backend
    state: present
  register: db_result

# Scale up storage on an existing instance
- name: Increase database storage
  mycompany.infrastructure.manage_database:
    db_identifier: myapp-prod-postgres
    provider: aws
    region: us-east-1
    storage_gb: 200
    state: present

# Delete a staging database (skip snapshot for cost savings)
- name: Remove staging database
  mycompany.infrastructure.manage_database:
    db_identifier: myapp-staging-postgres
    provider: aws
    region: us-east-1
    skip_final_snapshot: true
    state: absent
```

---

## Return Values

| Key | Description | Returned | Type |
|---|---|---|---|
| `database` | Details of the managed database instance. | when `state=present` | dict |
| `database.db_identifier` | Identifier of the database instance. | always | string — e.g. `"myapp-prod-postgres"` |
| `database.endpoint` | Connection endpoint hostname. | always | string — e.g. `"myapp-prod-postgres.abcdef123456.us-east-1.rds.amazonaws.com"` |
| `database.port` | Port the database engine listens on. | always | integer — e.g. `5432` |
| `database.engine` | Database engine in use. | always | string — e.g. `"postgres"` |
| `database.engine_version` | Engine version running on the instance. | always | string — e.g. `"15.4"` |
| `database.status` | Current status of the database instance. | always | string — e.g. `"available"` |
| `database.storage_gb` | Currently allocated storage in GB. | always | integer — e.g. `100` |
| `database.multi_az` | Whether the instance is in a Multi-AZ configuration. | always | bool |
| `changed` | Whether the module made any changes. | always | bool |

---

## Authors

- Bob Ramirez (@bob-r) — bob.ramirez@mycompany.example