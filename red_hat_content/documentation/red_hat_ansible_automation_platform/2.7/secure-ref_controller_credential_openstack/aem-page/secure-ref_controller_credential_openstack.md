+++
title = "OpenStack credential type - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_openstack"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_openstack/aem-page/secure-ref_controller_credential_openstack.html"
last_crumb = "OpenStack credential type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "OpenStack credential type"
oversized = "false"
page_slug = "secure-ref_controller_credential_openstack"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_openstack"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_openstack/toc/toc.json"
type = "aem-page"
+++

# OpenStack credential type

Select this credential type to enable synchronization of cloud inventory with OpenStack.

Enter the following information for OpenStack credentials:

- **Username**: The username to use to connect to OpenStack.
- **Password (API Key)**: The password or API key to use to connect to OpenStack.
- **Host (Authentication URL)**: The host to be used for authentication.
- **Project (Tenant Name)**: The Tenant name or Tenant ID used for OpenStack. This value is usually the same as the username.
- Optional: **Project (Domain Name)**: Give the project name associated with your domain.
- Optional: **Domain Name**: Give the FQDN to be used to connect to OpenStack.
- Optional: **Region Name**: Give the region name. For some cloud providers, such as OVH, the region must be specified.


If you are interested in using OpenStack Cloud Credentials, see [Associate cloud credentials with a job template](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_controller_cloud_credentials#controller-cloud-credentials "Automation controller can use Cloud Credentials to authenticate to cloud providers."), which includes a sample playbook.
