+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_data_collection_details"
title = "Details about data collected for Automation Analytics - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-con_user_data_tracking/", "Get insights on automation across your environment with Automation Analytics"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_data_collection_details/aem-page/optimize-ref_controller_data_collection_details.html"
last_crumb = "Details about data collected for Automation Analytics"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Details about data collected for Automation Analytics"
oversized = "false"
page_slug = "optimize-ref_controller_data_collection_details"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_data_collection_details"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-ref_controller_data_collection_details/toc/toc.json"
type = "aem-page"
+++

# Details about data collected for Automation Analytics

Learn about the specific data that automation controller collects and sends to Red Hat when you enable Automation Analytics.

Automation Analytics collects the following classes of data from automation controller:

- Basic configuration, such as which features are enabled, and what operating system is being used
- Topology and status of the automation controller environment and hosts, including capacity and health
- Counts of automation resources:
  * organizations, teams, and users
  * inventories and hosts
  * credentials (indexed by type)
  * projects (indexed by type)
  * templates
  * schedules
  * active sessions
  * running and pending jobs
- Job execution details (start time, finish time, launch type, and success)
- Automation task details (success, host id, playbook/role, task name, and module used)


You can use `awx-manage gather_analytics` (without `--ship`) to inspect the data that automation controller sends, so that you can satisfy your data collection concerns. This creates a .tar file that contains the analytics data that is sent to Red Hat.

This file contains several JSON and CSV files. Each file contains a different set of analytics data.

## Automation Analytics Data Dictionary

Automation Analytics Data is sent to the Red Hat Hybrid Cloud Console (HCC) to provide detailed analytics on your automation.

The data dictionary outlines the information collected by Automation Analytics from the Red Hat Ansible Automation Platform automation controller, also known as Automation Execution.
