# 4. Managing access with role-based access control
## 4.3. Users

A user is an individual or entity that can log in to the platform and perform tasks. Users are fundamental units to which roles can be assigned, either directly by an administrator or indirectly through a team.

Warning

Ansible Automation Platform automatically creates a default system administrator user so they can log in and set up Ansible Automation Platform for their organization. Do not delete this user. The containerized installer uses this account to register services with platform gateway. Deleting the default system administrator user causes installation and upgrade operations to fail.

If you have already deleted the default system administrator user, you must set the `gateway_admin_user` variable in your installer inventory file to specify an alternative system administrator account before running the installation program.

For more information about installer inventory variables, see [Platform gateway variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars#platform-gateway-variables).

You can sort or search the User list by **Username**, **First name**, **Last name**, or **Email**. Click the arrows in the header to toggle your sorting preference. You can view **User type** and **Email** beside the user name on the Users page.

