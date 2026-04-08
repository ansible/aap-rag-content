# 6. Using automation execution environments with Red Hat Model Context Protocol (MCP) servers
## 6.3. Building an execution environment with MCP servers
### 6.3.1. MCP Server Manifest Format




The MCP Server Manifest is a JSON file that describes the MCP servers installed within an Ansible execution environment.

The example generated `/opt/mcp/mcpservers.json` file contains server definitions:

```
{
"azure_mcp_registry": {
"type": "stdio",
"lang": "npm",
"package": "@azure/mcp",
"args":
- "server"
- "start"
- "--namespace"
- "az"
},
"aws-iam-mcp-server": {
"type": "stdio",
"command": "/opt/mcp/bin/awslabs.iam-mcp-server",
"args": [],
"package": "awslabs.iam-mcp-server"
},
"github-mcp-server": {
"type": "stdio",
"command": "/opt/mcp/bin/github-mcp-server",
"args": ["stdio"],
"description": "GitHub MCP Server - Access GitHub repositories, issues, and pull requests"
},
}
```

