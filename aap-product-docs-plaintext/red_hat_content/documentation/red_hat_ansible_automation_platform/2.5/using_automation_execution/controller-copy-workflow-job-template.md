# 8. Workflow job templates
## 8.9. Duplicating a workflow job template




With automation controller you can duplicate a workflow job template. When you duplicate a workflow job template, it does not duplicate any associated schedule, notifications, or permissions. Schedules and notifications must be recreated by the user or system administrator creating the duplicate of the workflow template. The user duplicating the workflow template is granted the administrator permission, but no permissions are assigned (duplicated) to the workflow template.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Templates.
1. Click the![More options](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/65fed3eab4f6ac2075ffa1b3caa55e46/options_menu.png)
) icon associated with the template that you want to duplicate and select the![Duplicate Template](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/df17e3afcfb728d4887b97e8605bd65c/copy.png)
Duplicate template icon.


- The new template with the name of the template from which you duplicated and a timestamp displays in the list of templates.

1. Click to open the new template and clickEdit template.
1. Replace the contents of the **Name** field with a new name, and give or change the entries in the other fields to complete this page.
1. ClickSave job template.


Note
If a resource has a related resource that you do not have the right level of permission to, you cannot duplicate the resource. For example, in the case where a project uses a credential that a current user only has Read access. However, for a workflow job template, if any of its nodes use an unauthorized job template, inventory, or credential, the workflow template can still be duplicated. But in the duplicated workflow job template, the corresponding fields in the workflow template node are absent.



