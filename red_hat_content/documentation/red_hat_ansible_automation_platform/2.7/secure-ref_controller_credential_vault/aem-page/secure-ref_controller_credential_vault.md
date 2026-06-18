+++
title = "Ansible Vault credential type - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_vault"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_vault/aem-page/secure-ref_controller_credential_vault.html"
last_crumb = "Ansible Vault credential type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Ansible Vault credential type"
oversized = "false"
page_slug = "secure-ref_controller_credential_vault"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_vault"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_vault/toc/toc.json"
type = "aem-page"
+++

# Ansible Vault credential type

You can use the Ansible Vault credential type to store sensitive data, such as passwords or keys, in encrypted files.

Select this credential type to enable synchronization of inventory with Ansible Vault.

Vault credentials require the **Vault Password** and an optional **Vault Identifier** if applying multi-Vault credentialing.

You can configure automation controller to ask the user for the password at launch time by selecting **Prompt on launch**.

When you select **Prompt on launch**, a dialog opens when the job is launched, prompting the user to enter the password.

Warning:

Credentials that are used in scheduled jobs must not be configured as **Prompt on launch**.
