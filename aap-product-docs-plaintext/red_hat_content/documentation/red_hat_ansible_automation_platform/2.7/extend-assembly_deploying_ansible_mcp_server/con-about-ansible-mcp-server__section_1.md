# Deploy the MCP server on Ansible Automation Platform
## Overview
### Data visibility and sensitive data handling

When you connect an MCP client to the MCP server for Red Hat Ansible Automation Platform and use it with an external LLM provider (such as Claude, ChatGPT, or others), **all tool call results are sent to that LLM provider** and included in the AI model's conversation context. This includes operational data such as job details, inventory contents, host variables, IP addresses, DNS names, and configuration settings.

The MCP server does not add its own data filtering — it returns the same Ansible Automation Platform API responses the authenticated user could retrieve directly, subject to that user's RBAC permissions and the Ansible API's existing sensitive-data handling.

Before enabling this integration, evaluate:

- What data exists in your AAP environment
- Which MCP tools you will enable
- Whether your MCP client sends context to an external LLM provider

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

The MCP server relies on the data filtering that the Ansible Automation Platform API already provides. The MCP server is a pass-through layer: it does not apply additional redaction, truncation, or access controls beyond what the AAP API enforces.

**Credential secrets:** Passwords, secret keys, and other secret credential input fields are masked by the AAP API before the MCP server receives them. These values are not returned in plaintext in credential tool responses.

**Role-based access control (RBAC):** RBAC restricts which resources a user can access through the MCP server. The MCP server inherits the permissions of the authenticated user's API token, so the AI tool can only retrieve data that the user is authorized to view. If a user lacks permission for a resource, the AAP API rejects the request and the MCP server passes that rejection back to the client.

**API parity:** Data returned through MCP tool calls is the same data the authenticated user can access through the AAP API directly. The MCP server does not expose additional data beyond what RBAC allows, and does not apply redaction beyond what the AAP API already provides.

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

