# Manage resources for pods and containers
## Resource types
### Size recommendations for resource requests

All jobs that use a container group use the same pod specification. The pod specification includes the resource requests for the pod that runs the job.

All jobs use the same resource requests. The specified resource requests for your particular job on the pod specification affect how Kubernetes schedules the job pod based on resources available on worker nodes. These are the default values.

- One fork typically requires 100Mb of memory. This is set by using `system_task_forks_mem`. If your jobs have five forks, the job pod specification must request 500Mb of memory.
- For job templates that have a particularly high forks value or otherwise need larger resource requests, you should create a separate container group with a different pod spec that indicates larger resource requests. Then you can assign it to the job template. For example, a job template with the forks value of 50 must be paired with a container group that requests 5GB of memory.
- If the fork value for a job is high enough that no single pod would be able to contain the job, use the job slicing feature. This splits the inventory up such that the individual job “slices” fit in an automation pod provisioned by the container group.
