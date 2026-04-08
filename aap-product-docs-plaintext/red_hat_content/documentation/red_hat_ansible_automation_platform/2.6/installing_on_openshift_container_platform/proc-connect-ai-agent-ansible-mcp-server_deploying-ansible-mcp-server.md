# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.4. Connecting an AI agent to the Ansible MCP server




Use the API token of the Ansible MCP server to connect it with your preferred AI agent, such as Claude, Cursor, or ChatGPT.

**Prerequisites**

- An Ansible MCP server is deployed on your Ansible Automation Platform 2.6 environment.
- An API token is created for your Ansible MCP server.


**Procedure**

1. Go to the AI tool that you want to connect to the Ansible Automation Platform.
1. Follow your AI client’s instructions to configure the MCP server settings.

Typically, you must specify the MCP server configurations in the `    mcp.json` file.


1. When configuring the `    mcp.json` file, add the Ansible MCP server URL in the following format:

`    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;Ansible MCP server URL&gt;</span></em></span>/<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;toolset&gt;</span></em></span>/mcp`

Key:


-  **Ansible MCP server URL** = The URL of the Ansible MCP server. For example, `        https://api.example.com/` .

To obtain the Ansible MCP server URL, contact your organization administrator.


-  **Toolset** = The toolset that you want to connect to. For example, `        job_management` , `        inventory_management` , `        system_monitoring` , `        user_management` , `        security_compliance` , and `        platform_configuration` .
-  **Token** = The API token of the Ansible MCP server.

Use the following format to add details about your Ansible MCP server in the `        mcp.json` file:


```
"mcpServers": {                "aap-mcp-job-management": {                  "type": "http",                  "url": "https://api.example.com/job_management/mcp",                  "headers": {                    "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"                  }                },                "aap-mcp-inventory-management": {                  "type": "http",                  "url": "https://api.example.com/inventory_management/mcp",                  "headers": {                    "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"                  }                },                "aap-mcp-system-monitoring": {                  "type": "http",                  "url": "https://api.example.com/system_monitoring/mcp",                  "headers": {                    "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"                  }                },                "aap-mcp-user-management": {                  "type": "http",                  "url": "https://api.example.com/user_management/mcp",                  "headers": {                    "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"                  }                },                "aap-mcp-security-compliance": {                  "type": "http",                  "url": "https://api.example.com/security_compliance/mcp",                  "headers": {                    "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"                  }                },                "aap-mcp-platform-configuration": {                  "type": "http",                  "url": "https://api.example.com/platform_configuration/mcp",                  "headers": {                    "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"                  }                }              },
```

Important
Use a concise MCP server name, ideally limited to 20 characters. This is because AI agents combine the MCP server name with the tool name to create a unique identifier, and most AI agents enforce a 64-character limit on this combined identifier.







**Verification**

- Verify that the AI tool successfully connects to the Ansible Automation Platform MCP server using the API token.

In your AI agent’s chat window, enter a prompt like `    What MCP tools are available for my Ansible Automation Platform?` . The AI agent should return a response with a list of tools that are enabled for the Ansible Automation Platform MCP server.




**Next step**

- Open a new chat in your AI agent, and enter your prompt.

For example: `    Give me a list of my Ansible Automation Platform jobs.` A list of all your Ansible Automation Platform jobs is displayed in the AI agent’s chat window.




**Additional resources**

-  [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)
-  [Configure Model Context Protocol (MCP) in Cursor](https://cursor.com/docs/context/mcp)
-  [Use MCP servers in VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
-  [Configuring MCP Servers - Cline](https://docs.cline.bot/mcp/configuring-mcp-servers)


