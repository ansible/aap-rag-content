# Deploy the MCP server on Ansible Automation Platform
## Overview

Model Context Protocol (MCP) is an open standard enabling AI models to use external AI tools and services through a unified interface. Using the MCP server for Red Hat Ansible Automation Platform, you can connect your Ansible instance to an external AI tool such as Claude, Cursor, or ChatGPT.

The AI tools can access key information about your Ansible Automation Platform environment and perform tasks. Ansible users can query information, execute workflows, and perform automation tasks using natural language prompts directly within their preferred AI tool.

Note:

As of the June 3, 2026 release, the MCP server for Red Hat Ansible Automation Platform is generally available and fully supported in Ansible Automation Platform 2.6 and later versions. You can deploy the MCP server in production environments with full Red Hat support coverage.

**Benefits**

The following are the benefits of the MCP server:

**For external AI tools**:

- Provides a standardized interface for securely querying infrastructure data and executing automation workflows within the Ansible Automation Platform.
- Enables agentic workflows to interact with the Ansible Automation Platform.

**For Ansible users**:

- Provides the ability to use the chatbot interface of their preferred external AI tool to get information about their Ansible Automation Platform environment, and run automation jobs directly through that tool.

**For developers**:

- Reduces the time and complexity of developing or integrating the Ansible Automation Platform with AI applications or agents.
- Simplifies AI integration, enabling existing automation through Ansible Automation Platform to be exposed to AI tools without writing custom API code or middleware.

**Workflow**

The standalone MCP server functions as a secure link between your external AI clients and the Ansible Automation Platform. The AI agent accesses underlying infrastructure only when the MCP server has appropriate permissions.

The following describes the workflow:

1. AI client (The requester): The user initiates a request through their external AI agent (for example, Cursor or Claude) using natural-language prompts.
2. The AI model (The translator): The AI agent receives the request, interprets the intent, and maps it to the appropriate exposed Ansible toolset. It then sends a structured toolset call with the necessary parameters.
3. MCP server (The gatekeeper): Upon receiving the call, the MCP server validates the request. It uses the user’s API token to authenticate with the automation controller.
4. Ansible controller (The executor): The automation controller accepts the validated command from the MCP server and triggers the appropriate automation job.
5. Response loop: The automation result is returned to the MCP server, standardized into a format the AI agent can process, and displayed to the user via the AI client.

Important:

Both the MCP server and the Ansible Automation Platform UI access the Ansible Automation Platform API. However, because the AI tool processes the API output before displaying it in its chat interface, you might observe different results when comparing the output from the AI tool with the Ansible Automation Platform UI.

**MCP server toolsets**

The MCP server provides a pre-configured suite of toolsets that effectively act as a bridge between your preferred AI agent and the Ansible Automation Platform. Once configured, these toolsets enable your AI agent to perform specific, authorized actions without requiring you to leave the chat interface.

The MCP server turns your AI agent from a passive assistant into an active operator that can interact with your Ansible Automation Platform infrastructure and execute workflows or automate tasks based on the permissions you define.

| Toolset                | Description                                                                                                                                                                                          | Usage examples                                                                                                                                                                                           |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Job management         | Tools to create and manage job templates, projects, and schedules; launch automation jobs and ad hoc commands, and monitor their real-time status.                                                   | Operators can:  Create job templates and projects to define reusable automation tasks.Launch job templates, workflows, and ad hoc commands to execute automation.Configure schedules to run automation at specified times.View job output and logs to troubleshoot failed automation tasks.Relaunch failed jobs to recover from temporary failures. |
| Inventory management   | Tools to create and manage inventories, hosts, and inventory sources, query host details, check group membership, and verify system facts.                                                           | Operators can:  Create inventories, hosts, and inventory sources to define the systems managed by automation.View and browse inventories across environments to understand which systems they are managing.Manage group assignments to target automation to specific sets of systems.View host details and system facts for hosts configured for automation. |
| System monitoring      | Tools to retrieve job logs, troubleshoot failed tasks, and check the health of your automation environment.                                                                                          | Administrators can:  Perform platform status and health checks across all services to identify issues and ensure the automation platform is running correctly.Monitor service health through the platform gateway to ensure all platform components are functioning correctly.Audit user activity and generate reports to ensure compliance and identify potential security issues. |
| User management        | Tools to allow the AI agent to administer access and organizational structure within the Ansible Automation Platform.                                                                                | Administrators can:  Use natural-language prompts to provision users and enforce hierarchy, rather than manually navigating the UI.Create, modify, and delete users and teams to manage access to the Ansible Automation Platform and support organizational changes.Configure role-based access control to ensure users have the appropriate permissions for their responsibilities while maintaining security.View team memberships and structure to see who else in their organization is working on automation. |
| Security/compliance    | Tools that enable the AI agent to act as a security operator, managing sensitive credentials and verifying platform integrity without exposing raw secrets.                                          | Operators can:  View available credentials to understand what authentication options are available for their automation jobs.  Administrators can:  Manage credentials and security policies to ensure secure access to external systems while maintaining proper governance.Manage custom credential types for seamless integration with third-party applications. |
| Platform configuration | Tools that enable organization administrators and developers to inspect and tune the Ansible Automation Platform infrastructure itself.                                                              | Administrators can:  Manage system settings across all components to configure the platform in line with the organizational requirements and policies.Manage and track licenses to ensure compliance with licensing terms and optimize license utilization.  Developers can:  Tune execution environments to optimize the runtime performance of their automation content. |
| Content discovery      | Tools to find Ansible content collections, explore execution environment repositories, and ask questions about your organization's Ansible environment through the automation intelligent assistant. | Developers can:  Search available Ansible content collections in automation hub to find roles, modules, and plugins for automation projects.Check version metadata for content collections to verify compatibility with their environment.List execution environment repositories to find available runtime images.  Any user with Bring your own knowledge enabled on their intelligent assistant deployment can:  Use the intelligent assistant to search your organization's Ansible knowledge base to find answers about policies, procedures, and platform configuration. |

