# Deploy the MCP server on Ansible Automation Platform
## Authenticate with the MCP server
### Enable OAuth 2.1 on the MCP server

An administrator must create an OAuth application and enable OAuth 2.1 on the MCP server before users can authenticate with their Ansible Automation Platform credentials.

#### About this task

Note:

OAuth 2.1 authentication supplements the existing personal access token (PAT) method. Users who currently connect to the MCP server with a manually created API token can continue to do so.

For OAuth authentication on Ansible Automation Platform 2.6, which requires manual endpoint configuration, see [Authenticate with OAuth](/documentation/en-us/red_hat_ansible_automation_platform/2.7/oauth-authentication-for-the-mcp-server.html "As an alternative to personal access tokens (PATs), you can configure OAuth authentication for the MCP server. With OAuth, users sign in with their Ansible Automation Platform credentials through an authorization code flow instead of creating and distributing personal access tokens.") in the AAP 2.6 documentation.

#### Procedure

1. Create an OAuth application on the Ansible Automation Platform gateway.
For instructions, see [Creating an OAuth application](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_create_oauth_app).

Configure the following settings:

| Setting                  | Value                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Authorization grant type | Authorization code                                                                                                             |
| Client type              | Confidential orPublic, based on your security requirements.                                                                    |
| Redirect URI             | The callback URL for your MCP client (for example,`http://localhost:6661/callback`). You can configure multiple redirect URIs. |
| PKCE required            | Selected by default for new applications. Do not disable unless you have a specific compatibility requirement.                 |
Existing OAuth applications created before this feature are migrated with PKCE disabled. If you have pre-existing OAuth applications that you want to use with the MCP server, enable PKCE on those applications manually.

2. Save the Client ID and, if you selected a Confidential client type, the Client secret. Users will need these values to connect their MCP clients.
3. Enable OAuth 2.1 on the MCP server through the installer extra settings.
**Containerized installer**

Add the `OAUTH2_ENABLED` variable to the `mcp_extra_settings` section in your inventory file:

```
[ansiblemcp]
<mcp-server-hostname>

[ansiblemcp:vars]
mcp_extra_settings=[{"setting": "OAUTH2_ENABLED", "value": "true"}]
```

Optionally, configure the OIDC discovery timeout:

```
[ansiblemcp:vars]
mcp_extra_settings=[{"setting": "OAUTH2_ENABLED", "value": "true"}, {"setting": "OAUTH2_DISCOVERY_TIMEOUT", "value": "30"}]
```

After updating the inventory file, re-run the installer for the changes to take effect.

**Operator-based deployments**

Add the `OAUTH2_ENABLED` setting to the `extra_settings` section of the `mcp:` configuration in the AnsibleAutomationPlatform custom resource:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: <app-name>
namespace: <namespace>
spec:
mcp:
disabled: false
extra_settings:
- setting: OAUTH2_ENABLED
value: true
```

Note:
The MCP server URL is automatically set in both operator and containerized installer deployments. You do not need to configure it manually.

#### What to do next

Provide the Client ID (and Client secret, if applicable) to users who need to connect their MCP clients with OAuth 2.1.

