+++
title = "Job type impact on capacity - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_controller_capacity_job_impacts"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-assembly_pod_spec_modifications/", "Performance tuning for operator environments"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-con_controller_capacity_job_impacts/aem-page/optimize-con_controller_capacity_job_impacts.html"
last_crumb = "Job type impact on capacity"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Job type impact on capacity"
oversized = "false"
page_slug = "optimize-con_controller_capacity_job_impacts"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/optimize-con_controller_capacity_job_impacts"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-con_controller_capacity_job_impacts/toc/toc.json"
type = "aem-page"
+++

# Job type impact on capacity

When configuring automation controller capacity, it is important to understand how different job types impact the system capacity.

automation controller uses Ansible to run jobs. Each job can have a different impact on system resources depending on the number of forks used for the job.

The default forks value for Ansible is five. This means that, by default, each job can run tasks on up to five systems concurrently.

However, if you set up automation controller to run against fewer systems than that, then the actual concurrency value is lower.

When a job is run in automation controller, the number of forks selected is incremented by 1, to compensate for the Ansible parent process.

For example, if you run a playbook against five systems with forks value of 5, then the actual forks value from the Job Impact perspective is 6.

## Impact of job types in automation controller

Jobs and ad hoc jobs follow the preceding model, forks +1. If you set a fork value on your job template, your job capacity value is the minimum of the forks value supplied and the number of hosts that you have, plus one. The +1 is to account for the parent Ansible process.

Instance capacity determines which jobs get assigned to any specific instance. Jobs and ad hoc commands use more capacity if they have a higher forks value.

Job types including the following, have a fixed impact:

- Inventory updates: 1
- Project updates: 1
- System jobs: 5


Note:

If you do not set a forks value on your job template, your job uses Ansible’s default forks value of five. However, it uses fewer if your job has fewer than five hosts. In general, setting a forks value higher than what the system is capable of can cause issues by running out of memory or over-committing CPU. The job template fork values that you use must fit on the system. If you have playbooks using 1000 forks but none of your systems individually has that much capacity, then your systems are undersized and at risk of performance or resource issues.

## Select the correct capacity

When an instance is created, automation controller calculates the capacity of the instance based on two algorithms: CPU-bound and memory-bound. The CPU-bound algorithm calculates the number of forks based on the number of CPU cores available to the instance.

### About this task

The memory-bound algorithm calculates the number of forks based on the amount of memory available to the instance. By default, automation controller selects the minimum number of forks calculated by these two algorithms. This is to ensure that the instance does not overcommit resources. However, in some cases, you might want to adjust this behavior.

Selecting a capacity out of the CPU-bound or the memory-bound capacity limits is selecting between the minimum or maximum number of forks. In the [previous examples](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_controller_capacity_determination#controller-memory-relative-capacity "The memory relative capacity option allows you to set the maximum number of concurrent tasks (forks) that can run on a controller based on the amount of memory available on the system. This setting is useful for systems where memory is a limiting factor for running Ansible jobs."), the CPU capacity permits a maximum of 16 forks while the memory capacity permits 20. For some systems, the disparity between these can be large and you might want to have a balance between these two.

The instance field `capacity_adjustment` enables you to select how much you want to consider. It is represented as a value between 0.0 and 1.0. If set to a value of 1.0, then the largest value is used. The previous example involves memory capacity, so a value of 20 forks can be selected. If set to a value of 0.0 then the smallest value is used. A value of 0.5 is a 50/50 balance between the two algorithms, which is 18:

```
16 + (20 - 16) * 0.5 = 18
```

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instance Groups.
2.  On the **Instance Groups** list view, select the required instance.
3.  Select the **Instances** tab and adjust the **Capacity adjustment** slider. Note:
      The slider adjusts whether the instance capacity algorithm yields less forks (towards the left) or yields more forks (towards the right).
