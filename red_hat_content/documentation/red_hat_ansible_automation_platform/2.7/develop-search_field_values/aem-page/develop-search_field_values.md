+++
title = "Search field values - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-search_field_values"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-search_and_filter_resources/", "Search and filter resources"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-search_field_values/aem-page/develop-search_field_values.html"
last_crumb = "Search field values"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Search field values"
oversized = "false"
page_slug = "develop-search_field_values"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-search_field_values"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-search_field_values/toc/toc.json"
type = "aem-page"
+++

# Search field values

You can determine the available search fields and related search fields for any resource by sending an `OPTIONS` request to the API endpoint.

## Procedure

1.  Send a `GET` request to the resource endpoint to identify the available field names.
      Field names come from the keys returned in the `GET` response. The `url`, `related`, and `summary_fields` keys are excluded.

      To search for jobs by type, enter `type:run` on the Jobs page. To discover valid values for the `type` field, send an `OPTIONS` request to `/api/v2/jobs` and locate the `"type"` entry.

2.  Send an `OPTIONS` request to the same endpoint to find related search fields.
      Related search fields are listed in the `related_search_fields` attribute of the `OPTIONS` response. Strip the `__search` suffix to get the related field name you can use in the search bar.

      The `/api/v2/jobs` endpoint returns:

```
"related_search_fields": [
    "modified_by__search",
    "project__search",
    "credentials__search",
    "created_by__search",
    "inventory__search",
    "labels__search",
    "schedule__search",
    "job_template__search",
    "instance_group__search",
    "hosts__search"
]
```

## Results

Any query that does not start with a recognized field or related field name is treated as a generic string search, equivalent to `?search=<term>`.
