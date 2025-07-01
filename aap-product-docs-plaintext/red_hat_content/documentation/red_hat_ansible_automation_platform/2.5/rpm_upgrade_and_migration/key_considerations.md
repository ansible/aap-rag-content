# 3. Ansible Automation Platform post-upgrade steps
## 3.1. Migrating admin users
### 3.1.1. Key considerations




**Component-level admin privileges are retained:** Administrators for automation controller and automation hub will retain their existing admin privileges for those respective services post-upgrade. For example, an admin of automation controller will continue to have full administration privileges for automation controller resources.

Note
Users previously designated as automation controller or automation hub administrators are labeled as **Normal** in the **User type** column of the Users list view. This is a mischaracterization. You can verify that these users have, in fact, retained their service level administrator privileges, by editing the account:



**Procedure**

1. From the navigation panel of the platform gateway, selectAccess Management→Users.
1. Select the check box for the user that you want to modify.
1. Click the Pencil icon and select **Edit user** .
1. The Edit user page is displayed where you can see the service level administrator privileges assigned by the **User type** checkboxes. See [Editing a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#gw-editing-a-user) for more information on these user types.


Note
Only a platform administrator can escalate your privileges.



**Escalation to platform gateway admin must be manually configured post-upgrade:** During the upgrade process, admin privileges for individual services are not automatically translated to platform administrator privileges. Escalation to platform gateway admin must be granted by the platform administrator after upgrade and migration. Each service admin retains the original scope of their access until the access is changed.

As a platform administrator, you can escalate a user’s privileges by selecting the **Ansible Automation Platform Administrator** checkbox.

