+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_upgrade_api_changes"
title = "API changes for platform gateway - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_upgrade_api_changes/aem-page/assembly_upgrade_api_changes.html"
last_crumb = "API changes for platform gateway"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "API changes for platform gateway"
oversized = "false"
page_slug = "assembly_upgrade_api_changes"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/assembly_upgrade_api_changes"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_upgrade_api_changes/toc/toc.json"
type = "aem-page"
+++

# API changes for platform gateway

Ansible Automation Platform uses a platform gateway that provides centralized API access to all services. While APIs for automation controller, automation hub, and Event-Driven Ansible remain accessible directly for backward compatibility, this direct access will be removed in a future release.

These changes impact your organization if you have API calls implemented directly with automation controller or private automation hub, or if you are integrating directly with automation controller or private automation hub hosts. You must migrate these integrations to the API endpoints exposed through the platform gateway to ensure they are not disrupted when direct service API access is removed in a future Ansible Automation Platform release.

For detailed API reference information, see the following sources:

- For platform gateway APIs, see the browsable API at `https://<gateway server name>/api/gateway/v1`.
- For automation controller APIs, see the browsable API at `https://<gateway server name>/api/controller/v2`.
- For automation hub APIs, see **Automation Hub API** in *API Catalog and Documentation*.
- For Event-Driven Ansible APIs, see the browsable API at `https://<gateway server name>/api/eda/v1`.
