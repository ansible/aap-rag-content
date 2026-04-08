# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.1. Overview
### 7.1.2. Workflow




The standalone Ansible MCP server functions as a secure link between your external AI clients and the Ansible Automation Platform. The AI agent accesses underlying infrastructure only when the Ansible MCP server has appropriate permissions.

The following describes the workflow:

1. AI client (The requester): The user initiates a request through their external AI agent (for example, Cursor or Claude) using natural-language prompts.
1. The AI model (The translator): The AI agent receives the request, interprets the intent, and maps it to the appropriate exposed Ansible toolset. It then sends a structured toolset call with the necessary parameters.
1. Ansible MCP server (The gatekeeper): Upon receiving the call, the Ansible MCP server validates the request. It uses the user’s API token to authenticate with the automation controller.
1. Ansible controller (The executor): The automation controller accepts the validated command from the MCP server and triggers the appropriate automation job.
1. Response loop: The automation result is returned to the Ansible MCP server, standardized into a format the AI agent can process, and displayed to the user via the AI client.


Important
Both the Ansible MCP server and the Ansible Automation Platform UI access the Ansible Automation Platform API. However, because the AI tool processes the API output before displaying it in its chat interface, you might observe different results when comparing the output from the AI tool with the Ansible Automation Platform UI.



