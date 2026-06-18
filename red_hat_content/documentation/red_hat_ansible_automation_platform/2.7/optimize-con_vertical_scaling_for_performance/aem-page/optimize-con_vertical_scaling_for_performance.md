+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_vertical_scaling_for_performance"
title = "Vertically scale tested deployment models to improve performance - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_vertical_scaling_for_performance/", "Vertically scale tested deployment models to improve performance"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-con_vertical_scaling_for_performance/aem-page/optimize-con_vertical_scaling_for_performance.html"
last_crumb = "Vertically scale tested deployment models to improve performance"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Vertically scale tested deployment models to improve performance"
oversized = "false"
page_slug = "optimize-con_vertical_scaling_for_performance"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/optimize-con_vertical_scaling_for_performance"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-con_vertical_scaling_for_performance/toc/toc.json"
type = "aem-page"
+++

# Vertically scale tested deployment models to improve performance

Vertical scaling increases the physical resources available to a service, including the CPU, memory, disk volume, and disk Input/Output Operations per Second (IOPS). Use vertical scaling for deployments with high resource utilization or workload demand.

## Benefits of vertical scaling

- Relieves resource contention: Applications have access to more resources and this can relieve resource contention or exhaustion.

## Drawbacks and other considerations for vertical scaling

- Extensive testing required: The installation program attempts to tune application and system configurations to use additional resources, but not all components of the application automatically scale in relation to machine size. Manually tuning each variable requires extensive testing. For this reason, after an instance size has been verified for an environment, horizontal scaling by adding more instances of the same size is recommended.
- Application-level limitations: For VM-based installation or Containerized deployments, instances with more than 64 CPU cores and 128 GB of RAM might not scale linearly due to system and application-level limits.
- Resource overcommit: Overcommitting virtual machine resources (for example, allocating more virtual CPU/RAM to guests than is physically available on the host) leads to unpredictable performance.
- CPU throttling: In OpenShift Container Platform, setting a CPU `limit` without an equivalent `request` can lead to CPU throttling, even if the node has spare CPU capacity. This throttling negatively impacts API latency.   * To mitigate this, always set CPU `requests` equal to CPU `limits`.
  * Monitor CPU throttling using the `container_cpu_cfs_throttled_seconds_total` metric.
- Database limitations: Scaling the application increases the maximum potential number of database connections from worker processes and the overall memory, I/O, and CPU utilization of the PostgreSQL instance. As you scale past the tested deployment models, deploy your separate Postgres instances per component (platform gateway, Event-Driven Ansible, automation controller, automation hub).
