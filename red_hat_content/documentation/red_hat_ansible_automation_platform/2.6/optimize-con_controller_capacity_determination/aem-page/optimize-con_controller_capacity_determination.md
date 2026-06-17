+++
title = "How job capacity is determined and impacts job runs - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_controller_capacity_determination"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_pod_spec_modifications/", "Performance tuning for operator environments"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-con_controller_capacity_determination/aem-page/optimize-con_controller_capacity_determination.html"
last_crumb = "How job capacity is determined and impacts job runs"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "How job capacity is determined and impacts job runs"
oversized = "false"
page_slug = "optimize-con_controller_capacity_determination"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-con_controller_capacity_determination"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-con_controller_capacity_determination/toc/toc.json"
type = "aem-page"
+++

# How job capacity is determined and impacts job runs

The automation controller capacity system determines how many jobs can run on an instance given the amount of resources available to the instance and the size of the jobs that are running (referred to as Impact). The algorithm used to determine this is based on the following two things:

- How much memory is available to the system (`mem_capacity`)
- How much processing capacity is available to the system (`cpu_capacity`)


Capacity also impacts instance groups. Since groups are made up of instances, instances can also be assigned to multiple groups. This means that impact to one instance can affect the overall capacity of other groups.

Instance groups, not instances themselves, can be assigned to be used by jobs at various levels.

When the Task Manager prepares its graph to decide the group a job runs on, it commits the capacity of an instance group to a job that is not ready to start yet.

In smaller configurations, if only one instance is available for a job to run, the Task Manager enables that job to run on the instance even if it pushes the instance over capacity. This guarantees that jobs do not get stuck as a result of an under-provisioned system.

## Resource determination for capacity algorithm

Capacity algorithms determine how many forks a system is capable of running simultaneously. These algorithms control how many systems Ansible can communicate with simultaneously.

Increasing the number of forks an automation controller system is running enables jobs to run faster by performing more work in parallel. However, this increases the load on the system, which can cause work to slow down.

The default, `mem_capacity`, enables you to over-commit processing resources while protecting the system from running out of memory. If most of your work is not processor-bound, then selecting this mode maximizes the number of forks.

## Memory relative capacity

The memory relative capacity option allows you to set the maximum number of concurrent tasks (forks) that can run on a controller based on the amount of memory available on the system. This setting is useful for systems where memory is a limiting factor for running Ansible jobs.

`mem_capacity` is calculated relative to the amount of memory needed per fork. Taking into account the overhead for internal components, this is about 100MB per fork. When considering the amount of memory available to Ansible jobs, the capacity algorithm reserves 2GB of memory to account for the presence of other services. The algorithm formula for this is:

```
(mem - 2048) / mem_per_fork
```
The following is an example:

```
(4096 - 2048) / 100 == ~20
```
A system with 4GB of memory is capable of running 20 forks. The value `mem_per_fork` is controlled by setting the value of `SYSTEM_TASK_FORKS_MEM`, which defaults to 100.

## CPU relative capacity

automation controller uses the `cpu_capacity` algorithm to determine the relative CPU capacity of managed nodes. This information is used to optimize the distribution of tasks across the available nodes.

Ansible workloads are often processor-bound. In such cases, you can reduce the simultaneous workload to enable more tasks to run faster and reduce the average time-to-completion of those jobs.

Just as the `mem_capacity` algorithm adjusts the amount of memory required per fork, the `cpu_capacity` algorithm adjusts the amount of processing resources required per fork. The baseline value for this is four forks per core. The algorithm formula for this is:

```
cpus * fork_per_cpu
```
For example, a 4-core system looks like the following:

```
4 * 4 == 16
```
You can control the value of `fork_per_cpu` by setting the value of `SYSTEM_TASK_FORKS_CPU` which defaults to 4.
