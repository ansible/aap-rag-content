# Organize and define automation sources and targets
## Create an automation execution project

A project is a logical collection of playbooks. Projects are useful as a way to group your automation content according to the organizing principle of your choice.

### About this task

You can set up an automation execution project in the platform UI.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  On the **Projects** page, click Create project to launch the **Create Project** window.
3.  Enter the appropriate details into the following required fields:

- **Name** (required)
- Optional: **Description**
- **Organization** (required): A project must have at least one organization. Select one organization now to create the project. When the project is created you can add additional organizations.
- Optional: **Execution Environment**: Enter the name of the execution environment or search from a list of existing ones to run this project.
- **Source Control Type** (required): Select an SCM type associated with this project from the menu. Options in the following sections become available depending on the type chosen. For more information, see [Managing playbooks manually](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_controller_adding_a_project "You can create a logical collection of playbooks, called projects in automation controller.") or [Managing playbooks using source control](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_manage_playbooks_with_source_control#ref-projects-manage-playbooks-with-source-control "Choose one of the following options when managing playbooks by using source control:").
- Optional: **Content Signature Validation Credential**: Use this field to enable content verification. Specify the GPG key to use for validating content signature during project synchronization. If the content has been tampered with, the job will not run. For more information, see [Project signing and verification](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_project_signing#assembly-controller-project-signing "Use project signing and verification in your project directory to sign files. You can then verify whether or not that content has changed in any way, or files have been added to, or removed from the project unexpectedly.").

4.  Click Create project.

