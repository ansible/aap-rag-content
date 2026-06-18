+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/get_started-assembly_gs_auto_op"
title = "Get started as an automation operator - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/get_started-assembly_gs_auto_op/", "Get started as an automation operator"]]
category = "Get started"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/get_started-assembly_gs_auto_op/aem-page/get_started-assembly_gs_auto_op.html"
last_crumb = "Get started as an automation operator"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Get started as an automation operator"
oversized = "false"
page_slug = "get_started-assembly_gs_auto_op"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/get_started-assembly_gs_auto_op"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/get_started-assembly_gs_auto_op/toc/toc.json"
type = "aem-page"
+++

# Get started as an automation operator

As an automation operator, Ansible Automation Platform helps you monitor and execute automation projects with Red Hat certified collections or custom content for your organization.

## View automation execution projects

A project is a logical collection of Ansible playbooks that you can manage in Ansible Automation Platform.

### About this task

Platform administrators and automation developers have the permissions to create projects. As an automation operator you can view and sync projects. The following procedure desribes how to view available projects.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects. The **Projects** page displays a list of projects that are currently available.
2.  Click a project to view its details.

### What to do next

For each project listed, you can sync the latest revision, edit the project, or copy the project’s attributes using the icons next to each project.

## Work with job templates

A job template is a definition and set of parameters for running an Ansible job.

A job template combines an Ansible Playbook from a project with the settings required to launch the job. Job templates are useful for running the same job many times. Job templates also encourage the reuse of Ansible Playbook content and collaboration between teams.

Platform administrators and automation developers have the permissions to create job templates. As an automation operator you can launch job templates and view their details.

## Launch a job template

Ansible Automation Platform provides push-button deployment with job templates. These templates store playbook parameters, inventories, and credentials normally passed through the command line.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Templates.
2.  Select a template to view its details. A default job template is created during your initial setup to help you get started, but you can also create your own.
3.  From the **Templates** page, click the launch icon to run your job template.

### Results

The **Templates** list view shows job templates that are currently available. The default view is collapsed (Compact), showing the template name, template type, and the timestamp of the last job that ran using that template. You can click the arrow icon next to each entry to expand and view more information. This list is sorted alphabetically by name, but you can sort by other criteria, or search by various template fields and attributes.

From this screen you can launch, edit, and copy a job template.

## Surveys in job templates

Surveys provide a way to prompt users for input when launching a job from a job template. This input can then be used as variables in the playbook run.

Job types of **Run** or **Check** provide a way to set up surveys in the **Job Template** creation or editing screens. Surveys set extra variables for the playbook similar to **Prompt for Extra Variables** does, but in a user-friendly question and answer way. Surveys also permit for validation of user input. Select the **Survey** tab to create a survey.

 **Example**

You can use surveys for several situations. For example, operations want to give developers a "push to stage" button that they can run without advance knowledge of Ansible. When launched, this task could prompt for answers to questions such as "What tag should we release?".

You can ask many types of questions, including multiple-choice questions.

## Create a survey

You can create a survey for a job template to prompt users for input when they launch a job based on that template. Surveys can include many questions of various types, such as text input, multiple choice, and passwords.

### About this task

The responses provided by users are stored in Ansible variables that can be used within the playbook associated with the job template.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Templates.
2.  Select the job template you want to create a survey for.
3.  From the **Survey** tab, click Create survey question.
4.  A survey can consist of any number of questions. For each question, enter the following information:

  - **Question**: The question to ask the user.
  - Optional: **Description**: A description of what is being asked of the user.
  - **Answer variable name**: The Ansible variable name to store the user’s response in. This is the variable to be used by the playbook. Variable names cannot contain spaces.
  - **Answer type**: Choose from the following question types:
    * **Text**: A single line of text. You can set the minimum and maximum length (in characters) for this answer.
    * **Textarea**: A multi-line text field. You can set the minimum and maximum length (in characters) for this answer.
    * **Password**: Responses are treated as sensitive information, similar to the way an actual password is treated. You can set the minimum and maximum length (in characters) for this answer.
    * **Multiple Choice (single select)**: A list of options, of which only one can be selected at a time. Enter the options, one per line, in the **Multiple Choice Options** field.
    * **Multiple Choice (multiple select)**: A list of options, any number of which can be selected at a time. Enter the options, one per line, in the **Multiple Choice Options** field.
    * **Integer**: An integer number. You can set the minimum and maximum length (in characters) for this answer.
    * **Float**: A decimal number. You can set the minimum and maximum length (in characters) for this answer.
  - **Required**: Whether or not an answer to this question is required from the user.
  - **Minimum length** and **Maximum length**: Specify if a certain length in the answer is required.
  - **Default answer**: The default answer to the question. This value is pre-filled in the interface and is used if the answer is not provided by the user.

5.  Once you have entered the question information, click Create question to add the question. The survey question displays in the **Survey** list. For any question, you can click ![Pencil](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) to edit it.

    Check the box next to each question and click Delete to delete the question, or use the toggle option in the menu bar to enable or disable the survey prompts.

    If you have more than one survey question, click Edit Order to rearrange the order of the questions by clicking and dragging on the grid icon.

6.  To add more questions, click Add.

## View hosts being automated in inventory files

An inventory is a file listing the collection of hosts managed by Ansible Automation Platform. Organizations are assigned to inventories, while permissions to launch playbooks against inventories are controlled at the user or team level.

Platform administrators and automation developers have the permissions to create inventories. As an automation operator you can view inventories and their details.

### Execute an inventory

The following steps describe how to execute an inventory.

#### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories. The **Inventories** window displays a list of inventories that are currently available, along with the following information:

  - **Name**: The inventory name.
  - **Status**: The statuses are:
    * **Success**: The inventory sync completed successfully.
    * **Disabled**: No inventory source added to the inventory.
    * **Error**: The inventory source completed with error.
  - **Type**: Identifies whether the inventory is a standard inventory, a smart inventory, or a constructed inventory.
  - **Organization**: The organization to which the inventory belongs.

2.  Select an inventory name to display the **Details** page for the inventory, including the inventory’s groups and hosts.

## View the status and output of automation jobs

A job is an instance of Ansible Automation Platform launching an Ansible Playbook against an inventory of hosts. You can view the status and output of automation jobs.

### Review a job status

The **Jobs** list view displays a list of jobs and their statuses, shown as completed successfully, failed, or as an active (running) job.

#### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Jobs. The default view is collapsed (Compact) with the job name, status, job type, start, and finish times. You can click the arrow icon to expand and see more information. You can sort this list by various criteria, and perform a search to filter the jobs of interest.

2.  From this screen, you can complete the following tasks:

  - View a job’s details and standard output.

  - Relaunch jobs.

  - Remove selected jobs. The relaunch operation only applies to relaunches of playbook runs and does not apply to project or inventory updates, system jobs, or workflow jobs.

### Review job output

When you relaunch a job, the jobs **Output** view is displayed.

#### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Jobs.
2.  Select a job. This takes you to the **Output** view for that job, where you can filter job output by these criteria:

  - The **Search output** option allows you to search by keyword.
  - The **Event** option enables you to filter by the events of interest, such as errors, host failures, host retries, and items skipped. You can include as many events in the filter as necessary.