**Reduce token consumption with the discover endpoint**

Use the discover endpoint to minimize token usage and simplify your configuration. Instead of loading the full tool catalog on every query, the discover endpoint sends a lightweight summary of available toolsets. When the AI model receives a query, it identifies the relevant toolset and loads only those tools.

Use the discover endpoint when you want access to all toolsets through a single configuration entry, without the overhead of loading every tool on every interaction.

```
<MCP server URL>/mcp/discover
```

Once the AI agent loads a toolset, those tools remain available for the rest of the session. Queries that require additional toolsets load them alongside the ones already in context.

**Access all tools at once**

If you want every tool available on every query and token consumption is not a concern, connect to the all-tools endpoint. This loads the complete tool catalog on every connection.

```
<MCP server URL>/mcp
```

**Control which tools are available**

If you need to restrict your AI agent to specific toolsets, configure separate connections for each toolset. This gives you fine-grained control over which tools the AI agent can access, but requires a separate MCP server entry for each toolset.

```
<MCP server URL>/mcp/<toolset>
```

Available toolsets: `job_management`, `inventory_management`, `system_monitoring`, `user_management`, `security_compliance`, `platform_configuration`, `content_discovery`.

**Server-level and user-level permissions**

The MCP server employs a dual-layer security model to ensure safe integration between AI tools and your Ansible Automation Platform infrastructure. This approach combines a global administrative safeguard with the granular Role-Based Access Control (RBAC) of the Ansible Automation Platform.

You can grant the following access types to the MCP server:

- **Server-level permissions**: Organization administrators assign a global-level permission while deploying the MCP server. Administrators can choose one of the following access levels:
* Read-only access: The default setting that enforces a strict "look but do not touch" policy. The AI agent can retrieve system data, such as logs and inventory, but the agent cannot launch jobs or modify configurations. This global safeguard overrides all individual user permissions to prevent unintended automation.
* Read-write access: This setting authorizes the AI agent to make changes in your Ansible Automation Platform, such as executing job templates, managing resources, and applying infrastructure changes. However, these actions are subject to the specific RBAC permissions of the user-provided API token.
- **User-level permissions**: The AI agent’s specific capabilities are inherited from the user account that generated the authentication API token.   * Inherited permissions: The AI tool inherits the user’s permissions and performs only the actions the user is authorized to perform. For example, if the user’s token only has permissions to view the "network" inventory, the AI tool cannot access or modify the "database" inventory even if the user requests it.
* Rejection of unauthorized actions: If the AI tool attempts an action (like launching a job) that the user’s token is not authorized to perform, the Ansible Automation Platform API rejects the request.

Warning:

Enabling read-write access for the MCP server grants the AI agent autonomy to directly make changes in your Ansible Automation Platform environment, for example, executing automation jobs. The AI agent can directly make changes in your Ansible Automation Platform environment only if the user has write permissions. Large Language Models (LLMs) can occasionally misinterpret prompts or hallucinate commands. Therefore, enabling read-write access may introduce a risk of unintended changes to your environment.

**Data visibility and sensitive data handling**

When you connect an MCP client to the MCP server for Red Hat Ansible Automation Platform and use it with an external LLM provider (such as Claude, ChatGPT, or others), **all tool call results are sent to that LLM provider** and included in the AI model's conversation context. This includes operational data such as job details, inventory contents, host variables, IP addresses, DNS names, and configuration settings.

The MCP server does not add its own data filtering — it returns the same Ansible Automation Platform API responses the authenticated user could retrieve directly, subject to that user's RBAC permissions and the Ansible API's existing sensitive-data handling.

Before enabling this integration, evaluate:

- What data exists in your AAP environment
- Which MCP tools you will enable
- Whether your MCP client sends context to an external LLM provider

