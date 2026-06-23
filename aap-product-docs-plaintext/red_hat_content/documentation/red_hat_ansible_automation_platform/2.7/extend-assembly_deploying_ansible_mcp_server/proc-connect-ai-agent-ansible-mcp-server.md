# Deploy the MCP server on Ansible Automation Platform
## Create an API token for the MCP server
### Connect an AI agent to the MCP server

Use the API token of the Ansible MCP server to connect it with your preferred AI agent, such as Claude, Cursor, or ChatGPT.

#### Before you begin

- The MCP server for Red Hat Ansible Automation Platform is deployed on your Ansible Automation Platform environment.
- An API token is created for your MCP server.

#### Procedure

1.  Go to the AI tool that you want to connect to the Ansible Automation Platform.
2.  Follow your AI client’s instructions to configure the MCP server settings. Typically, you must specify the MCP server configurations in the `mcp.json` file.

3.  When configuring the `mcp.json` file, add the Ansible MCP server URL in the following format:
`<Ansible MCP server URL>/<toolset>/mcp`

Key:

- **Ansible MCP server URL** = The URL of the Ansible MCP server. For example, `https://api.example.com/`. To obtain the Ansible MCP server URL, contact your organization administrator.

- **Toolset** = The toolset that you want to connect to. For example, `job_management`, `inventory_management`, `system_monitoring`, `user_management`, `security_compliance`, and `platform_configuration`.

- **Token** = The API token of the Ansible MCP server. Use the following format to add details about your Ansible MCP server in the the `mcp.json` file:



```
{
"mcpServers": {
"aap-mcp-job-mgmt": {
"type": "http",
"url": "https://api.example.com/job_management/mcp",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-inventory-mgmt": {
"type": "http",
"url": "https://api.example.com/inventory_management/mcp",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-system-monitor": {
"type": "http",
"url": "https://api.example.com/system_monitoring/mcp",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-user-mgmt": {
"type": "http",
"url": "https://api.example.com/user_management/mcp",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-security": {
"type": "http",
"url": "https://api.example.com/security_compliance/mcp",
"headers": {
"Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
}
},
"aap-mcp-platform-config": {
"type": "http",
"url": "https://api.example.com/platform_configuration/mcp",
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

- Verify that the AI tool successfully connects to the Ansible Automation Platform MCP server using the API token. In your AI agent’s chat window, enter a prompt like `What MCP tools are available for my Ansible Automation Platform?`. The AI agent should return a response with a list of tools that are enabled for the Ansible Automation Platform MCP server.

#### What to do next

- Open a new chat in your AI agent, and enter your prompt. For example: `Give me a list of my Ansible Automation Platform jobs.` A list of all your Ansible Automation Platform jobs is displayed in the AI agent’s chat window.

