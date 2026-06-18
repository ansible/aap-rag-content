+++
title = "Deploy the MCP server on Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server/", "Deploy the MCP server on Ansible Automation Platform"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server/aem-page/extend-assembly_deploying_ansible_mcp_server.html"
last_crumb = "Deploy the MCP server on Ansible Automation Platform"
modified = "2026-06-05T07:48:10.594Z"
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

### Benefits

The following are the benefits of the MCP server:

**For external AI tools**:

- Provides a standardized interface for securely querying infrastructure data and executing automation workflows within the Ansible Automation Platform.
- Enables agentic workflows to interact with the Ansible Automation Platform.


**For Ansible users**:

- Provides the ability to use the chatbot interface of their preferred external AI tool to get information about their Ansible Automation Platform environment, and run automation jobs directly through that tool.


**For developers**:

- Reduces the time and complexity of developing or integrating the Ansible Automation Platform with AI applications or agents.
- Simplifies AI integration, enabling existing automation through Ansible Automation Platform to be exposed to AI tools without writing custom API code or middleware.

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

### MCP server toolsets

The MCP server provides a pre-configured suite of toolsets that effectively act as a bridge between your preferred AI agent and the Ansible Automation Platform. Once configured, these toolsets enable your AI agent to perform specific, authorized actions without requiring you to leave the chat interface.

The MCP server turns your AI agent from a passive assistant into an active operator that can interact with your Ansible Automation Platform infrastructure and execute workflows or automate tasks based on the permissions you define.

| Toolset                    | Description                                                                                                                                                     | Usage examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Job management         | <br>Tools to list available job templates, launch automation jobs, and monitor their real-time status.                                                          | <br>Operators can:<br>Launch job templates and workflows to execute automation tasks for their projects and services.View job output and logs to troubleshoot failed automation tasks and understand what went wrong.Relaunch failed jobs to recover from temporary failures and complete necessary automation tasks.                                                                                                                                                                                                     |
| <br>Inventory management   | <br>Tools to query your inventory for host details, check group membership, and verify system facts.                                                            | <br>Operators can:<br>View and browse inventories across environments to understand which systems they are managing with automation.Manage group assignments to target automation to specific sets of systems.View hosts that are configured for automation.                                                                                                                                                                                                                                                              |
| <br>System monitoring      | <br>Tools to retrieve job logs, troubleshoot failed tasks, and check the health of your automation environment.                                                 | <br>Administrators can:<br>Perform platform status and health checks across all services to identify issues and ensure the automation platform is running correctly.Monitor service health through the platform gateway to ensure all platform components are functioning correctly.Audit user activity and generate reports to ensure compliance and identify potential security issues.                                                                                                                                 |
| <br>User management        | <br>Tools to allow the AI agent to administer access and organizational structure within the Ansible Automation Platform.                                       | <br>Administrators can:<br>Use natural-language prompts to provision users and enforce hierarchy, rather than manually navigating the UI.Create, modify, and delete users and teams to manage access to the Ansible Automation Platform and support organizational changes.Configure role-based access control to ensure users have the appropriate permissions for their responsibilities while maintaining security.View team memberships and structure to see who else in their organization is working on automation. |
| <br>Security/compliance    | <br>Tools that enable the AI agent to act as a security operator, managing sensitive credentials and verifying platform integrity without exposing raw secrets. | <br>Operators can:<br>View available credentials to understand what authentication options are available for their automation jobs.<br>Administrators can:<br>Manage credentials and security policies to ensure secure access to external systems while maintaining proper governance.Manage custom credential types for seamless integration with third-party applications.                                                                                                                                             |
| <br>Platform configuration | <br>Tools that enable organization administrators and developers to inspect and tune the Ansible Automation Platform infrastructure itself.                     | <br>Administrators can:<br>Manage system settings across all components to configure the platform in line with the organizational requirements and policies.Manage and track licenses to ensure compliance with licensing terms and optimize license utilization.<br>Developers can:<br>Tune execution environments to optimize the runtime performance of their automation content.                                                                                                                                      |

### Server-level and user-level permissions

