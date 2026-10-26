+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment"
title = "Back up and restore your containerized deployment - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment/", "Back up and restore your containerized deployment"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment/aem-page/administer-back_up_and_restore_your_containerized_deployment.html"
last_crumb = "Back up and restore your containerized deployment"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Back up and restore your containerized deployment"
oversized = "false"
page_slug = "administer-back_up_and_restore_your_containerized_deployment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment/toc/toc.json"
type = "aem-page"
+++

# Back up and restore your containerized deployment

Protecting your Ansible Automation Platform containerized deployment ensures that you can recover from system failures, data corruption, or configuration errors. Regular backups minimize downtime and protect your configurations and data.

Implementing backup and restore procedures helps you to:

- **Protect critical automation assets**: Safeguard your data including configurations, inventory, credentials, and job history from unexpected failures or data loss.
- **Enable disaster recovery**: Restore your environment quickly after hardware failures or other unexpected events to maintain business continuity.
- **Support testing and development**: Create copies of your environment for testing upgrades or configuration changes without affecting production systems.

Note:

For the lowest-risk restore outcome, upgrade the source environment to the same async release as the target before taking a backup. Restoring a backup from an earlier async release onto a later async release is possible but may encounter unexpected behavior if schema or configuration changes were introduced in the intervening releases.

## Back up containerized Ansible Automation Platform

Perform a backup of your container-based installation of Ansible Automation Platform.

### Before you begin

- You have logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.

### About this task

Important:

If you take a backup from an environment that is broken or degraded, that backup might not restore correctly. File system issues such as incorrect SELinux contexts, broken symbolic links, or NFS mount failures can be captured in the backup and reproduced on restore. Where possible, repair your environment before taking a backup.

Note:

- When backing up Ansible Automation Platform, use the installation program that matches your currently installed version of Ansible Automation Platform.
- Backup functionality only works with the PostgreSQL versions supported by your current Ansible Automation Platform version.
- Backup and restore for content stored in Azure Blob Storage or Amazon S3 must be handled through the vendor portals, as each vendor provides their own backup solutions.

### Procedure

1. Go to the Red Hat Ansible Automation Platform installation directory on your Red Hat Enterprise Linux host.
2. To control compression of the backup artifacts before they are sent to the host running the backup operation, you can use the following variables in your inventory file:
  1. For control of compression for filesystem related backup files:
  

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

  2. For control of compression for database related backup files:
  

```
# Global control of compression for database backup files
use_db_compression=true

        # Component-level control of compression for database backup files
#controller_use_db_compression=true
#eda_use_db_compression=true
#hub_use_db_compression=true
#gateway_use_db_compression=true
```

3. Run the `backup` playbook:
  

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

- Exclude paths that contain duplicated data, such as snapshot subdirectories, by using the `hub_data_path_exclude` variable.

    For example, to exclude a `.snapshot` subdirectory from the backup, add the following to your inventory file:

```
hub_data_path_exclude=["*/.snapshot", "*/.snapshot/*"]
```

    Alternatively, you can pass this variable at runtime by using the `-e` flag:

```
$ ansible-playbook -i inventory ansible.containerized_installer.backup -e hub_data_path_exclude="['*/.snapshot', '*/.snapshot/*']"
```

    You can also define the exclusion patterns in a YAML extra variables file and pass it at runtime:

    **exclude_vars.yml**

```
hub_data_path_exclude:
    - "*/.snapshot/*"
    - "*/.snapshot"
```

```
$ ansible-playbook -i inventory ansible.containerized_installer.backup -e @exclude_vars.yml
```

## Skip database backup when using an external database

If your Ansible Automation Platform deployment uses an external database, you can skip database backup operations and manage database backups separately using your database provider's tools or a third-party backup solution.

### About this task

When `postgresql_skip_data` is set to `true`, the backup playbook archives configuration files and data files and skips database backup operations.

You must skip database backup if your external database is running PostgreSQL 16 or later. Ansible Automation Platform backup tooling uses PostgreSQL 15 client tools, which cannot perform `pg_dump` operations against a PostgreSQL 16 or later database. If you run the backup playbook without setting `postgresql_skip_data=true` in this scenario, the playbook fails.

### Procedure

1. Add the `postgresql_skip_data` variable to your inventory file:
  

```
postgresql_skip_data=true
```

2. Run the `backup` playbook:
  

```
$ ansible-playbook -i <path_to_inventory>
  ansible.containerized_installer.backup
```

  The backup process archives configuration files and data files and skips database backup operations.

