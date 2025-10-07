# 3. Configuring access to external applications with token-based authentication
## 3.3. Manage OAuth2 token creation for external users
### 3.3.1. Enabling OAuth2 token creation for external users




To enable external users to create OAuth2 tokens, change the appropriate setting in your Ansible Automation Platform environment. Ensure the implementation of compensating security controls after enabling this setting.

**Procedure**

1. From the navigation panel, go toSettings→Platform gateway.
1. ClickEdit platform gatewaysettings.
1. Change the **Allow external users to create OAuth2 tokens** setting to **Enabled** .
1. ClickSave platform gateway settings.


**Next steps**

Implement the recommended security controls as described in _Implementing security controls for external user OAuth2 tokens_ .


