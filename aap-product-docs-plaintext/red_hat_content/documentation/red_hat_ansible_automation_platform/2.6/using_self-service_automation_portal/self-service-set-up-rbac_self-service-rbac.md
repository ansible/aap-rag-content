# 4. Working with custom self-service template permissions
## 4.1. Setting up RBAC for custom self-service templates




RBAC is set up in the Helm chart with the `admin` user set as the RBAC administrator ( `rbac_admin` ).

This procedure describes how to create a role in self-service automation portal that allows only a selected team to view and execute particular custom self-service templates.

Custom self-service templates in self-service automation portal are associated with job templates in Ansible Automation Platform. This association is set in the `steps.actions` section of the YAML file for the custom self-service template.

If you assign permissions to a particular team to launch a custom self-service template from self-service automation portal, then you must make sure that that team has permission to run the associated job templates in Ansible Automation Platform.

**Prerequisites**

- As the admin user in your Ansible Automation Platform instance, you have created a user, for example `    example-user` .

See [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-controller-creating-a-user) in the _Access management and authentication_ guide.


- You have added this user as a member of a team, for example `    example-team` .

See [Adding users to a team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-gw-team-add-user) in the _Access management and authentication_ guide.




**Procedure**

1. In a browser, log in to your self-service automation portal instance as an Ansible Automation Platform user with `    admin` privileges.
1. In the navigation panel, selectAdministration→RBAC.
1. In the **RBAC** view, click **Create** .

The **Create Role** view appears.


1. Enter a name for the role.
1. Select the user or group that you want to allow to use the role.
1. In the **Add Permission policies** section, select the plug-ins that you want to enable for the role.
1. Select **Permission** in the list of plug-ins to configure the fine-grained permission policies for the role.

1. Click **Next** .
1. Review the settings that you have selected for the role.
1. Click **Create** to create the role.


