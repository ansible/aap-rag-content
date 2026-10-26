# Distribute automation across a large number of hosts with job slicing
## Job slicing scaling behavior

Job slicing is intended to scale job executions horizontally. Enabling job slicing on a job template divides the target inventory into the number of slices configured at launch time, and then starts a job for each slice.

Set the number of slices equal to or less than the number of hybrid or execution nodes. You can also limit a job template to specific instances through its instance groups.

Sliced job templates that use prompts or extra variables behave the same as standard job templates: all variables and limits apply to the entire set of slice jobs in the resulting workflow job. However, if a limit causes any slice to have no hosts assigned, that slice fails, which causes the overall job to fail.

Automation controller calculates the status of a distributed job in the same way as a workflow job. The job fails if any of its sub-jobs have unhandled failures.

Note:

You can set a very high number of job slices, but doing so can degrade performance. The job scheduler is not designed to schedule thousands of workflow nodes at once. Each sliced job becomes one such node.