The MCP server employs a dual-layer security model to ensure safe integration between AI tools and your Ansible Automation Platform infrastructure. This approach combines a global administrative safeguard with the granular Role-Based Access Control (RBAC) of the Ansible Automation Platform.

You can grant the following access types to the MCP server:

- **Server-level permissions**: Organization administrators assign a global-level permission while deploying the MCP server. Administrators can choose one of the following access levels:
  * Read-only access: The default setting that enforces a strict "look but do not touch" policy. The AI agent can retrieve system data, such as logs and inventory, but the agent cannot launch jobs or modify configurations. This global safeguard overrides all individual user permissions to prevent unintended automation.
  * Read-write access: This setting authorizes the AI agent to make changes in your Ansible Automation Platform, such as executing job templates, managing resources, and applying infrastructure changes. However, these actions are subject to the specific RBAC permissions of the user-provided API token.
- **User-level permissions**: The AI agent’s specific capabilities are inherited from the user account that generated the authentication API token.   * Inherited permissions: The AI tool inherits the user’s permissions and performs only the actions the user is authorized to perform. For example, if the user’s token only has permissions to view the "network" inventory, the AI tool cannot access or modify the "database" inventory even if the user requests it.
  * Rejection of unauthorized actions: If the AI tool attempts an action (like launching a job) that the user’s token is not authorized to perform, the Ansible Automation Platform API rejects the request.


Warning:

Enabling read-write access for the MCP server grants the AI agent autonomy to directly make changes in your Ansible Automation Platform environment, for example, executing automation jobs. The AI agent can directly make changes in your Ansible Automation Platform environment only if the user has write permissions. Large Language Models (LLMs) can occasionally misinterpret prompts or hallucinate commands. Therefore, enabling read-write access may introduce a risk of unintended changes to your environment.

### Telemetry data collection for the MCP server

Red Hat collects anonymized telemetry data from the MCP server. The telemetry data includes metrics related to MCP server performance, adoption trends, and usage patterns.

Telemetry data will be automatically collected for MCP server deployments using Ansible Automation Platform patch release on 21 January 2026 and later versions. Red Hat will use this data to monitor the operational health of your MCP servers and to ensure the long-term scalability of the MCP ecosystem.

Important:

Telemetry data collection cannot be disabled, but strict user privacy is maintained. Red Hat does not collect users' personal information, such as usernames or passwords. If any personal information is inadvertently received, the data is deleted. For more information, see the Red Hat Privacy Statement under Related Links below.

### Prerequisites

- Platform version: An instance of Ansible Automation Platform 2.6 or later.
- Deployment environment:
  * OpenShift: Access to an OpenShift cluster with permissions to install operators.
  * Containerized: A supported container runtime.
- Access credentials: A valid user or service account within Ansible Automation Platform with permissions to execute the desired automation jobs. You will need to generate an API token for this account.

### Overview of deploying the MCP server

Perform the following tasks to deploy and configure an MCP server and integrate it with your preferred AI tool:

| Step number | Task                                                                   | Description                                                                                                                                                                                                                         |
| ----------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>1       | <br>Deploy and configure an MCP server on container-based installation | <br>An organization administrator deploys and configures the MCP server on a container-based installation of Ansible Automation Platform 2.6 or later.                                                                              |
| <br>2       | <br>Create an API token for the MCP server                             | <br>An Ansible user creates an API token for their Ansible Automation Platform instance and uses it to connect to their preferred AI tool. The AI tools will inherit the user’s permissions for authentication using the API token. |
| <br>3       | <br>Connect an external AI agent to the MCP server                     | <br>The Ansible user then configures an external AI tool with the MCP server’s API token, enabling the AI tool to connect to the MCP server and execute workflows and automate tasks.                                               |

## Deploy the MCP server for Red Hat Ansible Automation Platform on a container-based installation

As an organization administrator, you can deploy and configure the MCP server on a container-based installation of Ansible Automation Platform. Use the following procedure to deploy and configure the MCP server.

### Before you begin

- You have a valid subscription for Ansible Automation Platform 2.6 or later.

### Procedure

 Configure MCP server variables in the inventory file:

