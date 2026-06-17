+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_gw_config_keycloak_settings"
title = "Configure keycloak authentication - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_gw_config_keycloak_settings/aem-page/secure-proc_gw_config_keycloak_settings.html"
last_crumb = "Configure keycloak authentication"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure keycloak authentication"
oversized = "false"
page_slug = "secure-proc_gw_config_keycloak_settings"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_gw_config_keycloak_settings"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_gw_config_keycloak_settings/toc/toc.json"
type = "aem-page"
+++

# Configure keycloak authentication

You can configure Ansible Automation Platform to integrate Keycloak to manage user authentication.

## About this task

Note:

When using this authenticator some specific setup in your Keycloak instance is required. Refer to the [Python Keycloak reference](https://python-social-auth.readthedocs.io/en/latest/backends/keycloak.html) for more details.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a **Name** for this authentication configuration.
4.  Select **Keycloak** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
5.  Enter the location where the user’s token can be retrieved in the **Keycloak Access Token URL** field.
6.  Optional: Enter the redirect location the user is taken to during the login flow in the **Keycloak Provider URL** field.
7.  Enter the Client ID from your Keycloak installation in the **Keycloak OIDC Key** field.
8.  Enter the RS256 public key provided by your Keycloak realm in the **Keycloak Public Key** field.
9.  Enter the OIDC secret (Client Secret) from your Keycloak installation in the **Keycloak OIDC Secret** field.
10.  Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. Note:
      Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

11.  To automatically create organizations, users, and teams upon successful login, select **Create objects**.
12.  To enable this authentication method upon creation, select **Enabled**.
13.  To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users**.
14.  Click Create Authentication Method.

If you receive an `jwt.exceptions.InvalidAudienceError: Audience doesn’t match` error, you must re-enable the audience by doing the following:

1. From the navigation for your Keycloak configuration, select Client scopes> (and then)YOUR-CLIENT-ID-dedicated> (and then)Add mapper> (and then)Audience.
2. Pick a name for the mapper.
3. Select the **Client ID** corresponding to your client in `Included Client Audience`.

## What to do next

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#gw-mapping "To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.").
