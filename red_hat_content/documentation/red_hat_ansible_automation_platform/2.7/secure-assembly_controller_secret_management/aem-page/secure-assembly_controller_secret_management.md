+++
title = "Configure an external secret management system for automation - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_secret_management"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_access/", "Manage access with role-based access control"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_secret_management/aem-page/secure-assembly_controller_secret_management.html"
last_crumb = "Configure an external secret management system for automation"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure an external secret management system for automation"
oversized = "false"
page_slug = "secure-assembly_controller_secret_management"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_secret_management"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_secret_management/toc/toc.json"
type = "aem-page"
+++

# Configure an external secret management system for automation

Configure machine and cloud credentials to allow your automation to securely access external services and machines. Encrypting and storing sensitive values like SSH keys and API tokens in the database helps ensure your authentication details remain protected.

With external credentials backed by credential plugins, you can map credential fields (such as a password or an SSH Private key) to values stored in a `secret management system` instead of providing them to automation controller directly.

Automation controller provides a secret management system that include integrations for:

- AWS Secrets Manager Lookup
- Centrify Vault Credential Provider Lookup
- *CyberArk Central Credential Provider* Lookup (CCP)
- CyberArk Conjur Secrets Manager Lookup
- HashiCorp Vault *Key-Value* Store (KV)
- HashiCorp Vault SSH Secrets Engine
- Microsoft Azure *Key Management System* (KMS)
- Thycotic DevOps Secrets Vault
- Thycotic Secret Server
- GitHub app token lookup


These external secret values are fetched before running a playbook that needs them.
