# Deploy the MCP server on Ansible Automation Platform
## Authenticate with the MCP server
### Connect an AI agent to the MCP server

Use the API token of the MCP server to connect it with your preferred AI agent, such as Claude, Cursor, or ChatGPT.

#### Before you begin

- The MCP server for Red Hat Ansible Automation Platform is deployed on your Ansible Automation Platform environment.
- An API token is created for your MCP server.

#### Procedure

1. Go to the AI tool that you want to connect to the Ansible Automation Platform.
2. Follow your AI client's instructions to configure the MCP server settings. Typically, you must specify the MCP server configurations in the mcp.json file.
3. When configuring the mcp.json file, add the MCP server details using one of the following options.
**Option 1: Discover endpoint (recommended)**

To access all toolsets through a single connection with optimized token consumption, configure the discover endpoint:

```
{
"mcpServers": {
"aap-mcp": {
"type": "http",
"url": "https://aap.example.com:8448/mcp/discover",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
}
}
}
```

The discover endpoint dynamically identifies the appropriate toolset for each query, so you do not need to configure individual toolset connections.

**Option 2: Individual toolset endpoints**

To control exactly which tools your AI agent can access, configure a separate entry for each toolset:

```
{
"mcpServers": {
"aap-mcp-job-mgmt": {
"type": "http",
"url": "https://aap.example.com:8448/mcp/job_management",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-inventory-mgmt": {
"type": "http",
"url": "https://aap.example.com:8448/mcp/inventory_management",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-system-monitor": {
"type": "http",
"url": "https://aap.example.com:8448/mcp/system_monitoring",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-user-mgmt": {
"type": "http",
"url": "https://aap.example.com:8448/mcp/user_management",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-security": {
"type": "http",
"url": "https://aap.example.com:8448/mcp/security_compliance",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-platform-config": {
"type": "http",
"url": "https://aap.example.com:8448/mcp/platform_configuration",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-content": {
"type": "http",
"url": "https://aap.example.com:8448/mcp/content_discovery",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
}
}
}
```

Important:
Use a concise MCP server name, ideally limited to 20 characters. This is because AI agents combine the MCP server name with the tool name to create a unique identifier, and most AI agents enforce a 64-character limit on this combined identifier.

#### Results

Verify that the AI tool successfully connects to the Ansible Automation Platform MCP server using the API token.

In your AI agent's chat window, enter a prompt like `What MCP tools are available for my Ansible Automation Platform?` The AI agent should return a response with a list of tools that are enabled for the Ansible Automation Platform MCP server.

