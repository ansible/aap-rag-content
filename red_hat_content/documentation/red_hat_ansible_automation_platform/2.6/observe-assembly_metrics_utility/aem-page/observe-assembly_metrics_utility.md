+++
template = "docs/aem-title.html"
title = "Generate consumption-based billing reports with the metrics-utility - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_metrics_utility"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_metrics_utility/", "Generate consumption-based billing reports with the metrics-utility"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-assembly_metrics_utility/aem-page/observe-assembly_metrics_utility.html"
last_crumb = "Generate consumption-based billing reports with the metrics-utility"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Generate consumption-based billing reports with the metrics-utility"
oversized = "false"
page_slug = "observe-assembly_metrics_utility"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/observe-assembly_metrics_utility"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-assembly_metrics_utility/toc/toc.json"
type = "aem-page"
+++

# Generate consumption-based billing reports with the `metrics-utility`

The Ansible Automation Platform metrics utility tool (`metrics-utility`) is a command-line utility that is installed on a system containing an instance of automation controller.

When installed and configured, `metrics-utility` gathers billing-related metrics from your system and creates a consumption-based billing report. The `metrics-utility` tool is especially suited for users who have multiple managed hosts and want to use consumption-based billing. After a report is generated, it is deposited in a target location that you specify in the configuration file.

`metrics-utility` collects two types of data from your system: configuration data and reporting data.

The configuration data includes the following information:

- Version information for automation controller and for the operating system
- Subscription information
- The base URL


The reporting data includes the following information:

- Job name and ID
- Hostname
- Inventory name
- Organization name
- Project name
- Success or failure information
- Report date and time


To ensure that `metrics-utility` continues to work as configured, clear your report directories of outdated reports regularly.
