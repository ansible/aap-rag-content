# Planning your cluster environment

Learn about prerequisites and considerations for setting up a cluster.

Note the following considerations when setting up your cluster environment:

- PostgreSQL is a standalone instance and is not clustered. Automation controller does not manage replica configuration or database failover (if the user configures standby replicas).
- When you start a cluster, the database node must be a standalone server, and PostgreSQL must not be installed on one of the automation controller nodes.
- PgBouncer is not recommended for connection pooling with automation controller. Automation controller relies on `pg_notify` for sending messages across various components, and therefore, `PgBouncer` cannot readily be used in transaction pooling mode.
- All instances must be reachable from all other instances and they must be able to reach the database. It is also important for the hosts to have a stable address or hostname (depending on how the automation controller host is configured).
- All instances must be geographically collocated, with reliable low-latency connections between instances.
- To upgrade to a clustered environment, your primary instance must be part of the `default` group in the inventory and it needs to be the first host listed in the `default` group.
- Manual projects must be manually synced to all instances by the customer, and updated on all instances at once.
- The `inventory` file for platform deployments should be saved or persisted. If new instances are to be provisioned, the passwords, configuration options, and host names, must be made available to installation program.

## Cluster settings

Configure an automation controller cluster installation.

Provisioning new instances for a VM-based install involves updating the inventory file and re-running the setup playbook. It is important that the inventory file has all passwords and information used when installing the cluster or other instances might be reconfigured. The inventory file has a single inventory group,`automation controller`.

All instances are responsible for various housekeeping tasks related to task scheduling, such as determining where jobs are supposed to be launched and processing playbook events, as well as periodic cleanup.

Relevant inventory file examples include the following.

Note:

If no groups are selected for a resource, then the `automationcontroller` group is used, but if any other group is selected, then the `automationcontroller` group is not used in any way.

```
[automationcontroller]
hostA
hostB
hostC
[instance_group_east]
hostB
hostC
[instance_group_west]
hostC
hostD

```

When a playbook runs on an individual controller instance in a cluster, the output of that playbook is broadcast to all of the other nodes as part of automation controller’s WebSocket-based streaming output functionality. You must handle this data broadcast by using internal addressing by specifying a private routable address for each node in your inventory, as shown in the following example.

```
[automationcontroller]
hostA routable_hostname=10.1.0.2
hostB routable_hostname=10.1.0.3
hostC routable_hostname=10.1.0.4
routable_hostname
```

Note:

Earlier versions of automation controller used the variable name `rabbitmq_host`. If you are upgrading from an earlier version of the platform, and you specified `rabbitmq_host` in your inventory, rename `rabbitmq_host` to `routable_hostname` before upgrading.

### Instances and ports

Ports and instances used by automation controller and also required by the on-premise automation hub node are as follows:

- Port 80, 443 (normal automation controller and automation hub ports)
- Port 22 (SSH - ingress only required)
- Port 5432 (database instance - if the database is installed on an external instance, it must be opened to automation controller instances)

## Cluster health

Validate cluster health and understand how services behave during failures.

Automation controller reports as much status as possible using the browser API at `/api/v2/ping` to validate the health of the cluster. This includes the following status information:

- The instance servicing the HTTP request
- The timestamps of the last heartbeat of all other instances in the cluster
- Instance Groups and Instance membership in those groups

View more details about Instances and Instance Groups, including running jobs and membership information at `/api/v2/instances/` and `/api/v2/instance_groups/`.

### Instance services

*Table 1. Services running on each cluster instance*

| Service           | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| HTTP services     | This includes the automation controller application itself and external web services.                       |
| Callback receiver | Receives job events from running Ansible jobs.                                                              |
| Dispatcher        | The worker queue that processes and runs all jobs.                                                          |
| Redis             | This key value store is used as a queue for event data propagated from ansible-playbook to the application. |
| Rsyslog           | The log processing service used to deliver logs to various external logging services.                       |

Automation controller is configured so that if any of these services or their components fail, then all services are restarted. If these fail often in a short span of time, then the entire instance is placed offline in an automated fashion to allow remediation without causing unexpected behavior.

## Automation jobs in a clustered environment

Automation controller configured in a clustered environments allow job execution on any instance within the cluster.

The way jobs are run and reported to a *normal* user of automation controller does not change. On the system side, note the following differences:

- When a job is submitted from the API interface it is pushed into the dispatcher queue. Each automation controller instance connects to and receives jobs from that queue using a scheduling algorithm. Any instance in the cluster is just as likely to receive the work and run the task. If an instance fails while executing jobs, then the work is marked as permanently failed.

*Figure 1. Job runtime workflow for clusters*
![The job runtime workflow for clusters graphic shows how jobs submitted to a single API interface are distributed across hosts in a cluster.](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-clustering-visual.png)

- Project updates run successfully on any instance that could potentially run a job. Projects synchronize themselves to the correct version on the instance immediately before running the job. If the required revision is already locally checked out and Galaxy or Collections updates are not required, then a sync cannot be performed.
- When the synchronization happens, it is recorded in the database as a project update with a `launch_type = sync` and `job_type = run`. Project syncs do not change the status or version of the project; instead, they update the source tree only on the instance where they run.
- If updates are required from Galaxy or Collections, a sync is performed that downloads the required roles, consuming more space in your `/tmp file`. In cases where you have a large project (around 10 GB), disk space on `/tmp` can be an issue.
- If updates are required from Galaxy or Collections, a sync is performed that downloads the required roles, consuming more space in your `/tmp file`. In cases where you have a large project (around 10 GB), disk space on `/tmp` can be an issue.

### Running jobs in a cluster

Automation controller supports running jobs on a cluster of instances.

By default, when a job is submitted to the automation controller queue, it can be picked up by any of the workers. However, you can control where a particular job runs, such as restricting the instances from which a job runs on.

To support taking an instance offline temporarily, there is a property enabled defined on each instance. When this property is disabled, no jobs are assigned to that instance. Existing jobs finish, but no new work is assigned.

**Troubleshooting**

When you issue a `cancel` request on a running automation controller job, automation controller issues a `SIGINT` to the ansible-playbook process. While this causes Ansible to stop dispatching new tasks and exit, in many cases, module tasks that were already dispatched to remote hosts will run to completion. This behavior is similar to pressing `Ctrl-c` during a command-line Ansible run.With respect to software dependencies, if a running job is canceled, the job is removed but the dependencies remain.

## Deprovision cluster instances

Deprovision an instance from an automation controller cluster.

### About this task

Re-running the setup playbook does not automatically deprovision instances because clusters do not currently distinguish between an instance that was taken offline intentionally or due to failure. Instead, shut down all services on the automation controller instance and then run the deprovisioning tool from any other instance.

### Procedure

1.  Shut down the instance or stop the service with the command: `automation-controller-service stop `.
2.  Run the following deprovision command from another instance to remove it from the automation controller cluster: $ awx-manage deprovision_instance --hostname=<name used in inventory file.
3.  The following is an example deprovision command:`$ awx-manage deprovision_instance --hostname=hostB`
4.  Restart the services on the remaining instances with the command:`automation-controller-service start`.

### What to do next

Deprovisioning instance groups in automation controller does not automatically deprovision or remove instance groups.
