+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_backup_restore"
template = "docs/aem-title.html"
title = "Back up and restore data - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade/", "Upgrade the Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_backup_restore/aem-page/install-proc_self_service_rhel_backup_restore.html"
last_crumb = "Back up and restore data"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Back up and restore data"
oversized = "false"
page_slug = "install-proc_self_service_rhel_backup_restore"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_backup_restore"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_backup_restore/toc/toc.json"
type = "aem-page"
+++

# Back up and restore data

Use the built-in backup tool to create and restore backups of the database, configuration, and SSL certificates for the Ansible automation portal RHEL appliance.

## About this task

Important:

Backups contain credentials in plain text. Restrict file permissions on backup archives. Encrypt archives before transferring to remote storage:

```terminal
$ gpg --symmetric --cipher-algo AES256 /var/lib/portal/backups/*backup-file*.tar.gz
```

## Procedure

Create a backup

1.  Run the backup tool:
  

```terminal
$ sudo portal-backup
```

2.  Select a backup type from the menu. Select option 1 to create a backup with recommended defaults.
  

```
Portal Backup Tool
==================
1) Full backup (config + database + secrets) [recommended]
2) Config only (config + secrets, no database)
3) Database only

    Select backup type [1]: 1

    Creating backup...
  Backing up configuration... done
  Backing up secrets... done
  Backing up database... done

    Backup created: /var/lib/portal/backups/portal-backup-2026-05-07-143022.tar.gz
```
      Backups are stored in /var/lib/portal/backups/ as .tar.gz files.

Preview a backup

3.  Preview the contents of the most recent backup without restoring:
  

```terminal
$ sudo portal-restore --latest --dry-run
```

Restore from backup

4.  Restore the most recent backup:
  

```terminal
$ sudo portal-restore --latest
```
  

```
Portal Restore Tool
===================
Restoring from: /var/lib/portal/backups/portal-backup-2026-05-07-143022.tar.gz

    Stopping services...
  Restoring configuration... done
  Restoring secrets... done
  Restoring database... done
Starting services...

    Restore complete.
```
      Services stop during restore and restart automatically.
