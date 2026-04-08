# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.1. Overview
### 7.1.7. Process




Perform the following tasks to deploy and configure an Ansible MCP server and integrate it with your preferred AI tool:

| Step number | Task | Description |
| --- | --- | --- |
| 1 |  [Deploy and configure an Ansible MCP server on container-based installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#proc-configure-mcp-server-containerized-install_deploying-ansible-mcp-server) . | An organization administrator deploys and configures the Ansible MCP server on a container-based installation of Ansible Automation Platform 2.6. |
| 2 |  [Create an API token for the Ansible MCP server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#proc-create-api-token-ansible-mcp-server_deploying-ansible-mcp-server) . | An Ansible user creates an API token for their Ansible Automation Platform instance and uses it to connect to their preferred AI tool. The AI tools will inherit the user’s permissions for authentication using the API token. |
| 3 |  [Connect an external AI agent to the Ansible MCP server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#proc-connect-ai-agent-ansible-mcp-server_deploying-ansible-mcp-server) | The Ansible user then configures an external AI tool with the Ansible MCP server’s API token, enabling the AI tool to connect to the Ansible MCP server and execute workflows and automate tasks. |


