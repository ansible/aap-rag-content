# Back up and restore your containerized deployment
## Back up and restore metrics service

Back up and restore the metrics service database and configuration to recover from hardware failures, data corruption, or operational errors without losing historical metrics data.

### About this task

For **Ansible Automation Platform 2.7** (base metrics service without dashboard), no backup retention policy is required. Base metrics service does not contain user-visible data that needs backup or retention.

**When dashboard becomes GA:** Define retention based on dashboard data retention requirements (90 days default) and customer compliance requirements.

**Installer-provided backup script:** The Ansible Automation Platform containerized installer includes backup.yml and restore.yml playbooks that handle backup and restore operations for metrics service.

### Procedure

1.  Backup procedure
**Method 1: Use installer playbook (recommended)**

```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory backup.yml
```
The backup.yml playbook automatically backs up:

- `metrics_service` database
- Volume directories (`{{ aap_volumes_dir }}/automationmetrics`)
- Podman secrets (four secrets)
- Service configuration
Backup files are stored in the location specified by your inventory backup configuration.

**Method 2: Manual backup**

Use this method if you need custom backup procedures or granular control.

**What to back up:**

- **metrics_service database:** All collected and processed metrics data
- **Volume directories:** `{{ aap_volumes_dir }}/automationmetrics` (host path; maps to /var/lib/ansible-automation-platform/metrics in container)
- **Podman secrets:** Four secrets:
* `automationmetrics_pg_password`
* `automationmetrics_controller_read_pg_password`
* `automationmetrics_secret_key`
* `automationmetrics_resource_server`
- **Inventory file:** Configuration variables
Note:
For Ansible Automation Platform 2.7 base metrics service (without dashboard), backup is optional. When automation dashboard is enabled, back up the `metrics_service` database to preserve dashboard historical data.

**Step 1: Back up database**

```
pg_dump -h localhost -U metrics_service -F c -b -v \
-f /backup/metrics_service_$(date +%Y%m%d_%H%M%S).dump \
metrics_service
```
**Step 2: Back up volumes**

```
tar -czf /backup/automationmetrics_data_$(date +%Y%m%d_%H%M%S).tar.gz \
{{ aap_volumes_dir }}/automationmetrics
```

2.  Restore procedure

Warning:
Restoring from backup overwrites current metrics service data.

**Method 1: Use installer playbook (recommended)**

```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory restore.yml
```
The restore.yml playbook automatically performs the restore sequence:

1. Unarchives backup data
2. Restores Podman secrets (via common/restore_secrets.yml)
3. Imports TLS certificates (via tasks/tls_postgresql.yml)
4. Restores database
5. Restarts services
**Method 2: Manual restore**

Use this method for custom restore procedures or troubleshooting.

**Step 1: Stop metrics service**

```
systemctl --user stop automation-metrics-web.service automation-metrics-tasks.service automation-metrics-scheduler.service
```
**Step 2: Restore database**

```
psql -h localhost -U postgres -c "DROP DATABASE IF EXISTS metrics_service;"
psql -h localhost -U postgres -c "CREATE DATABASE metrics_service;"
pg_restore -h localhost -U metrics_service -d metrics_service -v \
/backup/metrics_service_TIMESTAMP.dump
```
Note:
The restore sequence (from installer tasks/restore.yml): unarchive data → restore secrets (via common/restore_secrets.yml) → import TLS certificates (via tasks/tls_postgresql.yml) → restore database → restart services.

**Step 3: Start metrics service**

```
systemctl --user start automation-metrics-web.service automation-metrics-tasks.service automation-metrics-scheduler.service
```
