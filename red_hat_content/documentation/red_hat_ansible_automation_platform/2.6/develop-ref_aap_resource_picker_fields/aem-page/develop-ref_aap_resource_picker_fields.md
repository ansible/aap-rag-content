+++
title = "AAP resource picker fields - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_aap_resource_picker_fields"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_aap_resource_picker_fields/aem-page/develop-ref_aap_resource_picker_fields.html"
last_crumb = "AAP resource picker fields"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "AAP resource picker fields"
oversized = "false"
page_slug = "develop-ref_aap_resource_picker_fields"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_aap_resource_picker_fields"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_aap_resource_picker_fields/toc/toc.json"
type = "aem-page"
+++

# AAP resource picker fields

Use `ui:field: AAPResourcePicker` to let users select Ansible Automation Platform resources by name. Ansible automation portal queries the Ansible Automation Platform API and displays available resources in a picker.

Set the `resource` property to specify the Ansible Automation Platform resource type.

The following table lists supported `resource` values:

| `resource` value | Ansible Automation Platform resource type | Selection mode               |
| ---------------- | ----------------------------------------- | ---------------------------- |
| `inventories`    | Inventories                               | Single-select                |
| `credentials`    | Credentials                               | Multi-select (`type: array`) |
| `organizations`  | Organizations                             | Single-select                |

## Single-select example (inventory)

```
inventory:
  title: Inventory
  description: Select target inventory.
  resource: inventories
  ui:field: AAPResourcePicker
  default: Production Servers
```

## Multi-select example (credentials)

```
credentials:
  title: Credentials
  description: Select credentials for accessing the target hosts.
  type: array
  resource: credentials
  ui:field: AAPResourcePicker
  default:
    - SSH Key
    - AWS Credentials
```
