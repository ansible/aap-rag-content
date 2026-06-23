# Platform gateway
## Overlapping administrative settings

Manually synchronize duplicate operational and administrative settings between platform gateway and component services like automation controller. This helps ensure your workflows and scripts can interact directly with the component API without issues.

**Effective settings table**

The following table clarifies the authoritative source for administrative settings that you can configure in both automation controller and platform gateway.

| **Setting name (UI text)**                              | **API variable name**                  | **Platform gateway configuration location** | **Automation controller configuration location**         | **Synchronization requirement and notes**                                                                                                                                         |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> **Organization Admins Can Manage Users and Teams** | <br> `MANAGE_ORGANIZATION_AUTH`        | <br>**Settings** > **Platform gateway**     | <br>**Settings** > **Automation Execution** > **System** | <br>Keep a consistent value across both systems. The automation controller setting might be used by direct API workflows.                                                         |
| <br> **All Users Visible to Organization Admins**       | <br> `ORG_ADMINS_CAN_SEE_ALL_USERS`    | <br>**Settings** > **Platform gateway**     | <br>**Settings** > **Automation Execution** > **System** | <br>Keep a consistent value across both systems. Automation controller does not follow gateway settings for this variable; direct API workflows use the controller’s local value. |
| <br> **Allow External Users to Create OAuth2 Tokens**   | <br> `ALLOW_OAUTH2_FOR_EXTERNAL_USERS` | <br>**Settings** > **Platform gateway**     | <br>N/A                                                  | <br>Platform gateway is authoritative. Configure this setting in the unified UI or through the gateway API.                                                                       |

