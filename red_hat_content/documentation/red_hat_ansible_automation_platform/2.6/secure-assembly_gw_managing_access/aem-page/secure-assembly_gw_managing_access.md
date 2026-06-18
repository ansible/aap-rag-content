+++
title = "Manage access with role-based access control - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_managing_access"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_managing_access/", "Manage access with role-based access control"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_managing_access/aem-page/secure-assembly_gw_managing_access.html"
last_crumb = "Manage access with role-based access control"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Manage access with role-based access control"
oversized = "false"
page_slug = "secure-assembly_gw_managing_access"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_managing_access"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_managing_access/toc/toc.json"
type = "aem-page"
+++

# Manage access with role-based access control

Role-based access control (RBAC) restricts user access based on the user’s role within the organization they are assigned to in Ansible Automation Platform. The roles in RBAC refer to the levels of access that users have to Ansible Automation Platform components and resources.

You can control what users can do with the components of Ansible Automation Platform at a broad or granular level depending on your RBAC policy. You can choose whether the user is a system administrator or normal user and align roles and access permissions with their positions within the organization.

You can define roles with multiple permissions that can then be assigned to resources, teams, and users. The permissions that make up a role govern what the assigned role allows. Permissions are allocated with only the access needed for a user to perform the tasks appropriate for their role.

Important:

When managing users, teams, and organizations, use the Unified UI or the platform gateway API to ensure real-time synchronization across all platform components, including Event-Driven Ansible controller. If you use the legacy automation controller API, changes can take up to 15 minutes to propagate to Event-Driven Ansible controller, which can result in authentication errors for new users or teams.
