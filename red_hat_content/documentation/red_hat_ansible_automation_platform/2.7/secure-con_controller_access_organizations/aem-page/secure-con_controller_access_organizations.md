+++
title = "Manage access to organizations - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_controller_access_organizations"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_access/", "Manage access with role-based access control"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_controller_access_organizations/aem-page/secure-con_controller_access_organizations.html"
last_crumb = "Manage access to organizations"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Manage access to organizations"
oversized = "false"
page_slug = "secure-con_controller_access_organizations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_controller_access_organizations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_controller_access_organizations/toc/toc.json"
type = "aem-page"
+++

# Manage access to organizations

You can manage access to an organization by selecting an organization from the **Organizations** list view and selecting the associated tabs for providing access to users, administrators, or teams.

## Assign a user to an organization

You can give a user with access to an organization, and therefore the resources within the organization, by assigning them to the organization and managing the organization roles associated with the user.

### About this task

You can view a list of users associated with an organization, along with the roles each user is directly assigned, in the organization’s **Users** tab. When you manage a user’s organization roles in the **Users** tab, you can also see how the user was assigned their roles, whether indirectly, through association with a team, or through direct user assignment by an administrator.

 Note:

If a user is assigned a "team member" role, this likely indicates that they have an indirectly-assigned role. To see a user’s indirectly-assigned roles, click the pencil icon ![Edit page](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png) to view and manage roles, and then click the link labeled **View indirectly-assigned organization roles** in the page banner.

To assign a user to an organization, the user must already exist. For more information, see [Creating a user](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_users#proc-controller-creating-a-user "You can create three types of users in Ansible Automation Platform:"). To assign roles to a user, the role must already exist. See [Creating a role](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_roles#proc-gw-create-roles "Ansible Automation Platform services provide a set of predefined roles with permissions enough for standard automation tasks. It is also possible to configure custom roles that define access permissions to a resource.") for more information.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Organizations.
2.  From the **Organizations** list view, select the organization to which you want to add a user.
3.  Click the **Users** tab, then click Assign Users to add users.
4.  Select one or more users from the list by clicking the checkbox next to the name to add them as members.
5.  Click Next.
6.  Select the roles you want the selected user to have. Scroll down for a complete list of roles.  Note:
      Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

7.  Click Next to review the roles settings.
8.  Click Finish to apply the roles to the selected users, and to add them as members. The **Add roles** dialog displays the updated roles assigned for each user.  Note:
      A user with roles associated with an organization loses those roles if they are removed from the organization.

9.  To remove a particular user from the organization, select **Remove user** from the More Actions**⋮** list next to the user. This launches a confirmation dialog, asking you to confirm the removal. Note that removing a user from an organization will also remove all organization roles that the user is indirectly assigned from that specific organization.
10.  To manage roles for users in an organization, click the **⚙** icon next to the user and select **Manage roles**. You can manage organization roles that are directly assigned to a user by selecting or clearing the checkboxes. Double-check the component column to ensure you are selecting the desired role in the correct component context.  Tip:
      From this screen, you can view, but not manage, indirectly-assigned roles that a user has inherited from a team assignment. To view indirectly-assigned roles, along with the team assignment they originated from, click **View indirectly-assigned organization roles** link in the banner beneath the page heading. To manage roles indirectly assigned to a user through a team assignment, [manage that team’s role assignments](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-controller-user-permissions "You can grant a team granular access to specific resources such as inventories, projects, and job templates by assigning the team roles associated with those particular resources. You can also set permissions at the level of the organization from the Organizations view.") or [remove the user from that team](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-gw-team-remove-user "You can remove a user from a team from the Team list view.").

## Assign an administrator to an organization

Assign existing users as administrators to an organization so they can manage its membership and settings. This allows designated administrators to create new users and teams and grant permissions.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Organizations.
2.  From the Organizations list view, select the organization to which you want to add a user, administrator, or team.
3.  Click the **Administrators** tab.
4.  Click Add administrators.
5.  Select the users from the list by clicking the checkbox next to the name to assign the administrator role to them for this organization.
6.  Click Add administrators.
7.  To remove a particular administrator from the organization, select **Remove administrator** from the **More actions ⋮** list next to the administrator name. This launches a confirmation dialog asking you to confirm the removal.  Note:
      If the user has been added as a member to this organization, they will continue to be a member of this organization. However, if they were added to the organization when the administrator assignment was made, they are removed from the organization.

## Assigning a team to an organization

You can give a team access to an organization, and to the resources within that organization, by assigning roles to the team in the organization’s **Teams** tab. All users who are part of a team assigned to the organization will inherit the team’s organization role assignments.

### About this task

To assign roles to a team, the team must already exist in the organization. For more information, see [Creating a team](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-controller-creating-a-team "Manage teams by creating them, assigning an organization, and adding users or administrators. Team members automatically inherit all assigned roles and permissions. Users must exist in the system before they can be added to a team."). To assign roles for a team, the role must already exist. See [Creating a role](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_roles#proc-gw-create-roles "Ansible Automation Platform services provide a set of predefined roles with permissions enough for standard automation tasks. It is also possible to configure custom roles that define access permissions to a resource.") for more information.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Organizations.
2.  From the Organizations list view, select the organization to which you want to assign team access.
3.  Click the **Teams** tab. If no teams exist, click Create team to create a team and assign it to this organization.
4.  Click Assign roles.
5.  Select the roles you want the selected team to have. Scroll down for a complete list of roles.  Note:
      Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

6.  Click Next to review the roles settings.
7.  Click Finish to apply the roles to the selected teams. The Assign roles dialog displays the updated roles assigned for each team.
8.  Click Close.  Note:
      A team with associated roles retains them if they are reassigned to another organization.

9.  To manage roles for teams in an organization, click the **⚙** icon next to the user and select **Manage roles**.

## Delete an organization

Before you can delete an organization, you must be an Organization administrator or System administrator. When you delete an organization, the organization, team, users and resources are permanently removed from Ansible Automation Platform.

### About this task

 Note:

When you try to delete items that are used by other resources, a message is displayed warning you that the deletion might impact other resources and prompts you to confirm the deletion. Some screens contain items that are invalid or have been deleted previously, and will fail to run.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Organizations.
2.  Click the **⋮** icon next to the organization you want removed and select **Delete organization**.
3.  Select the confirmation checkbox and click Delete organizations to proceed with the deletion. Otherwise, click Cancel.  Note:
      You can delete multiple organizations by selecting the checkbox next to each organization you want to remove, and selecting **Delete selected organizations** from the **More actions ⋮** list on the menu bar.
