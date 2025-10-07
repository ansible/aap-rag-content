# Chapter 8. Workflow job templates




You can create both Job templates and Workflow job templates fromAutomation Execution→Templates.

For Job templates, see [Job templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-job-templates) .

A workflow job template links together a sequence of disparate resources that tracks the full set of jobs that were part of the release process as a single unit. These resources include the following:

- Job templates
- Workflow job templates
- Project syncs
- Inventory source syncs


The **Automation Templates** page shows the workflow and job templates that are currently available.

Select the template name to display more information about the template, including when it last ran. This list is sorted alphabetically by name, but you can sort by other criteria, or search by various fields and attributes of a template.

From this screen you can launch![Launch icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/15376a8ac10d1efa9ec8cb3d4c707dfd/rightrocket.png)
, edit![Edit icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
, and duplicate![Duplicate icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/df17e3afcfb728d4887b97e8605bd65c/copy.png)
a workflow job template.

Only workflow templates have the workflow visualizer![Workflow visualizer](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/1dca9a5e84ebe1b6ed13d956d77cca6e/visualizer.png)
icon as a shortcut for accessing the workflow editor.

![Workflow templates home](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/36a351edf0787b03f9d039358a103bdd/ug-wf-templates-home.png)


Note
Workflow templates can be used as building blocks for another workflow template. You can enable **Prompt on Launch** by setting up several settings in a workflow template, which you can edit at the workflow job template level. These do not affect the values assigned at the individual workflow template level. For further instructions, see the [Workflow visualizer](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-workflow-visualizer) section.



