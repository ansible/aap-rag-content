# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.7. Configuring generic OIDC authentication




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
-  **Callback URL** - The OIDC **Callback URL** field registers the service as a service provider (SP) with each OIDC provider you have configured. Leave this field blank. After you save this authentication method, it is auto generated. Configure your IdP to allow redirects to this URL as part of the authentication flow.
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


#### 2.5.7.1. Troubleshoot Generic OIDC Single Sign-On authentication failures




Authentication fails if the `OIDC JWT Algorithm` setting is not explicitly defined. The authentication code requires a list of acceptable algorithms, which it does not retrieve automatically from the OpenID Connect (OIDC) configuration endpoint.

##### 2.5.7.1.1. Configuring JWT_Algorithms manually




To resolve the authentication failure, manually provide the list of supported algorithms in the platform gateway configuration.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. Select your OIDC authenticator from the list.
1. ClickEdit authenticationand locate the **OIDC JWT Algorithm(s)** field.
1. Enter the list of supported algorithms as a YAML list or a JSON array. These algorithms are typically available from your IdP’s OpenID Connect (OIDC) discovery endpoint.

**Example**


```
[        "PS384",        "ES384",        "RS384",        "HS256",        "HS512",        "ES256",        "RS256",        "HS384",        "ES512",        "PS256",        "PS512",        "RS512"    ]
```


1. Save your changes. The system uses these specified algorithms for token verification, resolving any authentication failures related to their absence.


##### 2.5.7.1.2. Enabling debugging for enterprise authentication




To further diagnose authentication issues, enable debug logging in platform gateway.

**Procedure**

1. Change the logging configuration in the platform gateway’s `    settings.py` file.
1. Set the logging level for the `    ansible_base` logger to `    DEBUG` :


```
LOGGING['loggers']['ansible_base']['level'] = 'DEBUG'
```

After this change, detailed `    AuthTokenError` messages are displayed in the logs, providing specific information about the cause of the failure.




##### 2.5.7.1.3. Troubleshooting Generic OIDC scope mismatches




Authentication fails when the Identity Provider (IdP) does not support the default scopes automatically appended by the system.

To prevent the system from appending this default scope, you must add a setting to your authenticator configuration.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. Select your OIDC authenticator from the list.
1. ClickEdit authentication.
1. In the **Additional Authenticator Fields** section, add the following attribute and value. This input box supports either YAML or JSON. Ensure you add this key-value pair on a new line if there are other fields present:


```
IGNORE_DEFAULT_SCOPE: True
```


1. Save your changes. The authenticator now only uses the scopes you explicitly defined, resolving any authentication failures related to unsupported scopes.


