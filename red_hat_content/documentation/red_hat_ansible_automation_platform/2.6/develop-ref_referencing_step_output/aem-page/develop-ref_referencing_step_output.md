+++
template = "docs/aem-title.html"
title = "Reference step output in output - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_referencing_step_output"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_referencing_step_output/aem-page/develop-ref_referencing_step_output.html"
last_crumb = "Reference step output in output"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Reference step output in output"
oversized = "false"
page_slug = "develop-ref_referencing_step_output"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_referencing_step_output"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_referencing_step_output/toc/toc.json"
type = "aem-page"
+++

# Reference step output in output

After the `rhaap:launch-job-template` action runs, the step output includes job execution data. Reference this data using the `${{ steps['<step-id>'].output.data.<field> }}` syntax.

The `rhaap:launch-job-template` action returns the following output fields:

| Reference                                       | Type   | Description                                                                               |
| ----------------------------------------------- | ------ | ----------------------------------------------------------------------------------------- |
| `${{ steps['launch-job'].output.data.id }}`     | number | Ansible Automation Platform Job ID.                                                       |
| `${{ steps['launch-job'].output.data.status }}` | string | Ansible Automation Platform Job status (for example, `pending`, `running`, `successful`). |
| `${{ steps['launch-job'].output.data.url }}`    | string | Direct URL to the job in Ansible Automation Platform.                                     |

## Displaying job execution data in the output

```
output:
  text:
    - title: Job launched
      content: |
        **Job ID:** ${{ steps['launch-job'].output.data.id }}
        **Status:** ${{ steps['launch-job'].output.data.status }}
  links:
    - title: View job in Ansible Automation Platform
      url: ${{ steps['launch-job'].output.data.url }}
```
