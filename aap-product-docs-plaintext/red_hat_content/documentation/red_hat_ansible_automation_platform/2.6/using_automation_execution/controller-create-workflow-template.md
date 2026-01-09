# 8. Workflow job templates
## 8.1. Creating a workflow job template




To create a new workflow job template, complete the following steps:

Important
If you set a limit to a workflow template, it is not passed down to the job template unless you check **Prompt on launch** for the limit. This can lead to playbook failures if the limit is mandatory for the playbook that you are running.



**Procedure**

1. From the navigation panel, selectAutomation Execution→Templates.
1. On the **Automation Templates** page, select **Create workflow job template** from the **Create template** list.
1. Enter the appropriate details in the following fields:

Note
If a field has the **Prompt on launch** checkbox selected, either launching the workflow template, or using the workflow template within another workflow template, you are prompted for the value for that field. Most prompted values override any values set in the job template. Exceptions are noted in the following table.



|  **Field** |  **Options** |  **Prompt on Launch** |
| --- | --- | --- |
| Name | Enter a name for the job. | N/A |
| Description | Enter an arbitrary description as appropriate (optional). | N/A |
| Organization | Choose the organization to use with this template from the organizations available to the logged in user. | N/A |
| Inventory | Optionally, select the inventory to use with this template from the inventories available to the logged in user. | Yes |
| Limit | A host pattern to further constrain the list of hosts managed or affected by the playbook. You can separate many patterns by colons (:). As with core Ansible:

- a:b means "in group a or b"
- a:b:&c means "in a or b but must be in c"
- a:!b means "in a, and definitely not in b" | Yes

If selected, even if a default value is supplied, you are prompted upon launch to select a limit. |
| Source control branch | Select a branch for the workflow. This branch is applied to all workflow job template nodes that prompt for a branch. | Yes |
| Labels | - Optionally, supply labels that describe this workflow job template, such as `    dev` or `    test` . Use labels to group and filter workflow job templates and completed jobs in the display.
- Labels are created when they are added to the workflow template. Labels are associated to a single Organization using the Project that is provided in the workflow template. Members of the Organization can create labels on a workflow template if they have edit permissions (such as the admin role).
- Once you save the job template, the labels appear in the workflow job template **Details** view.
- Labels are only applied to the workflow templates not the job template nodes that are used in the workflow.
- Select![Disassociate](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/48c2fa70cf2a09ae0fafa81899b143fc/disassociate.png)
beside a label to remove it. When a label is removed, it is no longer associated with that particular Job or Job Template, but it remains associated with any other jobs that reference it. | Yes

If selected, even if a default value is supplied, you are prompted when launching to supply additional labels, if needed. - You cannot delete existing labels, selecting![Disassociate](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/48c2fa70cf2a09ae0fafa81899b143fc/disassociate.png)
only removes the newly added labels, not existing default labels. |
| Job tags | Type and select the **Create** drop-down to specify which parts of the playbook should run. | Yes |
| Skip tags | Type and select the **Create** drop-down to specify certain tasks or parts of the playbook to skip. | Yes |
| Extra variables | - Pass extra command line variables to the playbook.


This is the "-e" or "-extra-vars" command line parameter for ansible-playbook that is documented in the Ansible documentation at [Controlling how Ansible behaves: precedence rules](https://docs.ansible.com/ansible/latest/reference_appendices/general_precedence.html) . - Give key or value pairs by using either YAML or JSON. These variables have a maximum value of precedence and overrides other variables specified elsewhere. The following is an example value: `git_branch: production release_version: 1.5` | Yes

If you want to be able to specify `extra_vars` on a schedule, you must select **Prompt on launch** for **Extra variables** on the workflow job template, or enable a survey on the job template. Those answered survey questions become `extra_vars` . For more information about extra variables, see [Extra Variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-extra-variables) . |



1. Specify the following **Options** for launching this template, if necessary:


- Check **Enable webhook** to turn on the ability to interface with a predefined SCM system web service that is used to launch a workflow job template. GitHub and GitLab are the supported SCM systems.


- If you enable webhooks, other fields display, prompting for additional information:


-  **Webhook service** : Select which service to listen for webhooks from.
-  **Webhook URL** : Automatically populated with the URL for the webhook service to POST requests to.
-  **Webhook key** : Generated shared secret to be used by the webhook service to sign payloads sent to automation controller. You must configure this in the settings on the webhook service so that webhooks from this service are accepted in automation controller. For additional information about setting up webhooks, see [Working with Webhooks](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-work-with-webhooks) .


- Check **Enable concurrent jobs** to allow simultaneous runs of this workflow. For more information, see [Automation controller capacity determination and job impact](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-capacity-determination) .

1. When you have completed configuring the workflow template, clickCreate workflow job template.

Saving the template exits the workflow template page and the workflow visualizer opens where you can build a workflow. For more information, see the [Workflow visualizer](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-workflow-visualizer) section. Otherwise, select one of these methods:


- Close the workflow visualizer to return to the **Details** tab of the newly saved template. There you can complete the following tasks:


- Review, edit, add permissions, notifications, schedules, and surveys
- View completed jobs
- Build a workflow template

- ClickLaunch templateto start the workflow.

Note
Save the template before launching, orLaunch templateremains disabled. The **Notifications** tab is only present after you save the template.







