# Deploy the MCP server on Ansible Automation Platform
## Authenticate with the MCP server
### Connect an MCP client with OAuth 2.1

After an administrator has created an OAuth application and enabled OAuth 2.1 on the MCP server, you can connect your MCP client to authenticate with your Ansible Automation Platform credentials.

#### Before you begin

- An OAuth application is created on the Ansible Automation Platform gateway.
- The `OAUTH2_ENABLED` setting is set to `true` on the MCP server.
- You have the Client ID (and optionally, the Client secret) from your administrator.
- You have the Ansible MCP server URL.

#### About this task

The following example shows how to connect Claude Code to the MCP server with OAuth 2.1.

#### Procedure

1. Configure the OAuth application on the Ansible Automation Platform gateway with the following redirect URIs:


```
http://localhost:6661/callback
http://127.0.0.1:6661/callback
```

2. Add the MCP server to Claude Code from your terminal:


```
$ claude mcp add --transport http --client-id <client-id> --callback-port 6661 aap-mcp-server \
https://<mcp-server-host>/mcp
```

The callback port (6661) must match the port in the redirect URIs configured on the OAuth application.

#### JSON configuration file

Alternatively, configure the MCP server in a JSON configuration file:

```
{
"mcpServers": {
"aap-mcp": {
"type": "http",
"url": "https://<mcp-server-url>/mcp",
"auth": {
"type": "oauth2",
"client_id": "<your-client-id>",
"client_secret": "<your-client-secret>"
}
}
}
}
```

