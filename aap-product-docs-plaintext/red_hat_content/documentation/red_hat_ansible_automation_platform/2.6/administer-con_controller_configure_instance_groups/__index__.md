# Configure instance groups from the API

You can configure instance groups in automation controller using the REST API.

You can create instance groups by POSTing to `/api/v2/instance_groups` as a system administrator.

Once created, you can associate instances with an instance group by using:

```
HTTP POST /api/v2/instance_groups/x/instances/ {'id': y}`
```
An instance that is added to an instance group automatically reconfigures itself to listen on the group’s work queue. For more information, see Instance group policies.

## Instance group policies

You can configure automation controller instances to automatically join instance groups when they come online by defining a policy. These policies are evaluated for every new instance that comes online.

Instance group policies are controlled by the following three optional fields on an `Instance Group`:

- `policy_instance_percentage`: This is a number between 0 - 100. It guarantees that this percentage of active automation controller instances are added to this instance group. As new instances come online, if the number of instances in this group relative to the total number of instances is less than the given percentage, then new ones are added until the percentage condition is satisfied.
- `policy_instance_minimum`: This policy attempts to keep at least this many instances in the instance group. If the number of available instances is lower than this minimum, then all instances are placed in this instance group.
- `policy_instance_list`: This is a fixed list of instance names to always include in this instance group.


The **Instance Groups** list view from the automation controller user interface (UI) provides a summary of the capacity levels for each instance group according to instance group policies:


![Instance Groups list view](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-instance-groups-list-view.png)

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

## Job runtime behavior

When you run a job associated with an instance group, note the following behaviors:

- If you divide a cluster into separate instance groups, then the behavior is similar to the cluster as a whole.
- If you assign two instances to a group then either one is as likely to receive a job as any other in the same group.
- As automation controller instances are brought online, it effectively expands the work capacity of the system.
- If you place those instances into instance groups, then they also expand that group’s capacity.
- If an instance is performing work and it is a member of multiple groups, then capacity is reduced from all groups for which it is a member.
- De-provisioning an instance removes capacity from the cluster wherever that instance was assigned. For more information, see the [Deprovisioning instance groups](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_controller_configure_instance_groups#controller-deprovision-instance-group "Re-running the setup playbook won't deprovision instances, as clusters can't distinguish between intentional offline status or failure. Instead, shut down all services on the automation controller instance, then run the deprovisioning tool from another instance.") section.


Note:

Not all instances are required to be provisioned with an equal capacity.

## Pin instances manually to specific instance groups

If you have a special instance that needs to be only assigned to a specific instance group but do not want it to automatically join other groups by "percentage" or "minimum" policies, you can pin an instance manually to specific groups.,

### Procedure

1.  Add the instance to one or more instance groups' `policy_instance_list`.
2.  Update the instance’s `managed_by_policy` property to be `False`. This prevents the instance from being automatically added to other groups based on percentage and minimum policy. It only belongs to the groups you have manually assigned it to:

```
HTTP PATCH /api/v2/instance_groups/N/
{
"policy_instance_list": ["special-instance"]
}
HTTP PATCH /api/v2/instances/X/
{
"managed_by_policy": False
}
```

## Capacity limits for instance groups

There is external business logic that can drive the need to limit the concurrency of jobs sent to an instance group, or the maximum number of forks to be consumed.

For traditional instances and instance groups, you might want to enable two organizations to run jobs on the same underlying instances, but limit each organization’s total number of concurrent jobs. This can be achieved by creating an instance group for each organization and assigning the value for `max_concurrent_jobs`.

For automation controller groups, automation controller is generally not aware of the resource limits of the OpenShift cluster. You can set limits on the number of pods on a namespace, or only resources available to schedule a certain number of pods at a time if no auto-scaling is in place. In this case, you can adjust the value for `max_concurrent_jobs`.

Another parameter available is `max_forks`. This provides additional flexibility for capping the capacity consumed on an instance group or container group. You can use this if jobs with a wide variety of inventory sizes and "forks" values are being run. You can limit an organization to run up to 10 jobs concurrently, but consume no more than 50 forks at a time:

```
max_concurrent_jobs: 10
max_forks: 50
```
If 10 jobs that use 5 forks each are run, an eleventh job waits until one of these finishes to run on that group (or be scheduled on a different group with capacity).

If 2 jobs are running with 20 forks each, then a third job with a `task_impact` of 11 or more waits until one of these finishes to run on that group (or be scheduled on a different group with capacity).

For container groups, using the `max_forks` value is useful given that all jobs are submitted using the same `pod_spec` with the same resource requests, irrespective of the "forks" value of the job. The default `pod_spec` sets requests and not limits, so the pods can "burst" above their requested value without being throttled or reaped. By setting the `max_forks value`, you can help prevent a scenario where too many jobs with large forks values get scheduled concurrently and cause the OpenShift nodes to be oversubscribed with multiple pods by using more resources than their requested value.

To set the maximum values for the concurrent jobs and forks in an instance group, see [Creating an instance group](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_set_up_virtual_machines#controller-create-instance-group "You can create instance groups with Automation controller to organize and manage your instances.").

## Deprovision instance groups

Re-running the setup playbook won't deprovision instances, as clusters can't distinguish between intentional offline status or failure. Instead, shut down all services on the automation controller instance, then run the deprovisioning tool from another instance.

### Procedure

1.  Shut down the instance or stop the service with the following command:


```
automation-controller-service stop
```

2.  Run the following deprovision command from another instance to remove it from the controller cluster registry:


```
awx-manage deprovision_instance --hostname=<name used in inventory file>
```
For example:

```
awx-manage deprovision_instance --hostname=hostB
```

### What to do next

Deprovisioning instance groups in automation controller does not automatically deprovision or remove instance groups, even though re-provisioning often causes these to be unused. They can still show up in API endpoints and stats monitoring. You can remove these groups with the following command:

```
awx-manage unregister_queue --queuename=<name>
```
Removing an instance’s membership from an instance group in the inventory file and re-running the setup playbook does not ensure that the instance is not added back to a group. To be sure that an instance is not added back to a group, remove it through the API and also remove it in your inventory file. You can also stop defining instance groups in the inventory file. You can manage instance group topology through the automation controller UI. For more information about managing instance groups in the UI, see [Managing Instance Groups](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_ug_controller_instance_groups#controller-instance-groups "An Instance Group enables you to group instances in a clustered environment. Policies dictate how instance groups behave and how jobs are executed. The following view displays the capacity levels based on policy algorithms:").

Note:

If you have isolated instance groups created in older versions of automation controller (3.8.x and earlier) and want to migrate them to execution nodes to make them compatible for use with the automation mesh architecture, see [Migrate isolated instances to execution nodes](https://legacy-controller-docs.ansible.com/automation-controller/4.4/html/upgrade-migration-guide/upgrade_to_ees.html#migrate-iso-to-exe) in the *Ansible Automation Platform Upgrade and Migration Guide*.
