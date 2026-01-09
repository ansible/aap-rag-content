# 5. Jobs in automation controller
## 5.2. SCM inventory jobs




When you synchronize an inventory source that is configured to use a source control management (SCM) system, such as Git, automation controller creates and runs an SCM inventory job. This job pulls the latest inventory data from the SCM repository and updates the inventory in automation controller.

SCM inventory jobs function similarly to standard inventory source update jobs, but they specifically handle the interaction with the SCM system. These jobs ensure that the inventory data in automation controller remains up-to-date with the latest changes made in the SCM repository.

When an inventory sourced from an SCM, for example git, is executed, the results are displayed in the **Output** tab. If used, the Ansible CLI displays the same information. This can be useful for debugging.

Use the navigation menu toRelaunch job,Cancel job, download![Download](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/8a61e20c21c53f44e207c84d454159ec/download.png)
the job output, or delete![Delete](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/6cfc80c0460fa4d4d18be2d2f5df16fa/delete-button.png)
the job.

