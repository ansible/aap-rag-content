+++
title = "Identity and access management migration during upgrade - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_upgrade_data_movement"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_upgrade_data_movement/aem-page/assembly_upgrade_data_movement.html"
last_crumb = "Identity and access management migration during upgrade"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Identity and access management migration during upgrade"
oversized = "false"
page_slug = "assembly_upgrade_data_movement"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/assembly_upgrade_data_movement"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_upgrade_data_movement/toc/toc.json"
type = "aem-page"
+++

# Identity and access management migration during upgrade

When upgrading from a version of Ansible Automation Platform that predates the platform gateway, Identity Access Management (IAM) data, including users, teams, organizations, their memberships, and associated roles, is migrated from automation controller and automation hub to platform gateway.

This migration establishes automation controller as the primary source of IAM data for platform gateway, ensuring continuity of user memberships and appropriate platform-level role assignments.

Note:

If your current version is more than one minor release behind the target version, upgrade directly to the target version rather than performing intermediate upgrades. A direct upgrade is less complex.
