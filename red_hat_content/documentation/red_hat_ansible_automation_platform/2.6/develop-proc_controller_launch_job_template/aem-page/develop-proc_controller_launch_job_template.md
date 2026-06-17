+++
title = "Launch a job template - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-proc_controller_launch_job_template"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_job_templates/", "Standardize and streamline automation with automation job templates"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_controller_launch_job_template/aem-page/develop-proc_controller_launch_job_template.html"
last_crumb = "Launch a job template"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Launch a job template"
oversized = "false"
page_slug = "develop-proc_controller_launch_job_template"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-proc_controller_launch_job_template"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_controller_launch_job_template/toc/toc.json"
type = "aem-page"
+++

# Launch a job template

You can configure a job template to store all the parameters that you would normally pass to the Ansible Playbook on the command line. In addition to the playbooks, the template passes the inventory, credentials, extra variables, and all options and settings that you can specify on the command line.

## About this task

Easier deployments drive consistency, by running your playbooks the same way each time, and allowing you to delegate responsibilities.

## Procedure

 Launch a job template by using one of these methods:

- From the navigation panel, select Automation Execution> (and then)Templates and click **Launch template**![Launch](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rightrocket.png) on the job template card.
- In the job template **Details** tab of the job template you want to launch, click Launch template.

## Additional information requested when launching a job template

A job can require additional information to run. The following data can be requested at launch:

- Credentials that were setup
- The option **Prompt on Launch** is selected for any parameter
- Passwords or passphrases that have been set to **Ask**
- A survey, if one has been configured for the job templates
- Extra variables, if requested by the job template


 Note:

If a job has user-provided values, then those are respected upon relaunch. If the user did not specify a value, then the job uses the default value from the job template. Jobs are not relaunched as-is. They are relaunched with the user prompts re-applied to the job template.

If you give values on one tab, return to a previous tab, continuing to the next tab results in having to re-provide values on the rest of the tabs. Ensure that you complete the tabs in the order that the prompts appear.

When launching, automation controller automatically redirects the web browser to the **Job Status** page for this job under the **Jobs** tab.

You can re-launch the most recent job from the list view to re-run on all hosts or just failed hosts in the specified inventory. For more information, see the [Jobs in automation controller](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_jobs#controller-jobs "A job is an instance of automation controller launching an Ansible Playbook against an inventory of hosts.") section.

When slice jobs are running, job lists display the workflow and job slices, and a link to view their details individually.

 Note:

You can launch jobs in bulk by using the newly added endpoint in the API, `/api/v2/bulk/job_launch`. This endpoint accepts JSON and you can specify a list of unified job templates (such as job templates and project updates) to launch. The user must have the appropriate permission to launch all the jobs. If all jobs are not launched an error is returned indicating why the operation was not able to complete. Use the `OPTIONS` request to return relevant schema. For more information, see [Use the REST API to browse, query, filter, and authenticate](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_controller_api_tools "Representational State Transfer (REST) relies on a stateless, client/server, and cacheable communications protocol, usually the HTTP protocol.")

## Set extra variables in job templates

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

## Relaunch a job template

Relaunching a job template creates a new job based on a previous job.

Instead of manually relaunching a job, a relaunch is denoted by setting `launch_type` to `relaunch`. The relaunch behavior deviates from the launch behavior in that it does not inherit `extra_vars`.

Job relaunching does not go through the inherit logic. It uses the same `extra_vars` that were calculated for the job being relaunched.

 **Example**

You launch a job template with no `extra_vars` which results in the creation of a job called **j1**. Then you edit the job template and add `extra_vars` (such as adding `"{ "hello": "world" }"`).

Relaunching **j1** results in the creation of **j2**, but because there is no inherit logic and **j1** has no extra_vars, **j2** does not have any `extra_vars`.

If you launch the job template with the `extra_vars` that you added after the creation of **j1**, the relaunch job created (**j3**) includes the extra_vars. Relaunching **j3** results in the creation of **j4**, which also includes `extra_vars`.

## Delete a job template

You can delete job templates in automation controller when they are no longer needed.

### About this task

Before deleting a job template, ensure that it is not used in a workflow job template.

### Procedure

 Delete a job template using the following method:

- Click the ⋮ icon and select the Delete Template ![Delete Template](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/delete-button.png) icon, or
- Select the required job template, on the **Details** page click the ⋮ icon and select ![Delete template](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/delete-button.png)Delete template.  Note:
      If deleting items that are used by other work items, a message opens listing the items that are affected by the deletion and prompts you to confirm the deletion. Some screens contain items that are invalid or previously deleted, and will fail to run.

## Store host facts in cache for faster playbook execution

Automation controller can store and retrieve facts on a per-host basis through an Ansible Fact Cache plugin. This behavior is configurable on a per-job template basis.

Fact caching is turned off by default but can be enabled to serve fact requests for all hosts in an inventory related to the job running. This enables you to use job templates with `--limit` while still having access to the entire inventory of host facts. You can specify a global timeout setting that the plugin enforces per-host, (in seconds) from the navigation panel, select Settings> (and then)Automation Execution> (and then)Job and edit the **Per-Host Ansible Fact Cache Timeout** field.

After launching a job that uses fact cache (`use_fact_cache=True`), each host’s `ansible_facts` are all stored by the controller in the job’s inventory.

The Ansible Fact Cache plugin that includes automation controller is enabled on jobs with fact cache enabled (`use_fact_cache=True`).

When a job that has fact cache enabled (`use_fact_cache=True`) has run, automation controller restores all records for the hosts in the inventory. Any records with update times newer than the currently stored facts per-host are updated in the database.

New and changed facts are logged through automation controller’s logging facility. Specifically, to the `system_tracking namespace` or logger. The logging payload includes the following fields:

-  `host_name`
-  `inventory_id`
-  `ansible_facts`


`ansible facts` is a dictionary of all Ansible facts for `host_name` in the automation controller inventory, `inventory_id`.

 Note:

If a hostname includes a forward slash (/), fact cache does not work for that host. If you have an inventory with 100 hosts and one host has a / in the name, the remaining 99 hosts still collect facts.

### Benefits of fact caching

Fact caching saves you time over running fact gathering. If you have a playbook in a job that runs against a thousand hosts and forks, it can take 10 minutes to gather facts across all of those hosts.

If you run a job on a regular basis, the first run of it caches these facts and the next run pulls them from the database. This reduces the runtime of jobs against large inventories.

 Note:

Do not change the ansible.cfg file to apply fact caching. Custom fact caching could conflict with the controller’s fact caching feature. You must use the fact caching module that includes automation controller.

You can select to use cached facts in your job by checking the **Enable fact storage** option when you create or edit a job template.

The following is an example playbook that uses the Ansible `clear_facts` meta task.

```
- hosts: all
  gather_facts: false
  tasks:
    - name: Clear gathered facts from all currently targeted hosts
      meta: clear_facts
```
You can find the API endpoint for fact caching at:

http://<controller server name>/api/v2/hosts/x/ansible_facts
