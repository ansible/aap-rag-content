# Set up permissions for custom self-service templates
## Set up RBAC for custom self-service templates

By default, Ansible Automation Platform administrators can define Ansible automation portal RBAC roles.

### Before you begin

- You have created a user, for example `example-user`.
- You have added this user as a member of a team, for example `example-team`.

### About this task

This procedure describes how to create a role in Ansible automation portal that allows only a selected team to view and execute particular custom self-service templates.

Custom self-service templates in Ansible automation portal are associated with job templates in Ansible Automation Platform. This association is set in the `steps.actions` section of the YAML file for the custom self-service template.

If you assign permissions to a particular team to launch a custom self-service template from Ansible automation portal, then you must make sure that that team has permission to run the associated job templates in Ansible Automation Platform.

### Procedure

1.  In a browser, log in to your Ansible automation portal instance as an Ansible Automation Platform user with Ansible Automation Platform administrator privileges.
2.  In the navigation panel, select Administration> (and then)RBAC.
3.  In the **RBAC** view, click **Create**. The **Create Role** view appears.

1.  Enter a name for the role.
2.  In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role.

![Select users and groups table showing Members column](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-rbac-select-users-groups.png)
Note:
The **Members** column displays the total count of users in each team, including both regular team members and administrators.

3.  In the **Add Permission policies** section, select the plug-ins that you want to enable for the role.
4.  Select **Permission** in the list of plug-ins to configure the fine-grained permission policies for the role.

4.  Click **Next**.
5.  Review the settings that you have selected for the role.
6.  Click **Create** to create the role.

