# Deploy the MCP server on Ansible Automation Platform
## Authenticate with the MCP server
### OAuth 2.1 settings for the MCP server

Configuration variables and token lifetime settings for OAuth 2.1 authentication on the Ansible MCP server.

#### MCP server variables

Add these variables to `mcp_extra_settings` (containerized installer) or `extra_settings` (operator) in your deployment configuration.

| Variable                   | Description                                                                                                                                                                     | Required              | Default    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------- |
| `OAUTH2_ENABLED`           | Enables OAuth 2.1 authentication on the MCP server.                                                                                                                             | Yes (to enable OAuth) | false      |
| `OAUTH2_DISCOVERY_TIMEOUT` | Timeout in seconds for the OIDC discovery probe at startup. Increase this value if the MCP server logs timeout errors during startup in environments with high network latency. | No                    | 10 seconds |

#### Token lifetime configuration

Access token and refresh token lifetimes are configured on the Ansible Automation Platform gateway, not the MCP server. You must set the access token lifetime to a shorter value than the default to ensure refresh tokens can renew access before requiring re-authentication.

Set the access token lifetime to 28800 seconds (8 hours):

| Setting                                        | Description                             | Default                   |
| ---------------------------------------------- | --------------------------------------- | ------------------------- |
| `OAUTH2_PROVIDER__ACCESS_TOKEN_EXPIRE_SECONDS` | How long an access token remains valid. | 31536000 seconds (1 year) |

For more information, see [Managing OAuth 2.0 for external users](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-con_gw_manage_oauth2_external_users).

