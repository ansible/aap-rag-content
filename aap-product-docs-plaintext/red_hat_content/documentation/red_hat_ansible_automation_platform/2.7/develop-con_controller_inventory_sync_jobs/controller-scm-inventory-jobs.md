# Sync inventory data with external sources
## Sync inventory data with a source control management system

When you synchronize an inventory source that is configured to use a source control management (SCM) system, such as Git, automation controller creates and runs an SCM inventory job. This job pulls the latest inventory data from the SCM repository and updates the inventory in automation controller.

SCM inventory jobs function similarly to standard inventory source update jobs, but they specifically handle the interaction with the SCM system. These jobs ensure that the inventory data in automation controller remains up-to-date with the latest changes made in the SCM repository.

When an inventory sourced from an SCM, for example git, is executed, the results are displayed in the **Output** tab. If used, the Ansible CLI displays the same information. This can be useful for debugging.

Use the navigation menu to Relaunch job, Cancel job, download ![Download](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/download.png) the job output, or delete ![Delete](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/delete-button.png) the job.

