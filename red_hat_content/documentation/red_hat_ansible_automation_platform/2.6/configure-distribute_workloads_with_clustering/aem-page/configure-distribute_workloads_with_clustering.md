+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/configure-distribute_workloads_with_clustering"
template = "docs/aem-title.html"
title = "Distribute workloads with clustering - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/configure-distribute_workloads_with_clustering/", "Distribute workloads with clustering"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/configure-distribute_workloads_with_clustering/aem-page/configure-distribute_workloads_with_clustering.html"
last_crumb = "Distribute workloads with clustering"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Distribute workloads with clustering"
oversized = "false"
page_slug = "configure-distribute_workloads_with_clustering"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/configure-distribute_workloads_with_clustering"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/configure-distribute_workloads_with_clustering/toc/toc.json"
type = "aem-page"
+++

# Distribute workloads with clustering

Clustering is sharing load between hosts. Each instance must be able to act as an entry point for UI and API access.

Note:

Administrators can use load balancers in front of as many instances as they want and keep good data visibility. However, load balancing is optional, and it is possible to have ingress on one or all instances as needed.

Each instance must be able to join the automation controller cluster and to expand its ability to run jobs. This is a simple system where jobs can run anywhere rather than be directed on where to run. Also, you can group clustered instances into different pools or queues, called instance groups.

Ansible Automation Platform supports container-based clusters by using Kubernetes, meaning you can install new automation controller instances on this platform without any variation or diversion in functionality. You can create instance groups to point to a Kubernetes container.

The following operating systems are supported for establishing a clustered environment:

Supported operating systems

- Red Hat Enterprise Linux 8 or later
