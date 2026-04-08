# 6. Using automation execution environments with Red Hat Model Context Protocol (MCP) servers
## 6.3. Building an execution environment with MCP servers
### 6.3.3. Securely connecting to remote services




The MCP architecture supports both local process execution and remote connections.

-  **Remote HTTP Connections** : To connect to a remote, hosted MCP server through HTTP, use the `    {role_name}_mode` variable and set it to remote. To change the accessed URL, provide it using the `    {role_name}_registry.path` variable.

Currently, only the `    github_mcp_server` role supports this.


-  **Authentication Tokens** : When running a server that requires authentication (such as the GitHub MCP server), pass credentials as environment variables in your automation job configuration.


