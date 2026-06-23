# Deploy the MCP server on Ansible Automation Platform
## Overview
### Workflow

The standalone MCP server functions as a secure link between your external AI clients and the Ansible Automation Platform. The AI agent accesses underlying infrastructure only when the MCP server has appropriate permissions.

The following describes the workflow:

1. AI client (The requester): The user initiates a request through their external AI agent (for example, Cursor or Claude) using natural-language prompts.
2. The AI model (The translator): The AI agent receives the request, interprets the intent, and maps it to the appropriate exposed Ansible toolset. It then sends a structured toolset call with the necessary parameters.
3. MCP server (The gatekeeper): Upon receiving the call, the MCP server validates the request. It uses the user’s API token to authenticate with the automation controller.
4. Ansible controller (The executor): The automation controller accepts the validated command from the MCP server and triggers the appropriate automation job.
5. Response loop: The automation result is returned to the MCP server, standardized into a format the AI agent can process, and displayed to the user via the AI client.


Important:

Both the MCP server and the Ansible Automation Platform UI access the Ansible Automation Platform API. However, because the AI tool processes the API output before displaying it in its chat interface, you might observe different results when comparing the output from the AI tool with the Ansible Automation Platform UI.

