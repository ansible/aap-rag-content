+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_dynamic_chained_dependencies"
template = "docs/aem-title.html"
title = "Chain multiple dynamic dependencies - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_dynamic_chained_dependencies/aem-page/develop-ref_dynamic_chained_dependencies.html"
last_crumb = "Chain multiple dynamic dependencies"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Chain multiple dynamic dependencies"
oversized = "false"
page_slug = "develop-ref_dynamic_chained_dependencies"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_dynamic_chained_dependencies"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_dynamic_chained_dependencies/toc/toc.json"
type = "aem-page"
+++

# Chain multiple dynamic dependencies

You can define multiple `dependencies` in the same parameter step. Each dependency operates independently.

In this example, selecting "Yes" for the restart confirmation reveals a reason field, while enabling advanced options reveals additional technical fields:

```
dependencies:
  showAdvanced:
    allOf:
      - if:
          properties:
            showAdvanced:
              const: true
        then:
          properties:
            maxSyncDelay:
              type: number
              title: Max sync delay (ms)
              default: 500
  serviceRestart:
    allOf:
      - if:
          properties:
            serviceRestart:
              const: 'Yes'
        then:
          properties:
            restartReason:
              type: string
              title: Reason for restart
              description: Provide a reason for restarting the service.
              default: Applying new configuration.
              minLength: 10
              errorMessage:
                minLength: 'Provide a more detailed reason (at least 10 characters).'
```
Each key under `dependencies` corresponds to a property name in the same parameter step. When the user changes a field value, only the matching `if`/`then` branch is displayed.
