+++
template = "docs/aem-title.html"
title = "Security settings for OAuth2 tokens and external users - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_gw_manage_oauth2_external_users"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_gw_manage_oauth2_external_users/aem-page/secure-con_gw_manage_oauth2_external_users.html"
last_crumb = "Security settings for OAuth2 tokens and external users"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Security settings for OAuth2 tokens and external users"
oversized = "false"
page_slug = "secure-con_gw_manage_oauth2_external_users"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_gw_manage_oauth2_external_users"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_gw_manage_oauth2_external_users/toc/toc.json"
type = "aem-page"
+++

# Security settings for OAuth2 tokens and external users

Configure your platform settings to enable OAuth2 token creation for external users. Allowing users authenticated via LDAP, SAML, or SSO to generate tokens prevents 403 Forbidden errors and helps ensure they maintain programmatic API access.

This default behavior is a deliberate security measure. Ansible Automation Platform prioritizes centralized control over token generation, which encourages administrators to select the appropriate method for enabling OAuth 2.0 user token generation for external authentication providers.

It is important to understand that an OAuth2 token is created within Ansible Automation Platform, and Ansible Automation Platform itself manages its lifecycle, including its expiration. This lifecycle is independent of the user’s session with their external Identity Provider (IdP). For example, if a user generates an Ansible Automation Platform token and their account is later disabled in the external IdP, the Ansible Automation Platform token remains valid until it expires or is manually revoked. Being aware of this interaction is crucial for a secure configuration, as it highlights the need for compensating controls if you enable token creation for external users.

## Enable OAuth2 token creation for external users

To enable external users to create OAuth2 tokens, change the appropriate setting in your Ansible Automation Platform environment. Ensure the implementation of compensating security controls after enabling this setting.

### Procedure

1. From the navigation panel, go to Settings> (and then)Platform gateway.
2. Click Edit platform gateway settings.
3. Change the **Allow external users to create OAuth2 tokens** setting to **Enabled**.
4. Click Save platform gateway settings.

### What to do next

Implement the recommended security controls as described in *Implementing security controls for external user OAuth2 tokens*.

## Implement security controls for external user OAuth2 tokens

After enabling OAuth2 token creation for external users, implement the following compensating controls to keep a strong security posture.

### Procedure

- **Limit token lifetime**: Configure a shorter duration for OAuth2 tokens to reduce the window of exposure. Adjust the OAuth2 access token expiration setting to limit token validity. A value of 28800 seconds (8 hours) is recommended, limiting token validity to a standard workday.

  * For manual `settings.py` configuration, see [Configure access to external applications with tokens](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication#gw-token-based-authentication "Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).").
  * For RPM or containerized installations, see the `gateway_extra_settings` example in [Platform gateway variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/../install/ref-gateway-variables.html "Reference information for the inventory file variables used to configure platform gateway.").
  * For operator-based installations on OpenShift Container Platform, see [Configure the OAuth access token lifetime on OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_applications_getting_started#proc-gw-configure-oauth-token-lifetime-operator "On an operator-based installation, set the OAuth access token lifetime in the AnsibleAutomationPlatform custom resource so platform gateway applies it across reconciliations.").

- **Enforce strict role-based access control (RBAC)**: Grant users only the minimum necessary permissions.   * Assign users who create tokens to **Teams** with highly restrictive roles. Avoid granting broad permissions that could lead to privilege escalation.

- **Establish a clear offboarding process**: Integrate token revocation into your organizational offboarding procedures. Your HR and IT offboarding processes must include a step for an Ansible Automation Platform administrator to revoke all active tokens for a departing user. Tokens can be manually revoked from the user’s profile under the **Tokens** tab.
- **Audit and monitor**: Regularly review token-related activities for legitimacy in the **Activity Stream**.
