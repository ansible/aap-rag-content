# Bulk-assign roles to users with teams
## Create a team

Manage teams by creating them, assigning an organization, and adding [users](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-gw-team-add-user "To assign a user to a team, the user must already have been created. For more information, see Creating a user. Assigning a user to a team adds them as a member only. Use the Roles tab to assign a role that gives users on the team resource access.") or [administrators](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-gw-add-admin-team "Assign existing users as administrators to a team so they can manage its membership and settings. This allows designated administrators to create new users and grant permissions within the team."). Team members inherit all assigned roles and permissions assigned to the team. Users must exist before they can be added.

### Procedure

1. From the navigation panel, select Access Management> (and then)Teams.
2. Click Create team.
3. Enter a **Name** and optionally give a **Description** for the team.
4. Select an **Organization** to be associated with this team. Note:
Each team can only be assigned to one organization.

Adding a user to a team does not automatically grant the user membership in the team's organization. If users require organization-level access, add them to the organization separately. For more information, see [Assign a user to an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_controller_access_organizations#proc-controller-add-organization-user "You can give a user with access to an organization, and therefore the resources within the organization, by assigning them to the organization and managing the organization roles associated with the user.").

5. Click Create team. The **Details** page opens, where you can review and edit your team information and access.

