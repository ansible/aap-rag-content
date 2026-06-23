# Set up initial RBAC rules in Ansible automation portal
## Configure RBAC for synchronization

Synchronization uses an Ansible Automation Platform token configured in the Ansible automation portal to determine which data to synchronize from Ansible Automation Platform.

### Before you begin

- You have credentials for an Ansible Automation Platform administrator.
- Synchronization of Ansible Automation Platform Organization information from Ansible Automation Platform is complete.
- Users who execute Ansible Automation Platform job templates through Ansible automation portal must have job template **Execute** permissions assigned in Ansible Automation Platform for the respective Ansible Automation Platform job templates.
- The **Allow external users to create OAuth2 tokens** setting is enabled in the Settings> (and then)Platform gateway settings in Ansible Automation Platform.

### About this task

By default, Ansible automation portal synchronizes Ansible Automation Platform Organization, Team, and User identity information. Ansible automation portal also synchronizes Ansible Automation Platform job template information accessible by the configured Ansible Automation Platform token.

### Procedure

1.  Log in to Ansible automation portal with an account that has Ansible Automation Platform administrator privileges.
2.  In the navigation pane of Ansible automation portal, select Administration> (and then)RBAC.
3.  Click Create to create a new role and enter a name, for example `portal-users`.
4.  Click Next.
![Create new role](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-create-new-rbac-role.png)
5.  In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role, then click Next.
![Select users and groups table showing Members column](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-rbac-select-users-groups.png)
Note:
The **Members** column displays the total count of users in each team, including both regular team members and administrators.

You can only select Ansible Automation Platform teams and users from the Ansible Automation Platform Organization that you have configured for synchronization with Ansible automation portal.

6.  Click Next to configure permissions in the **Add permission policies** section:
1.  Select the **Catalog** plugin from the **Select plugins** dropdown menu.
2.  Select the checkbox for `catalog.entity.read`.
![Add permission policies](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-add-permission-policies.png)
7.  Select the **Scaffolder** plugin and enable all scaffolder permissions:

-  `scaffolder.template.parameter.read`
-  `scaffolder.template.step.read`
-  `scaffolder.action.execute`
-  `scaffolder.task.cancel`
-  `scaffolder.task.create`
-  `scaffolder.task.read`
Note:
The `scaffolder.task.read` permission must be enabled so that users can view previous task runs in the **History** page in the Ansible automation portal console.

8.  Click Next to review your settings, then Create to create the new role. On successful completion, your new role is included in the **All roles** list when you select Administration> (and then)RBAC in the navigation pane in Ansible automation portal.

### Results

On successful completion, your new role is included in the **All roles** list when you select Administration> (and then)RBAC in the navigation pane in Ansible automation portal.

