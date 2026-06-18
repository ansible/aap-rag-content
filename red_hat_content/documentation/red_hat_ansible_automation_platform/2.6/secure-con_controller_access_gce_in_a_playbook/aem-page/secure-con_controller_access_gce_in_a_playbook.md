+++
template = "docs/aem-title.html"
title = "Access Google Compute Engine credentials in an Ansible Playbook - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_controller_access_gce_in_a_playbook"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_controller_access_gce_in_a_playbook/aem-page/secure-con_controller_access_gce_in_a_playbook.html"
last_crumb = "Access Google Compute Engine credentials in an Ansible Playbook"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Access Google Compute Engine credentials in an Ansible Playbook"
oversized = "false"
page_slug = "secure-con_controller_access_gce_in_a_playbook"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-con_controller_access_gce_in_a_playbook"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_controller_access_gce_in_a_playbook/toc/toc.json"
type = "aem-page"
+++

# Access Google Compute Engine credentials in an Ansible Playbook

You can access Google Compute Engine (GCE) credentials in an Ansible Playbook by using environment variables.

You can get GCE credential parameters from a job runtime environment:

```
vars:
  gce:
    email: '{{ lookup("env", "GCE_EMAIL") }}'
    project: '{{ lookup("env", "GCE_PROJECT") }}'
    pem_file_path: '{{ lookup("env", "GCE_PEM_FILE_PATH") }}'
```
