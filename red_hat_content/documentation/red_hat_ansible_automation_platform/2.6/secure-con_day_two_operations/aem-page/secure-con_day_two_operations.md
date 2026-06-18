+++
template = "docs/aem-title.html"
title = "RBAC security considerations for day two operations - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_day_two_operations"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_day_two_operations/aem-page/secure-con_day_two_operations.html"
last_crumb = "RBAC security considerations for day two operations"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "RBAC security considerations for day two operations"
oversized = "false"
page_slug = "secure-con_day_two_operations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-con_day_two_operations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_day_two_operations/toc/toc.json"
type = "aem-page"
+++

# RBAC security considerations for day two operations

Day 2 Operations include Cluster Health and Scaling Checks, including Host, Project, and environment level Sustainment. You must continually analyze configuration and security drift.

## RBAC considerations

Delegate access to resources and centralize credential management using Role-Based Access Controls (RBAC) in platform gateway. This helps ensure users can securely utilize secrets without exposure, increasing security and streamlining platform management.

RBAC is the practice of granting roles to users or teams. RBAC is easiest to think of in terms of Roles which define precisely who or what can see, change, or delete an “object” for which a specific capability is being set.

There are a few main concepts that you should become familiar with regarding Ansible Automation Platform’s RBAC design–roles, resources, and users. Users can be members of a role, which gives them certain access to any resources associated with that role, or any resources associated with “descendant” roles.

A role is essentially a collection of capabilities. Users are granted access to these capabilities and automation controller’s resources through the roles to which they are assigned or through roles inherited through the role hierarchy.

Roles associate a group of capabilities with a group of users. All capabilities are derived from membership within a role. Users receive capabilities only through the roles to which they are assigned or through roles they inherit through the role hierarchy. All members of a role have all capabilities granted to that role. Within an organization, roles are relatively stable, while users and capabilities are both numerous and may change rapidly. Users can have many roles.

The following is an example of an organization with roles and resource permissions:

*Figure 1. RBAC role scopes within automation controller*

![Reference architecture for an example of an organization with roles and resource permissions.](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/aap_ref_arch_2-4-1.png)

User access is based on managing permissions to system objects (users, groups, namespaces) rather than by assigning permissions individually to specific users. You can assign permissions to the groups you create. You can then assign users to these groups. This means that each user in a group has the permissions assigned to that group.

Teams created in automation hub can range from system administrators responsible for governing internal collections, configuring user access, and repository management to groups with access to organize and upload internally developed content to automation hub.

View-only access can be enabled for further lockdown of the private automation hub. By enabling view-only access, you can grant access for users to view collections or namespaces on your private automation hub without the need for them to log in. View-only access allows you to share content with unauthorized users while restricting their ability to only view or download source code, without permissions to edit anything on your private automation hub. Enable view-only access for your private automation hub by editing the inventory file found on your Red Hat Ansible Automation Platform installer.
