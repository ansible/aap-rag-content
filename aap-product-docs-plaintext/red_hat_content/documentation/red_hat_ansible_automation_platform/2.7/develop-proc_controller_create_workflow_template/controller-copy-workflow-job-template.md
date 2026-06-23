# Create a workflow job template
## Duplicate a workflow job template

Duplicate a workflow job template to create a copy of its structure. Note that associated schedules, notifications, and permissions are not copied and must be manually recreated for the new template.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Templates.
2.  Click the ![More options](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/options_menu.png)) icon associated with the template that you want to duplicate and select the ![Duplicate Template](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/copy.png) Duplicate template icon.   - The new template with the name of the template from which you duplicated and a timestamp displays in the list of templates.

3.  Click to open the new template and click Edit template.
4.  Replace the contents of the **Name** field with a new name, and give or change the entries in the other fields to complete this page.
5.  Click Save job template.  Note:
If a resource has a related resource that you do not have the right level of permission to, you cannot duplicate the resource. For example, in the case where a project uses a credential that a current user only has Read access. However, for a workflow job template, if any of its nodes use an unauthorized job template, inventory, or credential, the workflow template can still be duplicated. But in the duplicated workflow job template, the corresponding fields in the workflow template node are absent.
