# 6. Configuring Ansible Automation Platform
## 6.2. Platform gateway
### 6.2.7. Enabling OAuth2 token creation for external users

To enable external users to create OAuth2 tokens, change the appropriate setting in your Ansible Automation Platform environment. Ensure the implementation of compensating security controls after enabling this setting.

**Procedure**

1. From the navigation panel, go to Settings → Platform gateway.
2. Click Edit platform gateway settings.
3. Change the **Allow external users to create OAuth2 tokens** setting to **Enabled**.
4. Click Save platform gateway settings.

**Next steps**

Implement the recommended security controls as described in [Implementing security controls for external user OAuth2 tokens](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-token-based-authentication#gw-oauth2-security-controls).

