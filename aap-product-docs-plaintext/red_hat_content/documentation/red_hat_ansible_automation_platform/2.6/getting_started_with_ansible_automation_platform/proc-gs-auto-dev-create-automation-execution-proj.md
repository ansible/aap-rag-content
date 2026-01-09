# 3. Getting started as an automation developer
## 3.10. Creating an automation execution project




A project is a logical collection of playbooks. Projects are useful as a way to group your automation content according to the organizing principle of your choice.

You can set up an automation execution project in the platform UI.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Projects.
1. On the **Projects** page, clickCreate projectto launch the **Create Project** window.
1. Enter the appropriate details into the following required fields:


-  **Name** (required)
- Optional: **Description**
-  **Organization** (required): A project must have at least one organization. Select one organization now to create the project. When the project is created you can add additional organizations.
- Optional: **Execution Environment** : Enter the name of the execution environment or search from a list of existing ones to run this project.
-  **Source Control Type** (required): Select an SCM type associated with this project from the menu. Options in the following sections become available depending on the type chosen. For more information, see [Managing playbooks manually](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-projects#proc-controller-adding-a-project) or [Managing playbooks using source control](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-projects#ref-projects-manage-playbooks-with-source-control) .
- Optional: **Content Signature Validation Credential** : Use this field to enable content verification. Specify the GPG key to use for validating content signature during project synchronization. If the content has been tampered with, the job will not run. For more information, see [Project signing and verification](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/assembly-controller-project-signing) .

1. ClickCreate project.


