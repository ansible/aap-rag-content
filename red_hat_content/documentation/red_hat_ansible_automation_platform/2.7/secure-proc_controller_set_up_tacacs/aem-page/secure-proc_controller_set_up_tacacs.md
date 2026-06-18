+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_tacacs"
template = "docs/aem-title.html"
title = "Configure TACACS+ authentication - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_tacacs/aem-page/secure-proc_controller_set_up_tacacs.html"
last_crumb = "Configure TACACS+ authentication"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure TACACS+ authentication"
oversized = "false"
page_slug = "secure-proc_controller_set_up_tacacs"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_tacacs"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_tacacs/toc/toc.json"
type = "aem-page"
+++

# Configure TACACS+ authentication

Terminal Access Controller Access-Control System Plus (TACACS+) provides centralized AAA services (authentication, authorization, and accounting). You can configure Ansible Automation Platform to use TACACS+ as a source for remote authentication and access control.

## About this task

Note:

This feature is deprecated and will be removed in a future release.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a **Name** for this authentication configuration.
4.  Select **TACACS+** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
5.  Enter the following information:

  - Hostname of TACACS+ Server: Provide the hostname or IP address of the TACACS+ server with which to authenticate. If you leave this field blank, TACACS+ authentication is disabled.
  - TACACS+ Authentication Protocol: The protocol used by the TACACS+ client. The options are ascii or pap.
  - Shared secret for authenticating to TACACS+ server: The secret key for TACACS+ authentication server.

6.  The **TACACS+ client address sending enabled** is disabled by default. To enable client address sending, select the checkbox.
7.  Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. Note:
      Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

8.  To automatically create organizations, users, and teams upon successful login, select **Create objects**.
9.  To enable this authentication method upon creation, select **Enabled**.
10.  To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users**.
11.  Click Create Authentication Method.

## What to do next

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-mapping "To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.").
