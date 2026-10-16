# Configure instance groups from the API
## Job slice considerations

When setting up job slices, consider the following:

- A sliced job creates a workflow job, which then creates jobs.
- A job slice consists of a job template, an inventory, and a slice count.
- When executed, a sliced job splits each inventory into "slice size" chunks and queues an ansible-playbook run on each chunk. Each run receives a shortened inventory that contains only the hosts in that slice. Completed sliced jobs are labeled on the **Jobs** list with the number of sliced jobs that ran.
![Sliced jobs list view](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-sliced-job-shown-jobs-list-view.png)
- Sliced jobs follow normal scheduling behavior, including number of forks, queuing due to capacity, and assignment to instance groups based on inventory mapping.
- Any job that must orchestrate across hosts, rather than only applying changes to individual hosts, must not be configured as a slice job.
- If a sliced job fails, automation controller does not attempt to discover or account for the specific failed playbooks.

