+++
title = "Search syntax - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-search_syntax"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-search_and_filter_resources/", "Search and filter resources"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-search_syntax/aem-page/develop-search_syntax.html"
last_crumb = "Search syntax"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Search syntax"
oversized = "false"
page_slug = "develop-search_syntax"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-search_syntax"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-search_syntax/toc/toc.json"
type = "aem-page"
+++

# Search syntax

A search query consists of a field name, a colon, and a value. If you omit the colon, the platform treats the input as a simple string search.

## Syntax rules

- Use `field:value` to search a specific field.
- Use a plain string without a colon to run an `icontains` search against the name and description fields.
- Separate multiple terms with a space to return results that match all terms. Wrap terms in quotes to match the exact phrase.

Note:

Job template searches accept alphanumeric characters only.

## Examples

| Query                       | Behavior                                                                                                                                                                                                 |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name:localhost`            | Searches for`localhost` in the`name` field. If the field name does not match a known field or related field, the query is treated as a string search.                                                    |
| `organization.name:Default` | Related field search. The period separates the related model from the field. You can chain multiple periods for deeper lookups.                                                                          |
| `foobar`                    | Simple string search. Runs`?search=foobar`, which performs an`icontains` lookup against name and description. Note that API field names might differ from the UI labels, for example,`Management job` in the UI is`system_job` in the API. |
| `organization:Default`      | Related field search without specifying a sub-field. Runs an`icontains` search against both the name and description of the related organization.                                                        |
