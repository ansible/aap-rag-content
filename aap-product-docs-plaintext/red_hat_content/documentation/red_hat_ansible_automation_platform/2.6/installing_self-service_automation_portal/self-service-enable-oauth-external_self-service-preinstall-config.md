# 3. Pre-installation configuration
## 3.3. Enabling Oauth token creation for external users




Self-service automation portal uses Ansible Automation Platform or authentication and as an OAuth provider.

You must enable OAuth token creation in Ansible Automation Platform so that users can authenticate with the platform from self-service automation portal.

Note: Users who do not have permission to log in to Ansible Automation Platform cannot log in to Self-service portal, because Ansible Automation Platform provides the OAuth tokens. Therefore, a user who is removed from an external IdP (for example LDAP, SAML, Azure) can no longer log into Ansible Automation Platform or self-service automation portal. This prevents potential external token issues. For more information, refer to the [Manage OAuth2 token creation for external users](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication#gw-manage-oauth2-external-users) section of [Access management and authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication) .

**Procedure**

1. In a browser, log in to your Ansible Automation Platform instance as a user with admin privileges.
1. In the navigation pane, selectSettings→Platform gateway.
1. Locate the **Allow external users to create OAuth2 tokens** setting.
1. Enable **Allow external users to create OAuth2 tokens** if it is not already enabled:


1. ClickEdit platform gateway settings.
1. Set **Allow external users to create OAuth2 tokens** to **Enabled** .

![Allow external users to create OAuth2 tokens setting](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/359b09c0978651f1b89675b955228d2d/self-service-enable-external-oauth.png)



1. ClickSave platform gateway settingsto save your updates and return to the **Platform gateway settings** page.

1. In the **Platform gateway settings** page, verify that the **Allow external users to create OAuth2 tokens** setting is enabled.


