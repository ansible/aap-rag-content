# View output for your playbook job runs

You can run playbook jobs to run Ansible playbooks on one or more managed nodes directly from the automation controller interface without creating a job template.

Use playbook run jobs to perform tasks that are more complex than those that can be accomplished with remote command execution. Any task that you can describe as an Ansible Playbook can be run on a host or group of hosts in your inventory. You can manage your systems quickly and easily. Because of an RBAC engine and detailed audit logging, you know which user has completed a specific task.

When a playbook is run, the results display in the **Output** tab. If used, the Ansible CLI displays the same information. This can be useful for debugging.

The events summary displays the following events that are run as part of this playbook:

- The number of times this playbook has run is shown in the **Plays** field
- The number of tasks associated with this playbook is shown in the **Tasks** field
- The number of hosts associated with this playbook is shown in the **Hosts** field
- The amount of time it took to complete the playbook run is shown in the **Elapsed** field

![Job events summary](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-jobs-events-summary.png)


You can Relaunch job, Cancel job, download ![Download](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/download.png) the job output, or delete ![Delete](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/delete-button.png) the job.

Hover over a section of the host status bar in the **Output** view and the number of hosts associated with that status displays.

The output for a playbook job is also available after launching a job from the **Jobs** tab of its **Jobs Templates** page. View its host details by clicking the line item tasks in the output.

