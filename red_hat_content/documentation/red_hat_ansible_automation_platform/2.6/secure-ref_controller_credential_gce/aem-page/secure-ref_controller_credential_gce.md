+++
template = "docs/aem-title.html"
title = "Google Compute Engine credential type - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_credential_gce"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_controller_credential_gce/aem-page/secure-ref_controller_credential_gce.html"
last_crumb = "Google Compute Engine credential type"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Google Compute Engine credential type"
oversized = "false"
page_slug = "secure-ref_controller_credential_gce"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-ref_controller_credential_gce"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_controller_credential_gce/toc/toc.json"
type = "aem-page"
+++

# Google Compute Engine credential type

Select this credential to enable synchronization of a cloud inventory with Google Compute Engine (GCE).

Automation controller uses the following environment variables for GCE credentials:

```
GCE_EMAIL
GCE_PROJECT
GCE_CREDENTIALS_FILE_PATH
```
These are fields prompted in the user interface:

GCE credentials require the following information:

- **Service Account Email Address**: The email address assigned to the Google Compute Engine **service account**.
- Optional: **Project**: Provide the GCE assigned identification or the unique project ID that you provided at project creation time.
- Optional: **Service Account JSON File**: Upload a GCE service account file. Click Browse to browse for the file that has the special account information that can be used by services and applications running on your GCE instance to interact with other Google Cloud APIs. This grants permissions to the service account and virtual machine instances.
- **RSA Private Key**: The PEM file associated with the service account email.