**Types of data and protection levels**

The MCP server's data handling falls into two categories: always protected and context-dependent.

**Always protected: secrets and credentials**

Passwords, secret keys, API tokens, and other secret credential input fields are **always** masked by the Ansible API before the MCP server receives them. These values never appear in plaintext in tool responses.

What is protected:

- Credential passwords
- Secret keys
- Vault credentials
- SSH private keys
- API tokens stored in the credential system

What is NOT protected:

- Credential names
- Credential types
- Usernames
Non-secret credential metadata (credential names, types, usernames) is still returned by the Ansible API and will be visible to the LLM provider.

**Context-dependent: Operational infrastructure data**

IP addresses, DNS names, hostnames, and network configuration are **not filtered** by default. This is expected behavior for infrastructure management tools like Ansible Automation Platform.

What may be exposed:

- IP addresses
- DNS names
- Hostnames
- Network configuration details
- Job execution details
- Inventory structure and variables
- Project and template configurations

If your organization's security policies restrict sharing infrastructure details with external services, you should evaluate the available MCP toolsets and tools, the RBAC permissions of the tokens used to connect, and the potential data returned by the AAP APIs before enabling integration with an external LLM provider.

**How sensitive data is filtered**

The MCP server relies on the data filtering that the Ansible Automation Platform API already provides. The MCP server is a pass-through layer: it does not apply additional redaction, truncation, or access controls beyond what the AAP API enforces.

**Credential secrets:** Passwords, secret keys, and other secret credential input fields are masked by the AAP API before the MCP server receives them. These values are not returned in plaintext in credential tool responses.

**Role-based access control (RBAC):** RBAC restricts which resources a user can access through the MCP server. The MCP server inherits the permissions of the authenticated user's API token, so the AI tool can only retrieve data that the user is authorized to view. If a user lacks permission for a resource, the AAP API rejects the request and the MCP server passes that rejection back to the client.

**API parity:** Data returned through MCP tool calls is the same data the authenticated user can access through the AAP API directly. The MCP server does not expose additional data beyond what RBAC allows, and does not apply redaction beyond what the AAP API already provides.

**Secrets outside of the credential system**

The AAP API's credential masking **only applies to the AAP credential system**. If your organization stores secrets in other AAP-managed fields, those values are **not automatically protected** and can reach the MCP client and, depending on your client configuration, the configured LLM provider.

Fields that are NOT automatically protected:

- Inventory variables (host vars, group vars)
- Job template extra variables
- Job output and logs
- Workflow variable prompts
- Survey answers
- Custom inventory scripts

**Recommendation:** Use the AAP credential system for all secrets. Avoid storing passwords, tokens, API keys, or other sensitive values in inventory variables, extra vars, or job outputs. If you must store sensitive data outside the credential system, ensure your RBAC policies restrict access appropriately and understand that this data may be visible to LLM providers when using the MCP server.

Organizations should understand that when using the MCP server with an external LLM provider, this operational infrastructure data becomes part of the AI model's context and is processed by the LLM provider's systems.

**Telemetry data collection for the MCP server**

Red Hat collects anonymized telemetry data from the MCP server. The telemetry data includes metrics related to MCP server performance, adoption trends, and usage patterns.

Telemetry data will be automatically collected for MCP server deployments using Ansible Automation Platform patch release on 21 January 2026 and later versions. Red Hat will use this data to monitor the operational health of your MCP servers and to ensure the long-term scalability of the MCP ecosystem.

Important:

Telemetry data collection cannot be disabled, but strict user privacy is maintained. Red Hat does not collect users' personal information, such as usernames or passwords. If any personal information is inadvertently received, the data is deleted. For more information, see the Red Hat Privacy Statement under Related Links below.

**Requirements to deploy the MCP server**

- Platform version: An instance of Ansible Automation Platform 2.6 or later.
- Deployment environment:
* OpenShift: Access to an OpenShift cluster with permissions to install operators.
* Containerized: A supported container runtime.
- Access credentials: A valid user or service account within Ansible Automation Platform with permissions to execute the desired automation jobs. You will need to generate an API token for this account.

**Overview of deploying the MCP server**

Perform the following tasks to deploy and configure an MCP server and integrate it with your preferred AI tool:

| Step number | Task                                                               | Description                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1           | Deploy and configure an MCP server on container-based installation | An organization administrator deploys and configures the MCP server on a container-based installation of Ansible Automation Platform 2.6 or later.                                                       |
| 2           | Create an API token for the MCP server                             | An Ansible user creates an API token for their Ansible Automation Platform instance and uses it to connect to their preferred AI tool. The AI tools will inherit the user’s permissions for authentication using the API token. |
| 3           | Connect an external AI agent to the MCP server                     | The Ansible user then configures an external AI tool with the MCP server’s API token, enabling the AI tool to connect to the MCP server and execute workflows and automate tasks.                        |

