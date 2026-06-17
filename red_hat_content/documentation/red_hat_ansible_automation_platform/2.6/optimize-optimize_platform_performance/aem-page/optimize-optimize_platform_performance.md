+++
template = "docs/aem-title.html"
title = "Optimize platform performance - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-optimize_platform_performance"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-optimize_platform_performance/", "Optimize platform performance"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-optimize_platform_performance/aem-page/optimize-optimize_platform_performance.html"
last_crumb = "Optimize platform performance"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Optimize platform performance"
oversized = "false"
page_slug = "optimize-optimize_platform_performance"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-optimize_platform_performance"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-optimize_platform_performance/toc/toc.json"
type = "aem-page"
+++

# Optimize platform performance

Optimizing platform performance ensures your deployment responds efficiently to workload demands and maintains availability under load. Scale services appropriately and tune configurations to support your automation capacity requirements.

 Optimizing platform performance helps you to:

- **Maintain system responsiveness**: Scale services and adjust capacity to handle workload demands and prevent request queueing or timeouts.
- **Support growing automation workloads**: Plan deployment capacity based on your workload characteristics and add resources to accommodate increased managed hosts or concurrent jobs.
- **Resolve performance bottlenecks**: Monitor key performance indicators to identify services that require scaling and adjust configurations to improve throughput.

## How Ansible Automation Platform supports performance optimization

You can use multiple optimization approaches based on your deployment type and workload characteristics:

- **Scaling strategies** include horizontal scaling (adding more replicas) and vertical scaling (adding CPU, memory, or other resources). Scale services for platform gateway, automation controller, Event-Driven Ansible, and automation hub independently based on performance indicators.
- **Database tuning** includes configuring PostgreSQL parameters for memory allocation and maintenance operations to improve query performance and data management.
- **Capacity planning** involves characterizing workload based on managed hosts, concurrent jobs, and API request rates, then planning control and execution capacity.

## Automation execution settings

You can configure the following automation execution settings through the UI, API, or file settings:

- Live events in the automation controller UI
- Job event processing and scheduling
- Control and execution node capacity
- Instance and container groups capacity
- Internal cluster routing
- Web server tuning
