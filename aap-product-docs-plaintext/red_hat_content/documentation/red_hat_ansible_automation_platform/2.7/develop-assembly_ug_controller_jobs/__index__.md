# Use jobs to run playbooks against an inventory of hosts

A job is an instance of automation controller launching an Ansible Playbook against an inventory of hosts.

The **Jobs** list view displays a list of jobs and their statuses, shown as completed successfully, failed, or as an active (running) job. The default view is collapsed (Compact) with the job name, status, job type, start, and finish times. You can click the arrow ![Arrow](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/arrow.png) icon to expand and see more information. You can sort this list by various criteria, and perform a search to filter the jobs of interest.


![Jobs list expanded](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-jobs-list-all-expanded.png)


From this screen you can complete the following tasks:

- In the **Domains** taskbar you can specify a domain to make relevant resources easily accessible. Click the ![Wrench](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/wrench.png) icon to edit the existing labels or Add Domain to set up your own.
- View details and standard output of a particular job
- Relaunch ![Launch](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rightrocket.png) jobs
- Cancel or delete selected jobs


The relaunch operation only applies to relaunches of playbook runs and does not apply to project or inventory updates, system jobs, and workflow jobs. When a job relaunches, the **Output** view is displayed. Selecting any type of job also takes you to the **Output** view for that job, where you can filter jobs by various criteria:


![Job details view filters](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-job-details-view-filters.png)


- The **Event** option in the **Search output** list enables you to filter by the events of interest, such as errors, host failures, host retries, and items skipped. You can include as many events in the filter as necessary.
