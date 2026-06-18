+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_dynamic_toggle_fields"
template = "docs/aem-title.html"
title = "Show or hide fields based on a toggle - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_dynamic_toggle_fields/aem-page/develop-ref_dynamic_toggle_fields.html"
last_crumb = "Show or hide fields based on a toggle"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Show or hide fields based on a toggle"
oversized = "false"
page_slug = "develop-ref_dynamic_toggle_fields"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_dynamic_toggle_fields"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_dynamic_toggle_fields/toc/toc.json"
type = "aem-page"
+++

# Show or hide fields based on a toggle

Use a `boolean` toggle field to show or hide a group of additional fields.

In this example, selecting "Show advanced options" reveals one additional field. When the toggle is off, the field is hidden and not submitted.

```
parameters:
  - title: Time server settings
    required:
      - ntpServers
    properties:
      ntpServers:
        title: NTP servers
        type: string
        default: 0.rhel.pool.ntp.org, 1.rhel.pool.ntp.org
      showAdvanced:
        title: Show advanced options?
        type: boolean
        default: false
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
```
When `showAdvanced` is `true`, the form displays `maxSyncDelay`. When `showAdvanced` is `false`, the field is hidden.
