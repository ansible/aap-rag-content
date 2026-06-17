+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_settings_control_execution_nodes"
title = "Capacity settings for each node type - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_controller_improving_performance/", "Tune automation controller to improve performance"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_settings_control_execution_nodes/aem-page/optimize-ref_controller_settings_control_execution_nodes.html"
last_crumb = "Capacity settings for each node type"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Capacity settings for each node type"
oversized = "false"
page_slug = "optimize-ref_controller_settings_control_execution_nodes"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_settings_control_execution_nodes"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_settings_control_execution_nodes/toc/toc.json"
type = "aem-page"
+++

# Capacity settings for each node type

Configure capacity settings for control and execution nodes to manage resource allocation effectively.

The following settings impact capacity calculations on the cluster. Set them to the same value on all control nodes by using the following file-based settings.

- `AWX_CONTROL_NODE_TASK_IMPACT`: Sets the impact of controlling jobs. You can use it when your control plane exceeds required CPU or memory usage to control the number of jobs that your control plane can run at the same time.
- `SYSTEM_TASK_FORKS_CPU` and `SYSTEM_TASK_FORKS_MEM`: Influence how many resources are estimated to be consumed by each fork of Ansible. By default, 1 fork of Ansible is estimated to use 0.25 of a CPU and 100 Mb of memory.

## Capacity settings for instance group and container group

When using container groups or instance groups to run automation jobs, you can configure capacity settings to limit the number of concurrent jobs and forks that can be used.

Use the `max_concurrent_jobs` and `max_forks` settings available on instance groups to limit how many jobs and forks can be consumed across an instance group or container group.

- To calculate the `max_concurrent_jobs` you need on a container group consider the `pod_spec` setting for that container group. In the `pod_spec`, you can see the resource requests and limits for the automation job pod. Use the following equation to calculate the maximum concurrent jobs that you need:

```
((number of worker nodes in kubernetes cluster) * (CPU available on each worker)) / (CPU request on pod_spec) = maximum number of concurrent jobs
```
  * For example, if your `pod_spec` indicates that a pod will request 250 mcpu Kubernetes cluster has 1 worker node with 2 CPU, the maximum number of jobs that you need to start with is 8.

- You can also consider the memory consumption of the forks in the jobs. Calculate the appropriate setting of `max_forks` with the following equation:

```
((number of worker nodes in kubernetes cluster) * (memory available on each worker)) / (memory request on pod_spec) = maximum number of forks
```
  * For example, given a single worker node with 8 GB of Memory, we determine that the `max forks` we want to run is 81. This way, either 39 jobs with 1 fork can run (task impact is always forks + 1), or 2 jobs with forks set to 39 can run.

- You might have other business requirements that motivate using `max_forks` or `max_concurrent_jobs` to limit the number of jobs launched in a container group.

## Adjust settings for scheduling jobs

The controller uses a task manager to schedule jobs onto instances.

The task manager periodically collects tasks that need to be scheduled and determines what instances have capacity and are eligible for running them. The task manager has the following workflow:

1. Find and assign the control and execution instances.
2. Update the job’s status to waiting.
3. Message the control node through `pg_notify` for the dispatcher to pick up the task and start running it.


If the scheduling task is not completed within `TASK_MANAGER_TIMEOUT` seconds (default 300 seconds), the task is terminated early. Timeout issues generally arise when there are thousands of pending jobs.

One way the task manager limits how much work it can do in a single run is the `START_TASK_LIMIT` setting. This limits how many jobs it can start in a single run. The default is 100 jobs. If more jobs are pending, a new scheduler task is scheduled to run immediately after. Users who are willing to have potentially longer latency between when a job is launched and when it starts, to have greater overall throughput, can consider increasing the `START_TASK_LIMIT`. To see how long individual runs of the task manager take, use the Prometheus metric `task_manager__schedule_seconds`, available in `/api/v2/metrics`.

Jobs elected to begin running by the task manager do not do so until the task manager process exits and commits its changes. The `TASK_MANAGER_TIMEOUT` setting determines how long a single run of the task manager will run for before committing its changes. When the task manager reaches its timeout, it attempts to commit any progress it made. The task is not actually forced to exit until after a grace period (determined by `TASK_MANAGER_TIMEOUT_GRACE_PERIOD`) has passed.

## VM installation settings for internal cluster routing

Automation controller cluster hosts communicate across the network within the cluster. In the inventory file for the traditional VM installer, you can indicate several routes to the cluster nodes that are used in different ways:

**Example**:

```
[automationcontroller]
controller1 ansible_user=ec2-user ansible_host=10.10.12.11 node_type=hybrid routable_hostname=somehost.somecompany.org
```


- `controller1` is the inventory hostname for the automation controller host. The inventory hostname is what is shown as the instance hostname in the application. This can be useful when preparing for disaster recovery scenarios where you want to use the backup/restore method to restore the cluster to a new set of hosts that have different IP addresses. In this case you can have entries in `/etc/hosts` that map these inventory hostnames to IP addresses, and you can use internal IP addresses to mitigate any DNS issues when it comes to resolving public DNS names.
- `ansible_host=10.10.12.11` indicates how the installation program reaches the host, which in this case is an internal IP address. This is not used outside of the installation program.
- `routable_hostname=somehost.somecompany.org` indicates the hostname that is resolvable for the peers that connect to this node on the receptor mesh. Since it can cross many networks, we are using a hostname that maps to an IP address resolvable for the receptor peers.

## Tune the web server

The Control and Hybrid nodes each serve the UI and API of automation controller. WSGI traffic is served by the uwsgi web server on a local socket. ASGI traffic is served by Daphne. NGINX listens on port 443 and proxies traffic as needed.

To scale automation controller’s web service, follow these best practices:

- Deploy multiple control nodes and use a load balancer to spread web requests over multiple servers.
- Set max connections per automation controller to 100.


To optimize automation controller’s web service on the client side, follow these guidelines:

- Direct user to use dynamic inventory sources instead of individually creating inventory hosts by using the API.
- Use webhook notifications instead of polling for job status.
- Use the bulk APIs for host creation and job launching to batch requests.
- Use token authentication. For automation clients that must make many requests very quickly, using tokens is a best practice, because depending on the type of user, there might be additional overhead when using Basic authentication.
