# Bulk-assign roles to users with teams
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

