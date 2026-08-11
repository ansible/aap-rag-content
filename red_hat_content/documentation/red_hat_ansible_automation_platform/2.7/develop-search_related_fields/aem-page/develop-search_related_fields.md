+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-search_related_fields"
title = "Search related fields - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-search_and_filter_resources/", "Search and filter resources"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-search_related_fields/aem-page/develop-search_related_fields.html"
last_crumb = "Search related fields"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Search related fields"
oversized = "false"
page_slug = "develop-search_related_fields"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-search_related_fields"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-search_related_fields/toc/toc.json"
type = "aem-page"
+++

# Search related fields

You can search across related resources, such as organizations or projects, by prefixing the query with the related field name.

## Procedure

 In the search bar, type the related field name followed by a colon and the search value.

You can add secondary fields separated by periods to narrow the search.

| Query                                   | Behavior                                                                     |
| --------------------------------------- | ---------------------------------------------------------------------------- |
| `organization:Default`                  | Searches the name and description of the related organization for`Default`.  |
| `job_template.project.name:"A Project"` | Searches for job templates that use a project whose name matches`A Project`. |

Note:

The required prefix depends on the endpoint. The query `job_template.project.name` applies to the `unified_job_templates` endpoint. If you search from the `job_templates` endpoint directly, omit the `job_template` prefix and use `project.name` instead.
