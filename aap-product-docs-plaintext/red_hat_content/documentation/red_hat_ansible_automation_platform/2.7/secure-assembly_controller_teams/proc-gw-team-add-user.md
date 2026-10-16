# Bulk-assign roles to users with teams
## Assign users to a team

To assign a user to a team, the user must already have been created. For more information, see [Creating a user](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_users#proc-controller-creating-a-user "You can create three types of users in Ansible Automation Platform:"). Assigning a user to a team adds them as a member only. Use the **Roles** tab to assign a role that gives users on the team resource access.

### About this task

New user memberships to a team must be added at the platform level.

Important:

Assigning a user to a team does not make the user a member of the team's organization. To grant organization-level access, you must also add the user to the organization separately. For more information, see [Assign a user to an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_controller_access_organizations#proc-controller-add-organization-user "You can give a user with access to an organization, and therefore the resources within the organization, by assigning them to the organization and managing the organization roles associated with the user.").

### Procedure

1. From the navigation panel, select Access Management> (and then)Teams.
2. Select the team to which you want to add users.
3. Select the **Users** tab.
4. Select one or more users from the list by clicking the checkbox next to the name to add them as members of this team.
5. Click Add users.

