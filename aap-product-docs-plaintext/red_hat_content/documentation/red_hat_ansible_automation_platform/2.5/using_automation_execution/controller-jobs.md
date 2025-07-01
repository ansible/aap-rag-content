# Chapter 5. Jobs in automation controller




A job is an instance of automation controller launching an Ansible Playbook against an inventory of hosts.

The **Jobs** list view displays a list of jobs and their statuses, shown as completed successfully, failed, or as an active (running) job. The default view is collapsed (Compact) with the job name, status, job type, start, and finish times. You can click the arrow![Arrow](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/301c31ef51ac512bd11df2687c14dd9d/arrow.png)
icon to expand and see more information. You can sort this list by various criteria, and perform a search to filter the jobs of interest.

![Jobs list expanded](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/f750d7a4dc75820e6bdc1a63f58a8e43/ug-jobs-list-all-expanded.png)


From this screen you can complete the following tasks:

- In the **Domains** taskbar you can specify a domain to make relevant resources easily accessible. Click the![Wrench](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/7a43f0108a64710b5a161addfa9a8b3b/wrench.png)
icon to edit the existing labels orAdd Domainto set up your own.
- View details and standard output of a particular job
- Relaunch![Launch](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/15376a8ac10d1efa9ec8cb3d4c707dfd/rightrocket.png)
jobs
- Cancel or delete selected jobs


The relaunch operation only applies to relaunches of playbook runs and does not apply to project or inventory updates, system jobs, and workflow jobs. When a job relaunches, the **Output** view is displayed. Selecting any type of job also takes you to the **Output** view for that job, where you can filter jobs by various criteria:

![Job details view filters](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/57e589035d59ea50fd49c379d0acaee6/ug-job-details-view-filters.png)


- The **Event** option in the **Search output** list enables you to filter by the events of interest, such as errors, host failures, host retries, and items skipped. You can include as many events in the filter as necessary. For more information about using the search, see the [Search](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#assembly-controller-search) section.


