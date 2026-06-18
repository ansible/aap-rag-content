# Example capacity planning exercise

After you have determined the workload capacity that you want to support, you must plan your deployment based on the requirements of the workload. To help you with your deployment, review the following planning exercise.

For this example, the cluster must support the following capacity:

- 300 managed hosts
- 1,000 tasks per hour per host or 16 tasks per minute per host
- 10 concurrent jobs
- Forks set to 5 on playbooks. This is the default.
- Average event size is 1 Mb


The virtual machines have 4 CPU and 16 GB RAM, and disks that have 3000 IOPS.

## Example workload requirements

Learn how to calculate workload requirements for automation controller based on a hypothetical workload.

For this example capacity planning exercise, use the following workload requirements:

**Execution capacity**

The minimum execution capacity required is 60 units to support 10 concurrent jobs.

Derive the total capacity by summing the resource consumed by parallel execution forks and the base resource consumed by each job:

(10 x jobs * 5 x forks) + (10 x jobs * 1 x base task impact of a job) = (execution capacity)

**Control capacity**

- To control 10 concurrent jobs requires at least 10 units of control capacity.
- To calculate the number of events per hour that you need to support 300 managed hosts and 1,000 tasks per hour per host, use the following equation:
* 1000 tasks x 300 managed hosts per hour = 300,000 events per hour at minimum.
* You must run the job to see exactly how many events it produces, because this is dependent on the specific task and verbosity. For example, a debug task printing “Hello World” produces 6 job events with the verbosity of 1 on one host. With a verbosity of 3, it produces 34 job events on one host. Therefore, you must estimate that the task produces at least 6 events. This would produce closer to 3,000,000 events per hour, or approximately 833 events per second.


**Determining quantity of execution and control nodes needed**

Reference the experimental results in the following table that shows the observed event processing rate of a single control node with 5 execution nodes of equal size (API Capacity column). The default “forks” setting of job templates is 5.

Using this default, the maximum number of jobs a control node can dispatch to execution nodes makes 5 execution nodes of equal CPU and RAM use 100% of their capacity, arriving to the 1:5 ratio of control to execution capacity mentioned before.

| Node                                                                       | API capacity                     | Default execution capacity | Default control capacity | Mean event processing rate at 100% capacity usage | Mean events processing rate at 50% capacity usage | Mean event processing rate at 40% capacity usage |
| -------------------------------------------------------------------------- | -------------------------------- | -------------------------- | ------------------------ | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ |
| <br>4 CPU at 2.5Ghz, 16 GB RAM control node, a maximum of 3000 IOPS disk   | <br>about 10 requests per second | <br>n/a                    | <br>137 jobs             | <br>1100 per second                               | <br>1400 per second                               | <br>1630 per second                              |
| <br>4 CPU at 2.5Ghz, 16 GB RAM execution node, a maximum of 3000 IOPS disk | <br>n/a                          | <br>137                    | <br>n/a                  | <br>n/a                                           | <br>n/a                                           | <br>n/a                                          |
| <br>4 CPU at 2.5Ghz, 16 GB RAM database node, a maximum of 3000 IOPS disk  | <br>n/a                          | <br>n/a                    | <br>n/a                  | <br>n/a                                           | <br>n/a                                           | <br>n/a                                          |


Because controlling jobs competes with job event processing on the control node, over-provisioning control capacity can reduce processing times. When processing times are high, you can experience a delay between when the job runs and when you can view the output in the API or UI.

For this example, for a workload on 300 managed hosts, executing 1000 tasks per hour per host, 10 concurrent jobs with forks set to 5 on playbooks, and an average event size 1 Mb, use the following procedure:

- Deploy 1 execution node, 1 control node, 1 database node of 4 CPU at 2.5Ghz, 16 GB RAM, and disks that have about 3000 IOPS.
- Keep the default fork setting of 5 on job templates.
- Use the capacity change feature in the instance view of the UI on the control node to reduce the capacity down to 16, the lowest value, to reserve more of the control node’s capacity for processing events.


