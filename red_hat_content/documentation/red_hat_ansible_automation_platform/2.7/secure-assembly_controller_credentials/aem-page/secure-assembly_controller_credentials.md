+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials"
title = "Configure credentials to authenticate remote systems and services - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/aem-page/secure-assembly_controller_credentials.html"
last_crumb = "Configure credentials to authenticate remote systems and services"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure credentials to authenticate remote systems and services"
oversized = "false"
page_slug = "secure-assembly_controller_credentials"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/toc/toc.json"
type = "aem-page"
+++

# Configure credentials to authenticate remote systems and services

Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.

You can grant users and teams the ability to use these credentials, without exposing the credential to the user. If a user moves to a different team or leaves the organization, you do not have to re-key all of your systems just because that credential was available in automation controller.

Note:

Automation controller encrypts passwords and key information in the database and never makes secret information visible through the API.
