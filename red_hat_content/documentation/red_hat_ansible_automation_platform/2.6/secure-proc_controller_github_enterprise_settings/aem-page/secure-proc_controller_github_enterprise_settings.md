+++
template = "docs/aem-title.html"
title = "Configure GitHub enterprise authentication - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_github_enterprise_settings"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_github_enterprise_settings/aem-page/secure-proc_controller_github_enterprise_settings.html"
last_crumb = "Configure GitHub enterprise authentication"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure GitHub enterprise authentication"
oversized = "false"
page_slug = "secure-proc_controller_github_enterprise_settings"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_controller_github_enterprise_settings"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_github_enterprise_settings/toc/toc.json"
type = "aem-page"
+++

# Configure GitHub enterprise authentication

To set up social authentication for a GitHub enterprise, you must obtain a GitHub Enterprise URL, an API URL, OAuth2 key and secret for a web application.

## About this task

To obtain the URLs, see the [GitHub Enterprise administration documentation](https://docs.github.com/en/enterprise-server@3.1/rest/reference/enterprise-admin).

The OAuth2 key (Client ID) and secret (Client Secret) are used to supply the required fields in the UI. To register the application, you must supply it with your webpage URL, which is the **Callback URL** shown in the Authenticator details for your authenticator configuration. See [Displaying authenticator details](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_managing_authentication#gw-display-auth-details "After you locate the authenticator you want to review, you can display the configuration details:") for instructions on accessing this information.

Each key and secret must belong to a unique application and cannot be shared or reused between different authentication backends. The OAuth2 key (Client ID) and secret (Client Secret) are used to supply the required fields in the UI.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a **Name** for this authentication configuration.
4.  Select **GitHub enterprise** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
5.  When the application is registered, GitHub displays the **Client ID** and **Client Secret**:
  1.  Copy and paste the GitHub Client ID into the GitHub OAuth2 Key field.
  2.  Copy and paste the GitHub Client Secret into the GitHub OAuth2 Secret field.
6.  In the **Base URL** field, enter the hostname of the GitHub Enterprise instance, for example, `<https://github.example.com>`.
7.  In the **Github OAuth2 Enterprise API URL** field, enter the API URL of the GitHub Enterprise instance, for example, `<https://github.example.com/api/v3>`.
8.  Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. Note:
      Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

9.  To automatically create organizations, users, and teams upon successful login, select **Create objects**.
10.  To enable this authentication method upon creation, select **Enabled**.
11.  To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users**.
12.  Click Create Authentication Method.

## Results

To verify that the authentication is configured correctly, log out of Ansible Automation Platform and check that the login screen displays the logo of your authentication chosen method to enable logging in with those credentials.

## What to do next

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#gw-mapping "To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.").
