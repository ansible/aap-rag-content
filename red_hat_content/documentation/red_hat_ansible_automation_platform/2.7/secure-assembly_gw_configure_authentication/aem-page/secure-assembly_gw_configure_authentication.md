+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication"
title = "Configure central authentication for Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/aem-page/secure-assembly_gw_configure_authentication.html"
last_crumb = "Configure central authentication for Ansible Automation Platform"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure central authentication for Ansible Automation Platform"
oversized = "false"
page_slug = "secure-assembly_gw_configure_authentication"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/toc/toc.json"
type = "aem-page"
+++

# Configure central authentication for Ansible Automation Platform

Configure authentication methods such as LDAP or SAML to simplify the user login experience. Providing the correct connection details for your chosen identity provider helps ensure seamless and secure access to Ansible Automation Platform.

Configuring authentication involves the following procedures:

- Selecting an authentication type, where you select the type of authenticator plugin you want to configure, including the authentication details for the authentication type selected.
- Mapping, where you define mapping rule types and triggers to control access to the system, and mapping order where you can define the mapping precedence.

Important:

- During an upgrade to Ansible Automation Platform 2.6, platform gateway uses a new central authentication service.
- After the upgrade, local users that used to exist in automation controller can be automatically converted into local platform gateway users. Other types of authentication from automation controller, such as LDAP, SAML, or OIDC, are migrated to platform gateway but platform gateway might need additional configuration before those users are ready for use.

Local user passwords are not automatically synchronized between automation controller and platform gateway after an upgrade. Platform gateway uses the following process to authenticate a local user for the first time:

- Platform gateway attempts to authenticate the user with the platform gateway password.
- If the attempt fails, platform gateway authenticates the user with the automation controller password.
- On successful authentication, platform gateway updates the user’s password in its database.
- The user is authenticated directly by platform gateway on subsequent logins.


## Prerequisites

- A running installation of Ansible Automation Platform 2.6 or later
- A running instance of your authentication source
- Administrator rights to the Ansible Automation Platform
- Any connection information needed to connect Ansible Automation Platform 2.6 to your source (see individual authentication types for details).
