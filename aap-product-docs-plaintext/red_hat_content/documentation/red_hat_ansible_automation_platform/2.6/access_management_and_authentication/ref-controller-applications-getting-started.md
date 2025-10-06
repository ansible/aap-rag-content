# 3. Configuring access to external applications with token-based authentication
## 3.1. Manage OAuth applications
### 3.1.1. Getting started with OAuth Applications




You can access the **OAuth Applications** page from the navigation panel by selectingAccess Management→OAuth Applications. From there you can view, create, sort and search for applications currently managed by Ansible Automation Platform and automation controller.

If no applications exist, you can create one by clickingCreate OAuth application.


<span id="ref-gw-access-rules-apps-tokens"></span>
Access rules for applications are as follows:


- Platform administrators can view and manipulate all applications in the system.
- Platform auditors can only view applications in the system.
- Tokens, on the other hand, are resources used to authenticate incoming requests and mask the permissions of the underlying user.


Access rules for tokens are as follows:

- Users can create personal access tokens for themselves.
- Platform administrators are able to view and manipulate every token in the system.
- Platform auditors can only view tokens in the system.
- Other normal users are only able to view and manipulate their own tokens.


Note
Users can only view the token or refresh the token value at the time of creation.



#### 3.1.1.1. Application functions




Several OAuth 2 utilities are available for authorization, token refresh, and revoke. You can specify the following grant types when creating an application:

Note
You can only use the authorization code type to acquire an access token when using an application. When integrating an external web application with Ansible Automation Platform, that web application might need to create OAuth2 tokens on behalf of users in that other web application. Creating an application in the platform with the authorization code grant type is the preferred way to do this because:

- This allows an external application to obtain a token from Ansible Automation Platform for a user, using their credentials.
- Compartmentalized tokens issued for a particular application enables those tokens to be easily managed. For example, revoking _all_ tokens associated with that application without having to revoke all tokens in the system.




##### 3.1.1.1.1. Requesting an access token after expiration




The default expiration for access tokens is 1 year.

The best way to set up application integrations using the **Authorization code** grant type is to allowlist the origins for those cross-site requests. More generally, you must allowlist the service or application you are integrating with the platform, for which you want to provide access tokens.

To do this, have your administrator add this allowlist to their local Ansible Automation Platform settings file:

```
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGIN_REGEXES = [
r"http://django-oauth-toolkit.herokuapp.com*",
r"http://www.example.com*"
]
```

Where `<a class="link" href="http://django-oauth-toolkit.herokuapp.com">http://django-oauth-toolkit.herokuapp.com</a>` and `<a class="link" href="http://www.example.com">http://www.example.com</a>` are applications requiring tokens with which to access the platform.

#### 3.1.1.2. OAuth2 application and token migration (2.4 to 2.6)




During the upgrade from Ansible Automation Platform 2.4 to 2.6, there are important changes to how OAuth2 applications and tokens are managed. Ansible Automation Platform now uses platform gateway OAuth applications and deprecates automation controller OAuth applications.

-  **Automation controller OAuth applications** : You can view and edit existing automation controller applications, but new ones can no longer be created. These legacy applications continue to function, but they might be removed in a future release. Plan to migrate to platform gateway OAuth applications.
-  **Automation controller tokens** : Automation controller personal access tokens (PATs), are also deprecated. Guide users to move to platform gateway PATs.
-  **Platform gateway OAuth applications and tokens** : Platform applications and tokens offer an updated interface and are the standard for future use. Move to these applications and tokens.


#### 3.1.1.3. Manage `OAUTH2_PROVIDER` settings




The `OAUTH2_PROVIDER` settings from automation controller are managed by platform gateway after upgrading from 2.4. to 2.6. The default token expiration values might differ between automation controller and platform gateway.

- The default access token expiration is updated from 1,000 years to 1 year. This change increases credential security through more frequent token rotation.
- Platform gateway’s default OAUTH2_PROVIDER settings are:


```
{      "ACCESS_TOKEN_EXPIRE_SECONDS": 31536000000,      "REFRESH_TOKEN_EXPIRE_SECONDS": 2628000,      "AUTHORIZATION_CODE_EXPIRE_SECONDS": 600    }
```

If you previously set a token expiration shorter than one year, you must manually update the platform gateway settings to match your required configuration.




