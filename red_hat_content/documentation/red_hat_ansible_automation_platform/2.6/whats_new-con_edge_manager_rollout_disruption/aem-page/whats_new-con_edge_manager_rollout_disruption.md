+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_rollout_disruption"
title = "Define a rollout disruption budget - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_rollout_disruption/aem-page/whats_new-con_edge_manager_rollout_disruption.html"
last_crumb = "Define a rollout disruption budget"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Define a rollout disruption budget"
oversized = "false"
page_slug = "whats_new-con_edge_manager_rollout_disruption"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_rollout_disruption"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_rollout_disruption/toc/toc.json"
type = "aem-page"
+++

# Define a rollout disruption budget

A rollout disruption budget defines the acceptable level of service impact during a rollout. This ensures that a deployment does not take down too many devices at once, maintaining overall system stability.

## Disruption budget parameters

Configure rollout disruption parameters, such as grouping criteria (`groupBy`) and availability limits (`minAvailable`, `maxUnavailable`), to control the maximum acceptable service impact during fleet updates and keep overall system stability.

- `groupBy`: Defines how devices are grouped when applying the disruption budget. The grouping is done by label keys.
- `minAvailable`: Specifies the minimum number of devices that must remain available during a rollout.
- `maxUnavailable`: Limits the number of devices that can be unavailable at the same time.


 **Example**

The following shows an example YAML configuration for a fleet specification:

```
apiVersion: v1alpha1
kind: Fleet
metadata:
  name: default
spec:
  selector:
    matchLabels:
      fleet: default
  rolloutPolicy:
    disruptionBudget:
      groupBy: ['site', 'function']
      minAvailable: 1
      maxUnavailable: 10
```
In this example, the grouping is performed on 2 label keys: **site** and **function**. A group for disruption budget consists of all devices in a fleet having the same label values for the preceding label keys. For every such group the conditions defined in this specification are continuously enforced.
