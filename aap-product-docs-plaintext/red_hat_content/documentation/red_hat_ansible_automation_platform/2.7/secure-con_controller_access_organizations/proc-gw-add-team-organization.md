# Manage access to organizations
## Assigning a team to an organization

Give a team access to an organization by assigning roles to the team in the organization's **Teams** tab. Team role assignments do not automatically grant organization membership to team members.

### About this task

To assign roles to a team, the team must already exist in the organization. For more information, see [Creating a team](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-controller-creating-a-team "Manage teams by creating them, assigning an organization, and adding users or administrators. Team members inherit all assigned roles and permissions assigned to the team. Users must exist before they can be added."). To assign roles for a team, the role must already exist. See [Creating a role](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_roles#proc-gw-create-roles "Ansible Automation Platform services provide a set of predefined roles with permissions enough for standard automation tasks. It is also possible to configure custom roles that define access permissions to a resource.") for more information.

Users who are members of a team can exercise the team's assigned roles on organization resources. However, some operations, such as creating resources within the organization, require explicit organization membership in addition to team role assignments.

Important:

To ensure that team members can perform all operations granted by their team roles, verify that each user is also a member of the organization. For more information, see [Assign a user to an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_controller_access_organizations#proc-controller-add-organization-user "You can give a user with access to an organization, and therefore the resources within the organization, by assigning them to the organization and managing the organization roles associated with the user.").

### Procedure

1. From the navigation panel, select Access Management> (and then)Organizations.
2. From the Organizations list view, select the organization to which you want to assign team access.
3. Click the **Teams** tab. If no teams exist, click Create team to create a team and assign it to this organization.
4. Click Assign roles.
5. Select the roles you want the selected team to have. Scroll down for a complete list of roles. Note:
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

6. Click Next to review the roles settings.
7. Click Finish to apply the roles to the selected teams. The Assign roles dialog displays the updated roles assigned for each team.
8. Click Close. Note:
A team with associated roles retains them if they are reassigned to another organization.

9. To manage roles for teams in an organization, click the **⚙** icon next to the user and select **Manage roles**.

