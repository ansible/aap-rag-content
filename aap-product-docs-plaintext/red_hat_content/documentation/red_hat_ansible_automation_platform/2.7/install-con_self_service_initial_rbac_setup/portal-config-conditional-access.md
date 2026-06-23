# Set up initial RBAC rules in Ansible automation portal
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

