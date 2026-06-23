# Sync inventory data with external sources

Inventory synchronization jobs update automation controller data by pulling the latest information from configured sources. This ensures your inventory reflects the current state of the managed infrastructure.

Inventory sync jobs can be scheduled to run at regular intervals or triggered manually by users. These jobs gather data such as host details, group memberships, and variables from various sources such as cloud providers, dynamic inventory scripts, or static files.

When an inventory synchronization is executed, the results display in the **Output** tab.

If used, the Ansible CLI displays the same information. This can be useful for debugging. The `ANSIBLE_DISPLAY_ARGS_TO_STDOUT` parameter is set to `False` for all playbook runs. This parameter matches Ansible’s default behavior and does not display task arguments in task headers in the Job **Details** interface to avoid leaking certain sensitive module parameters to `stdout`. To restore the earlier behavior, set `ANSIBLE_DISPLAY_ARGS_TO_STDOUT` to `True` through the `AWX_TASK_ENV` configuration setting.

You can Relaunch job, Cancel job, download ![Download](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/download.png) the job output, or delete ![Delete](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/delete-button.png) the job.

Note:

You can perform an inventory update while a related job is running. In cases where you have a large project (around 10 GB), disk space on `/tmp` can be an issue.

