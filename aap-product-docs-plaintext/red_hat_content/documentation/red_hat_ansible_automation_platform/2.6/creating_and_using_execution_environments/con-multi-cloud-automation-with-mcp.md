# 6. Using automation execution environments with Red Hat Model Context Protocol (MCP) servers
## 6.3. Building an execution environment with MCP servers
### 6.3.2. Multi-cloud automation with MCP servers




Combine multiple MCP servers for comprehensive cloud and version control automation. For example, deploy an execution environment with GitHub MCP (Go binary or remotely hosted), Azure MCP (npm package), and AWS Core MCP (PyPI package) to manage resources across different platforms from a single Ansible workflow.

**Example prompts**

Create a deployment pipeline that:

- Performs operations using the AWS Core MCP server’s available proxy servers.
- Configures Azure resources using the Azure MCP server.
- Updates GitHub repository settings and creates deployment issues using the GitHub MCP server.

All of these operations can be orchestrated from a single Ansible playbook running in your custom execution environment.




