# 6. Configuring Ansible Automation Platform
## 6.2. Platform gateway
### 6.2.6. Overlapping administrative settings




Platform gateway acts as the centralized point for configuration management in Ansible Automation Platform. However, specific operational and administrative settings can exist on both platform gateway and component services, such as automation controller. To prevent issues, especially when workflows or scripts interact directly with the component API, you must manually keep these duplicate settings consistent between the component service and platform gateway.

**Effective settings table**

The following table clarifies the authoritative source for administrative settings that you can configure in both automation controller and platform gateway.

|  **Setting name (UI text)** |  **API variable name** |  **Platform gateway configuration location** |  **Automation controller configuration location** |  **Synchronization requirement and notes** |
| --- | --- | --- | --- | --- |
|  **Organization Admins Can Manage Users and Teams** |  `MANAGE_ORGANIZATION_AUTH` |  **Settings** > **Platform gateway** |  **Settings** > **Automation Execution** > **System** | Keep a consistent value across both systems. The automation controller setting might be used by direct API workflows. |
|  **All Users Visible to Organization Admins** |  `ORG_ADMINS_CAN_SEE_ALL_USERS` |  **Settings** > **Platform gateway** |  **Settings** > **Automation Execution** > **System** | Keep a consistent value across both systems. Automation controller does not follow gateway settings for this variable; direct API workflows use the controller’s local value. |
|  **Allow External Users to Create OAuth2 Tokens** |  `ALLOW_OAUTH2_FOR_EXTERNAL_USERS` |  **Settings** > **Platform gateway** | N/A | Platform gateway is authoritative. Configure this setting in the unified UI or through the gateway API. |


