# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.9. Configuring GitHub authentication




You can connect GitHub identities to Ansible Automation Platform using OAuth. To set up GitHub authentication, you need to obtain an OAuth2 key and secret by registering your organization-owned application from GitHub using the [registering the new application with GitHub](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app) .

The OAuth2 key (Client ID) and secret (Client Secret) are used to supply the required fields in the UI. To register the application, you must supply it with your webpage URL, which is the Callback URL shown in the Authenticator details for your authenticator configuration. See [Displaying authenticator details](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-display-auth-details) for instructions on accessing this information.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this authentication configuration.
1. Select **GitHub** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.


1. Select a legacy authenticator method from the **Auto migrate users from** list. After upgrading from 2.4 to 2.5, this is the legacy authenticator from which to automatically migrate users to this new authentication configuration. Refer to [Ansible Automation Platform post-upgrade steps](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade) in the RPM upgrade and migration guide for important information about migrating users.
1. When the application is registered, GitHub displays the **Client ID** and **Client Secret** :


1. Copy and paste the GitHub Client ID into the GitHub OAuth2 Key field.
1. Copy and paste the GitHub Client Secret into the GitHub OAuth2 Secret field.

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


