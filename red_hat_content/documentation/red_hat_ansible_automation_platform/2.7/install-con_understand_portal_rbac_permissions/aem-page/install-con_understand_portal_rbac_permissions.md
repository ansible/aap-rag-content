+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_understand_portal_rbac_permissions"
title = "Understand the permission model - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_understand_portal_rbac_permissions/aem-page/install-con_understand_portal_rbac_permissions.html"
last_crumb = "Understand the permission model"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Understand the permission model"
oversized = "false"
page_slug = "install-con_understand_portal_rbac_permissions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-con_understand_portal_rbac_permissions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_understand_portal_rbac_permissions/toc/toc.json"
type = "aem-page"
+++

# Understand the permission model

Ansible automation portal and Ansible Automation Platform use separate but related permission systems. Ansible Automation Platform RBAC is the source of truth for synchronization scope and execution permissions.

 **Ansible automation portal RBAC:**

- Controls which users can view templates in the Ansible automation portal catalog and submit jobs.
- Controls navigation permissions that determine which sidebar items and feature pages (such as the execution environment builder or administration menus) are visible to users.
- Maps portal roles to synchronized Ansible Automation Platform teams and users.

 **Ansible Automation Platform RBAC:**

- **Controls synchronization scope:** Only Ansible Automation Platform job templates accessible by the configured API token are synchronized to Ansible automation portal.
- **Controls auto-generated template visibility:** Ansible Automation Platform permissions determine whether authenticated users can view and execute auto-generated templates in Ansible automation portal. Custom templates are not filtered by Ansible Automation Platform permissions.
- **Validates execution permissions:** When an Ansible automation portal user executes a template, Ansible Automation Platform checks that user’s execute permissions before launching the job.

Note:

If a user can see an Ansible automation portal template in the catalog but lacks Ansible Automation Platform execution permissions for the associated job template in Ansible Automation Platform, the user cannot run the job.
