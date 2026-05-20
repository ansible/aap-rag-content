# 11. Projects
## 11.1. Adding a new project

You can create a logical collection of playbooks, called projects in automation controller.

**Procedure**

1. From the navigation panel, select Automation Execution → Projects.

2. On the **Projects** page, click Create project to launch the **Create Project** window.

3. Enter the appropriate details into the following required fields:


- **Name** (required)
- Optional: **Description**
- **Organization** (required): A project must have at least one organization. Select one organization now to create the project. When the project is created you can add additional organizations.
- Optional: **Execution environment**: Enter the name of the execution environment or search from a list of existing ones to run this project. For more information, see [Creating and using execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/creating_and_using_execution_environments/index).
- **Source control type** (required): Select an SCM type associated with this project from the menu. Options in the following sections become available depending on the type chosen. For more information, see [Managing playbooks manually](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-projects-manage-playbooks-manually) or [Managing playbooks using source control](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#ref-projects-manage-playbooks-with-source-control).
- Optional: **Content signature validation credential**: Use this field to enable content verification. Specify the GPG key to use for validating content signature during project synchronization. If the content has been tampered with, the job will not run. For more information, see [Project signing and verification](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/assembly-controller-project-signing).

4. Click Create project.

**Additional resources**

- [Managing playbooks manually](#proc-projects-manage-playbooks-manually "11.1.1.&nbsp;Managing playbooks manually")
- [Managing playbooks using source control](#ref-projects-manage-playbooks-with-source-control "11.1.2.&nbsp;Managing playbooks using source control")
- [SCM Types - Configuring playbooks to use Git and Subversion](#proc-scm-git-subversion "11.1.2.1.&nbsp;SCM Types - Configuring playbooks to use Git and Subversion")
- [SCM Type - Configuring playbooks to use Red Hat Lightspeed](#proc-scm-insights "11.1.2.2.&nbsp;SCM Type - Configuring playbooks to use Red Hat Lightspeed")
- [SCM Type - Configuring playbooks to use a remote archive](#proc-scm-remote-archive "11.1.2.3.&nbsp;SCM Type - Configuring playbooks to use a remote archive")

