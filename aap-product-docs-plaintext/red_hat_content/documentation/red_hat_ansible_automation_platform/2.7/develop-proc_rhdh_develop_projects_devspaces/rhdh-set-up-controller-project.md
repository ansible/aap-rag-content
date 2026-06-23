# Develop and execute projects in Dev Spaces
## Connect your project to Ansible Automation Platform

Access Ansible Automation Platform through the Red Hat Developer Hub to create a project for your playbook repository, then set up a job template that uses the playbook. You can go directly to your automation controller instance if it was not configured during the plug-in installation.

### Procedure

1.  The Ansible plug-ins provide a link to Ansible Automation Platform.
2.  Log in to your Red Hat Developer Hub UI.
3.  Click the Ansible `A` icon in the Red Hat Developer Hub navigation panel.
4.  Click **Operate** to display a link to your Ansible Automation Platform instance. If automation controller was not included in your plug-in installation, a link to the product feature page is displayed.

5.  Click **Go to Ansible Automation Platform** to open your platform instance in a new browser tab. Alternatively, if your platform instance was not configured during the Ansible plug-in installation, navigate to your automation controller instance in a browser and log in.

6.  Log in to automation controller.
7.  Create a project in Ansible Automation Platform for the GitHub repository where you stored your playbook project. Refer to [Projects](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_projects "A project is a logical collection of Ansible playbooks, represented in automation controller.") for more information.
8.  Create a job template that uses a playbook from the project that you created. Refer to [Workflow job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflow_job_templates "A workflow job template links together a sequence of disparate resources that tracks the full set of jobs that were part of the release process as a single unit.") for more information.

