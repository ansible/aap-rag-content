+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_dynamic_selection_fields"
title = "Show different fields based on a selection - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_dynamic_selection_fields/aem-page/develop-ref_dynamic_selection_fields.html"
last_crumb = "Show different fields based on a selection"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Show different fields based on a selection"
oversized = "false"
page_slug = "develop-ref_dynamic_selection_fields"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_dynamic_selection_fields"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_dynamic_selection_fields/toc/toc.json"
type = "aem-page"
+++

# Show different fields based on a selection

Use an `enum` field with `dependencies` and `allOf` to display different configuration fields for each option.

In this example, selecting a database type reveals a version dropdown specific to that engine:

```
properties:
  dbType:
    title: Database type
    type: string
    enum:
      - PostgreSQL
      - MySQL
dependencies:
  dbType:
    allOf:
      - if:
          properties:
            dbType:
              const: PostgreSQL
        then:
          properties:
            version:
              type: number
              enum: [13, 14, 15]
              title: PostgreSQL version
              default: 15
      - if:
          properties:
            dbType:
              const: MySQL
        then:
          properties:
            version:
              type: string
              enum: ['5.7', '8.0']
              title: MySQL version
              default: '8.0'
```
Each `if`/`then` block in the `allOf` array matches one `enum` value. Selecting "PostgreSQL" shows the PostgreSQL version list; selecting "MySQL" replaces it with the MySQL version list.
