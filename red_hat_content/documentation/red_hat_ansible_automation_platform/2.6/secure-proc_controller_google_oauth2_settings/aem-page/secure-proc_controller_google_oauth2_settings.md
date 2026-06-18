+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_google_oauth2_settings"
title = "Configure Google OAuth2 authentication - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_google_oauth2_settings/aem-page/secure-proc_controller_google_oauth2_settings.html"
last_crumb = "Configure Google OAuth2 authentication"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure Google OAuth2 authentication"
oversized = "false"
page_slug = "secure-proc_controller_google_oauth2_settings"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_controller_google_oauth2_settings"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_google_oauth2_settings/toc/toc.json"
type = "aem-page"
+++

# Configure Google OAuth2 authentication

To set up social authentication for Google, you must obtain an OAuth2 key and secret for a web application. To do this, you must first create a project and set it up with Google.

## About this task

For instructions, see [Setting up OAuth 2.0](https://support.google.com/googleapi/answer/6158849) in the Google API Console Help documentation.

If you have already completed the setup process, you can access those credentials by going to the Credentials section of the [Google API Manager Console](https://console.cloud.google.com/projectselector2/apis/dashboard?pli=1&supportedpurview=project). The OAuth2 key (Client ID) and secret (Client secret) are used to supply the required fields in the UI.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a **Name** for this authentication configuration.
4.  Select **Google OAuth** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
5.  The **Google OAuth2 Key** and **Google OAuth2 Secret** fields are pre-populated. If not, use the credentials Google supplied during the web application setup process. Save these settings for use in the following steps.

6.  Copy and paste Google’s Client ID into the **Google OAuth2 Key** field.
7.  Copy and paste Google’s Client secret into the **Google OAuth2 Secret** field.
8.  Optional: Enter information for the following fields using the tooltip provided for instructions and required format:

  -  **Access Token URL**
  -  **Access Token Method**
  -  **Authorization URL**
  -  **Revoke Token Method**
  -  **Revoke Token URL**
  -  **OIDC JWT Algorithm(s)**
  -  **OIDC JWT**

9.  Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. Note:
      Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

10.  To automatically create organizations, users, and teams upon successful login, select **Create objects**.
11.  To enable this authentication method upon creation, select **Enabled**.
12.  To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users**.
13.  Click Create Authentication Method.

## Results

To verify that the authentication is configured correctly, log out of Ansible Automation Platform and check that the login screen displays the logo of your authentication chosen method to enable logging in with those credentials.

## What to do next

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#gw-mapping "To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.").
