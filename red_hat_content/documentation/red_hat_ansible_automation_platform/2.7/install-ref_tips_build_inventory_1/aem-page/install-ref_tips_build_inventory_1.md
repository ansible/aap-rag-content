+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_tips_build_inventory_1"
template = "docs/aem-title.html"
title = "Tips for building inventories - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_tips_build_inventory_1/aem-page/install-ref_tips_build_inventory_1.html"
last_crumb = "Tips for building inventories"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Tips for building inventories"
oversized = "false"
page_slug = "install-ref_tips_build_inventory_1"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_tips_build_inventory_1"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_tips_build_inventory_1/toc/toc.json"
type = "aem-page"
+++

# Tips for building inventories

When building inventories for Ansible automation, consider the following best practices to ensure efficient and effective management of your hosts.

- Ensure that group names are meaningful and unique.
- Group names are also case sensitive.
- Do not use spaces, hyphens, or preceding numbers (use `floor_19`, not `19th_floor`) in group names.
- Group hosts in your inventory logically according to their What, Where, and When:
  * What: Group hosts according to the topology, for example: db, web, leaf, spine, metrics.
  * Where: Group hosts by geographic location, for example: data center, region, floor, building.
  * When: Group hosts by stage, for example: development, test, staging, production.

Note:

Metrics service deployment requirements:

- Metrics service must be included when automation controller is present. The `[automationmetrics]` inventory group is required in all deployments with `[automationcontroller]`.
