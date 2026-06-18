+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_controller_inventory_sync_jobs"
title = "Sync inventory data with external sources - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_jobs/", "Use jobs to run playbooks against an inventory of hosts"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_controller_inventory_sync_jobs/aem-page/develop-con_controller_inventory_sync_jobs.html"
last_crumb = "Sync inventory data with external sources"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Sync inventory data with external sources"
oversized = "false"
page_slug = "develop-con_controller_inventory_sync_jobs"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-con_controller_inventory_sync_jobs"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_controller_inventory_sync_jobs/toc/toc.json"
type = "aem-page"
+++

# Sync inventory data with external sources

Inventory synchronization jobs update automation controller data by pulling the latest information from configured sources. This ensures your inventory reflects the current state of the managed infrastructure.

Inventory sync jobs can be scheduled to run at regular intervals or triggered manually by users. These jobs gather data such as host details, group memberships, and variables from various sources such as cloud providers, dynamic inventory scripts, or static files.

When an inventory synchronization is executed, the results display in the **Output** tab.

If used, the Ansible CLI displays the same information. This can be useful for debugging. The `ANSIBLE_DISPLAY_ARGS_TO_STDOUT` parameter is set to `False` for all playbook runs. This parameter matches Ansible’s default behavior and does not display task arguments in task headers in the Job **Details** interface to avoid leaking certain sensitive module parameters to `stdout`. To restore the earlier behavior, set `ANSIBLE_DISPLAY_ARGS_TO_STDOUT` to `True` through the `AWX_TASK_ENV` configuration setting.

You can Relaunch job, Cancel job, download ![Download](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/download.png) the job output, or delete ![Delete](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/delete-button.png) the job.

 Note:

You can perform an inventory update while a related job is running. In cases where you have a large project (around 10 GB), disk space on `/tmp` can be an issue.

## Inventory sync details

Access the **Details** tab to view details about the job execution:


![Show job details for inventory sync](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/sync.png)  


You can view the following details for an executed job:

- **Status**: It can be any of the following:
  * **Pending**: The inventory sync has been created, but not queued or started yet. Any job, not just inventory source syncs, stays in pending until it is ready to be run by the system. Reasons for inventory source syncs not being ready include:
    + Dependencies that are currently running (all dependencies must be completed before the next step can run).
    + Insufficient capacity to run in the locations it is configured for.
  * **Waiting**: The inventory sync is in the queue waiting to be executed.
  * **Running**: The inventory sync is currently in progress.
  * **Successful**: The inventory sync job succeeded.
  * **Failed**: The inventory sync job failed.
- **Inventory**: The name of the associated inventory group.
- **Source**: The type of cloud inventory.
- **Inventory Source Project**: The project used as the source of this inventory sync job.
- **Execution Environment**: The execution environment used.
- **Execution node**: The node used to run the job.
- **Instance Group**: The name of the instance group used with this job (automation controller is the default instance group).


Selecting these items enables you to view the corresponding job templates, projects, and other objects.

## Sync inventory data with a source control management system

When you synchronize an inventory source that is configured to use a source control management (SCM) system, such as Git, automation controller creates and runs an SCM inventory job. This job pulls the latest inventory data from the SCM repository and updates the inventory in automation controller.

SCM inventory jobs function similarly to standard inventory source update jobs, but they specifically handle the interaction with the SCM system. These jobs ensure that the inventory data in automation controller remains up-to-date with the latest changes made in the SCM repository.

When an inventory sourced from an SCM, for example git, is executed, the results are displayed in the **Output** tab. If used, the Ansible CLI displays the same information. This can be useful for debugging.

Use the navigation menu to Relaunch job, Cancel job, download ![Download](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/download.png) the job output, or delete ![Delete](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/delete-button.png) the job.

### SCM inventory details

To view details about the job execution and its associated project, select the **Details** tab.

You can view the following details for an executed job:

- **Status**: It can be any of the following:
  * **Pending**: The SCM job has been created, but not queued or started yet. Any job, not just SCM jobs, stay in pending until it is ready to be run by the system. Reasons for SCM jobs not being ready include dependencies that are currently running (all dependencies must be completed before the next step can run), or there is not enough capacity to run in the locations it is configured to.
  * **Waiting**: The SCM job is in the queue waiting to be executed.
  * **Running**: The SCM job is currently in progress.
  * **Successful**: The last SCM job succeeded.
  * **Failed**: The last SCM job failed.
- **Type**: SCM jobs display Source Control Update.
- **Project**: The name of the project.
- **Status**: Indicates whether the associated project was successfully updated.
- **Revision**: Indicates the revision number of the sourced project that was used in this job.
- **Execution environment**: Specifies the execution environment used to run this job.
- **Execution node**: Indicates the node on which the job ran.
- **Instance group**: Indicates the instance group on which the job ran, if specified.
- **Job tags**: Tags show the various job operations executed.


Select these items to view the corresponding job templates, projects, and other objects.
