+++
template = "docs/aem-title.html"
title = "Manage platform credentials - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_credential_management_planning"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_credential_management_planning/aem-page/secure-con_credential_management_planning.html"
last_crumb = "Manage platform credentials"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Manage platform credentials"
oversized = "false"
page_slug = "secure-con_credential_management_planning"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_credential_management_planning"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_credential_management_planning/toc/toc.json"
type = "aem-page"
+++

# Manage platform credentials

Red Hat Ansible Automation Platform uses credentials to authenticate requests to jobs against machines, synchronize with inventory sources, and import project content from a version control system.

Ansible Automation Platform manages three sets of secrets:

- User passwords for **local Ansible Automation Platform users**.
- Secrets for Ansible Automation Platform **operational use** (database password, message bus password, and so on).
- Secrets for **automation use** (SSH keys, cloud credentials, external password vault credentials, and so on).


Implementing a privileged access or credential management solution to protect credentials from compromise is a highly recommended practice. Organizations should audit the use of, and provide additional programmatic control over, access and privilege escalation.

You can further secure automation credentials by ensuring they are unique and stored only in Ansible Automation Platform or in a supported external secrets management system. Services such as OpenSSH can be configured to allow credentials on connections only from specific addresses. Use different credentials for automation from those used by system administrators to log in to a server. Although direct access should be limited where possible, it can be used for disaster recovery or other ad hoc management purposes, allowing for easier auditing.

Different automation jobs might need to access a system at different levels. For example, you can have low-level system automation that applies patches and performs security baseline checking, while a higher-level piece of automation deploys applications. By using different keys or credentials for each piece of automation, the effect of any one key vulnerability is minimized. This also allows for easy baseline auditing.

## External credential vault considerations

Secrets management is an essential component of maintaining a secure automation platform. We recommend the following secrets management practice:

Use an external system to manage secrets. In cases where credentials need to be updated, an external system can retrieve updated credentials with less complexity than an internal system. External systems for managing secrets include CyberArk, HashiCorp Vault, {Azure} Key Management, and others.
