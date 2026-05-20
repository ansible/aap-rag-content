# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.16. Configuring GitHub enterprise team authentication

To set up social authentication for a GitHub enterprise team, you must obtain a GitHub Enterprise Organization URL, an Organization API URL, an Organization OAuth2 key and secret for a web application.

To obtain the URLs, see the [GitHub Enterprise administration documentation](https://docs.github.com/en/enterprise-server@3.1/rest/reference/enterprise-admin).

To obtain the key and secret, you must first register your enterprise organization-owned application at `<https://github.com/organizations/<yourorg>/settings/applications>`.

The OAuth2 key (Client ID) and secret (Client Secret) are used to supply the required fields in the UI. To register the application, you must supply it with your webpage URL, which is the **Callback URL** shown in the Authenticator details for your authenticator configuration. See [Displaying authenticator details](#gw-display-auth-details "2.8.3.&nbsp;Displaying authenticator details") for instructions on accessing this information.

Each key and secret must belong to a unique application and cannot be shared or reused between different authentication backends. The OAuth2key (Client ID) and secret (Client Secret) are used to supply the required fields in the UI.

**Procedure**

1. From the navigation panel, select Access Management → Authentication Methods.

2. Click Create authentication.

3. Enter a **Name** for this authentication configuration.

4. Select **GitHub enterprise team** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.

5. When the application is registered, GitHub displays the **Client ID** and **Client Secret**:


1. Copy and paste the GitHub Client ID into the GitHub OAuth2 Key field.
2. Copy and paste the GitHub Client Secret into the GitHub OAuth2 Secret field.

6. In the **Base URL** field, enter the hostname of the GitHub Enterprise instance, for example, `<https://github.orgexample.com>`.

7. In the **Github OAuth2 Enterprise API URL** field, enter the API URL of the GitHub Enterprise instance, for example, `<https://github.example.com/api/v3>`.

8. Enter the OAuth2 key (Client ID) from your GitHub developer application in the **GitHub OAuth2** team ID field.

9. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.


Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

10. To automatically create organizations, users, and teams upon successful login, select **Create objects**.

11. To enable this authentication method upon creation, select **Enabled**.

12. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users**.

13. Click Create Authentication Method.

**Verification**

To verify that the authentication is configured correctly, log out of Ansible Automation Platform and check that the login screen displays the logo of your authentication chosen method to enable logging in with those credentials.

**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#gw-mapping).

