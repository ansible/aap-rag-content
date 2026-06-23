# View output for your playbook job runs
## Playbook run details

Learn how to view the details of a playbook run in Automation controller.

Access the **Details** tab to view details about the job execution:


![Job details for example run](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-job-details-for-example-job.png)


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

