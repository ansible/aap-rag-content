+++
template = "docs/aem-title.html"
title = "Horizontally scale tested deployment models to improve performance - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_horizontal_scaling_for_performance"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_horizontal_scaling_for_performance/", "Horizontally scale tested deployment models to improve performance"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-con_horizontal_scaling_for_performance/aem-page/optimize-con_horizontal_scaling_for_performance.html"
last_crumb = "Horizontally scale tested deployment models to improve performance"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Horizontally scale tested deployment models to improve performance"
oversized = "false"
page_slug = "optimize-con_horizontal_scaling_for_performance"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-con_horizontal_scaling_for_performance"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-con_horizontal_scaling_for_performance/toc/toc.json"
type = "aem-page"
+++

# Horizontally scale tested deployment models to improve performance

Horizontal scaling involves increasing the number of replicas (pods or virtual machines) for a given service. Similar to vertical scaling, this approach is useful for high resource utilization or workload scaling.

## Benefits of horizontal scaling

- Improved availability: Distributes load across more instances to reduce the impact of a single slow or failing node.
- Redundancy: Provides extra capacity, allowing individual service nodes to recover or cool-off without impacting overall availability.
- Increased authentication capacity: Scaling the platform gateway directly increases the platform’s authentication throughput, because each platform gateway pod includes its own authentication service.
- Repeatable scaling procedure: After the instance size and configuration are verified for your environment, deploy identical instances to scale.

## Drawbacks and other considerations for horizontal scaling

- Database limitations: Scaling the application increases the maximum potential number of database connections from worker processes. This also increases the overall memory, I/O, and CPU utilization of the PostgreSQL instance. When you scale past the tested deployment models, deploy separate PostgreSQL instances per component (platform gateway, Event-Driven Ansible, automation controller, automation hub).
- Health Check Overhead: In a mesh architecture, each Envoy proxy sends health checks to every other cluster member. Horizontal scaling increases this baseline traffic, adding to system usage.
