+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_generic_oidc"
template = "docs/aem-title.html"
title = "Configure generic OIDC authentication - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_generic_oidc/aem-page/secure-proc_controller_set_up_generic_oidc.html"
last_crumb = "Configure generic OIDC authentication"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure generic OIDC authentication"
oversized = "false"
page_slug = "secure-proc_controller_set_up_generic_oidc"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_generic_oidc"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_generic_oidc/toc/toc.json"
type = "aem-page"
+++

# Configure generic OIDC authentication

OpenID Connect (OIDC) uses OAuth 2.0 to verify identity and obtain user info. Unlike SAML’s provider-to-provider trust, OIDC relies on the HTTPS channel to secure tokens. To set up OIDC with Ansible Automation Platform, consult your IdP's documentation for the required credentials.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a **Name** for this authentication configuration.
4.  Select **Generic OIDC** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
5.  Enter the following information:

  - **OIDC Provider URL**: The URL for your OIDC provider.
  - **OIDC Key**: The client ID from your third-party IdP.
  - **OIDC Secret**: The client secret from your IdP.

6.  Optional: Select the HTTP method to be used when requesting an access token from the **Access Token Method** list. The default method is **POST**.
7.  Optionally enter information for the following fields using the tooltip provided for instructions and required format:

  - **Access Token Method** - The default method is **POST**.
  -  **Access Token URL**
  -  **Access Token Method**
  -  **Authorization URL**
  - **Callback URL** - The OIDC **Callback URL** field registers the service as a service provider (SP) with each OIDC provider you have configured. Leave this field blank. After you save this authentication method, it is auto generated. Configure your IdP to allow redirects to this URL as part of the authentication flow.
  -  **ID Key**
  -  **ID Token Issuer**
  -  **JWKS URI**
  -  **OIDC Public Key**
  - **Revoke Token Method** - The default method is **GET**.
  -  **Revoke Token URL**
  -  **Response Type**
  -  **Token Endpoint Auth Method**
  -  **Userinfo URL**
  -  **Username Key**

8.  Use the **Verify OIDC Provider Certificate** to enable or disable the OIDC provider SSL/TLS certificate verification.
9.  Use the **Redirect** State to enable or disable the state parameter in the redirect URI. Enable this to prevent Cross Site Request Forgery (CSRF) attacks.
10.  Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. Note:
      Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

11.  To automatically create organizations, users, and teams upon successful login, select **Create objects**.
12.  To enable this authentication method upon creation, select **Enabled**.
13.  To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users**.
14.  Click Create Authentication Method.

## What to do next

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-mapping "To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.").

## Troubleshoot Generic OIDC Single Sign-On authentication failures

Authentication fails if the `OIDC JWT Algorithm` setting is not explicitly defined. The authentication code requires a list of acceptable algorithms, which it does not retrieve automatically from the OpenID Connect (OIDC) configuration endpoint.
