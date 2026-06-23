# View, create, or assign roles to users

A user is an individual or entity that can log in to the platform and perform tasks. Users are fundamental units to which roles can be assigned, either directly by an administrator or indirectly through a team.

Warning:

Ansible Automation Platform automatically creates a default system administrator user so they can log in and set up Ansible Automation Platformfor their organization. Do not delete this user.

The containerized installer uses this account to register services with platform gateway. Deleting the default system administrator user causes installation and upgrade operations to fail.

If you have already deleted the default system administrator user, you must set the `gateway_admin_user` variable in your installer inventory file to specify an alternative system administrator account before running the installation program.

You can sort or search the User list by **Username**, **First name**, **Last name**, or **Email**. Click the arrows in the header to toggle your sorting preference. You can view **User type** and **Email** beside the user name on the Users page.

