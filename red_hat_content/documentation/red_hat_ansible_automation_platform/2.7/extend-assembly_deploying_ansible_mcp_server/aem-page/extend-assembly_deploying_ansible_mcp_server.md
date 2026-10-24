+++
template = "docs/aem-title.html"
title = "Deploy the MCP server on Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server/", "Deploy the MCP server on Ansible Automation Platform"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server/aem-page/extend-assembly_deploying_ansible_mcp_server.html"
last_crumb = "Deploy the MCP server on Ansible Automation Platform"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Deploy the MCP server on Ansible Automation Platform"
oversized = "false"
page_slug = "extend-assembly_deploying_ansible_mcp_server"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server/toc/toc.json"
type = "aem-page"
+++

# Deploy the MCP server on Ansible Automation Platform

As an organization administrator, you can deploy the Model Context Protocol (MCP) server for Red Hat Ansible Automation Platform on an operator-based installation or container-based installation of Ansible Automation Platform.

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

## Deploy the MCP server for Red Hat Ansible Automation Platform on a container-based installation

As an organization administrator, you can deploy and configure the MCP server on a container-based installation of Ansible Automation Platform. Use the following procedure to deploy and configure the MCP server.

### Before you begin

- You have a valid subscription for Ansible Automation Platform 2.6 or later.

### Procedure

Configure MCP server variables in the inventory file:

1. Create an `[ansiblemcp]` group and add a host for the MCP server.
2. Add the following installation variables to your inventory file under the `[all:vars]` group:

  - `mcp_allow_write_operations`: Use to grant read-only or read-write permissions to the external AI tool.
  - `mcp_ignore_certificate_errors`: Use to bypass SSL/TLS certificate validation.

