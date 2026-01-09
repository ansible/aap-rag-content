# 6. Configuring Ansible Automation Platform
## 6.2. Platform gateway
### 6.2.5. Configuring additional platform options




Configure extra settings in platform gateway, such as the JWT expiration buffer. Adjusting these options helps ensure continuous token validity and smooth communication between platform services.

**Procedure**

1. From the navigation panel, selectSettings→Platform gateway.
1. The **Platform gateway settings** page is displayed.
1. ClickEdit platform gateway settings.
1. You can configure the following **Other settings** :


-  **Jwt expiration buffer in seconds** : The number of seconds before a JWT token’s expiration to revoke from the cache.

When authentication happens a JWT token is created for the user and that token is cached. When subsequent calls happen to services such as automation controller or Event-Driven Ansible, the token is taken from the cache and sent to the service. Both the token and the cache of the token have an expiration time. If the token expires while in the cache the authentication process attempts results in a 401 error (unauthorized). This setting gives Red Hat Ansible Automation Platform a buffer by removing the JWT token from the cache before the token expires. When a token is revoked from cache a new token with a new expiration is generated and cached for the user. As a result, expired tokens from the cache are never used. This setting defaults to 2 seconds. If you have a large latency between platform gateway and your services and observe 401 responses you must increase this setting to lower the number of 401 responses.


-  **Status endpoint backend timeout seconds** : Timeout (in seconds) for the status endpoint to wait when trying to connect to a backend.
-  **Status endpoint backend verify** : Specifies whether SSL/TLS certificates of the services are verified when calling individual nodes for statuses.
-  **Resource client request timeout** : The timeout (in seconds) before the resource client will drop requests after forming connections.
-  **Request timeout** : Specifies, in seconds, the length of time before the proxy will report a timeout and generate a 504.
-  **Manage organization auth** : Controls whether any organization administrator has the privileges to create and manage users and teams. You might want to disable this ability if you are using an LDAP or SAML integration.

Important
The `        MANAGE_ORGANIZATION_AUTH` setting is moved to platform gateway during an upgrade from Ansible Automation Platform 2.4 to 2.6. However, the values are not automatically synchronized between platform gateway and automation controller after the migration. To prevent administrative issues, keep the `        MANAGE_ORGANIZATION_AUTH` value consistent across both environments, especially if automation workflows run directly against automation controller.




-  **Stream idle timeout** : Timeout in seconds for idle streaming connections, for example, for the Red Hat Ansible Lightspeed chatbot. Stream is closed if no data is transmitted within this period.
-  **Max stream duration** : Maximum total duration in seconds for streaming connections, for example, for the Red Hat Ansible Lightspeed chatbot. Stream is closed after this time regardless of activity.
-  **Aap deployment type** : The deployment type for this Ansible Automation Platform instance.

1. ClickSave platform gateway settingsto save the changes or proceed to configure the other platform options available.


