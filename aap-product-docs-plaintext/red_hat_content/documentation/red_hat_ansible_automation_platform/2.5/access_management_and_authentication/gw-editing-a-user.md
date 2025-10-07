# 4. Managing access with role-based access control
## 4.3. Users
### 4.3.3. Editing a user




You can modify the properties of a user account after it is created.

In upgrade scenarios, there might be pre-existing user accounts from automation controller or automation hub services. When editing these user accounts, the **User type** checkboxes indicate whether the account had one of the following service level administrator privileges:

Platform administrators can revoke or assign administrator permissions for the individual services and designate the user as either an **Ansible Automation Platform Administrator** , **Ansible Automation Platform Auditor** or normal user. Assigning administrator privileges to all of the individual services automatically designates the user as an **Ansible Automation Platform Administrator** . See [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-creating-a-user) for more information about user types.

To see whether a user had service level auditor privileges, you must refer to the API.

Note
Users previously designated as automation controller or automation hub administrators are labeled as **Normal** in the **User type** column in the [Users list view](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-gw-users-list-view) . You can see whether these users have administrator privileges, from the **Edit Users** page.



**Procedure**

1. From the navigation panel, selectAccess Management→Users.
1. Select the checkbox for the user that you want to modify.
1. Click the **Pencil** icon and select **Edit user** .
1. The **Edit** user page is displayed where you can modify user details such as, **Password** , **Email** , **User type** , and **Organization** .

Note
If the user account was migrated to Ansible Automation Platform 2.5 during the upgrade process and had administrator privileges for an individual service, additional User type checkboxes will be available. You can use these checkboxes to revoke or add individual privileges or designate the user as a platform administrator, system auditor or normal user.




1. After your changes are complete, click **Save user** .


