# 11. Projects
## 11.1. Adding a new project




You can create a logical collection of playbooks, called projects in automation controller.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Projects.
1. On the **Projects** page, clickCreate projectto launch the **Create Project** window.
1. Enter the appropriate details into the following required fields:


-  **Name** (required)
- Optional: **Description**
-  **Organization** (required): A project must have at least one organization. Select one organization now to create the project. When the project is created you can add additional organizations.
- Optional: **Execution environment** : Enter the name of the execution environment or search from a list of existing ones to run this project. For more information, see [Creating and using execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/index) .
-  **Source control type** (required): Select an SCM type associated with this project from the menu. Options in the following sections become available depending on the type chosen. For more information, see [Managing playbooks manually](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-projects-manage-playbooks-manually) or [Managing playbooks using source control](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#ref-projects-manage-playbooks-with-source-control) .
- Optional: **Content signature validation credential** : Use this field to enable content verification. Specify the GPG key to use for validating content signature during project synchronization. If the content has been tampered with, the job will not run. For more information, see [Project signing and verification](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#assembly-controller-project-signing) .

1. ClickCreate project.


**Additional resources**

The following describe the ways projects are sourced:


-  [Managing playbooks manually](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-projects-manage-playbooks-manually)
-  [Managing playbooks using source control](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#ref-projects-manage-playbooks-with-source-control)


-  [SCM Types - Configuring playbooks to use Git and Subversion](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-scm-git-subversion)
-  [SCM Type - Configuring playbooks to use Red Hat Insights](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-scm-insights)
-  [SCM Type - Configuring playbooks to use a remote archive](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-scm-remote-archive)



