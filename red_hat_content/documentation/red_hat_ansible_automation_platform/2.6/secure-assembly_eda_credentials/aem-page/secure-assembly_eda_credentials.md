+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials"
template = "docs/aem-title.html"
title = "Configure credentials for Event-Driven Ansible - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials/", "Configure credentials for Event-Driven Ansible"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials/aem-page/secure-assembly_eda_credentials.html"
last_crumb = "Configure credentials for Event-Driven Ansible"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure credentials for Event-Driven Ansible"
oversized = "false"
page_slug = "secure-assembly_eda_credentials"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials/toc/toc.json"
type = "aem-page"
+++

# Configure credentials for Event-Driven Ansible

You can use credentials to store secrets that can be used for authentication purposes with resources, such as decision environments, rulebook activations and projects for Event-Driven Ansible controller, and projects for automation controller.

Credentials authenticate users when launching jobs against machines and importing project content from a version control system.

You can grant users and teams the ability to use these credentials without exposing the credential to the user. If a user moves to a different team or leaves the organization, you do not have to rekey all of your systems just because that credential was previously available.

Note:

In the context of automation controller and Event-Driven Ansible controller, you can use both `extra_vars` and credentials to store a variety of information. However, credentials are the preferred method of storing sensitive information such as passwords or API keys because they offer better security and centralized management, whereas `extra_vars` are more suitable for passing dynamic, non-sensitive data.
