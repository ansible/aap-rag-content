+++
title = "General changes - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/ref_upgrade_api_general_changes"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/ref_upgrade_api_general_changes/aem-page/ref_upgrade_api_general_changes.html"
last_crumb = "General changes"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "General changes"
oversized = "false"
page_slug = "ref_upgrade_api_general_changes"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/ref_upgrade_api_general_changes"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/ref_upgrade_api_general_changes/toc/toc.json"
type = "aem-page"
+++

# General changes

In Ansible Automation Platform 2.5 and later, API endpoints across components changed with the addition of platform gateway.

| Component                 | 2.4 and earlier endpoints start with… | 2.5 and later endpoints start with… | Notes                                                                                                   |
| ------------------------- | ------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| <br>Automation controller | <br> `/api/v2/`                       | <br> `/api/controller/v2/`          |                                                                                                         |
| <br>Automation hub        | <br> `/api/automation-hub`            | <br> `/api/galaxy/v1`               | <br>This is the default path, but this path can be changed. For example: `https://<local_hub_URL>/api/` |
| <br>Platform gateway      | <br>Not applicable                    | <br> `/api/gateway/v1/`             |                                                                                                         |
| <br>Event-Driven Ansible  | <br>Not applicable                    | <br> `/api/eda/v1/`                 |                                                                                                         |
