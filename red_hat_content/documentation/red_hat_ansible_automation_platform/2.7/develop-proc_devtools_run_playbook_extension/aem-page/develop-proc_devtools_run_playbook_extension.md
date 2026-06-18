+++
title = "Run your playbook automation to test behavior - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_devtools_run_playbook_extension"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_devtools_intro/", "Create, test, and deploy automation content with ansible-dev-tools"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_devtools_run_playbook_extension/aem-page/develop-proc_devtools_run_playbook_extension.html"
last_crumb = "Run your playbook automation to test behavior"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Run your playbook automation to test behavior"
oversized = "false"
page_slug = "develop-proc_devtools_run_playbook_extension"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_devtools_run_playbook_extension"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_devtools_run_playbook_extension/toc/toc.json"
type = "aem-page"
+++

# Run your playbook automation to test behavior

Run your playbook using two methods provided by the Ansible VS Code extension.

## Procedure

 The Ansible VS Code extension provides two options to run your playbook:

- `ansible-playbook` runs the playbook on your local machine using Ansible Core.
- `ansible-navigator` runs the playbook in an execution environment in the same manner that Ansible Automation Platform runs an automation job. You specify the base image for the execution environment in the Ansible extension settings.

## Run your playbook with `ansible-playbook`

You can run your Ansible playbook locally by using the `ansible-playbook` command directly within the VS Code extension.

### Procedure

 To run a playbook, right-click the playbook name in the **Explorer** pane, then select Run Ansible Playbook via> (and then)Run playbook via ansible-playbook.

 ![Run playbook via ansible-playbook](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-playbook-run.png)

The output is displayed in the **Terminal** tab of the VS Code terminal. The `ok=2` and `failed=0` messages indicate that the playbook ran successfully.

 ![Success message for ansible-playbook execution](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-playbook-success.png)

## Run your playbook with `ansible-navigator`

You can run an Ansible playbook through `ansible-navigator` by right-clicking the playbook name in the Explorer pane. This procedure explains how to view the playbook’s output and navigate the results for each play and task within the terminal.

### Before you begin

- You enabled the use of an execution environment in the Ansible extension settings.
- You entered the path or URL for the execution environment image in the Ansible extension settings.

### Procedure

1.  To run a playbook, right-click the playbook name in the Explorer pane, then select Run Ansible Playbook via> (and then)Run playbook via ansible-navigator run.
2.  View the output in the **Terminal** tab of the VS Code terminal. The **Successful** status indicates that the playbook ran successfully.  ![Output for ansible-navigator execution](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/devtools-extension-navigator-output.png)

3.  Enter the number next to a play to step into the play results. The example playbook only contains one play. Enter `0` to view the status of the tasks executed in the play.  ![Tasks in ansible-navigator output](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/devtools-extension-navigator-tasks.png)

    Type the number next to a task to review the task results.

## Publish and run your playbook automation

The following procedures describe how to deploy your new playbooks in your instance of Ansible Automation Platform so that you can use them to run automation jobs.

### Save your project in SCM

Save your playbook project as a repository in your source control management system, for example GitHub.

#### Procedure

1.  Initialize your project directory as a git repository.
2.  Push your project up to a source control system such as GitHub.

### Run your playbook in Ansible Automation Platform

To run your playbook in Ansible Automation Platform, you must create a project in automation controller for the repository where you stored your playbook project. You can then create a job template for each playbook from the project.

#### Procedure

1.  In a browser, log in to automation controller.
2.  Configure a Source Control credential type for your source control system if necessary. See the [Creating new credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_create_credential "Learn how to create new credentials in Automation controller.") section of *Using automation execution* for more details.
3.  In automation controller, create a project for the GitHub repository where you stored your playbook project. Refer to the [Projects](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_projects "A project is a logical collection of Ansible playbooks, represented in automation controller.") chapter of *Using automation execution*.
4.  Create a job template that uses a playbook from the project that you created. Refer to the [Job Templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .") chapter of *Using automation execution*.
5.  Run your playbook from automation controller by launching the job template. Refer to the [Launching a job template](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_controller_launch_job_template#controller-launch-job-template "You can configure a job template to store all the parameters that you would normally pass to the Ansible Playbook on the command line. In addition to the playbooks, the template passes the inventory, credentials, extra variables, and all options and settings that you can specify on the command line.") section of *Using automation execution*.
