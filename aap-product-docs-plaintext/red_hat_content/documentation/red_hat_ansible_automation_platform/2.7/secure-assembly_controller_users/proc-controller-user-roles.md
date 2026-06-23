# View, create, or assign roles to users
## Assign roles to a user

You can grant users granular access to specific resources such as inventories, projects, or job templates by assigning users roles.

### About this task

You can view and manage roles that were assigned directly to a user by an administrator in the user’s **Roles** tab.

You can view roles that a user inherited from a team assignment in the **View indirectly assigned roles** link in the page banner. You cannot directly manage an indirectly-assigned role. You can only manage indirectly-assigned roles by [editing the team’s role assignments](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-controller-user-permissions "You can grant a team granular access to specific resources such as inventories, projects, and job templates by assigning the team roles associated with those particular resources. You can also set permissions at the level of the organization from the Organizations view."), or by [removing the user from the team](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-gw-team-remove-user "You can remove a user from a team from the Team list view.").

Note:

Users cannot be assigned to an organization through role assignment, nor can you assign users organization roles from this screen. Refer to the steps provided in [Adding a user to an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_controller_access_organizations#proc-controller-add-organization-user "You can give a user with access to an organization, and therefore the resources within the organization, by assigning them to the organization and managing the organization roles associated with the user.") for detailed instructions on assigning a user to an organization.

Roles are labeled with their associated Ansible Automation Platform component and function. These components align with Ansible Automation Platform services and the side navigation structure in the user interface. Component labels can be understood as follows:

- **Automation Execution** refers to automation controller
- **Automation Decisions** refers to Event-Driven Ansible
- **Automation Content** refers to automation hub


When assigning roles, ensure that you are selecting the required resource in the correct component context, because resources such as projects and credentials can be associated with both Automation Execution and Automation Decisions.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  From the **Users** list view, click the user to which you want to add roles.
3.  Select the **Roles** tab to display the set of roles assigned to this user. These provide the ability to read, change, and administer resources.
4.  To add new roles, click Add roles.  Note:
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

5.  Select a Resource type and click Next.
6.  Select the resources that you want to give role-based access to and click Next.
7.  Select the roles that will be applied to the resources and click Next.  Tip:
If you are selecting more than one role, consider [creating a custom role](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_roles#proc-gw-create-roles "Ansible Automation Platform services provide a set of predefined roles with permissions enough for standard automation tasks. It is also possible to configure custom roles that define access permissions to a resource.") that includes all the permissions for this resource type so you can give your users the appropriate level of access.

8.  Review the settings and click Finish. The **Add roles** dialog displays indicating whether the role assignments were successfully applied. Click Close to close the dialog.

