# Distribute automation across a large number of hosts with job slicing

A sliced job refers to the concept of a distributed job. Use distributed jobs for running a job across a large number of hosts.

You can then run many ansible-playbooks, each on a subset of an inventory that you can be schedule in parallel across a cluster.

By default, Ansible runs jobs from a single control instance. For jobs that do not require cross-host orchestration, job slicing takes advantage of automation controller’s ability to distribute work to many nodes in a cluster.

Job slicing works by adding a Job Template field `job_slice_count`, which specifies the number of jobs into which to slice the Ansible run. When this number is greater than `1`, automation controller generates a workflow from a job template instead of a job. The inventory is distributed evenly among the slice jobs. The workflow job is then started, and proceeds as though it were a normal workflow.

When launching a job, the API returns either a job resource (if `job_slice_count = 1`) or a workflow job resource. The corresponding User Interface (UI) redirects to the appropriate screen to display the status of the run.

## Job slice considerations

When setting up job slices, consider the following:

- A sliced job creates a workflow job, which then creates jobs.
- A job slice consists of a job template, an inventory, and a slice count.
- When executed, a sliced job splits each inventory into several "slice size" chunks. It then queues jobs of ansible-playbook runs on each chunk of the appropriate inventory. The inventory fed into ansible-playbook is a shortened version of the original inventory that only has the hosts in that particular slice. The completed sliced job that displays on the **Jobs** list are labeled accordingly, with the number of sliced jobs that have run:
![Sliced jobs list view](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-sliced-job-shown-jobs-list-view.png)
- These sliced jobs follow normal scheduling behavior (number of forks, queuing due to capacity, assignation to instance groups based on inventory mapping).  Note:
Job slicing is intended to scale job executions horizontally. Enabling job slicing on a job template divides an inventory to be acted upon in the number of slices configured at launch time and then starts a job for each slice.

Normally, the number of slices is equal to or less than the number of hybrid or execution nodes. A job template can also be limited to certain instances through its instance groups. You can set an extremely high number of job slices but it can cause performance degradation. The job scheduler is not designed to simultaneously schedule thousands of workflow nodes, which are what the sliced jobs become.

* Sliced job templates with prompts or extra variables behave the same as standard job templates, applying all variables and limits to the entire set of slice jobs in the resulting workflow job. However, when passing a limit to a sliced job, if the limit causes slices to have no hosts assigned, those slices will fail, causing the overall job to fail.
* A job slice job status of a distributed job is calculated in the same manner as workflow jobs. It fails if there are any unhandled failures in its sub-jobs.

- Any job that intends to orchestrate across hosts (rather than just applying changes to individual hosts) must not be configured as a slice job.
- If a sliced job fails, automation controller does not attempt to discover or account for the specific failed playbooks.

## Job slice execution behavior

When jobs are sliced, they can run on any node. Insufficient capacity in the system can cause some to run at a different time. When slice jobs are running, job details display the workflow and job slices currently running, and a link to view their details individually.

By default, job templates are not normally configured to execute simultaneously (you must check `allow_simultaneous` in the API or **Concurrent jobs** in the UI). Slicing overrides this behavior and implies `allow_simultaneous` even if that setting is clear. See [Job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .") for information about how to specify this, and the number of job slices on your job template configuration.

The [Job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .") section provides additional detail on performing the following operations in the UI:

- Launch workflow jobs with a job template that has a slice number greater than one.
- Cancel the whole workflow or individual jobs after launching a slice job template.
- Relaunch the whole workflow or individual jobs after slice jobs finish running.
- View the details about the workflow and slice jobs after launching a job template.
- Search slice jobs specifically after you create them, according to the [Searching job slices](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_job_slicing#controller-search-job-slices "You can search for job slices and their parent workflow jobs by using the search functionality in Automation controller.") section.

## Search job slices

You can search for job slices and their parent workflow jobs by using the search functionality in Automation controller.

### About this task

To make it easier to find slice jobs, use the search functionality to apply a search filter to:

- Job lists to show only slice jobs
- Job lists to show only parent workflow jobs of job slices
- Job template lists to only show job templates that produce slice jobs

### Procedure

Search for slice jobs by using one of the following methods:

- To show only slice jobs in job lists, as with most cases, you can filter either on the type (jobs here) or `unified_jobs`:

```
/api/v2/jobs/?job_slice_count__gt=1
```

- To show only parent workflow jobs of job slices:

```
/api/v2/workflow_jobs/?job_template__isnull=false
```

- To show only job templates that produce slice jobs:

```
/api/v2/job_templates/?job_slice_count__gt=1
```
