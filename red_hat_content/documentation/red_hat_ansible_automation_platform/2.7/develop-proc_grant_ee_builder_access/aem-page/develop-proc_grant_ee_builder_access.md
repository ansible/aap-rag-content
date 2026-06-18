+++
title = "Grant execution environment builder access to a role - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_grant_ee_builder_access"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_permissions/", "Execution environment builder permissions"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_grant_ee_builder_access/aem-page/develop-proc_grant_ee_builder_access.html"
last_crumb = "Grant execution environment builder access to a role"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Grant execution environment builder access to a role"
oversized = "false"
page_slug = "develop-proc_grant_ee_builder_access"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_grant_ee_builder_access"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_grant_ee_builder_access/toc/toc.json"
type = "aem-page"
+++

# Grant execution environment builder access to a role

Enable navigation permissions in the Ansible automation portal RBAC configuration so that non-admin users can access execution environment builder features.

## Before you begin

- You have configured base RBAC roles per [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_configure#rhdh-configure-rbac "Red Hat Developer Hub offers Role-based Access Control (RBAC) functionality. RBAC can then be applied to the Ansible plug-ins content.").
- You have the AAP Administrator role and access to **Administration > RBAC** in automation portal.

## Procedure

1.  In automation portal, navigate to **Administration > RBAC** in the sidebar.
2.  Select an existing role to edit, or click **Create Role** to create a new role (for example, `ee-builder-users`).
3.  In the permissions section, add the execution environment builder permissions.
      For the list of permissions, see [Execution environment builder permissions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_permissions "Execution environment builder uses navigation-level permissions that control which sidebar items and pages are visible to users in Ansible automation portal.").

4.  If creating a new role, assign the role to the appropriate users or groups.
5.  Click **Save**.

## Results

To verify the configuration:

1. Log out and log in as a user assigned to the modified role.
2. Verify that the expected sidebar items are visible based on the permissions you assigned.
3. If you granted full access, navigate to **Execution Environments > Create** and verify that templates are visible and the wizard launches.


To hide execution environment builder from specific user groups, remove these permissions from their assigned roles.
