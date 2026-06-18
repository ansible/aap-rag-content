+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_output_links"
title = "Output links - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_output_links/aem-page/develop-ref_output_links.html"
last_crumb = "Output links"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Output links"
oversized = "false"
page_slug = "develop-ref_output_links"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_output_links"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_output_links/toc/toc.json"
type = "aem-page"
+++

# Output links

Use `output.links` to display clickable buttons. Each link has a `title` and `url` field. You can optionally set an `icon` field.

```
output:
  links:
    - title: Check Request Status
      url: https://portal.example.com/requests/status
      icon: help
```
You can reference step output data in link URLs:

```
output:
  links:
    - title: View job in Ansible Automation Platform
      url: ${{ steps['launch-job'].output.data.url }}
```
You can include multiple links:

```
output:
  links:
    - title: View job in Ansible Automation Platform
      url: ${{ steps['launch-job'].output.data.url }}
    - title: RHEL documentation
      url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/
      icon: docs
```
