+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-back_up_and_restore_your_rpm_deployment"
title = "Back up and restore your RPM deployment - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-back_up_and_restore_your_rpm_deployment/", "Back up and restore your RPM deployment"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-back_up_and_restore_your_rpm_deployment/aem-page/administer-back_up_and_restore_your_rpm_deployment.html"
last_crumb = "Back up and restore your RPM deployment"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Back up and restore your RPM deployment"
oversized = "false"
page_slug = "administer-back_up_and_restore_your_rpm_deployment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-back_up_and_restore_your_rpm_deployment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-back_up_and_restore_your_rpm_deployment/toc/toc.json"
type = "aem-page"
+++

# Back up and restore your RPM deployment

Protecting your Ansible Automation Platform RPM deployment ensures that you can recover from system failures, data corruption, or configuration errors. Regular backups minimize downtime and protect your configurations and data.

Implementing backup and restore procedures helps you to:

- **Protect critical automation assets**: Safeguard your data including configurations, inventory, credentials, and job history from unexpected failures or data loss.
- **Enable disaster recovery**: Restore your environment quickly after hardware failures or other unexpected events to maintain business continuity.
- **Support testing and development**: Create copies of your environment for testing upgrades or configuration changes without affecting production systems.

## Considerations for back up and restore

Consider the following points when you back up and restore your system:

Disk space
Review your disk space requirements to ensure you have enough room to backup configuration files, keys, other relevant files, and the database of the Ansible Automation Platform installation.

Important:

Database backup files can be significantly larger than the reported size because the backup process creates a logical dump that represents data differently than the live database. There is no reliable formula for predicting backup size, so ensure that you have sufficient storage available before running a backup. To reduce backup size, see the compression options described in [Back up the platform using automation installer](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-back_up_and_restore_your_rpm_deployment#GUID-4df8407e-ca4a-43ea-9d72-4bc154398a3c "Run the setup script to create a verified archive of your platform database, configurations, and secrets. This ensures your instance is captured in a compatible format for reliable restoration during a system failure or migration.").

Note:

The Ansible Automation Platform database backups are staged on each node at `/var/backups/automation-platform` through the variable `backup_dir`. You might need to mount a new volume to `/var/backups` or change the staging location with the variable `backup_dir` to prevent issues with disk space before running the `./setup.sh -b` script.

System credentials
Confirm you have the required system credentials when working with a local database or a remote database. On local systems, you might need `root` or `sudo` access, depending on how credentials are set up. On remote systems, you might need different credentials to grant you access to the remote system you are trying to backup or restore.

Version
You must always use the most recent minor version of a release to backup or restore your Ansible Automation Platform installation version. For example, if the current platform version you are on is 2.0.x, only use the latest 2.0 installer.

Backup file location
- **Default location:** If the backup file is placed in the same directory as the `./setup.sh` installer, the restore playbook locates it automatically.
- **Non-default location:** If your backup file is stored in a different directory, you must specify the path using the `restore_backup_file` extra variable when running the restore command.

## Back up the Ansible Automation Platform

Back up your instance using the `setup.sh` script to save your environment content and configuration. Use the optional `backup_dest` flag only to change the default save location. Apply compression flags to reduce artifact size before transmission.

### Backup playbook

The Ansible Automation Platform installer (`install.yml`) includes the `backup.yml `playbook, which automates the backup and restoration of your environment. You can use this playbook to capture critical configuration data and databases for the following components:

- Platform gateway:
  * The database
  * The `SECRET_KEY` file
- Automation controller:
  * The database
  * The `SECRET_KEY` file
  * The `RESOURCE_SERVER` key
  * The per-host custom configuration files
- Automation hub:
  * The database
  * The `database_fields.symmetric.key` file
  * The `SECRET_KEY` file
  * The `RESOURCE_SERVER` key
  * Automation hub pulp content
- Event-Driven Ansible controller:
  * The database
  * The `SECRET_KEY` file
  * The `RESOURCE_SERVER` key

### Back up the platform using automation installer

Run the setup script to create a verified archive of your platform database, configurations, and secrets. This ensures your instance is captured in a compatible format for reliable restoration during a system failure or migration.

#### Procedure

1.  Navigate to your Ansible Automation Platform installation directory.
2.  Run the `./setup.sh` script as in the following example:
  

```
$ ./setup.sh -e 'backup_dest=/ansible/mybackup' -e
'use_archive_compression=true' 'use_db_compression=true @credentials.yml -b
```
  Where:
  - `backup_dest`: Specifies a directory to save your backup to.
  - `backup_dir`: Specifies the directory used on the host staging backup files before they are transferred to `backup_dest` locally.
  - `use_archive_compression=true` and `use_db_compression=true`: Compresses the backup artifacts before they are sent to the host running the backup operation.
  You can use the following variables to customize the compression:
  - `use_archive_compression=true`: For global control of compression for filesystem related backup files.
  - `<componentName>_use_archive_compression`: For component-level control of compression for filesystem related backup files.
  - `use_db_compression=true`: For global control of compression for database related backup files.
  - `<componentName>_use_db_compression=true`: For component-level control of compression for database related backup files.

#### Results

After a successful backup, a backup file is created at `/ansible/mybackup/automation-platform-backup-<date/time>.tar.gz``.

## Restore Ansible Automation Platform

Restoring your instance using the `setup.sh script` helps you safely reinstate your environment content and configuration. Use the optional `restore_backup_file` flag *only* to change the `TAR` file location.

### Restore playbook

Automation controller includes playbooks to backup and restore your installation.

In addition to the `install.yml` file included with your `setup.sh` setup playbook, there are also `restore.yml` files. The restore backup restores the backed up files and data to a freshly installed and working second instance of automation controller.

When restoring your system, installation program checks to see that the backup file exists before beginning the restoration. If the backup file is not available, your restoration fails.

Note:

Make sure that your automation controller hosts are properly set up with SSH keys, user or pass variables in the hosts file, and that the user has `sudo` access.

### Restore the platform to its original state

Restore your environment by running the setup.sh script to recover platform data and configurations. Ensure the backup `TAR` file is available in the default location, or use the optional `restore_backup_file` flag to specify a custom path before starting.

#### Procedure

1.  Navigate to your Ansible Automation Platform installation directory.
2.  Run the `./setup.sh script`:
  `root@localhost:~# ./setup.sh -e 'restore_backup_file=/path/to/nondefault/backup.tar.gz' -r`  

    Where:

    `restore_backup_file`: Path to the `TAR` file used for the platform restore.
