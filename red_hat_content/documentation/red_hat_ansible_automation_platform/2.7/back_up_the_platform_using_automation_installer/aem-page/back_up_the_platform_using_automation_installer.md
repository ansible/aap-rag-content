+++
title = "Back up the platform using automation installer - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/back_up_the_platform_using_automation_installer"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/back_up_the_platform_using_automation_installer/aem-page/back_up_the_platform_using_automation_installer.html"
last_crumb = "Back up the platform using automation installer"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Back up the platform using automation installer"
oversized = "false"
page_slug = "back_up_the_platform_using_automation_installer"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/back_up_the_platform_using_automation_installer"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/back_up_the_platform_using_automation_installer/toc/toc.json"
type = "aem-page"
+++

# Back up the platform using automation installer

Run the setup script to create a verified archive of your platform database, configurations, and secrets. This ensures your instance is captured in a compatible format for reliable restoration during a system failure or migration.

## Procedure

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

## Results

After a successful backup, a backup file is created at `/ansible/mybackup/automation-platform-backup-<date/time>.tar.gz``.
