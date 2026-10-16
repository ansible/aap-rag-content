+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication"
title = "Configure access to external applications with tokens - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_token_based_authentication/aem-page/secure-assembly_gw_token_based_authentication.html"
last_crumb = "Configure access to external applications with tokens"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
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
