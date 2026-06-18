+++
title = "Configure access to external applications with tokens - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication/aem-page/secure-assembly_gw_token_based_authentication.html"
last_crumb = "Configure access to external applications with tokens"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure access to external applications with tokens"
oversized = "false"
page_slug = "secure-assembly_gw_token_based_authentication"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication/toc/toc.json"
type = "aem-page"
+++

# Configure access to external applications with tokens

Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).

In Ansible Automation Platform 2.7, you must create and manage all tokens through platform gateway. Component-level token creation has been removed.

OAuth Tokens
OAuth Tokens are tied to specific applications and allow applications to access data without disclosing user login information.

Personal Access Tokens
PATs are personal to a user and not tied to a specific application. They are created directly by a user for their own use through platform gateway.

The default expiration for access tokens has been updated from 1000 years to 1 year. This change ensures frequent token rotation for increased credential security.

Note:

Access tokens in controller 2.4 and previous versions of the platform gateway were valid for 1000 years. Any existing tokens created before the 2.5.20250604 patch release will retain a 1000 year expiration.

You can customize this setting to meet your specific requirements by modifying the expiration time in your `settings.py` file as follows:

```
OAUTH2_PROVIDER__ACCESS_TOKEN_EXPIRE_SECONDS = 31536000
```

## Manage OAuth applications

Create and configure token-based authentication for external applications such as ServiceNow and Jenkins. With token-based authentication, external applications can easily integrate with Ansible Automation Platform.

Important:

Automation controller OAuth applications on the platform UI are not supported for 2.4 to 2.5 migration.

As a platform administrator, you can configure a custom external application URL within the platform, providing seamless integration with external services. This functionality is currently available as a Technology Preview. Once configured, the external application URL is displayed in the platform UI navigation panel, providing users with easy access to the application. This feature streamlines workflows by ensuring quick access to external services from within the platform UI.

Note:

Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

With OAuth 2 you can use tokens to share data with an application without disclosing login information. You can configure these tokens as read-only.

You can create an application that is representative of the external application you are integrating with, then use it to create tokens for the application to use on behalf of its users.

Associate these tokens with an application resource to manage all tokens issued for a particular application. By separating the issue of tokens under **OAuth Applications**, you can revoke all tokens based on the application without having to revoke all tokens in the system.

## Get started with OAuth Applications

You can access the **OAuth Applications** page from the navigation panel by selecting Access Management> (and then)OAuth Applications. From there you can view, create, sort and search for applications currently managed by Ansible Automation Platform and automation controller.

If no applications exist, you can create one by clicking Create OAuth application.

### Application functions

Several OAuth 2 utilities are available for authorization, token refresh, and revoke. You can specify the following grant types when creating an application:

Password
This grant type is ideal for users who have native access to the web application and must be used when the client is the resource owner.

Authorization code
This grant type should be used when access tokens must be issued directly to an external application or service.

Note:

You can only use the authorization code type to acquire an access token when using an application. When integrating an external web application with Ansible Automation Platform, that web application might need to create OAuth2 tokens on behalf of users in that other web application. Creating an application in the platform with the authorization code grant type is the preferred way to do this because:

- This allows an external application to obtain a token from Ansible Automation Platform for a user, using their credentials.
- Compartmentalized tokens issued for a particular application enables those tokens to be easily managed. For example, revoking *all* tokens associated with that application without having to revoke all tokens in the system.

### Request an access token after expiration

The default expiration for access tokens is 1 year.

The best way to set up application integrations by using the **Authorization code** grant type is to allowlist the origins for those cross-site requests. More generally, you must allowlist the service or application you are integrating with the platform, for which you want to provide access tokens.

To do this, have your administrator add this allowlist to their local Ansible Automation Platform settings file:

```
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"http://django-oauth-toolkit.herokuapp.com*",
    r"http://www.example.com*"
]
```
Where `<http://django-oauth-toolkit.herokuapp.com>` and `<http://www.example.com>` are applications requiring tokens with which to access the platform.

### OAuth2 application and token migration (2.4 to 2.6)

During the upgrade from Ansible Automation Platform 2.4 to 2.6, there are important changes to how OAuth2 applications and tokens are managed. Ansible Automation Platform now uses platform gateway OAuth applications and deprecates automation controller OAuth applications.

- **Automation controller OAuth applications**: You can view and edit existing automation controller applications, but new ones can no longer be created. These legacy applications continue to function, but they might be removed in a future release. Plan to migrate to platform gateway OAuth applications.
- **Automation controller tokens**: Automation controller personal access tokens (PATs), are also deprecated. Guide users to move to platform gateway PATs.
- **Platform gateway OAuth applications and tokens**: Platform applications and tokens offer an updated interface and are the standard for future use. Move to these applications and tokens.

### Manage `OAUTH2_PROVIDER` settings

The `OAUTH2_PROVIDER` settings from automation controller are managed by platform gateway after upgrading from 2.4. to 2.6. The default token expiration values might differ between automation controller and platform gateway.

- The default access token expiration is updated from 1,000 years to 1 year. This change increases credential security through more frequent token rotation.

- Platform gateway’s default OAUTH2_PROVIDER settings are:

```
{
  "ACCESS_TOKEN_EXPIRE_SECONDS": 31536000000,
  "REFRESH_TOKEN_EXPIRE_SECONDS": 2628000,
  "AUTHORIZATION_CODE_EXPIRE_SECONDS": 600
}
```
    If you previously set a token expiration shorter than one year, you must manually update the platform gateway settings to match your required configuration.
