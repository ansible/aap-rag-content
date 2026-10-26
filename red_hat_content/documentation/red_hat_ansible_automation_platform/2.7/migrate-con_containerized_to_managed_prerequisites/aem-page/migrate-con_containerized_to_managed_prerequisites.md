+++
title = "Containerized to Managed Ansible Automation Platform migration prerequisites - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-con_containerized_to_managed_prerequisites"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_migration_prerequisites/", "Migration prerequisites"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-con_containerized_to_managed_prerequisites/aem-page/migrate-con_containerized_to_managed_prerequisites.html"
last_crumb = "Containerized to Managed Ansible Automation Platform migration prerequisites"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Containerized to Managed Ansible Automation Platform migration prerequisites"
oversized = "false"
page_slug = "migrate-con_containerized_to_managed_prerequisites"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-con_containerized_to_managed_prerequisites"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-con_containerized_to_managed_prerequisites/toc/toc.json"
type = "aem-page"
+++

# Containerized to Managed Ansible Automation Platform migration prerequisites

Before migrating from a container-based deployment to a Managed Ansible Automation Platform deployment, ensure that you meet the following prerequisites:

- You have a source container-based deployment of Ansible Automation Platform.
- The source deployment is on the latest release of the Ansible Automation Platform version you are on.
- You have a target Managed Ansible Automation Platform deployment.
- You have enabled local authentication on the source deployment before the migration.
- A local administrator account must be functional on the source deployment before migration. Verify this by performing a successful login to the source deployment.
- You have a plan to retain a backup throughout the migration process and to ensure that your existing Ansible Automation Platform deployment remains active until your migration has completed successfully.
- You have a plan for any environment changes based on the migration from a self-hosted Ansible Automation Platform deployment to a Managed Ansible Automation Platform deployment:
  * Job log retention changes from a customer-configured option to 30 days.
  * Network changes occur when moving the control plane to the managed service.
  * Automation mesh requires reconfiguration.
- You must reconfigure or re-create Single Sign-On (SSO) identity providers post-migration to account for URL changes.
