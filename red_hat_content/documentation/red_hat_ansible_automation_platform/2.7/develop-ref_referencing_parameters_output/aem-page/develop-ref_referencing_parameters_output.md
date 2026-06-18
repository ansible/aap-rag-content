+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_referencing_parameters_output"
title = "Reference parameters in output - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_referencing_parameters_output/aem-page/develop-ref_referencing_parameters_output.html"
last_crumb = "Reference parameters in output"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Reference parameters in output"
oversized = "false"
page_slug = "develop-ref_referencing_parameters_output"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_referencing_parameters_output"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_referencing_parameters_output/toc/toc.json"
type = "aem-page"
+++

# Reference parameters in output

You can reference any value the user entered in the `parameters` section by using the `${{ parameters.<field_name> }}` syntax.

The following table lists common parameter references:

| Reference                       | Description                                             | Example output                   |
| ------------------------------- | ------------------------------------------------------- | -------------------------------- |
| `${{ parameters.app_name }}`    | User-entered text field value                           | `my-app`                         |
| `${{ parameters.inventory }}`   | User-selected Ansible Automation Platform resource name | `Production Servers`             |
| `${{ parameters.credentials }}` | User-selected credentials (array)                       | `["SSH Key", "AWS Credentials"]` |
| `${{ parameters.environment }}` | User-selected enum value                                | `production`                     |

## Displaying user selections in the output

```
output:
  text:
    - title: Request submitted
      content: |
        Your request for **${{ parameters.app_name }}** has been submitted.

        **Configuration:**
        - Inventory: ${{ parameters.inventory }}
        - Environment: ${{ parameters.environment }}
```