For more information about workloads with high levels of API interaction, see [Scaling Automation Controller for API Driven Workloads](https://www.ansible.com/blog/scaling-automation-controller-for-api-driven-workloads). For more information about managing capacity with instances, see [Managing capacity with Instances](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_automation_mesh_operator_aap "Scaling your automation mesh is available on OpenShift deployments of Red Hat Ansible Automation Platform and is possible through adding or removing nodes from your cluster dynamically, using the Instances resource of the Ansible Automation Platform UI, without running the installation script."). For more information about operator-based deployments, see [Red Hat Ansible Automation Platform considerations for operator environments](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-assembly_pod_spec_modifications "A pod in Kubernetes is the smallest deployable compute unit, consisting of one or more containers sharing networking and storage on a single host. Red Hat Ansible Automation Platform uses a default pod specification, which can be customized with a user-defined YAML or JSON document.").

## Troubleshoot common performance issues

This section provides guidance on troubleshooting common performance issues with automation controller.

### Common performance issues and their resolution

**Users experience many request timeouts (504 or 503 errors), or in general high API latency. In the UI, clients face slow login and long wait times for pages to load. What system is the likely culprit?**

- If these issues occur only on login, and you use external authentication, the problem is likely with the integration of your external authentication provider and you should seek Red Hat support.
- For other issues with timeouts or high API latency, see [Web server tuning](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-ref_controller_settings_control_execution_nodes#ref-controller-web-service-tuning "The Control and Hybrid nodes each serve the UI and API of automation controller. WSGI traffic is served by the uwsgi web server on a local socket. ASGI traffic is served by Daphne. NGINX listens on port 443 and proxies traffic as needed.").


**Long wait times for job output to load.**

- Job output streams from the execution node where the ansible-playbook is actually run to the associated control node. Then the callback receiver serializes this data and writes it to the database. Relevant settings to observe and tune can be found in Settings for managing job event processing and [PostgreSQL database configuration and maintenance for automation controller](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-ref_controller_database_settings#ref-controller-database-settings "Improve the performance of automation controller, by configuring the following configuration parameters in the database:").
- In general, to resolve this symptom it is important to observe the CPU and memory use of the control nodes. If CPU or memory use is very high, you can either horizontally scale the control plane by deploying more virtual machines to be control nodes that naturally spreads out work more, or to modify the number of jobs a control node will manage at a time. For more information, see [Capacity settings for control and execution nodes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-ref_controller_settings_control_execution_nodes#ref-controller-settings-control-execution-nodes "Configure capacity settings for control and execution nodes to manage resource allocation effectively.") for more information.
- Job output delay can occur on initial job runs that use execution environments that have not been pulled into the platform. The output becomes visible after the job run completes.


**What can you do to increase the number of jobs that automation controller can run concurrently?**

- Factors that cause jobs to remain in “pending” state are:
* **Waiting for “dependencies” to finish**: this includes project updates and inventory updates when “update on launch” behavior is enabled.
* **The “allow_simultaneous” setting of the job template**: if multiple jobs of the same job template are in “pending” status, check the “allow_simultaneous” setting of the job template (“Concurrent Jobs” checkbox in the UI). If this is not enabled, only one job from a job template can run at a time.
* **The “forks” value of your job template**: the default value is 5. The amount of capacity required to run the job is roughly the forks value (some small overhead is accounted for). If the forks value is set to a very large number, this will limit what nodes will be able to run it.
* **Lack of either control or execution capacity**: see “awx_instance_remaining_capacity” metric from the application metrics available on /api/v2/metrics. See [Metrics for monitoring automation controller application](/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-ensure_system_health_and_efficiency_through_monitoring#ref-controller-metrics-monitoring "For application level monitoring, automation controller provides Prometheus-style metrics on an API endpoint /api/v2/metrics. Use these metrics to check data about job status and subsystem performance, such as for job output processing or job scheduling.") for more information about how to check metrics. See [Capacity planning for deploying automation controller](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-ref_controller_capacity_planning#ref-controller-capacity-planning "Capacity planning for automation controller is planning the scale and characteristics of your deployment so that it has the capacity to run the planned workload.") for information about how to plan your deployment to handle the number of jobs you are interested in.


**Jobs run more slowly on automation controller than on a local machine.**

- Some additional overhead is expected, because automation controller might be dispatching your job to a separate node. In this case, automation controller is starting a container and running ansible-playbook there, serializing all output and writing it to a database.
- Project update on launch and inventory update on launch behavior can cause additional delays at job start time.
- Size of projects can impact how long it takes to start the job, as the project is updated on the control node and transferred to the execution node. Internal cluster routing can impact network performance. For more information, see [Internal cluster routing](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-ref_controller_settings_control_execution_nodes#ref-controller-internal-cluster-routing "Automation controller cluster hosts communicate across the network within the cluster. In the inventory file for the traditional VM installer, you can indicate several routes to the cluster nodes that are used in different ways:").
- Container pull settings can impact job start time. The execution environment is a container that is used to run jobs within it. Container pull settings can be set to “Always”, “Never” or “If not present”. If the container is always pulled, this can cause delays.
- Ensure that all cluster nodes, including execution, control, and the database, have been deployed in instances with storage rated to the minimum required IOPS, because the manner in which automation controller runs ansible and caches event data implicates significant disk I/O. For more information, see [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_system_requirements "Use this information when planning your Red Hat Ansible Automation Platform installations and designing automation mesh topologies that fit your use case.").


**Database storage does not stop growing.**

- Automation controller has a management job titled “Cleanup Job Details”. By default, it is set to keep 120 days of data and to run once a week. To reduce the amount of data in the database, you can shorten the retention time.
- Running the cleanup job deletes the data in the database. However, the database must at some point perform its vacuuming operation which reclaims storage. See [PostgreSQL database configuration and maintenance for automation controller](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-ref_controller_database_settings#ref-controller-database-settings "Improve the performance of automation controller, by configuring the following configuration parameters in the database:") for more information about database vacuuming.
