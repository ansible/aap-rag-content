# 4. Managing access with role-based access control
## 4.3. Users
### 4.3.5. Assigning roles to a user




You can grant users granular access to specific resources such as inventories, projects, or job templates by assigning users roles.

You can view and manage roles that were assigned directly to a user by an administrator in the user’s **Roles** tab.

You can view roles that a user inherited from a team assignment in the **View indirectly assigned roles** link in the page banner. You cannot directly manage an indirectly-assigned role. You can only manage indirectly-assigned roles by [editing the team’s role assignments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-controller-user-permissions) , or by [removing the user from the team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-gw-team-remove-user) .

Note
Users cannot be assigned to an organization through role assignment, nor can you assign users organization roles from this screen. Refer to the steps provided in [Adding a user to an organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-controller-add-organization-user) for detailed instructions on assigning a user to an organization.



Roles are labeled with their associated Ansible Automation Platform component and function. These components align with Ansible Automation Platform services and the side navigation structure in the user interface. Component labels can be understood as follows:

-  **Automation Execution** refers to automation controller
-  **Automation Decisions** refers to Event-Driven Ansible
-  **Automation Content** refers to automation hub


When assigning roles, ensure that you are selecting the desired resource in the correct component context, because resources like projects and credentials can be associated with both Automation Execution and Automation Decisions.

**Procedure**

1. From the navigation panel, selectAccess Management→Users.
1. From the **Users** list view, click the user to which you want to add roles.
1. Select the **Roles** tab to display the set of roles assigned to this user. These provide the ability to read, modify, and administer resources.
1. To add new roles, clickAdd roles.

Note
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).




1. Select a Resource type and clickNext.
1. Select the resources that you want to give role-based access to and clickNext.
1. Select the roles that will be applied to the resources and clickNext.

Tip
If you are selecting more than one role, consider [creating a custom role](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/assembly-gw-roles#proc-gw-create-roles) that includes all the permissions for this resource type so you can give your users the appropriate level of access.




1. Review the settings and clickFinish. The Add roles dialog displays indicating whether the role assignments were successfully applied. ClickCloseto close the dialog.


