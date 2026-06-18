+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_credential"
title = "Create new credentials - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_credential/aem-page/secure-proc_controller_create_credential.html"
last_crumb = "Create new credentials"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Create new credentials"
oversized = "false"
page_slug = "secure-proc_controller_create_credential"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_credential"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_credential/toc/toc.json"
type = "aem-page"
+++

# Create new credentials

Learn how to create new credentials in Automation controller.

## About this task

Credentials added to a team are made available to all members of the team. You can also add credentials to individual users.

As part of the initial setup, two credentials are available for your use: Demo Credential and Ansible Galaxy. Use the Ansible Galaxy credential as a template. You can copy this credential, but not edit it. Add more credentials as needed.

## Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Credentials.
2.  On the **Credentials** page, click Create credential.
3.  Enter the following information:

  - **Name**: the name for your new credential.
  - (Optional) **Description**: a description for the new credential.
  - Optional **Organization**: The name of the organization with which the credential is associated. The default is **Default**.
  - **Credential type**: enter or select the credential type you want to create.

4.  Enter the appropriate details depending on the type of credential selected, as described in [Credential types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_credential_types "Ansible Automation Platform supports a number of credential types.").  ![Credential types drop down list](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/credential-types-drop-down-menu.png)

5.  Click Create credential.
