# Deploy the MCP server on Ansible Automation Platform
## Authenticate with the MCP server

To connect an AI agent to the MCP server, you must first authenticate with your Ansible Automation Platform instance.

Ansible Automation Platform supports two authentication methods for the MCP server:

- **Personal access token (PAT):** Create an API token and configure your MCP client with the token value. This method works with all MCP clients.
- **OAuth:** Configure your MCP client to authenticate through an OAuth authorization code flow. In Ansible Automation Platform 2.6, this method requires an MCP client that supports manual OAuth endpoint configuration.

