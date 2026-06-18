+++
template = "docs/aem-title.html"
title = "Connect to external secret management systems with built-in credentials - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credential_types"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials/", "Configure credentials for Event-Driven Ansible"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credential_types/aem-page/secure-assembly_eda_credential_types.html"
last_crumb = "Connect to external secret management systems with built-in credentials"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Connect to external secret management systems with built-in credentials"
oversized = "false"
page_slug = "secure-assembly_eda_credential_types"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credential_types"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credential_types/toc/toc.json"
type = "aem-page"
+++

# Connect to external secret management systems with built-in credentials

Event-Driven Ansible controller includes built-in credentials to sync projects, run rulebooks, execute job templates, fetch container images, and process data through event streams.

These built-in credential types are not editable. So if you want credential types that support authentication with other systems, you can create your own credential types that can be used in your source plugins. Each credential type contains an input configuration and an injector configuration that can be passed to an Ansible rulebook to configure your sources. For more information, see Create custom credentials for Event-Driven Ansible.

If you will be executing job templates through automation controller, you can retrieve credential values from external secret management systems listed in External secret management credential types.

## External secret management credential types

In addition to the built-in credential types, Event-Driven Ansible supports a variety of external secret management credential types. These credential types allow rulebooks to securely retrieve sensitive information (API keys, and similar) directly from your organization’s centralized secret vault.

The following external credential types are available for use in Event-Driven Ansible controller:

- AWS Secrets Manager
- Azure Key Vault
- Centrify Vault Credential Provider
- CyberArk Central Credential Provider
- CyberArk Conjur Secrets Manager
- HashiCorp Vault Secret
- HashiCorp Vault Signed SSH
- Thycotic DevOps Secrets Vault
- Thycotic Secret Server
- GitHub App Installation Access Token


The process for using these credentials in a rulebook activation is consistent with how they are used in automation controller.
