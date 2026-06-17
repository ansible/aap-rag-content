+++
title = "Migration process overview - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/migrate-con_migration_process_overview"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/migrate-con_migration_process_overview/", "Migration process overview"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/migrate-con_migration_process_overview/aem-page/migrate-con_migration_process_overview.html"
last_crumb = "Migration process overview"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Migration process overview"
oversized = "false"
page_slug = "migrate-con_migration_process_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/migrate-con_migration_process_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/migrate-con_migration_process_overview/toc/toc.json"
type = "aem-page"
+++

# Migration process overview

Understand the complete migration workflow including preparation, export, artifact creation, import, reconciliation, and validation steps for moving between Ansible Automation Platform installation types.

Important:

You can only migrate to a different installation type of the same Ansible Automation Platform version. For example, you can migrate from RPM version 2.6 to containerized 2.6, but not from RPM version 2.4 to containerized 2.6.

The migration between Ansible Automation Platform installation types follows this general workflow:

1. Prepare and assess the source environment
2. Export the source environment
3. Create and verify the migration artifact
4. Prepare and assess the target environment
5. Import the migration content to the target environment
6. Reconcile the target environment post-import
7. Validate the target environment
