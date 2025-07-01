# 5. Managing access with role based access control
## 5.3. Users
### 5.3.5. Adding roles for a user




You can grant access for users to use, read, or write credentials by assigning roles to them.

Note
Users can not be assigned to an organization by adding roles. Refer to the steps provided in [Adding a user to an organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#proc-controller-add-organization-user) for detailed instructions.



**Procedure**

1. From the navigation panel, selectAccess Management→Users.
1. From the **Users** list view, click on the user to which you want to add roles.
1. Select the **Roles** tab to display the set of roles assigned to this user. These provide the ability to read, modify, and administer resources.
1. To add new roles, clickAdd roles.

Note
If you have multiple Ansible Automation Platform components installed, you will see selections for the roles associated with each component in the **Roles** menu bar. For example, Automation Execution for automation controller roles, Automation Decisions for Event-Driven Ansible roles.




1. Select a Resource type and clickNext.
1. Select the resources that will receive new roles and clickNext.
1. Select the roles that will be applied to the resources and clickNext.
1. Review the settings and clickFinish.

The Add roles dialog displays indicating whether the role assignments were successfully applied. ClickCloseto close the dialog.




