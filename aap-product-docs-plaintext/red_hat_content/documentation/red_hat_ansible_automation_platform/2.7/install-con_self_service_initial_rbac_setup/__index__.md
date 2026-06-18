# Set up initial RBAC rules in Ansible automation portal

After you install Ansible automation portal and synchronize it with Ansible Automation Platform, only users with Ansible Automation Platform administrator privileges can view the auto-generated templates.

You must configure initial Role-Based Access Control (RBAC) permissions to allow non-admin users to view and execute synchronized Ansible Automation Platform job templates.

Important:

Role-Based Access Control (RBAC) differs by template type:

-   * **Auto-generated templates:** Permissions are synchronized from Ansible Automation Platform. Users must have permissions on the underlying Ansible Automation Platform job template.
* **Custom templates:** Permissions must be explicitly configured within the Ansible Automation Portal. Users must also have permissions to run the associated job templates in Ansible Automation Platform.

## Understand the permission model

Ansible automation portal and Ansible Automation Platform use separate but related permission systems. Ansible Automation Platform RBAC is the source of truth for synchronization scope and execution permissions.

**Ansible automation portal RBAC:**

- Controls which users can view templates in the Ansible automation portal catalog.
- Controls which users can access portal templates and submit jobs.


**Ansible Automation Platform RBAC:**

- **Controls synchronization scope:** Only Ansible Automation Platform job templates accessible by the configured Ansible Automation Platform token (ansible.rhaap.token) are synchronized to Ansible automation portal.
- **Controls Ansible Automation Platform job template visibility and execution:** Ansible Automation Platform permissions determine whether authenticated users can view and execute Ansible Automation Platform job templates in Ansible automation portal.
- **Validates execution permissions:** When a Ansible automation portal user executes a template, Ansible Automation Platform checks that user’s execute permissions before launching the job.


Note:

If a user can see a Ansible automation portal template in the catalog but lacks Ansible Automation Platform execution permissions for the associated Ansible Automation Platform job template in Ansible Automation Platform, the user cannot run the Ansible Automation Platform Job.

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

## Configure conditional access

Optionally, you can configure conditional Ansible automation portal RBAC policies to filter role access to specific Ansible Automation Platform job templates by tag for specific Ansible Automation Platform teams or users.

### Before you begin

- Ansible Automation Platform job templates must have Ansible Automation Platform labels applied and synchronized with Ansible automation portal.
- Users who execute Ansible Automation Platform job templates through Ansible automation portal must have Ansible Automation Platform job template **Execute** permissions assigned in Ansible Automation Platform for the respective Ansible Automation Platform job templates.

### About this task

Ansible Automation Platform labels applied to Ansible Automation Platform job templates are synchronized to Ansible automation portal as tags and can be used for conditional access control.

Note:

Ansible Automation Platform labels are converted to lowercase tags with special characters replaced by hyphens (for example, the Ansible Automation Platform label `Network-Automation` becomes the tag `network-automation`).

### Procedure

1.  Log in to Ansible automation portal with an account that has Ansible Automation Platform administrator privileges.
2.  In the navigation pane of Ansible automation portal, select Administration> (and then)RBAC.
3.  Click Create to create a new role and enter a name, for example `network-templates`.
4.  Click Next.
5.  In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role (for example, the Ansible Automation Platform network-team), then click Next.
![Select users and groups table showing Members column](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-rbac-select-users-groups.png)
Note:
The **Members** column displays the total count of users in each team, including both regular team members and administrators.

You can only select Ansible Automation Platform teams and users from the Ansible Automation Platform Organization that you are using in Ansible automation portal.

6.  Click Next to configure permissions in the **Add permission policies** section:

- Select the **Catalog** plugin from the **Select plugins** dropdown menu.
- Select the checkbox for `catalog.entity.read`.
- Click Conditional to configure a condition-based policy.

7.  In the condition builder, configure a rule to filter by tag:

- **Rule:** Select `HAS_METADATA` from the dropdown menu
- **Key:** Enter `tags`
- **Value:** Enter the tag value to filter by (for example, `network-automation`)

8.  Select the **Scaffolder** plugin and enable all scaffolder permissions:

-  `scaffolder.template.parameter.read`
-  `scaffolder.template.step.read`
-  `scaffolder.action.execute`
-  `scaffolder.task.cancel`
-  `scaffolder.task.create`
-  `scaffolder.task.read`

9.  Click Next to review your settings, then click Create to create the new role.

### Results

On successful completion, your new role is included in the **All roles** list when you select Administration> (and then)RBAC in the navigation pane in Ansible automation portal.

1. Log in to Ansible automation portal as a non-Ansible Automation Platform administrator user who is a member of a team you granted permissions to.
2. Verify that the user can see auto-generated templates in Ansible automation portal.   - If you configured conditional access by tag, the user should see only templates with the specified tags.
- If you did not configure conditional access, the user should see all Ansible Automation Platform job templates for which they have job template **Execute** permissions in Ansible Automation Platform.
3. To verify execution permissions work correctly, attempt to execute a template:
1. If the user has job template **Execute** permissions in Ansible Automation Platform for the template, the user can view the template, and the job launches successfully.

## Permissions reference for Ansible Automation Platform job template access

Permissions for Ansible Automation Platform job templates

| Permission                                | Resource type           | Policy     | Description                                                                                                 |
| ----------------------------------------- | ----------------------- | ---------- | ----------------------------------------------------------------------------------------------------------- |
| <br> `catalog.entity.read`                | <br>catalog-entity      | <br>read   | <br>Users can view synchronized Ansible Automation Platform job templates in the Ansible automation portal. |
| <br> `scaffolder.template.parameter.read` | <br>scaffolder-template | <br>read   | <br>Users can read template parameters.                                                                     |
| <br> `scaffolder.action.execute`          | <br>scaffolder-action   | <br>use    | <br>Users can execute actions through templates.                                                            |
| <br> `scaffolder.task.create`             |                         | <br>create | <br>Users can trigger the execution of Ansible Automation Platform job templates.                           |
| <br> `scaffolder.task.read`               |                         | <br>read   | <br>Users can view task execution history and logs on the **History** page.                                 |
| <br> `scaffolder.task.cancel`             |                         | <br>use    | <br>Users can cancel currently running templates.                                                           |

## Adjust synchronization frequency between Ansible Automation Platform and Ansible automation portal

The Helm chart defines how frequently users, teams and organization configuration information is synchronized from Ansible Automation Platform to Ansible automation portal.

### About this task

The frequency is set by the `catalog.providers.rhaap.schedule.frequency` key. By default, the synchronization occurs hourly.

### Procedure

To adjust the synchronization frequency, edit the value for the `catalog.providers.rhaap.schedule.frequency` key in the Helm chart.

```
catalog:
...
providers:
rhaap:
'{{- include "catalog.providers.env" . }}':
schedule:
frequency: {minutes: 60}
timeout: {seconds: 30}
```


Note:

Increasing the synchronization frequency generates extra traffic.

Bear this in mind when deciding the frequency, particularly if you have a large number of users.