3. To make your system trust a self-signed custom certificate, add the following required variables to your inventory file:

  - `mcp_tls_cert`: Path to TLS certificate

  - `mcp_tls_key`: Path to TLS key         For information about using your own TLS certificates and keys, see [Configuring custom TLS certificates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_advanced_configuration_containerized "Configure external databases, custom TLS certificates, execution nodes, HAProxy load balancers, and hub storage for complex containerized Ansible Automation Platform deployments."). For information about required and optional variables, see [MCP server variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_inventory_file_vars#GUID-4eedb0f5-69e7-4e4e-baec-a59dee75d41d "Inventory file variables for the MCP server for Red Hat Ansible Automation Platform.").

```
# This is the list of inventory file variables required to deploy an Ansible MCP server on a container-based installation.

        # This section is for the MCP server host
# -------------------------------------------------
[ansiblemcp]
aap.example.com

        # This section is for Ansible MCP server permissions
# --------------------------------------------------
[all:vars]
mcp_allow_write_operations=false <To enable read-write access, set the "mcp_allow_write_operations" variable to "true">
mcp_ignore_certificate_errors=false
mcp_tls_cert= <path to tls certificate>
mcp_tls_key= <path to tls key>

        # Additional MCP server settings
mcp_extra_settings='[{"setting": "DEFAULT_PAGE_SIZE", "value": "25"}]' <Overrides the default page size for list-type API responses>
```

4. Optional: add additional MCP server settings such as `DEFAULT_PAGE_SIZE` as in the example above.

### Results

Check the pods after installation is complete. You should see an `ansiblemcp` pod running with the following command:

```none
$ podman ps
```

### What to do next

1. Obtain the location of the MCP server:
  - The service is exposed on port 8448 of the host, and HTTPS is enabled.
  - The example above deploys the MCP server on `aap.example.com`, so the service base URL will be `https://aap.example.com:8448`.
2. [Create an API token for the MCP server](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#proc-create-api-token-ansible-mcp-server "Create an API token for your Ansible Automation Platform instance to authenticate your MCP client with a personal access token.").

## Deploy the MCP server for Red Hat Ansible Automation Platform on an operator-based installation

As an organization administrator, you can deploy and configure the MCP server on an operator-based installation of Ansible Automation Platform. Use the following procedure to deploy and configure the MCP server.

### Before you begin

- You have a valid Ansible Automation Platform subscription.

### Procedure

1. Log in to Red Hat OpenShift Container Platform as an administrator.
2. Navigate to the namespace where you want to install the MCP server.
3. Select Operators> (and then)Installed Operators.
4. From the list of installed operators, select **Ansible Automation Platform**.
5. In the Ansible Automation Platform tile, click **Create instance**.
6. From the **Configure via** field, select the **Form** view, then provide the instance name. For example, `aap-mcp`.
7. Select the **YAML** view, and under the `spec:` section, add the `mcp` component:
  

```
spec:
  mcp:
    disabled: false
    allow_write_operations: false
```

8. Use the `allow_write_operations` variable to configure the operational access level of the MCP server:
9. Click **Create**. the MCP server is created.
10. Optional: If you changed the permissions of the MCP server after it was created and deployed, you must delete the **AnsibleMCPServer** custom resource and recreate it. Perform the following steps:

  1. Go to the Ansible Automation Platform portal.
  2. Under **Resources**, search for the **AnsibleMCPServer** custom resource.
  3. Select the active **AnsibleMCPServer** instance. An active AnsibleMCPServer instance is identified by the `-mcp` suffix appended to the Ansible Automation Platform custom resource name.
  4. Select the **Settings menu** on the right side of the instance, and then click **Delete AnsibleMCPServer**.
  5. After the reconciliation process completes, the existing MCP server instance is deleted, and a new MCP server instance is created.

### Results

1. Navigate to Workloads> (and then)Deployments.
2. Check that the deployment you created is listed there. For example: `aap-mcp`.
3. Check one of the pod’s logs and verify there are no errors.

### What to do next

1. Obtain the following information:
  - **Ansible Automation Platform login screen URL**:
    1. Navigate to Networking> (and then)Routes.
    2. For the Ansible Automation Platform deployment, click the **Copy icon** in the **Location** field. This is the URL of the Ansible Automation Platform login screen.
  - **Ansible Automation Platform administrator password**:
    1. Navigate to Workloads> (and then)Secrets and click `aap-admin-password`.
    2. Click **Reveal values** and then use the **Copy** icon to save the Ansible Automation Platform administrator password for future use.
  - **MCP server URL**:
    1. Navigate to Networking> (and then)Routes.
    2. For the deployment you recently created (`aap-mcp`), click the **Copy** icon from the **Location** field. This is the URL required to configure your AI agent to connect to the MCP server.
2. [Create an API token for the MCP server](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#proc-create-api-token-ansible-mcp-server "Create an API token for your Ansible Automation Platform instance to authenticate your MCP client with a personal access token.").

## Authenticate with the MCP server

To connect an AI agent to the MCP server, you must first authenticate with your Ansible Automation Platform instance.

Ansible Automation Platform supports two authentication methods for the MCP server:

- **Personal access token (PAT):** Create an API token and configure your MCP client with the token value. This method works with all MCP clients.
- **OAuth:** Configure your MCP client to authenticate through an OAuth authorization code flow. In Ansible Automation Platform 2.6, this method requires an MCP client that supports manual OAuth endpoint configuration.

### Authenticate with a personal access token

Create an API token for your Ansible Automation Platform instance to authenticate your MCP client with a personal access token.

#### Before you begin

- Your organization administrator has deployed the MCP server for Red Hat Ansible Automation Platform.

#### Procedure

1. From the navigation panel, select Access Management> (and then)Users.
2. Select the username for your user profile to configure OAuth 2 tokens.
3. Select the **Tokens** tab. When no tokens are present, the **Tokens** screen prompts you to add them.
4. Click **Create token**, and provide the following details:

  - **Application**: Enter the name of the application with which you want to associate your token. Alternatively, you can search for it by clicking **Browse**. This opens a separate window that enables you to choose from the available options. Select **Name** from the filter list to filter by name if the list is extensive. Note:
            To create a Personal Access Token (PAT) that is not linked to any application, leave the **Application** field blank.

  - **Description**: (Optional) Provide a short description for your token.
  - **Scope**: (Required) Specify the level of access you want this token to have. The scope of an OAuth 2 token can be set as one of the following:
    * **Write**: Allows requests sent with this token to add, edit, and delete resources in the system.
    * **Read**: Limits actions to read only. The write scope includes the read scope.

5. Click **Create token**. The token information is displayed.
6. On the token information page that appears, click the **Copy icon** and save the token for future use. Important:
      This will be the only time the token is displayed. Therefore, ensure that you save the token for future use.

#### Results

You can verify that the application now shows the user with the appropriate token by selecting the **Tokens** tab on the **Application Details** page:

1. From the navigation panel, select Access Management> (and then)OAuth Applications.

2. Select the application you want to verify from the **Applications** list view.

3. Select the **Tokens** tab. Your token should be displayed in the list of tokens associated with the application you chose.

#### What to do next

-  [Connect an external AI agent to the MCP server](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#proc-connect-ai-agent-ansible-mcp-server "Use the API token of the MCP server to connect it with your preferred AI agent, such as Claude, Cursor, or ChatGPT.")

### Enable OAuth 2.1 on the MCP server

An administrator must create an OAuth application and enable OAuth 2.1 on the MCP server before users can authenticate with their Ansible Automation Platform credentials.

#### About this task

Note:

OAuth 2.1 authentication supplements the existing personal access token (PAT) method. Users who currently connect to the MCP server with a manually created API token can continue to do so.

For OAuth authentication on Ansible Automation Platform 2.6, which requires manual endpoint configuration, see [Authenticate with OAuth](/documentation/en-us/red_hat_ansible_automation_platform/2.7/oauth-authentication-for-the-mcp-server.html "As an alternative to personal access tokens (PATs), you can configure OAuth authentication for the MCP server. With OAuth, users sign in with their Ansible Automation Platform credentials through an authorization code flow instead of creating and distributing personal access tokens.") in the AAP 2.6 documentation.

#### Procedure

1. Create an OAuth application on the Ansible Automation Platform gateway.
      For instructions, see [Creating an OAuth application](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_create_oauth_app).

    Configure the following settings:

    | Setting                  | Value                                                                                                                          |
    | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
    | Authorization grant type | Authorization code                                                                                                             |
    | Client type              | Confidential orPublic, based on your security requirements.                                                                    |
    | Redirect URI             | The callback URL for your MCP client (for example,`http://localhost:6661/callback`). You can configure multiple redirect URIs. |
    | PKCE required            | Selected by default for new applications. Do not disable unless you have a specific compatibility requirement.                 |
    Existing OAuth applications created before this feature are migrated with PKCE disabled. If you have pre-existing OAuth applications that you want to use with the MCP server, enable PKCE on those applications manually.

2. Save the Client ID and, if you selected a Confidential client type, the Client secret. Users will need these values to connect their MCP clients.
3. Enable OAuth 2.1 on the MCP server through the installer extra settings.
      **Containerized installer**

    Add the `OAUTH2_ENABLED` variable to the `mcp_extra_settings` section in your inventory file:

```
[ansiblemcp]
<mcp-server-hostname>

    [ansiblemcp:vars]
mcp_extra_settings=[{"setting": "OAUTH2_ENABLED", "value": "true"}]
```

    Optionally, configure the OIDC discovery timeout:

```
[ansiblemcp:vars]
mcp_extra_settings=[{"setting": "OAUTH2_ENABLED", "value": "true"}, {"setting": "OAUTH2_DISCOVERY_TIMEOUT", "value": "30"}]
```

    After updating the inventory file, re-run the installer for the changes to take effect.

    **Operator-based deployments**

    Add the `OAUTH2_ENABLED` setting to the `extra_settings` section of the `mcp:` configuration in the AnsibleAutomationPlatform custom resource:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: <app-name>
  namespace: <namespace>
spec:
  mcp:
    disabled: false
    extra_settings:
      - setting: OAUTH2_ENABLED
        value: true
```

  Note:
  The MCP server URL is automatically set in both operator and containerized installer deployments. You do not need to configure it manually.

#### What to do next

Provide the Client ID (and Client secret, if applicable) to users who need to connect their MCP clients with OAuth 2.1.

### Connect an MCP client with OAuth 2.1

After an administrator has created an OAuth application and enabled OAuth 2.1 on the MCP server, you can connect your MCP client to authenticate with your Ansible Automation Platform credentials.

#### Before you begin

- An OAuth application is created on the Ansible Automation Platform gateway.
- The `OAUTH2_ENABLED` setting is set to `true` on the MCP server.
- You have the Client ID (and optionally, the Client secret) from your administrator.
- You have the Ansible MCP server URL.

#### About this task

The following example shows how to connect Claude Code to the MCP server with OAuth 2.1.

#### Procedure

1. Configure the OAuth application on the Ansible Automation Platform gateway with the following redirect URIs:
  

```
http://localhost:6661/callback
http://127.0.0.1:6661/callback
```

2. Add the MCP server to Claude Code from your terminal:
  

```
$ claude mcp add --transport http --client-id <client-id> --callback-port 6661 aap-mcp-server \
  https://<mcp-server-host>/mcp
```

    The callback port (6661) must match the port in the redirect URIs configured on the OAuth application.

#### JSON configuration file

Alternatively, configure the MCP server in a JSON configuration file:

```
{
  "mcpServers": {
    "aap-mcp": {
      "type": "http",
      "url": "https://<mcp-server-url>/mcp",
      "auth": {
        "type": "oauth2",
        "client_id": "<your-client-id>",
        "client_secret": "<your-client-secret>"
      }
    }
  }
}
```

### OAuth 2.1 settings for the MCP server

Configuration variables and token lifetime settings for OAuth 2.1 authentication on the Ansible MCP server.

#### MCP server variables

Add these variables to `mcp_extra_settings` (containerized installer) or `extra_settings` (operator) in your deployment configuration.

| Variable                   | Description                                                                                                                                                                     | Required              | Default    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------- |
| `OAUTH2_ENABLED`           | Enables OAuth 2.1 authentication on the MCP server.                                                                                                                             | Yes (to enable OAuth) | false      |
| `OAUTH2_DISCOVERY_TIMEOUT` | Timeout in seconds for the OIDC discovery probe at startup. Increase this value if the MCP server logs timeout errors during startup in environments with high network latency. | No                    | 10 seconds |

#### Token lifetime configuration

Access token and refresh token lifetimes are configured on the Ansible Automation Platform gateway, not the MCP server. You must set the access token lifetime to a shorter value than the default to ensure refresh tokens can renew access before requiring re-authentication.

Set the access token lifetime to 28800 seconds (8 hours):

| Setting                                        | Description                             | Default                   |
| ---------------------------------------------- | --------------------------------------- | ------------------------- |
| `OAUTH2_PROVIDER__ACCESS_TOKEN_EXPIRE_SECONDS` | How long an access token remains valid. | 31536000 seconds (1 year) |

For more information, see [Managing OAuth 2.0 for external users](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-con_gw_manage_oauth2_external_users).

### Connect an AI agent to the MCP server

Use the API token of the MCP server to connect it with your preferred AI agent, such as Claude, Cursor, or ChatGPT.

#### Before you begin

- The MCP server for Red Hat Ansible Automation Platform is deployed on your Ansible Automation Platform environment.
- An API token is created for your MCP server.

#### Procedure

1. Go to the AI tool that you want to connect to the Ansible Automation Platform.
2. Follow your AI client's instructions to configure the MCP server settings. Typically, you must specify the MCP server configurations in the mcp.json file.
3. When configuring the mcp.json file, add the MCP server details using one of the following options.
      **Option 1: Discover endpoint (recommended)**

    To access all toolsets through a single connection with optimized token consumption, configure the discover endpoint:

```
{
    "mcpServers": {
        "aap-mcp": {
            "type": "http",
            "url": "https://aap.example.com:8448/mcp/discover",
            "headers": {
                "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
            }
        }
    }
}
```

    The discover endpoint dynamically identifies the appropriate toolset for each query, so you do not need to configure individual toolset connections.

    **Option 2: Individual toolset endpoints**

    To control exactly which tools your AI agent can access, configure a separate entry for each toolset:

```
{
    "mcpServers": {
        "aap-mcp-job-mgmt": {
            "type": "http",
            "url": "https://aap.example.com:8448/mcp/job_management",
            "headers": {
                "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
            }
        },
        "aap-mcp-inventory-mgmt": {
            "type": "http",
            "url": "https://aap.example.com:8448/mcp/inventory_management",
            "headers": {
                "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
            }
        },
        "aap-mcp-system-monitor": {
            "type": "http",
            "url": "https://aap.example.com:8448/mcp/system_monitoring",
            "headers": {
                "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
            }
        },
        "aap-mcp-user-mgmt": {
            "type": "http",
            "url": "https://aap.example.com:8448/mcp/user_management",
            "headers": {
                "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
            }
        },
        "aap-mcp-security": {
            "type": "http",
            "url": "https://aap.example.com:8448/mcp/security_compliance",
            "headers": {
                "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
            }
        },
        "aap-mcp-platform-config": {
            "type": "http",
            "url": "https://aap.example.com:8448/mcp/platform_configuration",
            "headers": {
                "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
            }
        },
        "aap-mcp-content": {
            "type": "http",
            "url": "https://aap.example.com:8448/mcp/content_discovery",
            "headers": {
                "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
            }
        }
    }
}
```

  Important:
  Use a concise MCP server name, ideally limited to 20 characters. This is because AI agents combine the MCP server name with the tool name to create a unique identifier, and most AI agents enforce a 64-character limit on this combined identifier.

#### Results

Verify that the AI tool successfully connects to the Ansible Automation Platform MCP server using the API token.

In your AI agent's chat window, enter a prompt like `What MCP tools are available for my Ansible Automation Platform?` The AI agent should return a response with a list of tools that are enabled for the Ansible Automation Platform MCP server.

### Troubleshoot MCP server errors

This section contains information to help you diagnose and resolve issues with deploying the MCP server for Red Hat Ansible Automation Platform and connecting it to an external AI agent.

#### SSL certificate validation fails when the MCP server connects to Ansible Automation Platform

**Issue**: When your OpenShift Container Platform deployment uses a custom certificate authority (CA) or self-signed certificates, the MCP server cannot validate the ingress certificate. This results in `SELF_SIGNED_CERT_IN_CHAIN `errors that prevent the server from connecting to Ansible Automation Platform.

To resolve this issue, create a secret that contains your CA certificate and reference it in the AnsibleMCPServer custom resource. The operator then mounts the certificate, adds it to the combined CA bundle, and redeploys the server pods.

**Workaround**:

To implement this solution you must have a custom CA certificate file that signed the OpenShift Container Platform ingress certificate. You must also have `oc`CLI access to the namespace where the MCP server is deployed. 1. Create a secret that contains your CA certificate in the namespace where the Ansible MCP server is deployed:

```
$ oc create secret generic <secret_name> \
 --from-file=bundle-ca.crt=<ca_cert_file> \
 -n <namespace>
```

Replace the following values:
  1. `secret_name`: a name for the secret.
  2. `ca_cert_file`: The path to your CA certificate file.
  3. `namespace`: The namespace of the MCP server deployment.

2. Edit the AnsibleMCPServer custom resource to reference the secret:

```
spec:
  bundle_cacert_secret: <secret_name>
```

Replace `secret_name` with the name of the secret you created.

3. Save the custom resource. The operator detects the configuration change, mounts the CA certificate, adds it to the combined CA bundle, and redeploys the MCP server pods.
**Verification**:

1. Check the pod logs for the MCP server and verify that no SSL errors are present.
2. Verify that the init container logs contain the message “Added customer CA bundle”.

#### API output format rejected with 406 Status Code

**Issue**: Ansible Automation Platform rejects an API request (for example, retrieving job stdout) with an HTTP `406` status code if the MCP server’s requested output is not in `JSON` format.

**Workaround**: To obtain the output in a specific format, instruct your AI tool to use `JSON` format first. You can then transform the `JSON` output into your desired format.

#### User requests rejected with 400 status code

**Issue**: The MCP server may reject user requests from the external AI tool with `400 Bad Request` status code. This error is encountered when the Ansible Automation Platform uses a self-signed certificate.

**Workaround**: Configure the MCP server to ignore certificate errors using the following steps:

- For container-based installation: Set the value of variable `mcp_ignore_certificate_errors` to `true`.

- For operator-based installation:     Add the `IGNORE_CERTIFICATE_ERRORS` setting to the `mcp:` section of **AnsibleAutomationPlatform** custom resource in the following format:

```none
spec:
  mcp:
    extra_settings:
      - setting: IGNORE_CERTIFICATE_ERRORS
        value: true
```

#### MCP server permissions are changed post deployment

**Issue**: If you changed the permissions of the MCP server after it was created and deployed, you must delete the **AnsibleMCPServer** custom resource and recreate it.

**Workaround**: Perform the following steps:

1. Navigate to the Ansible Automation Platform portal.
2. Under **Resources**, search for the **AnsibleMCPServer** custom resource.
3. Select the active **AnsibleMCPServer** instance. An active AnsibleMCPServer instance is identified by the `-mcp` suffix appended to the Ansible Automation Platform custom resource name.
4. Select the **Settings menu** (3-dot menu icon) on the right side of the instance, then click **Delete AnsibleMCPServer**.
5. After the reconciliation process is completed, the existing MCP server instance is deleted and a new MCP server instance is created.
