# 9. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 9.7. Ansible Automation Platform post-upgrade steps
### 9.7.2. Migrating admin users




Follow this procedure to migrate admin users.

**Prerequisites**

- Review current admin roles for the individual services in your current deployment.
- Confirm the users who will require platform gateway admin rights post-upgrade.


**Procedure**

1. From the navigation panel of the platform gateway, selectAccess Management→Users.
1. Select the check box for the user that you want to modify.
1. Click the Pencil icon and select **Edit user** .
1. The Edit user page is displayed where you can see the service level administrator privileges assigned by the **User type** checkboxes. See [Editing a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#gw-editing-a-user) for more information on these user types.


