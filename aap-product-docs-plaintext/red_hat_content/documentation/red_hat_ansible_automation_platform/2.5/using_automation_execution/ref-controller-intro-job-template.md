# 6. Job templates
## 6.1. Automation templates




The **Automation Templates** page shows both **job templates** and **workflow job templates** that are currently available.

Automation Templates serve as a powerful blueprint for automating and orchestrating complex IT tasks.

Whether defined as a Job Template or Workflow Template, they standardize and streamline routine operations, enabling consistent execution across various environments.

By specifying playbooks, inventory, credentials, and other configuration details, an Automation Template eliminates manual intervention, reduces errors, and accelerates task completion.

It also provides flexibility by allowing the chaining of multiple tasks in a Workflow Template, supporting sophisticated automation use cases that can span across multiple systems and processes.

This ensures IT teams can reliably scale automation while maintaining high efficiency and control.

The default view is collapsed (Compact), showing the template name, template type, and the timestamp of the last job that ran using that template. You can click the![Arrow](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/301c31ef51ac512bd11df2687c14dd9d/arrow.png)
icon next to each entry to expand and view more information. This list is sorted alphabetically by name, but you can sort by other criteria, or search by various fields and attributes of a template.

From this screen you can launch![Launch icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/15376a8ac10d1efa9ec8cb3d4c707dfd/rightrocket.png)
, edit![Edit icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
, and duplicate![Duplicate icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/df17e3afcfb728d4887b97e8605bd65c/copy.png)
a job template.

Select the template name to display more information about the template, including when it last ran.

This list is sorted alphabetically by name, but you can sort by other criteria, or search by various fields and attributes of a template.

Note
Search functionality for Job templates is limited to alphanumeric characters only.



Workflow templates have the workflow visualizer![Workflow visualizer](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/1dca9a5e84ebe1b6ed13d956d77cca6e/visualizer.png)
icon as a shortcut for accessing the workflow editor.

Note
You can use job templates to build a workflow template. Templates that show the **Workflow Visualizer** ![Visualizer](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/1dca9a5e84ebe1b6ed13d956d77cca6e/visualizer.png)
icon next to them are workflow templates. Clicking the icon allows you to build a workflow graphically. Many parameters in a job template enable you to select **Prompt on Launch** that you can change at the workflow level, and do not affect the values assigned at the job template level. For instructions, see the [Workflow Visualizer](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-workflow-visualizer) section.



