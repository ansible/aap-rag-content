# Bulk-assign roles to users with teams

As an administrator, you can use teams to bulk-assign roles to users that need to share the same access.

A team is a subdivision of an organization that groups users and roles together for specific resources. Teams offer a means to implement role-based access control schemes and delegate responsibilities across organizations by allowing you to grant access to users in bulk. For example, you can grant resource access to a team, and therefore to all the users in the team, rather than granting access to each individual user on the team.

You can create as many teams as needed for your organization. Teams can only be assigned to one organization while an organization can be made up of multiple teams. Each team can be assigned roles, the same way roles are assigned for users. Teams can also scalably assign ownership for credentials, preventing multiple interface click-throughs to assign the same credentials to the same user.

## View the Teams list

The **Teams** page displays the existing teams for your installation. From here, you can search for a specific team, filter the list of teams by team name or organization, or change the sort order for the list.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  In the **Search** bar, enter an appropriate keyword for the team you want to search for and click the arrow icon.
3.  From the menu bar, you can sort the list of teams by using the arrows for **Name** and **Organization** to toggle your sorting preference.
4.  You can view team details by clicking a team **Name** on the **Teams** page.
5.  You can view organization details by clicking the link in the **Organization** column.

## Create a team

Manage teams by creating them, assigning an organization, and adding [users](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-gw-team-add-user "To assign a user to a team, the user must already have been created. For more information, see Creating a user. Assigning a user to a team adds them as a member only. Use the Roles tab to assign a role that gives users on the team resource access.") or [administrators](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-gw-add-admin-team "Assign existing users as administrators to a team so they can manage its membership and settings. This allows designated administrators to create new users and grant permissions within the team."). Team members automatically inherit all assigned roles and permissions. Users must exist in the system before they can be added to a team.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  Click Create team.
3.  Enter a **Name** and optionally give a **Description** for the team.
4.  Select an **Organization** to be associated with this team. Note:
Each team can only be assigned to one organization.

5.  Click Create team. The **Details** page opens, where you can review and edit your team information and access.

## Assign users to a team

To assign a user to a team, the user must already have been created. For more information, see [Creating a user](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_users#proc-controller-creating-a-user "You can create three types of users in Ansible Automation Platform:"). Assigning a user to a team adds them as a member only. Use the **Roles** tab to assign a role that gives users on the team resource access.

### About this task

New user memberships to a team must be added at the platform level.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  Select the team to which you want to add users.
3.  Select the **Users** tab.
4.  Select one or more users from the list by clicking the checkbox next to the name to add them as members of this team.
5.  Click Add users.

## Remove users from a team

You can remove a user from a team from the Team list view.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  Select the team from which you want to remove users.
3.  Select the **Users** tab.
4.  Click the **Remove user** icon next to the user you want to remove as a member of the team.
5.  You can delete multiple users by selecting the checkbox next to each user you want to remove, and selecting **Remove selected users** from the **More actions ⋮** list. Note:
If the user is a Team administrator, you can remove their membership to the team from the **Administrators** tab.

6.  A confirmation dialog asking you to confirm the removal will appear. Confirm the removal. Note that removing a user from a team removes all of that team’s role assignments from the user.

## Assign administrators to a team

Assign existing users as administrators to a team so they can manage its membership and settings. This allows designated administrators to create new users and grant permissions within the team.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  Select the team to which you want to add an administrator.
3.  Select the **Administrators** tab and click Add administrator(s).
4.  Select one or more users from the list by clicking the checkbox next to the name to add them as administrators of this team.
5.  Click Add administrators.

## Assign roles to a team

You can grant a team granular access to specific resources such as inventories, projects, and job templates by assigning the team roles associated with those particular resources. You can also set permissions at the level of the organization from the Organizations view.

### About this task

Note:

Teams cannot be assigned to an organization through role assignment, nor can teams be assigned organization roles from the Teams view. Refer to the steps provided in [Adding a team to an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_controller_access_organizations#proc-gw-add-team-organization "You can give a team access to an organization, and to the resources within that organization, by assigning roles to the team in the organization’s Teams tab. All users who are part of a team assigned to the organization will inherit the team’s organization role assignments.") for detailed instructions on assigning a team to an organization.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  Select the team **Name** to which you want to add roles.
3.  Select the **Roles** tab and click Add roles. Note:
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

4.  Select a **Resource type** and click Next.
5.  Select the resources that you want to give the team role-based access to and click Next.
6.  Select the roles to apply to the resources and click Next. Tip:
If you are selecting more than one role in this step, consider [creating a custom role](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_roles#proc-gw-create-roles "Ansible Automation Platform services provide a set of predefined roles with permissions enough for standard automation tasks. It is also possible to configure custom roles that define access permissions to a resource.") that includes all the permissions for this resource type to give the team the correct access.

7.  Review the settings and click Finish.
8.  The **Add roles** dialog displays indicating whether the role assignments were successfully applied. Click Close to close the dialog.

## Remove roles from a team

Remove roles from a team to revoke access to specific Ansible Automation Platform resources. Updating these permissions helps ensure that team members only keep the necessary access for their tasks within the correct component context.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  Select the team **Name** from which you want to remove roles.
3.  Select the **Roles** tab.
4.  To remove a single role, click the minus icon next to the resource and confirm removal on the dialog that is displayed. Note:
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

5.  To remove roles in bulk, select the checkbox next to each resource you want to remove and click **Delete selected roles** from the More Actions**⋮** list on the menu bar, then confirm removal and click **Delete role**.

## Delete a team

Before you can delete a team, you must have team permissions. When you delete a team, the roles that users inherited from that team are revoked.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  To remove a single team, click the minus icon **-** next to the team and confirm removal on the dialog that is displayed.
3.  To remove teams in bulk, select the checkbox next to each team that you want to remove, then click the More Actions**⋮** icon and select **Delete team**.
