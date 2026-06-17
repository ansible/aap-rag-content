+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_set_up_azure"
template = "docs/aem-title.html"
title = "Configure Microsoft Entra ID authentication - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_set_up_azure/aem-page/secure-proc_controller_set_up_azure.html"
last_crumb = "Configure Microsoft Entra ID authentication"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure Microsoft Entra ID authentication"
oversized = "false"
page_slug = "secure-proc_controller_set_up_azure"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-proc_controller_set_up_azure"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-proc_controller_set_up_azure/toc/toc.json"
type = "aem-page"
+++

# Configure Microsoft Entra ID authentication

To set up enterprise authentication for Microsoft Entra ID, formerly known as Microsoft Azure Active Directory (AD), follow these steps:

## About this task

1. **Configure your Ansible Automation Platform** to use Microsoft Entra ID authentication using the steps in this procedure.
2. **Register Ansible Automation Platform** in Microsoft Entra ID by following the [Quickstart: Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app). This process provides you with an Application (client) ID and Application secret.
3. **Add the redirect URL in Microsoft Entra ID**. After completing the configuration wizard for Microsoft Entra ID authentication in your platform, copy the URL displayed in the **Azure AD OAuth2 Callback URL** field. Then, go to your registered enterprise application in Azure and add this URL as a **Redirect URL** (also referred to as a **Callback URL** in Ansible Automation Platform) as described in [How to add a redirect URI to your application](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri). This step is required for the login flow to work correctly.


The attributes provided by Microsoft Entra ID are not set in the Ansible Automation Platform configuration for this authentication type. Instead, the [social_core azuread backend](https://github.com/python-social-auth/social-core/blob/master/social_core/backends/azuread.py#L85-L98) provides the translation of claims provided by Microsoft Entra ID. The user attributes that allow Ansible Automation Platform to correctly identify the user and assign the proper attributes such as given name, surname, email, and username include the following:

| Ansible Automation Platform attribute | Microsoft Entra ID parameter    |
| ------------------------------------- | ------------------------------- |
| <br>authenticator\_uid                | <br>upn                         |
| <br>Username                          | <br>name                        |
| <br>First Name                        | <br>given\_name                 |
| <br>Last Name                         | <br>family\_name                |
| <br>Email                             | <br>email (falling back to upn) |


To set up enterprise authentication for Microsoft Azure Active Directory (AD), you need to obtain an OAuth2 key and secret by registering your organization-owned application from Azure at: [Quickstart: Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).

Each key and secret must belong to a unique application and cannot be shared or reused between different authentication backends. To register the application, you must supply it with your webpage URL, which is the Callback URL shown in the Authenticator details for your authenticator configuration. See [Displaying authenticator details](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_managing_authentication#gw-display-auth-details "After you locate the authenticator you want to review, you can display the configuration details:") for instructions on accessing this information.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a **Name** for this authentication configuration.
4.  Select **Azuread** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
5.  Click Edit, copy and paste Microsoft’s **Application (Client) ID** to the **OIDC Key** field.
6.  If your Microsoft Entra ID is configured to provide user group information within a groups claim, ensure that the platform is configured with a **Groups Claim** name that matches your Microsoft Entra ID configuration. This allows the platform to correctly identify and associate groups for users logging in through Microsoft Entra ID. Note:
      Groups coming from Microsoft Entra ID can be identified using either unique IDs or group names. When creating group mappings for a Microsoft Entra ID authenticator, you can use either the unique ID or the group name.

    By default, Microsoft Entra ID uses groups as the default group claim name. So, be sure to either set the value to the default or to any custom override you have set in your IdP. The current default is set to preserve the existing behavior unless explicitly changed.

7.  Following instructions for [registering your application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app), supply the key (shown at one time only) to the client for authentication.
8.  Copy and paste the secret key created for your Microsoft Entra ID/Microsoft Azure AD application to the **OIDC Secret** field.
9.  Optional: By default, the name attribute from Microsoft Entra ID is used as the username field within Ansible Automation Platform. If you want to override that default value and use another attribute from Microsoft Entra ID, enter that attribute in the username field.
10.  Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. Note:
      Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

11.  To automatically create organizations, users, and teams upon successful login, select **Create objects**.
12.  To enable this authentication method upon creation, select **Enabled**.
13.  To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users**.
14.  Click Create Authentication Method.

## Results

To verify that the authentication is configured correctly, log out of Ansible Automation Platform and check that the login screen displays the logo of your authentication chosen method to enable logging in with those credentials.

## What to do next

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#gw-mapping "To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.").
