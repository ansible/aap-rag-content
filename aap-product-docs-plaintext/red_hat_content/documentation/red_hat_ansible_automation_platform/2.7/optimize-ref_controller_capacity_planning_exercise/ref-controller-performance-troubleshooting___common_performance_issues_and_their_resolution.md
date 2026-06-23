# Example capacity planning exercise
## Troubleshoot common performance issues
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
