# Configure access to external applications with tokens
## Get started with OAuth Applications
### OAuth2 application and token migration (2.4 to 2.6)

During the upgrade from Ansible Automation Platform 2.4 to 2.6, there are important changes to how OAuth2 applications and tokens are managed. Ansible Automation Platform now uses platform gateway OAuth applications and deprecates automation controller OAuth applications.

- **Automation controller OAuth applications**: You can view and edit existing automation controller applications, but new ones can no longer be created. These legacy applications continue to function, but they might be removed in a future release. Plan to migrate to platform gateway OAuth applications.
- **Automation controller tokens**: Automation controller personal access tokens (PATs), are also deprecated. Guide users to move to platform gateway PATs.
- **Platform gateway OAuth applications and tokens**: Platform applications and tokens offer an updated interface and are the standard for future use. Move to these applications and tokens.

### Manage `OAUTH2_PROVIDER` settings

The `OAUTH2_PROVIDER` settings from automation controller are managed by platform gateway after upgrading from 2.4. to 2.6. The default token expiration values might differ between automation controller and platform gateway.

- The default access token expiration is updated from 1,000 years to 1 year. This change increases credential security through more frequent token rotation.

- Platform gateway’s default OAUTH2_PROVIDER settings are:

```
{
"ACCESS_TOKEN_EXPIRE_SECONDS": 31536000000,
"REFRESH_TOKEN_EXPIRE_SECONDS": 2628000,
"AUTHORIZATION_CODE_EXPIRE_SECONDS": 600
}
```
If you previously set a token expiration shorter than one year, you must manually update the platform gateway settings to match your required configuration.