3. Back up your PostgreSQL database using your external database provider's tools or a third-party backup solution.

## What the restore playbook restores

The containerized restore playbook restores data from a backup archive. It does not restore database connection secrets or Transport Layer Security (TLS) certificates, which are managed by the installation playbook.

The restore playbook is a data-restoration tool, not a complete environment rebuild tool. It applies data to a working installation of Ansible Automation Platform. Knowing this helps you plan your restore procedure and avoid errors.

### Data restored from backup

The restore playbook restores the following from the backup archive:

- PostgreSQL database content for all Ansible Automation Platform components
- Application encryption keys used to protect credential and configuration data at rest
- Configuration files for each Ansible Automation Platform component
- Data files for each Ansible Automation Platform component

The restore playbook selectively restores application encryption keys so that each component can decrypt its database content after the restore. If encryption keys are not restored from the same backup, components cannot read their stored credentials.

### Data not restored by the restore playbook

The restore playbook does not restore the following, which are created or managed by the installation playbook:

- **Database connection secrets**: Podman secrets that store database hostnames, port numbers, and user credentials are not restored. These values are environment-specific and must match the target environment's database configuration. Do not delete these secrets before running the restore playbook.
- **TLS certificates and private keys**: TLS certificates and private keys are not restored from the backup. The certificates and keys from the target installation remain in place after the restore.
- **Platform service configuration**: Configuration files generated by the installation playbook during installation, such as service settings and proxy configuration, are not restored.
- **Inventory file**: The inventory file is not included in the backup archive. You must preserve your inventory file independently. The installation playbook uses the inventory file to configure the target environment.

Important:

Do not delete database connection secrets or platform service configuration before running the restore playbook. These are created by the installation playbook and are not restored from backup. If they are missing, the restore will not complete successfully, and services cannot connect to their databases after the restore.

## Restore containerized Ansible Automation Platform

Restore your container-based installation of Ansible Automation Platform from a backup, or to a different environment.

### Before you begin

