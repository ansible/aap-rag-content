+++
template = "docs/aem-title.html"
title = "Output text - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_output_text"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_output_text/aem-page/develop-ref_output_text.html"
last_crumb = "Output text"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Output text"
oversized = "false"
page_slug = "develop-ref_output_text"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_output_text"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_output_text/toc/toc.json"
type = "aem-page"
+++

# Output text

Use `output.text` to display information to the user after the template runs. Each text block has a `title` and `content` field. The `content` field supports markdown formatting.

```
output:
  text:
    - title: Request submitted
      content: |
        Your request has been submitted.
```
You can include multiple text blocks:

```
output:
  text:
    - title: Request submitted
      content: |
        Your deployment of **${{ parameters.app_name }}** has been submitted.

        **Job ID:** ${{ steps['launch-job'].output.data.id }}
        **Status:** ${{ steps['launch-job'].output.data.status }}

    - title: Configuration summary
      content: |
        - Inventory: ${{ parameters.inventory }}
        - Application: ${{ parameters.app_name }}
```
