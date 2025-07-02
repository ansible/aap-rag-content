# 5. Jobs in automation controller
## 5.1. Inventory sync jobs




When an inventory synchronization is executed, the results display in the **Output** tab.

For more information about inventory synchronization, see [Constructed inventories](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-inventories#ref-controller-constructed-inventories) .

If used, the Ansible CLI displays the same information. This can be useful for debugging. The `ANSIBLE_DISPLAY_ARGS_TO_STDOUT` parameter is set to `False` for all playbook runs. This parameter matches Ansible’s default behavior and does not display task arguments in task headers in the Job **Details** interface to avoid leaking certain sensitive module parameters to `stdout` . To restore the earlier behavior, set `ANSIBLE_DISPLAY_ARGS_TO_STDOUT` to `True` through the `AWX_TASK_ENV` configuration setting.

For more information, see [ANSIBLE_DISPLAY_ARGS_TO_STDOUT](http://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_DISPLAY_ARGS_TO_STDOUT) in the Ansible Configuration Settings.

You canRelaunch job,Cancel job, download![Download](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/8a61e20c21c53f44e207c84d454159ec/download.png)
the job output, or delete![Delete](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/6cfc80c0460fa4d4d18be2d2f5df16fa/delete-button.png)
the job.

Note
You can perform an inventory update while a related job is running. In cases where you have a large project (around 10 GB), disk space on `/tmp` can be an issue.



