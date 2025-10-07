# 4. Managing access with role-based access control
## 4.2. Teams
### 4.2.6. Assigning roles to a team




You can grant a team granular access to specific resources such as inventories, projects, and job templates by assigning the team roles associated with those particular resources. You can also set permissions at the level of the organization from the Organizations view.

Note
Teams cannot be assigned to an organization through role assignment, nor can teams be assigned organization roles from the Teams view. Refer to the steps provided in [Adding a team to an organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-gw-add-team-organization) for detailed instructions on assigning a team to an organization.



**Procedure**

1. From the navigation panel, selectAccess Management→Teams.
1. Select the team **Name** to which you want to add roles.
1. Select the **Roles** tab and clickAdd roles.

Note
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).




1. Select a **Resource type** and clickNext.
1. Select the resources that you want to give the team role-based access to and clickNext.
1. Select the roles to apply to the resources and clickNext.

Tip
If you are selecting more than one role in this step, consider [creating a custom role](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/assembly-gw-roles#proc-gw-create-roles) that includes all the permissions for this resource type to give the team the correct access.




1. Review the settings and clickFinish.
1. The **Add roles** dialog displays indicating whether the role assignments were successfully applied. ClickCloseto close the dialog.


