+++
title = "Manage user access to resources - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_resources"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_access/", "Manage access with role-based access control"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_resources/aem-page/secure-assembly_gw_resources.html"
last_crumb = "Manage user access to resources"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Manage user access to resources"
oversized = "false"
page_slug = "secure-assembly_gw_resources"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_resources"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_resources/toc/toc.json"
type = "aem-page"
+++

# Manage user access to resources

Manage user access to Ansible Automation Platform resources via directly assigned or team-inherited roles. Resources vary by function, such as job templates and projects for automation execution, or decision environments and rulebook activations for automation decisions.

## Provide team access to a resource

You can grant users access based on their team membership. When you add a user as a member of a team, they inherit access to the roles and resources defined for that team.

### About this task

 Note:

Direct team access cannot be granted to Automation Content> (and then)Remote Registries resources.

### Procedure

1.  From the navigation panel, click the name of the resource that you want to give a team access to. For example, Automation Execution> (and then)Templates.
2.  On the details page, select the **Team Access** tab.
3.  Click Assign Teams.
4.  Click the checkbox beside the team to assign that team access to your chosen resource and click Next.
5.  Select the roles you want applied to the team for the chosen resource and click Next.
6.  Review the settings and click Finish. The Assign Teams dialog displays indicating whether the role assignments were successfully applied.
7.  You can remove resource access for a team by selecting the **Remove team** icon next to the team. This launches a confirmation dialog, asking you to confirm the removal.

## Provide direct user access to a resource

You can directly grant users access to resources, and edit their access after it has been granted.

### About this task

 Note:

Direct user access cannot be granted to Automation Content> (and then)Remote Registries resources.

### Procedure

1.  From the navigation panel, select a resource that you want to give a team access to. For example, Automation Execution> (and then)Templates.
2.  Select the **User access** tab.
3.  Click Assign users.
4.  Click the checkbox beside the user to assign that user to your chosen resource and click Next.
5.  Select the roles you want applied to the user for the chosen resource and click Next.
6.  Review the settings and click Finish. The Assign Roles dialog displays indicating whether the role assignments were successfully applied.
7.  You can edit a user’s access to a resource from the **User Access** tab by clicking the pencil icon ![Edit page](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png) next to the user’s name and adding or removing directly-assigned roles.
8.  You can remove resource access for a user by selecting the **Remove role** icon next to the user. This launches a confirmation dialog asking you to confirm the removal.
