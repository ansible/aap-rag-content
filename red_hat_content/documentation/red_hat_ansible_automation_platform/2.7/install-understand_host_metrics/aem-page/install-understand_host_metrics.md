+++
title = "Understand host metrics - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-understand_host_metrics"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_aap_activate_2/", "Activate your subscription"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-understand_host_metrics/aem-page/install-understand_host_metrics.html"
last_crumb = "Understand host metrics"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Understand host metrics"
oversized = "false"
page_slug = "install-understand_host_metrics"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-understand_host_metrics"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-understand_host_metrics/toc/toc.json"
type = "aem-page"
+++

# Understand host metrics

You can use host metrics to accurately count node usage and ensure subscription compliance. If a host is no longer in use or otherwise should not be counted towards the subscription total, you can soft delete it.

To view your host metrics, in the navigation pane, select Automation Analytics >Host Metric. The Host Metrics dashboard provides high level automation run details per managed host, including:

- The first and last time a host was automated.
- The number of times automation has been run or attempted to be run against a host.
- The number of times a managed host has been deleted.
The ability to view the number of times automation has been run on hosts enables you to:

- View your most commonly automated hosts.
- More accurately reflect the scope of your automation landscape.

## Soft deletion

Soft deletion enables the removal of decommissioned hosts from the Host Metrics view and excludes them from any potential managed node counting. Additionally, the following host types can also be deleted:

- Ephemeral, uniquely provisioned hosts, such as those used for CI-CD, or testing only.
- Bench provisioning or temporary hosts.
- Older hosts that have been decommissioned and are never automated against.

Soft deletion is intended for legitimate use case scenarios only. It must not be used to violate subscription counting, for example, for the purposes of node recycling.