1.  Create an `[ansiblemcp]` group and add a host for the MCP server.
2.  Add the following installation variables to your inventory file under the `[all:vars]` group:

  - `mcp_allow_write_operations`: Use to grant read-only or read-write permissions to the external AI tool.
  - `mcp_ignore_certificate_errors`: Use to bypass SSL/TLS certificate validation.

3.  To make your system trust a self-signed custom certificate, add the following required variables to your inventory file:

  - `mcp_tls_cert`: Path to TLS certificate

  - `mcp_tls_key`: Path to TLS key         For information about using your own TLS certificates and keys, see [Configuring custom TLS certificates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_advanced_configuration_containerized "Configure external databases, custom TLS certificates, execution nodes, HAProxy load balancers, and hub storage for complex containerized Ansible Automation Platform deployments."). For information about required and optional variables, see [MCP server variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-mcp_server_variables "Inventory file variables for the MCP server for Red Hat Ansible Automation Platform.").



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

4.  Optional: add additional MCP server settings such as `DEFAULT_PAGE_SIZE` as in the example above.

### Results

Check the pods after installation is complete. You should see an `ansiblemcp` pod running with the following command:

```none
$ podman ps
```

### What to do next

1. Obtain the location of the MCP server:
  - The service is exposed on port 8448 of the host, and HTTPS is enabled.
  - The example above deploys the MCP server on `aap.example.com`, so the service base URL will be `https://aap.example.com:8448`.
