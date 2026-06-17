+++
title = "Tune performance for Event-Driven Ansible - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_eda_performance_tuning"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_eda_performance_tuning/", "Tune performance for Event-Driven Ansible"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_eda_performance_tuning/aem-page/optimize-assembly_eda_performance_tuning.html"
last_crumb = "Tune performance for Event-Driven Ansible"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Tune performance for Event-Driven Ansible"
oversized = "false"
page_slug = "optimize-assembly_eda_performance_tuning"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-assembly_eda_performance_tuning"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-assembly_eda_performance_tuning/toc/toc.json"
type = "aem-page"
+++

# Tune performance for Event-Driven Ansible

Event-Driven Ansible controller provides the interface in which Event-Driven Ansible automation performs. Tune your Event-Driven Ansible controller to optimize performance and scalability through:

- Characterizing your workload
- Performance troubleshooting
- System level monitoring

## Characterize your workload

Characterize your workload by quantifying event ingestion rate and concurrent rulebook activations to effectively optimize performance and capacity.

Consider the following factors to characterize your Event-Driven Ansible controller workload:

1. Number of simultaneous rulebook activations
2. Number of events received by Event-Driven Ansible controller

## Modify the default memory limit for each rulebook activation

Memory usage is based on the number of events that Event-Driven Ansible controller has to process. By default, each rulebook activation container has a 200 MB memory limit.

### About this task

For example, with 4 CPU and 16 GB of RAM, one rulebook activation container with an assigned 200 MB memory limit cannot handle more than 150,000 events per minute. If the number of parallel running rulebook activations is higher, then the maximum number of events each rulebook activation can process is reduced.

If there are too many incoming events at a very high rate, the container can run out of memory trying to process the events, which will kill the container, and your rulebook activation will fail with a status code of 137.

To mitigate this status, you can modify the default memory limit for each rulebook activation *during* or *after* installation.

### Procedure

1.  Perform the following steps to modify your default memory limit for your rulebook activations *during* installation:
  1.  Navigate to the setup inventory file.
  2.  Add `automationedacontroller_podman_mem_limit` in the [all:vars] section. For example, `automationedacontroller_podman_mem_limit='400m'`.
  3.  Run the setup.
2.  Perform the following steps to modify your default memory limit for your rulebook activations *after* installation:
  1.  Navigate to the environment file at `/etc/ansible-automation-platform/eda/settings.yaml`.
  2.  Modify the default container memory limit. For example, `PODMAN_MEM_LIMIT = '300m'`.
  3.  Restart the Event-Driven Ansible controller services using `automation-eda-controller-service restart`.

## System level monitoring for Event-Driven Ansible controller

After characterizing your workload to determine how many rulebook activations you are running in parallel and how many events you are receiving at any given point, conduct system-level monitoring to ensure the host environment can sustain the resource demands of the event-driven workload.

Using system level monitoring to review information about Event-Driven Ansible’s performance over time helps when diagnosing problems or when considering capacity for future growth.

System level monitoring includes the following information:

- Disk I/O
- RAM utilization
- CPU utilization
- Network traffic


Higher CPU, RAM, or Disk utilization can affect the overall performance of Event-Driven Ansible controller.

For example, a high utilization of any of these system level resources indicates that either the Event-Driven Ansible controller is running too many rulebook activations, or some of the individual rulebook activations are using a high volume of resources. In this case, you must increase your system level resources to support your workload.
