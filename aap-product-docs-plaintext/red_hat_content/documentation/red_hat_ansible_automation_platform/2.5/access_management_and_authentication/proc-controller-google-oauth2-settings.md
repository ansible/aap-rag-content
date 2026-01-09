# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.6. Configuring Google OAuth2 authentication




To set up social authentication for Google, you must obtain an OAuth2 key and secret for a web application. To do this, you must first create a project and set it up with Google.

For instructions, see [Setting up OAuth 2.0](https://support.google.com/googleapi/answer/6158849) in the Google API Console Help documentation.

If you have already completed the setup process, you can access those credentials by going to the Credentials section of the [Google API Manager Console](https://console.cloud.google.com/projectselector2/apis/dashboard?pli=1&supportedpurview=project) . The OAuth2 key (Client ID) and secret (Client secret) are used to supply the required fields in the UI.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this authentication configuration.
1. Select **Google OAuth** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.


1. Select a legacy authenticator method from the **Auto migrate users from** list. After upgrading from 2.4 to 2.5, this is the legacy authenticator from which to automatically migrate users to this new authentication configuration. Refer to [Ansible Automation Platform post-upgrade steps](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade) in the RPM upgrade and migration guide for important information about migrating users.
1. The **Google OAuth2 Key** and **Google OAuth2 Secret** fields are pre-populated.

If not, use the credentials Google supplied during the web application setup process. Save these settings for use in the following steps.


1. Copy and paste Google’s Client ID into the **Google OAuth2 Key** field.
1. Copy and paste Google’s Client secret into the **Google OAuth2 Secret** field.
1. Optional: Enter information for the following fields using the tooltips provided for instructions and required format:


-  **Access Token URL**
-  **Access Token Method**
-  **Authorization URL**
-  **Revoke Token Method**
-  **Revoke Token URL**
-  **OIDC JWT Algorithm(s)**
-  **OIDC JWT**

1. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.

Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.




1. To automatically create organizations, users, and teams upon successful login, select **Create objects** .
1. To enable this authentication method upon creation, select **Enabled** .
1. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .

ClickCreate Authentication Method.




**Verification**

To verify that the authentication is configured correctly, log out of Ansible Automation Platform and check that the login screen displays the logo of your authentication chosen method to enable logging in with those credentials.


**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (like username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-mapping) .


