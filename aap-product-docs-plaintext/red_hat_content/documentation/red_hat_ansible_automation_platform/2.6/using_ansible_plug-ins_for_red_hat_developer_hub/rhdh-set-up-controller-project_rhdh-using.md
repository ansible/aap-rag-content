# 1. Using the Ansible plug-ins
## 1.8. Setting up a controller project to run your playbook project




**Procedure**

1. The Ansible plug-ins provide a link to Ansible Automation Platform.
1. Log in to your Red Hat Developer Hub UI.
1. Click the Ansible `    A` icon in the Red Hat Developer Hub navigation panel.
1. Click **Operate** to display a link to your Ansible Automation Platform instance.

If automation controller was not included in your plug-in installation, a link to the product feature page is displayed.


1. Click **Go to Ansible Automation Platform** to open your platform instance in a new browser tab.

Alternatively, if your platform instance was not configured during the Ansible plug-in installation, navigate to your automation controller instance in a browser and log in.


1. Log in to automation controller.
1. Create a project in Ansible Automation Platform for the GitHub repository where you stored your playbook project. Refer to the [Projects](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-projects) chapter of _TitleControllerUserGuide_ .
1. Create a job template that uses a playbook from the project that you created. Refer to the [Workflow job templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-workflow-job-templates) chapter of _TitleControllerUserGuide_ .


