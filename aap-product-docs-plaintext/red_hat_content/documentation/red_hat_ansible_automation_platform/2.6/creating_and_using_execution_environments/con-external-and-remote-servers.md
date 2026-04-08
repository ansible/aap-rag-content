# 6. Using automation execution environments with Red Hat Model Context Protocol (MCP) servers
## 6.3. Building an execution environment with MCP servers
### 6.3.5. External and remote MCP server connection




When building an execution environment with MCP servers, you can choose to include external or remote servers instead of embedding them directly into the environment.

The MCP architecture supports connecting to a remote, hosted MCP server through HTTP. To configure a remote connection, you must set the role-specific variable `&lt;role_name&gt;_mode` to remote.

You can change the accessed URL for the remote server by providing it through the `&lt;role_name&gt;_registry.path` variable.

