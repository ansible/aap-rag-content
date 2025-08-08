# 3. Configuring authentication in the Ansible Automation Platform
## 3.5. Configuring an authentication type
### 3.5.5. Configuring Microsoft Entra ID authentication




To set up enterprise authentication for Microsoft Entra ID, formerly known as Microsoft Azure Active Directory (AD), follow these steps:

1.  **Configure your Ansible Automation Platform** to use Microsoft Entra ID authentication using the steps in this procedure.
1.  **Register Ansible Automation Platform** in Microsoft Entra ID by following the [Quickstart: Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) . This process provides you with an Application (client) ID and Application secret.
1.  **Add the redirect URL in Microsoft Entra ID** . After completing the configuration wizard for Microsoft Entra ID authentication in your platform, copy the URL displayed in the **Azure AD OAuth2 Callback URL** field. Then, go to your registered enterprise application in Azure and add this URL as a **Redirect URL** (also referred to as a **Callback URL** in Ansible Automation Platform) as described in [How to add a redirect URI to your application](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri) . This step is required for the login flow to work correctly.


The attributes provided by Microsoft Entra ID are not set in the Ansible Automation Platform configuration for this authentication type. Instead, the [social_core azuread backend](https://github.com/python-social-auth/social-core/blob/master/social_core/backends/azuread.py#L85-L98) provides the translation of claims provided by Microsoft Entra ID. The user attributes that allow Ansible Automation Platform to correctly identify the user and assign the proper attributes like first name, last name, email, and username include the following:

| Ansible Automation Platform attribute | Microsoft Entra ID parameter |
| --- | --- |
| authenticator_uid | upn |
| Username | name |
| First Name | given_name |
| Last Name | family_name |
| Email | email (falling back to upn) |


Each key and secret must belong to a unique application and cannot be shared or reused between different authentication backends. To register the application, you must supply it with your webpage URL, which is the Callback URL shown in the Authenticator details for your authenticator configuration. See [Displaying authenticator details](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-display-auth-details) for instructions on accessing this information.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this authentication configuration.
1. Select **Azuread** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
1. Select a legacy authenticator method from the **Auto migrate users from** list. After upgrading from 2.4 to 2.5, this is the legacy authenticator from which to automatically migrate users to this new authentication configuration. Refer to [Ansible Automation Platform post-upgrade steps](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade) in the RPM upgrade and migration guide for important information about migrating users.
1. ClickEdit, copy and paste Microsoft’s **Application (Client) ID** to the **OIDC Key** field.
1. If your Microsoft Entra ID is configured to provide user group information within a groups claim, ensure that the platform is configured with a **Groups Claim** name that matches your Microsoft Entra ID configuration. This allows the platform to correctly identify and associate groups for users logging in through Microsoft Entra ID.

Note
Groups coming from Microsoft Entra ID can be identified using either unique IDs or group names. When creating group mappings for a Microsoft Entra ID authenticator, you can use either the unique ID or the group name.

By default, Microsoft Entra ID uses groups as the default group claim name. So, be sure to either set the value to the default or to any custom override you have set in your IdP. The current default is set to preserve the existing behavior unless explicitly changed.




1. Following instructions for [registering your application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) , supply the key (shown at one time only) to the client for authentication.
1. Copy and paste the secret key created for your Microsoft Entra ID/Microsoft Azure AD application to the **OIDC Secret** field.
1. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.

Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.




1. To automatically create organizations, users, and teams upon successful login, select **Create objects** .
1. To enable this authentication method upon creation, select **Enabled** .
1. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .
1. ClickCreate Authentication Method.


**Verification**

To verify that the authentication is configured correctly, log out of Ansible Automation Platform and check that the login screen displays the logo of your authentication chosen method to enable logging in with those credentials.


**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (like username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-mapping) .


**Additional resources**

-  [What is the Microsoft identity platform?](https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview)


