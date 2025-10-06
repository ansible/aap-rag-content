# 6. Configuring Ansible Automation Platform
## 6.2. Platform gateway
### 6.2.1. Configuring platform security




From the **Platform gateway settings** page, you can configure platform security settings.

**Procedure**

1. From the navigation panel, selectSettings→Platform gateway.
1. The **Platform gateway settings** page is displayed.
1. To configure the options, clickEdit.
1. You can configure the following **Security** settings:


-  **Allow admin to set insecure** : Whether a superuser account can save an insecure password when editing any local user account.
-  **Gateway basic auth enabled** : Enable basic authentication to the platform gateway API.

Turning this off prevents all basic authentication (local users), so customers need to make sure they have their alternative authentication mechanisms correctly configured before doing so.

Turning it off with only local authentication configured also prevents all access to the UI.

**Social auth username is full email** : Enabling this setting alerts social authentication to use the full email as username instead of the full name.

**Gateway token name** : The header name to push from the proxy to the backend service.

Warning
If this name is changed, backends must be updated to compensate.




-  **Gateway access token expiration** : How long the access tokens are valid for.
-  **Jwt private key** : The private key used to encrypt the JWT tokens sent to backend services.

This should be a private RSA key and one should be generated automatically on installation.

Note
Use caution when rotating the key as it will cause current sessions to fail until their JWT keys are reset.




- (Read only) **Jwt public key** : The private key used to encrypt the JWT tokens sent to backend services.

This should be a private RSA key and one should be generated automatically on installation.

Note
See other services' documentation on how they consume this key.





1. ClickSave changesto save the changes or proceed to configure the other platform options available.


