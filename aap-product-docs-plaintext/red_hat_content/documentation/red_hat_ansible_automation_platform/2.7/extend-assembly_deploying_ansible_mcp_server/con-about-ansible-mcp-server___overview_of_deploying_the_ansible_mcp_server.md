# Deploy the MCP server on Ansible Automation Platform
## Overview
### Overview of deploying the MCP server

Perform the following tasks to deploy and configure an MCP server and integrate it with your preferred AI tool:

| Step number | Task                                                                   | Description                                                                                                                                                                                                                         |
| ----------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>1       | <br>Deploy and configure an MCP server on container-based installation | <br>An organization administrator deploys and configures the MCP server on a container-based installation of Ansible Automation Platform 2.6 or later.                                                                              |
| <br>2       | <br>Create an API token for the MCP server                             | <br>An Ansible user creates an API token for their Ansible Automation Platform instance and uses it to connect to their preferred AI tool. The AI tools will inherit the user’s permissions for authentication using the API token. |
| <br>3       | <br>Connect an external AI agent to the MCP server                     | <br>The Ansible user then configures an external AI tool with the MCP server’s API token, enabling the AI tool to connect to the MCP server and execute workflows and automate tasks.                                               |

