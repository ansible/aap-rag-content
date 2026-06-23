# Create repeatable, shareable job templates to standardize automation runs
## Automation templates

The **Automation Templates** page shows both **job templates** and **workflow job templates** that are currently available.

Automation Templates serve as a powerful blueprint for automating and orchestrating complex IT tasks.

Whether defined as a Job Template or Workflow Template, they standardize and streamline routine operations, enabling consistent execution across various environments.

By specifying playbooks, inventory, credentials, and other configuration details, an Automation Template eliminates manual intervention, reduces errors, and accelerates task completion.

It also provides flexibility by allowing the chaining of multiple tasks in a Workflow Template, supporting sophisticated automation use cases that can span across multiple systems and processes.

This ensures IT teams can reliably scale automation while maintaining high efficiency and control.

The default view is collapsed (Compact), showing the template name, template type, and the timestamp of the last job that ran using that template. You can click the ![Arrow](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/arrow.png) icon next to each entry to expand and view more information. This list is sorted alphabetically by name, but you can sort by other criteria, or search by various fields and attributes of a template.

From this screen you can launch ![Launch icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rightrocket.png) , edit ![Edit icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png), and duplicate ![Duplicate icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/copy.png) a job template.

Select the template name to display more information about the template, including when it last ran.

This list is sorted alphabetically by name, but you can sort by other criteria, or search by various fields and attributes of a template.

Note:

Search functionality for Job templates is limited to alphanumeric characters only.

Workflow templates have the workflow visualizer ![Workflow visualizer](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/visualizer.png) icon as a shortcut for accessing the workflow editor.

Note:

You can use job templates to build a workflow template. Templates that show the **Workflow Visualizer**![Visualizer](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/visualizer.png) icon next to them are workflow templates. Clicking the icon allows you to build a workflow graphically. Many parameters in a job template enable you to select **Prompt on Launch** that you can change at the workflow level, and do not affect the values assigned at the job template level. For instructions, see the [Workflow Visualizer](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_controller_workflow_visualizer#controller-workflow-visualizer "The Workflow Visualizer provides a graphical way of linking together job templates, workflow templates, project syncs, and inventory syncs to build a workflow template.") section.

