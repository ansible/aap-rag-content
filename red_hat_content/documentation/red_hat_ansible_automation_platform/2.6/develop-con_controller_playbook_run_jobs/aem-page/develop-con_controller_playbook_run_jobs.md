+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_controller_playbook_run_jobs"
title = "View output for your playbook job runs - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_jobs/", "Use jobs to run playbooks against an inventory of hosts"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_controller_playbook_run_jobs/aem-page/develop-con_controller_playbook_run_jobs.html"
last_crumb = "View output for your playbook job runs"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "View output for your playbook job runs"
oversized = "false"
page_slug = "develop-con_controller_playbook_run_jobs"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-con_controller_playbook_run_jobs"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_controller_playbook_run_jobs/toc/toc.json"
type = "aem-page"
+++

# View output for your playbook job runs

You can run playbook jobs to run Ansible playbooks on one or more managed nodes directly from the automation controller interface without creating a job template.

Use playbook run jobs to perform tasks that are more complex than those that can be accomplished with remote command execution. Any task that you can describe as an Ansible Playbook can be run on a host or group of hosts in your inventory. You can manage your systems quickly and easily. Because of an RBAC engine and detailed audit logging, you know which user has completed a specific task.

When a playbook is run, the results display in the **Output** tab. If used, the Ansible CLI displays the same information. This can be useful for debugging.

The events summary displays the following events that are run as part of this playbook:

- The number of times this playbook has run is shown in the **Plays** field
- The number of tasks associated with this playbook is shown in the **Tasks** field
- The number of hosts associated with this playbook is shown in the **Hosts** field
- The amount of time it took to complete the playbook run is shown in the **Elapsed** field

![Job events summary](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-jobs-events-summary.png)  


You can Relaunch job, Cancel job, download ![Download](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/download.png) the job output, or delete ![Delete](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/delete-button.png) the job.

Hover over a section of the host status bar in the **Output** view and the number of hosts associated with that status displays.

The output for a playbook job is also available after launching a job from the **Jobs** tab of its **Jobs Templates** page. View its host details by clicking the line item tasks in the output.

## Search

Use **Search** to look up specific events, hostnames, and their statuses. To filter only certain hosts with a particular status, specify one of the following valid statuses:

ok
Indicates that a task completed successfully but no change was executed on the host.

changed
The playbook task executed. Since Ansible tasks should be written to be idempotent, tasks can exit successfully without executing anything on the host. In these cases, the task returns **ok**, but not **changed**.

failed
The task failed. Further playbook execution stopped for this host.

unreachable
The host is unreachable from the network or has another unrecoverable error associated with it.

skipped
The playbook task skipped because no change was necessary for the host to reach the target state.

rescued
This shows the tasks that failed and then executes a rescue section.

ignored
This shows the tasks that failed and have `ignore_errors: yes configured`.

The following example shows a search with only unreachable hosts:


![Stdout pane unreachable](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-std-out-unreachable.png)  


For more information about using the search, see the [Search](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-search) section.

The standard output view displays the events that occur on a particular job.

Click a line of an event from the **Stdout** pane and a **Host Events** window displays in a separate window. This window shows the host that was affected by that particular event.

 Note:

Upgrading to the latest versions of Ansible Automation Platform involves progressively migrating all historical playbook output and events. This migration process is gradual, and happens automatically in the background after installation is complete. Installations with very large amounts of historical job output (tens or hundreds of GB of output) can have missing job output until migration is complete. The most recent data shows up at the top of the output, followed by older events.

## Playbook run details

Learn how to view the details of a playbook run in Automation controller.

Access the **Details** tab to view details about the job execution:


![Job details for example run](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-job-details-for-example-job.png)  


You can view the following details for an executed job:

- **Status**: It can be any of the following:
  * **Pending**: The playbook run has been created, but not queued or started yet. Any job, not just playbook runs, stay in pending until it is ready to be run by the system. Reasons for playbook runs not being ready include dependencies that are currently running (all dependencies must be completed before the next step can run), or there is not enough capacity to run in the locations it is configured to.
  * **Waiting**: The playbook run is in the queue waiting to be executed.
  * **Running**: The playbook run is currently in progress.
  * **Successful**: The last playbook run succeeded.
  * **Failed**: The last playbook run failed.
- **Job template**: The name of the job template from which this job launched.
- **Inventory**: The inventory selected to run this job against.
- **Project**: The name of the project associated with the launched job.
- **Project Status**: The status of the project associated with the launched job.
- **Playbook**: The playbook used to launch this job.
- **Execution environment**: The name of the execution environment used in this job.
- **Credentials**: The credentials used in this job.
- **Extra variables**: Any extra variables passed when creating the job template are displayed here.


Select one of these items to view the corresponding job templates, projects, and other objects.

## Playbook access and information sharing

Automation controller’s use of automation execution environments and Linux containers prevents playbooks from reading files outside of their project directory.

By default, the only data exposed to the ansible-playbook process inside the container is the current project being used.

You can customize this in the Job Settings and expose additional directories from the host into the container.

## Isolation functionality and variables

Automation controller uses container technology to isolate jobs from each other. By default, only the current project is exposed to the container running a job template.

If you need to expose additional directories, you must customize your playbook runs. To configure job isolation, you can set variables.

By default, automation controller uses the system’s `tmp` directory (`/tmp` by default) as its staging area. You can change this in the **Job Execution Path** field of the **Jobs settings** page, or in the REST API at `/api/v2/settings/jobs`:

```
AWX_ISOLATION_BASE_PATH = "/opt/tmp"
```
If there are any additional directories that should specifically be exposed from the host to the container that playbooks run in, you can specify those in the **Paths to expose to isolated jobs** field of the **Jobs Settings** page, or in the REST API at `/api/v2/settings/jobs`:

```
AWX_ISOLATION_SHOW_PATHS = ['/list/of/', '/paths']
```


 Note:

- If a path to a specific file is entered, then the entire directory containing that file will be mounted inside the execution environment.
- If your playbooks need to use keys or settings defined in `AWX_ISOLATION_SHOW_PATHS`, then add this file to `/var/lib/awx/.ssh`.

The fields described here can be found on the **Jobs settings** page:


![Jobs settings options](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/job-settings-full.png)  
