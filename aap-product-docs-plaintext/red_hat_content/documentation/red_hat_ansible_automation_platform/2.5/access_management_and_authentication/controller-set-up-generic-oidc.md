# 3. Configuring authentication in the Ansible Automation Platform
## 3.5. Configuring an authentication type
### 3.5.7. Configuring generic OIDC authentication




OpenID Connect (OIDC) uses the OAuth 2.0 framework. It enables third-party applications to verify the identity and obtain basic end-user information. The main difference between OIDC and SAML is that SAML has a service provider (SP)-to-IdP trust relationship, whereas OIDC establishes the trust with the channel (HTTPS) that is used to obtain the security token. To obtain the credentials needed to set up OIDC with Ansible Automation Platform, see the documentation from the IdP of your choice that has OIDC support.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this authentication configuration.
1. Select **Generic OIDC** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
1. Select a legacy authenticator method from the **Auto migrate users from** list. After upgrading from 2.4 to 2.5, this is the legacy authenticator from which to automatically migrate users to this new authentication configuration. Refer to [Ansible Automation Platform post-upgrade steps](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade) in the RPM upgrade and migration guide for important information about migrating users.
1. Enter the following information:


-  **OIDC Provider URL** : The URL for your OIDC provider.
-  **OIDC Key** : The client ID from your third-party IdP.
-  **OIDC Secret** : The client secret from your IdP.

1. Optional: Select the HTTP method to be used when requesting an access token from the **Access Token Method** list. The default method is **POST** .
1. Optionally enter information for the following fields using the tooltips provided for instructions and required format:


-  **Access Token Method** - The default method is **POST** .
-  **Access Token URL**
-  **Access Token Method**
-  **Authorization URL**
-  **ID Key**
-  **ID Token Issuer**
-  **JWKS URI**
-  **OIDC Public Key**
-  **Revoke Token Method** - The default method is **GET** .
-  **Revoke Token URL**
-  **Response Type**
-  **Token Endpoint Auth Method**
-  **Userinfo URL**
-  **Username Key**

1. Use the **Verify OIDC Provider Certificate** to enable or disable the OIDC provider SSL certificate verification.
1. Use the **Redirect** State to enable or disable the state parameter in the redirect URI. It is recommended that this is enabled to prevent Cross Site Request Forgery (CSRF) attacks.
1. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.

Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.




1. To automatically create organizations, users, and teams upon successful login, select **Create objects** .
1. To enable this authentication method upon creation, select **Enabled** .
1. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .
1. ClickCreate Authentication Method.


**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (like username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-mapping) .


