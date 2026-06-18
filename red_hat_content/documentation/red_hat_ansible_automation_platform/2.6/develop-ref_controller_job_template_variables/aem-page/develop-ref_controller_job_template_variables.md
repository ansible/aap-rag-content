+++
title = "Set extra variables in job templates - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_controller_job_template_variables"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_job_templates/", "Standardize and streamline automation with automation job templates"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_controller_job_template_variables/aem-page/develop-ref_controller_job_template_variables.html"
last_crumb = "Set extra variables in job templates"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Set extra variables in job templates"
oversized = "false"
page_slug = "develop-ref_controller_job_template_variables"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_controller_job_template_variables"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_controller_job_template_variables/toc/toc.json"
type = "aem-page"
+++

# Set extra variables in job templates

Along with any extra variables set in the job template and survey, automation controller automatically adds the following variables to the job environment.

 Note:

- `awx_*` variables are defined by the system and cannot be overridden.
- Variables about the job context, such as `awx_job_template_name` are not affected if they are set in `extra_vars`.

- `awx_job_id`: The job ID for this job run.
- `awx_job_launch_type`: The description to indicate how the job was started:
  * **manual**: The job was started manually by a user.
  * **relaunch**: The job was started via relaunch.
  * **callback**: The job was started via host callback.
  * **scheduled**: The job was started from a schedule.
  * **dependency**: The job was started as a dependency of another job.
  * **workflow**: The job was started from a workflow job.
  * **sync**: The job was started from a project sync.
  * **scm**: The job was created as an Inventory SCM sync.
- `awx_job_template_id`: The job template ID that this job run uses.
- `awx_job_template_name`: The job template name that this job uses.
- `awx_execution_node`: The Execution Node name that launched this job.
- `awx_project_revision`: The revision identifier for the source tree that this particular job uses (it is also the same as the job’s field scm_revision).
- `awx_project_scm_branch`: The configured default project SCM branch for the project the job template uses.
- `awx_job_scm_branch`: If the SCM Branch is overwritten by the job, the value is shown here.
- `awx_user_email`: The user email of the controller user that started this job. This is not available for callback or scheduled jobs.
- `awx_user_first_name`: The user’s first name of the automation controller user that started this job. This is not available for callback or scheduled jobs.
- `awx_user_id`: The user ID of the automation controller user that started this job. This is not available for callback or scheduled jobs.
- `awx_user_last_name`: The last name of the automation controller user that started this job. This is not available for callback or scheduled jobs.
- `awx_user_name`: The user name of the automation controller user that started this job. This is not available for callback or scheduled jobs.
- `awx_schedule_id`: If applicable, the ID of the schedule that launched this job.
- `awx_schedule_name`: If applicable, the name of the schedule that launched this job.
- `awx_workflow_job_id`: If applicable, the ID of the workflow job that launched this job.
- `awx_workflow_job_name`: If applicable, the name of the workflow job that launched this job. Note this is also the same as the workflow job template.
- `awx_inventory_id`: If applicable, the ID of the inventory this job uses.
- `awx_inventory_name`: If applicable, the name of the inventory this job uses.


For compatibility, all variables are also given an "awx" prefix, for example, `awx_job_id`.

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

## Optional survey questions

The **Required** setting on a survey question determines whether the answer is optional or not for the user interacting with it.

Optional survey variables can also be passed to the playbook in `extra_vars`.

- If a non-text variable (input type) is marked as optional, and is not filled in, no survey `extra_var` is passed to the playbook.
- If a text input or text area input is marked as optional, is not filled in, and has a minimum `length > 0`, no survey `extra_var` is passed to the playbook.
- If a text input or text area input is marked as optional, is not filled in, and has a minimum `length === 0`, that survey `extra_var` is passed to the playbook, with the value set to an empty string ("").

## Extra variables

You can pass extra variables to a automation controller job template in several ways, including through surveys and the API.

When you pass survey variables, they are passed as extra variables (`extra_vars`) within automation controller. However, passing extra variables to a job template (as you would do with a survey) can override other variables being passed from the inventory and project.

By default, `extra_vars` are marked as `!unsafe` unless you specify them on the Job Template’s Extra Variables section. These are trusted, because they can only be added by users with enough privileges to add or edit a Job Template. For example, nested variables do not expand when entered as a prompt, as the Jinja brackets are treated as a string.

 Note:

`extra_vars` passed to the job launch API are only honored if one of the following is true:

- They correspond to variables in an enabled survey.
- `ask_variables_on_launch` is set to **True**.

**Example** You have a defined variable for an inventory for `debug = true`. It is possible that this variable, `debug = true`, can be overridden in a job template survey.

To ensure the variables that you pass are not overridden, ensure they are included by redefining them in the survey. You can define extra variables at the inventory, group, and host levels.

If you are specifying the `ALLOW_JINJA_IN_EXTRA_VARS` parameter, which controls whether Jinja templating is allowed in extra variables for job templates in automation controller, you can configure the parameter in the UI Jobs Settings.

-
- Only on Template Definitions (default); Never (recommended); Always (strongly discouraged)
Setting The job template extra variables dictionary is merged with the survey variables.

The following are some simplified examples of `extra_vars` in YAML and JSON formats:

- The configuration in YAML format:

```
launch_to_orbit: true
satellites:
  - sputnik
  - explorer
  - satcom
```


- The configuration in JSON format:

```
{
  "launch_to_orbit": true,
  "satellites": ["sputnik", "explorer", "satcom"]
}
```
The following table notes the behavior (hierarchy) of variable precedence in automation controller as it compares to variable precedence in Ansible.

 **Automation controller Variable Precedence Hierarchy (last listed wins)**

| Ansible                         | automation controller                         |
| ------------------------------- | --------------------------------------------- |
| <br>role defaults               | <br>role defaults                             |
| <br>dynamic inventory variables | <br>dynamic inventory variables               |
| <br>inventory variables         | <br>automation controller inventory variables |
| <br>inventory `group_vars`      | <br>automation controller group variables     |
| <br>inventory `host_vars`       | <br>automation controller host variables      |
| <br>playbook `group_vars`       | <br>playbook `group_vars`                     |
| <br>playbook `host_vars`        | <br>playbook `host_vars`                      |
| <br>host facts                  | <br>host facts                                |
| <br>registered variables        | <br>registered variables                      |
| <br>set facts                   | <br>set facts                                 |
| <br>play variables              | <br>play variables                            |
| <br>play `vars_prompt`          | <br>(not supported)                           |
| <br>play `vars_files`           | <br>play `vars_files`                         |
| <br>role and include variables  | <br>role and include variables                |
| <br>block variables             | <br>block variables                           |
| <br>task variables              | <br>task variables                            |
| <br>extra variables             | <br>Job Template extra variables              |
|                                 | <br>Job Template Survey (defaults)            |
|                                 | <br>Job Launch extra variables                |
