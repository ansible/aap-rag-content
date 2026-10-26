+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_initial_rbac_setup"
title = "Set up initial RBAC rules in Ansible automation portal - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_self_service_initial_rbac_setup/aem-page/install-con_self_service_initial_rbac_setup.html"
last_crumb = "Set up initial RBAC rules in Ansible automation portal"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Set up initial RBAC rules in Ansible automation portal"
oversized = "false"
page_slug = "install-con_self_service_initial_rbac_setup"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-con_self_service_initial_rbac_setup"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_self_service_initial_rbac_setup/toc/toc.json"
type = "aem-page"
+++

# Set up initial RBAC rules in Ansible automation portal

After you install Ansible automation portal and synchronize it with Ansible Automation Platform, only users with Ansible Automation Platform administrator privileges can view the auto-generated templates.

You must configure initial Role-Based Access Control (RBAC) permissions to allow non-admin users to view and execute synchronized Ansible Automation Platform job templates.

For the complete RBAC configuration procedure, including navigation permissions required for non-admin users to access portal pages, see the external reference *Configure role-based access control for Ansible automation portal*.

Important:

Role-Based Access Control (RBAC) differs by template type:

- **Auto-generated templates:** Permissions are synchronized from Ansible Automation Platform. Users must have permissions on the underlying Ansible Automation Platform job template.
- **Custom templates:** Permissions must be explicitly configured within the Ansible Automation Portal. Users must also have permissions to run the associated job templates in Ansible Automation Platform.
