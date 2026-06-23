# Create an OAuth application
## Enable Oauth token creation for external users

Ansible automation portal uses Ansible Automation Platform or authentication and as an OAuth provider.

### About this task

You must enable OAuth token creation in Ansible Automation Platform so that users can authenticate with the platform from Ansible automation portal.

Note:

Users who do not have permission to log in to Ansible Automation Platform cannot log in to Self-service portal, because Ansible Automation Platform provides the OAuth tokens. Therefore, a user who is removed from an external IdP (for example LDAP, SAML, Azure) can no longer log into Ansible Automation Platform or Ansible automation portal. This prevents potential external token issues. For more information, refer to the [Manage OAuth2 token creation for external users](/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-con_gw_manage_oauth2_external_users#gw-manage-oauth2-external-users "Configure your platform settings to enable OAuth2 token creation for external users. Allowing users authenticated via LDAP, SAML, or SSO to generate tokens prevents 403 Forbidden errors and helps ensure they maintain programmatic API access.") section of[Configure central authentication for Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication "Configure authentication methods such as LDAP or SAML to simplify the user login experience. Providing the correct connection details for your chosen identity provider helps ensure seamless and secure access to Ansible Automation Platform.").

### Procedure

1.  In a browser, log in to your Ansible Automation Platform instance as a user with admin privileges.
2.  In the navigation pane, select Settings> (and then)Platform gateway.
3.  Locate the **Allow external users to create OAuth2 tokens** setting.
4.  Enable **Allow external users to create OAuth2 tokens** if it is not already enabled:
1.  Click Edit platform gateway settings.
2.  Set **Allow external users to create OAuth2 tokens** to **Enabled**.
![Allow external users to create OAuth2 tokens setting](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-enable-external-oauth.png)
3.  Click Save platform gateway settings to save your updates and return to the **Platform gateway settings** page.
5.  In the **Platform gateway settings** page, verify that the **Allow external users to create OAuth2 tokens** setting is enabled.

