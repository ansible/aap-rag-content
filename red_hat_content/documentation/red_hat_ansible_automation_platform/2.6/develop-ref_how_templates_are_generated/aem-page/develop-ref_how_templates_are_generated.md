+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_how_templates_are_generated"
title = "How templates are generated - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_how_templates_are_generated/aem-page/develop-ref_how_templates_are_generated.html"
last_crumb = "How templates are generated"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "How templates are generated"
oversized = "false"
page_slug = "develop-ref_how_templates_are_generated"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_how_templates_are_generated"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_how_templates_are_generated/toc/toc.json"
type = "aem-page"
+++

# How templates are generated

When synchronization runs, Ansible automation portal reads Ansible Automation Platform Job Template configurations and generates corresponding templates.

## Metadata mapping

The following table shows how Ansible Automation Platform Job Template properties are mapped to template metadata fields:

| Ansible Automation Platform Job Template property | Generated template field | Transformation                                                   |
| ------------------------------------------------- | ------------------------ | ---------------------------------------------------------------- |
| Name                                              | `metadata.name`          | Converted to lowercase with hyphens                              |
| Name                                              | `metadata.title`         | Copied directly                                                  |
| Description                                       | `metadata.description`   | Copied directly                                                  |
| Labels                                            | `metadata.tags`          | Converted to lowercase, special characters replaced with hyphens |
| N/A                                               | `metadata.namespace`     | Hardcoded to `default`                                           |

## Parameter mapping

The following table shows how Ansible Automation Platform Job Template sources are mapped to template parameters:

| Ansible Automation Platform Job Template source | Generated template parameter type                                    |
| ----------------------------------------------- | -------------------------------------------------------------------- |
| Survey questions                                | Standard form fields (`type: string`, `enum`, `ui:widget`)           |
| "Prompt on Launch" options                      | `AAPResourcePicker` fields for Ansible Automation Platform resources |

## Field order

Ansible automation portal generates form fields from two sources in the Ansible Automation Platform Job Template configuration. Fields appear in the following order:

1. **OAuth token (hidden):** Auto-populated with the user's authentication token. This field is always present and always hidden.
2. **"Prompt on Launch" fields:** Each enabled "Prompt on Launch" option becomes an `AAPResourcePicker` field. Users select Ansible Automation Platform resources by name (Inventories, Credentials, Execution Environments). Ansible automation portal resolves names to Ansible Automation Platform internal IDs at launch time.
3. **Survey questions:** Each survey question becomes a form field with the matching input type (`text`, `dropdown`, `password`, `textarea`, `integer`, `float`, `multiplechoice`, `multiselect`).

## Defaults and required fields

- Survey question defaults and required/optional settings are preserved from the Ansible Automation Platform Job Template Survey.
- "Prompt on Launch" fields use the current Ansible Automation Platform Job Template settings for defaults and required/optional status.
- Ansible Automation Platform resource picker fields display resource names, not internal IDs.