2. [Create an API token for the MCP server](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#proc-create-api-token-ansible-mcp-server "Create an API token for your Ansible Automation Platform instance, so you can use it to connect with your preferred AI agent. The AI tool will inherit the user’s permissions for API token-based authentication.").

## Deploy the MCP server for Red Hat Ansible Automation Platform on an operator-based installation

As an organization administrator, you can deploy and configure the MCP server on an operator-based installation of Ansible Automation Platform. Use the following procedure to deploy and configure the MCP server.

### Before you begin

- You have a valid Ansible Automation Platform subscription.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform as an administrator.
2.  Navigate to the namespace where you want to install the MCP server.
3.  Select Operators> (and then)Installed Operators.
4.  From the list of installed operators, select **Ansible Automation Platform**.
5.  In the Ansible Automation Platform tile, click **Create instance**.
6.  From the **Configure via** field, select the **Form** view, then provide the instance name. For example, `aap-mcp`.
7.  Select the **YAML** view, and under the `spec:` section, add the `mcp` component:
  

```
spec:
  mcp:
    disabled: false
    allow_write_operations: false
```

8.  Use the `allow_write_operations` variable to configure the operational access level of the MCP server:
9.  Click **Create**. the MCP server is created.
10.  Optional: If you changed the permissions of the MCP server after it was created and deployed, you must delete the **AnsibleMCPServer** custom resource and recreate it. Perform the following steps:

  1.  Go to the Ansible Automation Platform portal.
  2.  Under **Resources**, search for the **AnsibleMCPServer** custom resource.
  3.  Select the active **AnsibleMCPServer** instance. An active AnsibleMCPServer instance is identified by the `-mcp` suffix appended to the Ansible Automation Platform custom resource name.
  4.  Select the **Settings menu** on the right side of the instance, and then click **Delete AnsibleMCPServer**.
  5.  After the reconciliation process completes, the existing MCP server instance is deleted, and a new MCP server instance is created.

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
2. [Create an API token for the MCP server](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#proc-create-api-token-ansible-mcp-server "Create an API token for your Ansible Automation Platform instance, so you can use it to connect with your preferred AI agent. The AI tool will inherit the user’s permissions for API token-based authentication.").

## Create an API token for the MCP server

Create an API token for your Ansible Automation Platform instance, so you can use it to connect with your preferred AI agent. The AI tool will inherit the user’s permissions for API token-based authentication.

### Before you begin

- Your organization administrator has deployed the MCP server for Red Hat Ansible Automation Platform.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  Select the username for your user profile to configure OAuth 2 tokens.
3.  Select the **Tokens** tab. When no tokens are present, the **Tokens** screen prompts you to add them.
4.  Click **Create token**, and provide the following details:

  - **Application**: Enter the name of the application with which you want to associate your token. Alternatively, you can search for it by clicking **Browse**. This opens a separate window that enables you to choose from the available options. Select **Name** from the filter list to filter by name if the list is extensive. Note:
            To create a Personal Access Token (PAT) that is not linked to any application, leave the **Application** field blank.

  - **Description**: (Optional) Provide a short description for your token.
  - **Scope**: (Required) Specify the level of access you want this token to have. The scope of an OAuth 2 token can be set as one of the following:
    * **Write**: Allows requests sent with this token to add, edit, and delete resources in the system.
    * **Read**: Limits actions to read only. The write scope includes the read scope.

5.  Click **Create token**. The token information is displayed.
6.  On the token information page that appears, click the **Copy icon** and save the token for future use. Important:
      This will be the only time the token is displayed. Therefore, ensure that you save the token for future use.

### Results

You can verify that the application now shows the user with the appropriate token by selecting the **Tokens** tab on the **Application Details** page:

1. From the navigation panel, select Access Management> (and then)OAuth Applications.

2. Select the application you want to verify from the **Applications** list view.

3. Select the **Tokens** tab. Your token should be displayed in the list of tokens associated with the application you chose.

### What to do next

-  [Connect an external AI agent to the MCP server](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#proc-connect-ai-agent-ansible-mcp-server "Use the API token of the Ansible MCP server to connect it with your preferred AI agent, such as Claude, Cursor, or ChatGPT.")

### Connect an AI agent to the MCP server

Use the API token of the Ansible MCP server to connect it with your preferred AI agent, such as Claude, Cursor, or ChatGPT.

#### Before you begin

- The MCP server for Red Hat Ansible Automation Platform is deployed on your Ansible Automation Platform environment.
- An API token is created for your MCP server.

#### Procedure

1.  Go to the AI tool that you want to connect to the Ansible Automation Platform.
2.  Follow your AI client’s instructions to configure the MCP server settings. Typically, you must specify the MCP server configurations in the `mcp.json` file.

3.  When configuring the `mcp.json` file, add the Ansible MCP server URL in the following format:
       `<Ansible MCP server URL>/<toolset>/mcp`

    Key:

  - **Ansible MCP server URL** = The URL of the Ansible MCP server. For example, `https://api.example.com/`. To obtain the Ansible MCP server URL, contact your organization administrator.

  - **Toolset** = The toolset that you want to connect to. For example, `job_management`, `inventory_management`, `system_monitoring`, `user_management`, `security_compliance`, and `platform_configuration`.

  - **Token** = The API token of the Ansible MCP server. Use the following format to add details about your Ansible MCP server in the the `mcp.json` file:



```
{
  "mcpServers": {
    "aap-mcp-job-mgmt": {
      "type": "http",
      "url": "https://api.example.com/job_management/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    },
    "aap-mcp-inventory-mgmt": {
      "type": "http",
      "url": "https://api.example.com/inventory_management/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    },
    "aap-mcp-system-monitor": {
      "type": "http",
      "url": "https://api.example.com/system_monitoring/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    },
    "aap-mcp-user-mgmt": {
      "type": "http",
      "url": "https://api.example.com/user_management/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    },
    "aap-mcp-security": {
      "type": "http",
      "url": "https://api.example.com/security_compliance/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    },
    "aap-mcp-platform-config": {
      "type": "http",
      "url": "https://api.example.com/platform_configuration/mcp",
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

- Verify that the AI tool successfully connects to the Ansible Automation Platform MCP server using the API token. In your AI agent’s chat window, enter a prompt like `What MCP tools are available for my Ansible Automation Platform?`. The AI agent should return a response with a list of tools that are enabled for the Ansible Automation Platform MCP server.

#### What to do next

- Open a new chat in your AI agent, and enter your prompt. For example: `Give me a list of my Ansible Automation Platform jobs.` A list of all your Ansible Automation Platform jobs is displayed in the AI agent’s chat window.

### Troubleshoot MCP server errors

This section contains information to help you diagnose and resolve issues with deploying the MCP server for Red Hat Ansible Automation Platform and connecting it to an external AI agent.

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
