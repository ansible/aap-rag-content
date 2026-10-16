# Post-upgrade requirements
## Verify your authentication configuration after upgrade
### About this task

In Ansible Automation Platform 2.7, all third-party authentication provider configuration has moved to platform gateway. Configuration in automation controller has been removed.

This applies to:

- LDAP
- SAML
- RADIUS
- TACACS+
- OAuth providers (GitHub, Google, Azure AD, Generic OIDC)

### Procedure

1. Log in to the platform gateway UI.
2. Navigate to Access Management> (and then)Authentication Methods.
3. Verify that all previously configured authentication providers are present and enabled.
4. Test user login for each configured authentication method.

