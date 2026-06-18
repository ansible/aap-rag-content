+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_github_organization_settings"
title = "Configure GitHub organization authentication - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_github_organization_settings/aem-page/secure-proc_controller_github_organization_settings.html"
last_crumb = "Configure GitHub organization authentication"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure GitHub organization authentication"
oversized = "false"
page_slug = "secure-proc_controller_github_organization_settings"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-proc_controller_github_organization_settings"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_github_organization_settings/toc/toc.json"
type = "aem-page"
+++

# Configure GitHub organization authentication

When defining account authentication with either an organization or a team within an organization, you should use the specific organization and team settings. Account authentication can be limited by an organization and by a team within an organization.

## About this task

You can also choose to permit all by specifying non-organization or non-team based settings. You can limit users who can log in to the platform by limiting only those in an organization or on a team within an organization.

To set up social authentication for a GitHub organization, you must obtain an OAuth2 key and secret for a web application by using the [registering the new application with GitHub](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app).

The OAuth2 key (Client ID) and secret (Client Secret) are used to supply the required fields in the UI. To register the application, you must supply it with your webpage URL, which is the Callback URL shown in the Authenticator details for your authenticator configuration. See [Displaying authenticator details](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_authentication#gw-display-auth-details "After you locate the authenticator you want to review, you can display the configuration details:") for instructions on accessing this information.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a **Name** for this authentication configuration.
4.  Select **GitHub organization** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
5.  When the application is registered, GitHub displays the **Client ID** and **Client Secret**:
  1.  Copy and paste the GitHub Client ID into the GitHub OAuth2 Key field.
  2.  Copy and paste the GitHub Client Secret into the GitHub OAuth2 Secret field.
6.  Enter the name of your GitHub organization, as used in your organization’s URL, for example, `https://github.com/<yourorg>/` in the **GitHub OAuth Organization Name** field.
7.  Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. Note:
      Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

8.  Enter the authorization scope for users in the **GitHub OAuth2 Scope** field. The default is `read:org`.
9.  To automatically create organizations, users, and teams upon successful login, select **Create objects**.
10.  To enable this authentication method upon creation, select **Enabled**.
11.  To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users**.
12.  Click Create Authentication Method.

## Results

To verify that the authentication is configured correctly, log out of Ansible Automation Platform and check that the login screen displays the logo of your authentication chosen method to enable logging in with those credentials.

## What to do next

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-mapping "To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.").
