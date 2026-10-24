+++
title = "Search limitations - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-search_limitations"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-search_and_filter_resources/", "Search and filter resources"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-search_limitations/aem-page/develop-search_limitations.html"
last_crumb = "Search limitations"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Search limitations"
oversized = "false"
page_slug = "develop-search_limitations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-search_limitations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-search_limitations/toc/toc.json"
type = "aem-page"
+++

# Search limitations

The search function has the following limitations that affect how queries are processed and combined.

- `OR` queries are not supported. All search terms are combined with `AND` logic.
- Wrap the field name in quotes to search for field names that contain spaces.
- All field searches use `__icontains` matching. For example, `name:localhost` sends `?name__icontains=localhost` to the API.