- You have logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.
- You have a backup of your Ansible Automation Platform deployment. For more information, see [Back up containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#backing-up-containerized-ansible-automation-platform "Perform a backup of your container-based installation of Ansible Automation Platform.").
- The target environment has a successful installation of Ansible Automation Platform with the same topology as the source environment. Note:
  The restore playbook restores data to a working installation. It does not recreate platform services, secrets, or PostgreSQL connection credentials. If the target environment has not been installed or has installation errors, run the installation playbook before running the restore playbook.

- You have ensured that the administrator credentials on the target environment match the administrator credentials from the source environment.
- If restoring to a different environment with the same hostnames, you have performed a fresh installation on the target environment with the same topology as the original (source) environment.
- If your deployment uses an external PostgreSQL database, one of the following conditions is true:
  * You have configured `postgresql_admin_username` and `postgresql_admin_password` in your inventory file. The restore playbook uses these credentials to grant the `CREATEDB` privilege to the application database users before the restore operation and revoke the privilege afterward.
  * You have ensured that the application database users, such as `gateway_pg_username` or `controller_pg_username`, have the `CREATEDB` privilege on the external PostgreSQL instance.
  Important:
  If your external PostgreSQL database uses high availability or streaming replication, you must close all replica connections to the platform databases before running the restore playbook. Open replica connections prevent the restore playbook from dropping the platform databases. Consult your database provider's documentation to suspend replica synchronization and terminate active connections to the platform databases. After the restore completes, verify that replicas have resynchronized with the restored primary before restarting Ansible Automation Platform services.

### About this task

Note:

When restoring Ansible Automation Platform, use the latest installation program available at the time of the restore. Use the latest installer for the same Ansible Automation Platform version as the backup.

Restore functionality only works with the PostgreSQL versions supported by your current Ansible Automation Platform version. For more information, see [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_cont_aap_system_requirements "Use this information when planning your installation of containerized Ansible Automation Platform.").

For the lowest-risk restore outcome, upgrade the source environment to the same async release as the target before taking a backup. Restoring a backup from an earlier async release onto a later async release is possible but may encounter unexpected behavior if schema or configuration changes were introduced in the intervening releases.

### Procedure

1. Go to the installation directory on your Red Hat Enterprise Linux host.
2. Run the restore playbook for your environment:

  - If you are restoring to the same environment with the same hostnames, run the `restore` playbook:

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.restore
```

        The restore playbook restores the following:

    * PostgreSQL databases
    * Configuration files
    * Data files
    * Podman secrets for application credentials and encryption keys

        By default, the backup directory is set to `./backups`. You can change this by using the `backup_dir` variable in your `inventory` file.

    Important:
            The restore playbook does not restore database connection secrets. These secrets store the connection configuration used by each component to connect to its database. Restoring them from a backup could configure services to connect to a database server from the source environment, which might not be accessible from the restored environment.

        If a database connection secret is missing on an existing installation, rerun the installation playbook to recreate it:

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.installcontext
```

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

### What to do next

If you are using an external PostgreSQL database and manually granted the `CREATEDB` privilege to your application database users before the restore, revoke the privilege after the restore completes. Run the following command for each component, where *<username>* is the value of the corresponding `*_pg_username` variable in your inventory file:

```
ALTER USER *<username>* NOCREATEDB;
```

If you used `postgresql_admin_username` and `postgresql_admin_password` in your inventory file, the restore playbook revokes the privilege automatically and no further action is required.

## Skip database restore when using an external database

If your Ansible Automation Platform deployment uses an external database, and you are restoring the database separately through your database provider or a third-party tool, you can skip database restore operations by using the `postgresql_skip_data` variable.

### About this task

You must set `postgresql_skip_data` to `true` if no database dump file exists in the backup archive, for example if you used `postgresql_skip_data` during backup. If the restore playbook cannot find a database dump file and `postgresql_skip_data` is not set, the playbook fails.

Important:

Restore your external PostgreSQL database before running the restore playbook. The restore playbook starts all Ansible Automation Platform services immediately after restoring configuration files. If the database is not yet restored when services start, the services cannot connect to a valid database.

### Procedure

1. Restore your PostgreSQL database using your external database provider's tools or a third-party restore solution.
2. Add the `postgresql_skip_data` variable to your inventory file:
  

```
postgresql_skip_data=true
```

3. Run the `restore` playbook:
  

```
$ ansible-playbook -i <path_to_inventory>
  ansible.containerized_installer.restore
```

    The restore playbook restores configuration files and data files and skips database restore operations.

## Recover from a broken or degraded environment

If your containerized Ansible Automation Platform deployment is broken or degraded, rerun the installation playbook as a first recovery step before deciding to uninstall and restore from backup.

### About this task

When your environment is broken or degraded, choose a recovery approach based on whether users are active in the environment:

- **In-place recovery**: Attempt in-place repair by rerunning the installation playbook. Reinstall only if rerunning the playbook does not resolve the issue. Use this approach when users are not actively working in the environment.
- **Restore to separate infrastructure**: Perform a fresh installation on new hosts and restore your data from a backup. Use this approach when users are active in the broken environment, because continued use of a degraded environment can corrupt data. For more information, see [Restore containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#proc-restore-aap-container "Restore your container-based installation of Ansible Automation Platform from a backup, or to a different environment.").

Important:

Where possible, use a backup that was taken before the environment became broken. A backup taken from a broken or degraded environment might contain the same data or configuration that caused the breakage, and restoring it can reproduce the original problem.

### Procedure

1. Go to the Red Hat Ansible Automation Platform installation directory on your Red Hat Enterprise Linux host.
2. Run the installation playbook:
  

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.install
```

3. Verify that the environment is stable and accessible.
      If the environment is stable, no further action is required. A restore is not needed unless data loss occurred.

4. If the environment is still broken, run the uninstall playbook:
  

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.uninstall
```

5. Run the installation playbook:
  

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.install
```

6. Run the restore playbook:
  

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.restore
```

    For more information about restore prerequisites and procedures, see [Restore containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#proc-restore-aap-container "Restore your container-based installation of Ansible Automation Platform from a backup, or to a different environment.").

## Back up and restore metrics service

Back up and restore the metrics service database and configuration to recover from hardware failures, data corruption, or operational errors without losing historical metrics data.

### About this task

For **Ansible Automation Platform 2.7** (base metrics service without dashboard), no backup retention policy is required. Base metrics service does not contain user-visible data that needs backup or retention.

**When dashboard becomes GA:** Define retention based on dashboard data retention requirements (90 days default) and customer compliance requirements.

**Installer-provided backup script:** The Ansible Automation Platform containerized installer includes backup.yml and restore.yml playbooks that handle backup and restore operations for metrics service.

### Procedure

1. Backup procedure
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

2. Restore procedure
  
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
