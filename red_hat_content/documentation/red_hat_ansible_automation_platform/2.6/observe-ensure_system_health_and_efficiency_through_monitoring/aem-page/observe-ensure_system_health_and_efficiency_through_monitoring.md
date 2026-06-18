+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-ensure_system_health_and_efficiency_through_monitoring"
title = "Ensure system health and efficiency through monitoring - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-ensure_system_health_and_efficiency_through_monitoring/", "Ensure system health and efficiency through monitoring"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-ensure_system_health_and_efficiency_through_monitoring/aem-page/observe-ensure_system_health_and_efficiency_through_monitoring.html"
last_crumb = "Ensure system health and efficiency through monitoring"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Ensure system health and efficiency through monitoring"
oversized = "false"
page_slug = "observe-ensure_system_health_and_efficiency_through_monitoring"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/observe-ensure_system_health_and_efficiency_through_monitoring"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-ensure_system_health_and_efficiency_through_monitoring/toc/toc.json"
type = "aem-page"
+++

# Ensure system health and efficiency through monitoring

Monitor your deployment to maintain system health and identify performance issues before they affect operations. Track application metrics and system resources to understand workload patterns and optimize capacity allocation.

 Monitoring your deployment helps you to:

- **Track application performance**: Monitor job status, system performance, and event processing to identify bottlenecks and understand how jobs impact your deployment.
- **Manage system resources**: Monitor CPU, memory, and disk performance to prevent resource exhaustion and maintain optimal system responsiveness.
- **Optimize capacity allocation**: Use monitoring data to adjust instance capacity settings and balance workloads across available resources based on actual usage patterns.

## How Ansible Automation Platform supports monitoring

Ansible Automation Platform provides metrics endpoints for job status and subsystem performance data. Access these endpoints to view job output processing, scheduling, and other operational metrics.

## Metrics for monitoring automation controller application

For application level monitoring, automation controller provides Prometheus-style metrics on an API endpoint `/api/v2/metrics`. Use these metrics to check data about job status and subsystem performance, such as for job output processing or job scheduling.

The metrics endpoint includes descriptions of each metric. Metrics of particular interest for performance include:

-  `awx_status_total`
  * Current total of jobs in each status. Helps correlate other events to activity in system.
  * Can check upticks in errored or failed jobs.
- awx_instance_remaining_capacity
  * Amount of capacity remaining for running additional jobs.
-  `callback_receiver_event_processing_avg_seconds`
  * colloquially called “job events lag”.
  * Running average of the lag time between when a task occurred in ansible and when the user is able to see it. This indicates how far behind the callback receiver is in processing events. When this number is very high, users can consider scaling up the control plane or using the capacity adjustment feature to reduce the number of jobs a control node controls.
-  `callback_receiver_events_insert_db`
  * Counter of events that have been inserted by a node. Can be used to calculate the job event insertion rate over a given time period.
-  `callback_receiver_events_queue_size_redis`
  * Indicator of how far behind callback receiver is in processing events. If too high, Redis can cause the control node to run out of memory (OOM).

## System level monitoring

Monitoring CPU and memory is vital since instance capacity management doesn't introspect host resource usage. Automation impact varies by playbook; cloud modules process on the execution node, while native modules like "yum" perform work on target hosts, leaving the node waiting for results.

If CPU or memory usage is very high, consider lowering the capacity adjustment (available on the instance detail page) on affected instances in the automation controller. This limits how many jobs are run on or controlled by this instance.

Monitor the disk I/O and use of your system. The manner in which an automation controller node runs Ansible and caches output on the file system, and eventually saves it in the database, creates high levels of disk reads and writes. Identifying poor disk performance early can help prevent poor user experience and system degradation.
