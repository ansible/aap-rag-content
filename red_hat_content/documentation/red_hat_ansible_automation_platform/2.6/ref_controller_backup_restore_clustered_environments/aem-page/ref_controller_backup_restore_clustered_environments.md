+++
title = "Backup and restore in clustered environments - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/ref_controller_backup_restore_clustered_environments"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/ref_controller_backup_restore_clustered_environments/aem-page/ref_controller_backup_restore_clustered_environments.html"
last_crumb = "Backup and restore in clustered environments"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Backup and restore in clustered environments"
oversized = "false"
page_slug = "ref_controller_backup_restore_clustered_environments"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/ref_controller_backup_restore_clustered_environments"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/ref_controller_backup_restore_clustered_environments/toc/toc.json"
type = "aem-page"
+++

# Backup and restore in clustered environments

Learn how to back up and restore automation controller in a clustered environment.

The procedure for backup and restore for a clustered environment is similar to a single install, except for some of the following considerations:

- If restoring to a new cluster, ensure that the old cluster is shut down before proceeding because they can conflict with each other when accessing the database.
- Per-node backups are only restored to nodes bearing the same hostname as the backup.
- When restoring to an existing cluster, the restore has the following:
  * A dump of the PostgreSQL database
  * UI artifacts, included in the database dump
  * An automation controller configuration (retrieved from `/etc/tower`)
  * An automation controller secret key
  * Manual projects
