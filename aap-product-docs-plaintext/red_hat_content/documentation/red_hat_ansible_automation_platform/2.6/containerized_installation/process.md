# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.1. Overview
### 7.1.7. Process

Perform the following tasks to deploy and configure an Ansible MCP server and integrate it with your preferred AI tool:

| Step number | Task | Description |
| --- | --- | --- |
| <br>  1 | <br> [Deploy and configure an Ansible MCP server on container-based installation](#proc-configure-mcp-server-containerized-install_deploying-ansible-mcp-server "7.2.&nbsp;Deploying an Ansible MCP server on a container-based installation"). | <br>  An organization administrator deploys and configures the Ansible MCP server on a container-based installation of Ansible Automation Platform 2.6. |
| <br>  2 | <br> [Create an API token for the Ansible MCP server](#proc-create-api-token-ansible-mcp-server_deploying-ansible-mcp-server "7.3.&nbsp;Creating an API token for the Ansible MCP server"). | <br>  An Ansible user creates an API token for their Ansible Automation Platform instance and uses it to connect to their preferred AI tool. The AI tools will inherit the user’s permissions for authentication using the API token. |
| <br>  3 | <br> [Connect an external AI agent to the Ansible MCP server](#proc-connect-ai-agent-ansible-mcp-server_deploying-ansible-mcp-server "7.4.&nbsp;Connecting an AI agent to the Ansible MCP server") | <br>  The Ansible user then configures an external AI tool with the Ansible MCP server’s API token, enabling the AI tool to connect to the Ansible MCP server and execute workflows and automate tasks. |

