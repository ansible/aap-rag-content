+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_virtualization"
title = "Red Hat Virtualization credential type - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_virtualization/aem-page/secure-ref_controller_credential_virtualization.html"
last_crumb = "Red Hat Virtualization credential type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Red Hat Virtualization credential type"
oversized = "false"
page_slug = "secure-ref_controller_credential_virtualization"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_virtualization"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_virtualization/toc/toc.json"
type = "aem-page"
+++

# Red Hat Virtualization credential type

Select this credential to enable automation controller to access Ansible’s `oVirt4.py` dynamic inventory plugin, which is managed by *Red Hat Virtualization*.

Automation controller uses the following environment variables for Red Hat Virtualization credentials. These are fields in the user interface:

```
OVIRT_URL
OVIRT_USERNAME
OVIRT_PASSWORD
```
Provide the following information for Red Hat Virtualization credentials:

- **Host (Authentication URL)**: The host URL or IP address to connect to. To sync with the inventory, the credential URL needs to include the `ovirt-engine/api` path.
- **Username**: The username to use to connect to oVirt4. This must include the domain profile to succeed, for example `username@ovirt.host.com`.
- **Password**: The password to use to connect to it.
- Optional: **CA File**: Provide an absolute path to the oVirt certificate file (it might end in `.pem`, `.cer` and `.crt` extensions, but preferably `.pem` for consistency)
