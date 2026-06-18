+++
template = "docs/aem-title.html"
title = "Dynamic fields - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_dynamic_fields"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_dynamic_fields/aem-page/develop-ref_dynamic_fields.html"
last_crumb = "Dynamic fields"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Dynamic fields"
oversized = "false"
page_slug = "develop-ref_dynamic_fields"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_dynamic_fields"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_dynamic_fields/toc/toc.json"
type = "aem-page"
+++

# Dynamic fields

Dynamic fields appear or disappear based on user selections. Use the `dependencies` keyword with `allOf` and `if`/`then` to define conditional field visibility.

This lets you build forms where selecting a value in one field reveals additional fields relevant to that selection.

Dynamic fields are useful for:

- Showing advanced options only when the user enables them.
- Displaying different configuration fields based on a resource type or category selection.
- Requesting a reason or justification when the user selects a specific option.
