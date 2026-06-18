# Back up and restore your containerized deployment

Protecting your Ansible Automation Platform containerized deployment ensures that you can recover from system failures, data corruption, or configuration errors. Regular backups minimize downtime and protect your configurations and data.

Implementing backup and restore procedures helps you to:

- **Protect critical automation assets**: Safeguard your data including configurations, inventory, credentials, and job history from unexpected failures or data loss.
- **Enable disaster recovery**: Restore your environment quickly after hardware failures or other unexpected events to maintain business continuity.
- **Support testing and development**: Create copies of your environment for testing upgrades or configuration changes without affecting production systems.

## Back up containerized Ansible Automation Platform

Perform a backup of your container-based installation of Ansible Automation Platform.

### Before you begin

- You have logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.

### About this task

Note:

- When backing up Ansible Automation Platform, use the installation program that matches your currently installed version of Ansible Automation Platform.
- Backup functionality only works with the PostgreSQL versions supported by your current Ansible Automation Platform version.
- Backup and restore for content stored in Azure Blob Storage or Amazon S3 must be handled through the vendor portals, as each vendor provides their own backup solutions.

### Procedure

1.  Go to the Red Hat Ansible Automation Platform installation directory on your Red Hat Enterprise Linux host.
2.  To control compression of the backup artifacts before they are sent to the host running the backup operation, you can use the following variables in your inventory file:
1.  For control of compression for filesystem related backup files:


```
# Global control of compression for filesystem backup files
use_archive_compression=true

# Component-level control of compression for filesystem backup files
#controller_use_archive_compression=true
#eda_use_archive_compression=true
#gateway_use_archive_compression=true
#hub_use_archive_compression=true
#pcp_use_archive_compression=true
#postgresql_use_archive_compression=true
#receptor_use_archive_compression=true
#redis_use_archive_compression=true
```

2.  For control of compression for database related backup files:


```
# Global control of compression for database backup files
use_db_compression=true

# Component-level control of compression for database backup files
#controller_use_db_compression=true
#eda_use_db_compression=true
#hub_use_db_compression=true
#gateway_use_db_compression=true
```

3.  Run the `backup` playbook:


```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.backup
```
The backup process creates archives of the following data:

- PostgreSQL databases
- Configuration files
- Data files

### What to do next

To customize the backup process, you can use the following variables in your inventory file:

- Change the backup destination directory from the default `./backups` by using the `backup_dir` variable.

-      Exclude paths that contain duplicated data, such as snapshot subdirectories, by using the `hub_data_path_exclude` variable.

For example, to exclude a `.snapshots` subdirectory from the backup, add the following to your inventory file:



```
hub_data_path_exclude=["*/.snapshots", "*/.snapshots/*"]
```
Alternatively, you can pass this variable at runtime by using the `-e` flag:



```
$ ansible-playbook -i inventory ansible.containerized_installer.backup -e hub_data_path_exclude="['*/.snapshots', '*/.snapshots/*']"
```
You can also define the exclusion patterns in a YAML extra variables file and pass it at runtime:

**exclude_vars.yml**



```
hub_data_path_exclude:
- "*/.snapshots/*"
- "*/.snapshots"
```


```
$ ansible-playbook -i inventory ansible.containerized_installer.backup -e @exclude_vars.yml
```

## Restore containerized Ansible Automation Platform

Restore your container-based installation of Ansible Automation Platform from a backup, or to a different environment.

### Before you begin

- You have logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.
- You have a backup of your Ansible Automation Platform deployment. For more information, see [Back up containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#backing-up-containerized-ansible-automation-platform "Perform a backup of your container-based installation of Ansible Automation Platform.").
- If restoring to a different environment with the same hostnames, you have performed a fresh installation on the target environment with the same topology as the original (source) environment.
- You have ensured that the administrator credentials on the target environment match the administrator credentials from the source environment.

### About this task

Note:

When restoring Ansible Automation Platform, use the latest installation program available at the time of the restore. For example, if you are restoring a backup taken from version `2.6-1`, use the latest `2.6-x` installation program available at the time of the restore.

Restore functionality only works with the PostgreSQL versions supported by your current Ansible Automation Platform version. For more information, see [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_cont_aap_system_requirements "Use this information when planning your installation of containerized Ansible Automation Platform.").

### Procedure

1.  Go to the installation directory on your Red Hat Enterprise Linux host.
2.  Perform the relevant restoration steps:

- If you are restoring to the same environment with the same hostnames, run the `restore` playbook:

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.restore
```
This restores the important data deployed by the containerized installer such as:

* PostgreSQL databases

* Configuration files

* Data files             By default, the backup directory is set to `./backups`. You can change this by using the `backup_dir` variable in your `inventory` file.

- If you are restoring to a different environment with different hostnames, perform the following additional steps before running the `restore` playbook:
Important:
Restoring to a different environment with different hostnames is not recommended and is intended only as a workaround.
1. For each component, identify the backup file from the source environment that contains the PostgreSQL dump file. For example:



```
$ cd ansible-automation-platform-containerized-setup-<version_number>/backups
```


```
$ tar tvf gateway_env1-gateway-node1.tar.gz | grep db

-rw-r--r-- ansible/ansible 4850774 2025-06-30 11:05 aap/backups/awx.db
```

2. Copy the backup files from the source environment to the target environment.

3. Rename the backup files on the target environment to reflect the new node names. For example:



```
$ cd ansible-automation-platform-containerized-setup-<version_number>/backups
```


```
$ mv gateway_env1-gateway-node1.tar.gz gateway_env2-gateway-node1.tar.gz
```

4. For enterprise topologies, ensure that the component backup file containing the `component.db` file is listed first in its group within the inventory file. For example:



```
$ cd ansible-automation-platform-containerized-setup-<version_number>
```


```
$ ls backups/gateway*

gateway_env2-gateway-node1.tar.gz
gateway_env2-gateway-node2.tar.gz
```


```
$ tar tvf backups/gateway_env2-gateway-node1.tar.gz | grep db

-rw-r--r-- ansible/ansible 416687 2025-06-30 11:05 aap/backups/gateway.db
```


```
$ tar tvf backups/gateway_env2-gateway-node2.tar.gz | grep db
```


```
$ vi inventory

[automationgateway]
env2-gateway-node1
env2-gateway-node2
```

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
