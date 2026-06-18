+++
template = "docs/aem-title.html"
title = "VMware vCenter credential type - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_vmware_vcenter"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_vmware_vcenter/aem-page/secure-ref_controller_credential_vmware_vcenter.html"
last_crumb = "VMware vCenter credential type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "VMware vCenter credential type"
oversized = "false"
page_slug = "secure-ref_controller_credential_vmware_vcenter"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_vmware_vcenter"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_vmware_vcenter/toc/toc.json"
type = "aem-page"
+++

# VMware vCenter credential type

Select this credential type to enable synchronization of inventory with VMware vCenter.

Automation controller uses the following environment variables for VMware vCenter credentials:

```
VMWARE_HOST
VMWARE_USER
VMWARE_PASSWORD
VMWARE_VALIDATE_CERTS
```
These are fields prompted in the user interface.

VMware credentials require the following inputs:

- **vCenter Host**: The vCenter hostname or IP address to connect to.
- **Username**: The username to use to connect to vCenter.
- **Password**: The password to use to connect to vCenter.


Note:

If the VMware guest tools are not running on the instance, VMware inventory synchronization does not return an IP address for that instance.

## Access VMware vCenter credentials in an Ansible Playbook

You can get VMware vCenter credential parameters from a job runtime environment:

```
vars:
  vmware:
    host: '{{ lookup("env", "VMWARE_HOST") }}'
    username: '{{ lookup("env", "VMWARE_USER") }}'
    password: '{{ lookup("env", "VMWARE_PASSWORD") }}'
```
