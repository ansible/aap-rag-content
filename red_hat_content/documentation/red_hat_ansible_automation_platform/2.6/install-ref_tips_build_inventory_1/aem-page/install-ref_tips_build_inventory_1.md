+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_tips_build_inventory_1"
title = "Tips for building inventories - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_platform_install_overview/", "Install RPM-based Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_tips_build_inventory_1/aem-page/install-ref_tips_build_inventory_1.html"
last_crumb = "Tips for building inventories"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Tips for building inventories"
oversized = "false"
page_slug = "install-ref_tips_build_inventory_1"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-ref_tips_build_inventory_1"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_tips_build_inventory_1/toc/toc.json"
type = "aem-page"
+++

# Tips for building inventories

When building inventories for Ansible automation, consider the following best practices to ensure efficient and effective management of your hosts.

- Ensure that group names are meaningful and unique.
- Group names are also case sensitive.
- Do not use spaces, hyphens, or preceding numbers (use `floor_19`, not `19th_floor`) in group names.
- Group hosts in your inventory logically according to their What, Where, and When:
  * What: Group hosts according to the topology, for example: db, web, leaf, spine.
  * Where: Group hosts by geographic location, for example: data center, region, floor, building.
  * When: Group hosts by stage, for example: development, test, staging, production.
