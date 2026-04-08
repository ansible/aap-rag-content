# 6. Using automation execution environments with Red Hat Model Context Protocol (MCP) servers
## 6.3. Building an execution environment with MCP servers
### 6.3.4. Authentication for embedded MCP servers




When embedding MCP servers within an Ansible execution environment, it is crucial to ensure secure authentication mechanisms are in place to protect sensitive data and maintain the integrity of interactions between the MCP server and external systems.

Authentication is handled by passing required credentials (such as a GitHub token) as an environment variable or a parameter when invoking the MCP server.

