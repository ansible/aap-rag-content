+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-define_where_automation_runs_with_host_and_node_groupings"
title = "Define where automation runs with host and node groupings - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-define_where_automation_runs_with_host_and_node_groupings/", "Define where automation runs with host and node groupings"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-define_where_automation_runs_with_host_and_node_groupings/aem-page/administer-define_where_automation_runs_with_host_and_node_groupings.html"
last_crumb = "Define where automation runs with host and node groupings"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Define where automation runs with host and node groupings"
oversized = "false"
page_slug = "administer-define_where_automation_runs_with_host_and_node_groupings"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-define_where_automation_runs_with_host_and_node_groupings"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-define_where_automation_runs_with_host_and_node_groupings/toc/toc.json"
type = "aem-page"
+++

# Define where automation runs with host and node groupings

Managing hosts and controlling where automation jobs run ensures efficient resource utilization and proper workload distribution across your infrastructure. Define which systems to manage and organize execution capacity to align with your operational requirements.

Defining where automation runs helps you to:

- **Target the right systems**: Organize hosts into inventories to define which systems to manage and ensure automation runs against the correct infrastructure components.
- **Control where jobs run**: Group instances into instance groups and assign them to resources to control where jobs run and manage capacity.
- **Optimize resource allocation**: Balance automation workloads across available capacity by configuring how instance groups distribute jobs.

## How Ansible Automation Platform supports host and node groupings

Ansible Automation Platform uses two grouping mechanisms:

- **Hosts and inventories** define which systems you want to manage. A host is a system managed by Ansible Automation Platform. It can be a physical server, a virtual machine, a cloud-based server, or another device. Group hosts in inventories and use patterns to select which hosts or groups to target when running automation.
- **Instance groups** organize instances together to control where automation jobs run. Assign instance groups to organizations, inventories, or job templates. When you launch a job, the platform checks for instance groups associated with the job template, then the inventory, then the organization in that order. The platform then runs the job on the instance group with available capacity.
