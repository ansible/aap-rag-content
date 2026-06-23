# Distribute automation across a large number of hosts with job slicing
## Job slice execution behavior

When jobs are sliced, they can run on any node. Insufficient capacity in the system can cause some to run at a different time. When slice jobs are running, job details display the workflow and job slices currently running, and a link to view their details individually.

By default, job templates are not normally configured to execute simultaneously (you must check `allow_simultaneous` in the API or **Concurrent jobs** in the UI). Slicing overrides this behavior and implies `allow_simultaneous` even if that setting is clear. See [Job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .") for information about how to specify this, and the number of job slices on your job template configuration.

The [Job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .") section provides additional detail on performing the following operations in the UI:

- Launch workflow jobs with a job template that has a slice number greater than one.
- Cancel the whole workflow or individual jobs after launching a slice job template.
- Relaunch the whole workflow or individual jobs after slice jobs finish running.
- View the details about the workflow and slice jobs after launching a job template.
- Search slice jobs specifically after you create them, according to the [Searching job slices](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_job_slicing#controller-search-job-slices "You can search for job slices and their parent workflow jobs by using the search functionality in Automation controller.") section.

