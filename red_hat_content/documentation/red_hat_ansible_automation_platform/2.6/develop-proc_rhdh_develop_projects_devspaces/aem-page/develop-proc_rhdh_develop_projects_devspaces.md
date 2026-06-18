+++
template = "docs/aem-title.html"
title = "Develop and execute projects in Dev Spaces - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_develop_projects_devspaces"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_rhdh_using/", "Streamline development by integrating Red Hat Developer Hub plug-ins"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_develop_projects_devspaces/aem-page/develop-proc_rhdh_develop_projects_devspaces.html"
last_crumb = "Develop and execute projects in Dev Spaces"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Develop and execute projects in Dev Spaces"
oversized = "false"
page_slug = "develop-proc_rhdh_develop_projects_devspaces"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_develop_projects_devspaces"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_develop_projects_devspaces/toc/toc.json"
type = "aem-page"
+++

# Develop and execute projects in Dev Spaces

OpenShift Dev Spaces provides a web-based Integrated Development Environment that includes the Ansible VS Code extension and command line tools. You can use this environment to develop and test your automation code.

## About this task

The OpenShift Dev Spaces instance provides a default configuration that installs the Ansible VS Code extension and provides the Ansible command line tools.

## Procedure

 Activate Ansible Lightspeed in the Ansible VS Code extension. For more information, refer to the [Red Hat Ansible Lightspeed with IBM watsonx Code Assistant User Guide](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index).

 Important:

[OpenShift Dev Spaces](https://access.redhat.com/products/red-hat-openshift-dev-spaces) is not included with your Ansible Automation Platform subscription or the Ansible plug-ins for Red Hat Developer Hub.

## Execute automation tasks in Dev Spaces

The default configuration for Dev Spaces provides access to the Ansible command line tools.

### Procedure

 To execute an automation task in Dev Spaces from the VSCode user interface:

1.  Right-click a playbook name in the list of files.
2.  Select **Run Ansible Playbook via ansible-navigator run** or **Run playbook via ansible-playbook**.  
![Run a playbook from VS Code](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/playbook.png)  

## Connect your project to Ansible Automation Platform

Access Ansible Automation Platform through the Red Hat Developer Hub to create a project for your playbook repository, then set up a job template that uses the playbook. You can go directly to your automation controller instance if it was not configured during the plug-in installation.

### Procedure

1.  The Ansible plug-ins provide a link to Ansible Automation Platform.
2.  Log in to your Red Hat Developer Hub UI.
3.  Click the Ansible `A` icon in the Red Hat Developer Hub navigation panel.
4.  Click **Operate** to display a link to your Ansible Automation Platform instance. If automation controller was not included in your plug-in installation, a link to the product feature page is displayed.

5.  Click **Go to Ansible Automation Platform** to open your platform instance in a new browser tab. Alternatively, if your platform instance was not configured during the Ansible plug-in installation, navigate to your automation controller instance in a browser and log in.

6.  Log in to automation controller.
7.  Create a project in Ansible Automation Platform for the GitHub repository where you stored your playbook project. Refer to [Projects](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_controller_projects "A project is a logical collection of Ansible playbooks, represented in automation controller.") for more information.
8.  Create a job template that uses a playbook from the project that you created. Refer to [Workflow job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_workflow_job_templates "A workflow job template links together a sequence of disparate resources that tracks the full set of jobs that were part of the release process as a single unit.") for more information.

## Example: Automate a Red Hat Linux firewall configuration

This example demonstrates how the Ansible plug-ins can help Ansible users of all skill levels create quality Ansible content.

As an infrastructure engineer new to Ansible, you have been tasked to create a playbook to configure a Red Hat Enterprise Linux (RHEL) host firewall.

The following procedures show you how to use the Ansible plug-ins and Dev Spaces to develop a playbook.

### Learn more about playbooks

The first step is to learn more about Ansible playbooks using the available learning paths.

#### Procedure

1.  Click the Ansible `A` icon in the Red Hat Developer Hub navigation panel.
2.  Click **Learn** and select the **Getting Started with Ansible Playbooks** learning path. This redirects you to the Red Hat Developer website.
3.  If you are prompted to log in, create a Red Hat Developer account, or enter your details.
4.  Complete the learning path.
