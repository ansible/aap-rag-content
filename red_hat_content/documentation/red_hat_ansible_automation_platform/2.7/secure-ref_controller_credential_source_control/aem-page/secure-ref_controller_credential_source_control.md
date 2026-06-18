+++
title = "Source Control credential type - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_source_control"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_source_control/aem-page/secure-ref_controller_credential_source_control.html"
last_crumb = "Source Control credential type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Source Control credential type"
oversized = "false"
page_slug = "secure-ref_controller_credential_source_control"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_source_control"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_source_control/toc/toc.json"
type = "aem-page"
+++

# Source Control credential type

*Source Control* credentials are used with projects to clone and update local source code repositories from a remote revision control system such as Git or Subversion.

Source Control credentials require the following inputs:

- **Username**: The username to use in conjunction with the source control system.
- **Password**: The password to use in conjunction with the source control system.
- **SCM Private Key**: Copy or drag-and-drop the actual SSH Private Key to be used to authenticate the user to the source control system through SSH.
- **Private Key Passphrase**: If the SSH Private Key used is protected by a passphrase, you can configure a Key Passphrase for the private key.


Note:

You cannot configure Source Control credentials as **Prompt on launch**.

If you are using a GitHub account for a Source Control credential and you have *Two Factor Authentication* (2FA) enabled on your account, you must use your Personal Access Token in the password field rather than your account password.
