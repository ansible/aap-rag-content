# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.3. Configuring SAML authentication




SAML allows the exchange of authentication and authorization data between an Identity Provider (IdP) and a Service Provider (SP). Ansible Automation Platform is a SAML SP that you can configure to talk with one or more SAML IdPs to authenticate users.

Based on groups and attributes optionally provided by the SAML IdP, users can be placed into teams and organizations in Ansible Automation Platform based on the authenticator maps tied to this authenticator. This mapping ensures that when a user logs in through SAML, Ansible Automation Platform can correctly identify the user and assign the proper attributes like first name, last name, email, and group membership.

**Prerequisites**

Before you configure SAML authentication in Ansible Automation Platform, be sure you do the following:


- Configure a SAML Identity Provider (IdP).
- Pre-configure the SAML IdP with the settings required for integration with Ansible Automation Platform. For example, in Microsoft Entra ID you can configure the following:


-  **Identifier (Entity ID):** This can be any value that you want, but it needs to match the one configured in your Ansible Automation Platform.
-  **Reply URL (Assertion Consumer Service (ACS) URL):** This URL is auto generated when the SAML method is configured in Ansible Automation Platform. That value must be copied from Ansible Automation Platform and pasted in your IdP settings.

- Gather the user attributes for your SAML IdP application. Different IdPs might use different attribute names and formats. Refer to documentation for your specific IdP for the exact attribute names and the expected values.
- Generate a private key and public certificate using the following command:


```
$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes
```




**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this SAML configuration.
1. Select **SAML** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.


1. Select a legacy authenticator method from the **Auto migrate users from** list. After upgrading from 2.4 to 2.5, this is the legacy authenticator from which to automatically migrate users to this new authentication configuration. Refer to [Ansible Automation Platform post-upgrade steps](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade) in the RPM upgrade and migration guide for important information about migrating users.
1. Enter the application-defined unique identifier used as the audience of the SAML service provider configuration in the **SAML Service Provider Entity ID** field. This is usually the base URL of your service provider, but the actual value depends on the Entity ID expected by your IdP.
1. Include the certificate content in the **SAML Service Provider Public Certificate** field. This information is contained in the cert.pem you created as a prerequisite and must include the `    —–BEGIN CERTIFICATE—–` and `    —–END CERTIFICATE—–` .
1. Include the private key content in the **SAML Service Provider Private Key** field. This information is contained in the key.pem you created as a prerequisite and must include the `    —–BEGIN PRIVATE KEY—–` and `    —–END PRIVATE KEY—–` .
1. Enter the URL to redirect the user to for login initiation in the **IdP Login URL** field. This is the login URL from your SAML IdP application.
1. Enter the public cert used for secrets coming from the **IdP in the IdP Public Cert** field. This is the SAML certificate available for download from IdP.

Note
The IdP in the IdP Public Cert field should contain the entire certificate, including the `    —–BEGIN CERTIFICATE—–` and `    —–END CERTIFICATE—–` . You must manually enter the prefix and suffix if the IdP does not include it.




1. Enter the entity ID returned in the assertion in the **Entity ID** . This is the identifier from your IdP SAML application. You can find this value in the SAML metadata provided by your IdP.
1. Enter user details in the **Groups** , **User Email** , **Username** , **User Last Name** and **User First Name** .
1. Enter a permanent ID for the user in the **User Permanent ID** field. This field is required.

Note
Additional attributes might be available through your SAML IdP. Those values must be included in either the **Additional Authenticators Fields** or the **SAML IDP to extra_data attribute mapping** field. Refer to those steps for details.




1. The **SAML Assertion Consumer Service (ACS) URL** field registers the service as a service provider (SP) with each identity provider (IdP) you have configured. Leave this field blank. After you save this authentication method, it is auto generated. This field must match the **Reply URL** setting in your IdP.
1. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. For example, to ensure all SAML IdP attributes other than Email, Username, Last Name, First Name are included for mapping, enter the following:


```
GET_ALL_EXTRA_DATA: true
```

Alternatively, you can include a list of SAML IdP attributes in the **SAML IDP to extra_data attribute mapping** field.

Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.




1. In the **SAML Service Provider Organization Info** field, provide the URL, display name, and the name of your app.


```
{      "en-US": {        "url": "http://www.example.com",        "displayname": "Example",        "name": "example"      }    }
```


1. In the **SAML Service Provider Technical Contact** field, give the name and email address of the technical contact for your service provider.


```
{    "givenName": "Some User",    "emailAddress": "suser@example.com"    }
```


1. In the **SAML Service Provider Support Contact** field, give the name and email address of the support contact for your service provider.


```
{    "givenName": "Some User",    "emailAddress": "suser@example.com"    }
```


1. Optional: Provide extra configuration data in the **SAML Service Provider extra configuration data** field. For example, you can choose to enable signing requests for added security:


```
{    "sign_request": True,    }
```

This field is the equivalent to the `    SOCIAL_AUTH_SAML_SP_EXTRA` in the API. For more information, see [OneLogin’s SAML Python Toolkit](https://github.com/SAML-Toolkits/python-saml#settings) to learn about the valid service provider extra (SP_EXTRA) parameters.


1. Optional: Provide security settings in the **SAML Security Config** field. This field is the equivalent to the `    SOCIAL_AUTH_SAML_SECURITY_CONFIG` field in the API.


```
// Indicates whether the &lt;samlp:AuthnRequest&gt; messages sent by this SP // will be signed. [Metadata of the SP will offer this info]    "authnRequestsSigned": false,        // Indicates a requirement for the &lt;samlp:Response&gt;, &lt;samlp:LogoutRequest&gt; // and &lt;samlp:LogoutResponse&gt; elements received by this SP to be signed.    "wantMessagesSigned": false,        // Indicates a requirement for the &lt;saml:Assertion&gt; elements received by // this SP to be signed. [Metadata of the SP will offer this info]    "wantAssertionsSigned": false,        // Authentication context.    // Set to false and no AuthContext will be sent in the AuthNRequest,    // Set true or don't present this parameter and you will get an AuthContext 'exact' 'urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport'    // Set an array with the possible auth context values: array ('urn:oasis:names:tc:SAML:2.0:ac:classes:Password', 'urn:oasis:names:tc:SAML:2.0:ac:classes:X509'),    "requestedAuthnContext": true,
```

For more information and additional options, see [OneLogin’s SAML Python Toolkit](https://github.com/SAML-Toolkits/python-saml#settings) .


1. Optional: In the **SAML IDP to extra_data attribute mapping** field, enter values to map IDP attributes to extra_data attributes. These values will include additional user information beyond standard attributes like Email or Username to be mapped. For example:


```
- Department    - UserType    - Organization
```

For more information on the values you can include, see [advanced SAML settings](https://python-social-auth.readthedocs.io/en/latest/backends/saml.html#advanced-settings) .

Important
Make sure you include all relevant values so that everything gets mapped correctly for your configuration. Alternatively, you can include the `    GET_ALL_EXTRA_DATA: true` in the **Additional Authenticator Fields** to allow mapping of all available SAML IdP attributes.




1. To automatically create organizations, users, and teams upon successful login, select **Create objects** .
1. To enable this authentication method upon creation, select **Enabled** .
1. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .
1. ClickCreate Authentication Method.


Important
You can configure an HTTPS redirect for SAML in operator-based deployments to simplify login for your users. For the steps to configure this setting, see [Enabling single sign-on (SSO) for platform gateway on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#proc-operator-enable-https-redirect) .



**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (like username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-mapping) .


#### 2.5.3.1. Configuring transparent SAML logins




For transparent logins to work, you must first get IdP-initiated logins to work.

**Procedure**

- Set the `    RelayState` on the IdP to "IdP".


