+++
title = "Automation dashboard deployment options - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_automation_dashboard_deployment_options"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_automation_dashboard_deployment_options/", "Automation dashboard deployment options"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_automation_dashboard_deployment_options/aem-page/install-con_automation_dashboard_deployment_options.html"
last_crumb = "Automation dashboard deployment options"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Automation dashboard deployment options"
oversized = "false"
page_slug = "install-con_automation_dashboard_deployment_options"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-con_automation_dashboard_deployment_options"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_automation_dashboard_deployment_options/toc/toc.json"
type = "aem-page"
+++

# Automation dashboard deployment options

When you are ready to measure the savings your automation delivers, choose how to deploy the automation dashboard: integrated with your Ansible Automation Platform installation (2.7 and later), or as a standalone utility on Red Hat Enterprise Linux (RHEL) (2.4 and later).

Automation dashboard calculates the time and cost savings your automation delivers so you can report on and improve the return on your automation investment. You can deploy it in two ways, depending on how you run Ansible Automation Platform and how you want to manage the dashboard over its lifecycle.

Both options present the same savings metrics and visualizations. The difference is the deployment model and how many deployments you measure, not the data you see.

## Integrated automation dashboard

The integrated automation dashboard is deployed as part of an Ansible Automation Platform 2.7 installation and is managed within the platform, under the Analytics section. You enable and configure it during installation using one of the following deployment methods:

- Containerized installation on RHEL
- Operator-based installation on Red Hat OpenShift

Because it is part of the platform, the integrated dashboard is upgraded and maintained alongside your Ansible Automation Platform deployment, and it collects data from that deployment automatically.

## Standalone automation dashboard utility (RHEL only)

The standalone automation dashboard utility is installed and managed separately from the Ansible Automation Platform installer, and is supported on RHEL only. It has its own lifecycle, including installation, configuration, data synchronization, cluster access token verification, and uninstallation.

Use the standalone utility when you want to connect to multiple Ansible Automation Platform instances, including deployments on different Ansible Automation Platform versions (2.4 and later), and aggregate their savings data in a single dashboard.

Note:

The standalone utility cannot filter the dashboard UI by source Ansible Automation Platform instance.

## Running both together

You can run the integrated dashboard and one or more standalone utilities at the same time. The Ansible Automation Platform 2.7 UI provides the integrated dashboard for that deployment, and you can also deploy the standalone utility to connect to one or more Ansible Automation Platform versions.

## Comparison

*Table 1. Integrated vs. standalone automation dashboard*

| Consideration                                    | Integrated automation dashboard                                 | Standalone utility (RHEL only)                                                                         |
| ------------------------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Where it is deployed                             | Part of the platform installation                               | Installed separately on RHEL                                                                           |
| Supported install methods                        | Containerized (RHEL) or Operator (OpenShift)                    | RHEL only                                                                                              |
| Lifecycle management                             | Upgraded and maintained with the platform                       | Installed, configured, upgraded, and uninstalled independently                                         |
| Data source                                      | The Ansible Automation Platform deployment it is installed with | One or more clusters or Ansible Automation Platform deployments, connected using cluster access tokens |
| Ansible Automation Platform version availability | Ansible Automation Platform 2.7 onwards                         | Utility can connect to Ansible Automation Platform versions 2.4 onwards                                |

## When to use each option

Use the **integrated automation dashboard** when:

- You are installing, or already running, Ansible Automation Platform 2.7 or later with the containerized or operator-based installer.
- You want the dashboard deployed, upgraded, and maintained as part of the platform.
- Your automation savings data comes from a single Ansible Automation Platform deployment.

Use the **standalone automation dashboard utility (RHEL only)** when:

- You run on RHEL and cannot or do not want to enable the dashboard during a platform installation.
- You want to connect to and aggregate savings from multiple Ansible Automation Platform deployments (2.4 and later).
- You want to manage the dashboard on its own lifecycle, separate from the platform.
