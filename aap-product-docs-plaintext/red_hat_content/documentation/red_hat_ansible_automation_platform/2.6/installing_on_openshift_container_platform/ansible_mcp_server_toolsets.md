# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.1. Overview
### 7.1.3. Ansible MCP server toolsets




The Ansible MCP server provides a pre-configured suite of toolsets that effectively act as a bridge between your preferred AI agent and the Ansible Automation Platform. Once configured, these toolsets enable your AI agent to perform specific, authorized actions without requiring you to leave the chat interface.

The Ansible MCP server turns your AI agent from a passive assistant into an active operator that can interact with your Ansible Automation Platform infrastructure and execute workflows or automate tasks based on the permissions you define.

The following toolsets are available in this Technology Preview release:

| Toolset | Description | Usage examples |
| --- | --- | --- |
| Job management | Tools to list available job templates, launch automation jobs, and monitor their real-time status. | Operators can:

- Launch job templates and workflows to execute automation tasks for their projects and services.
- View job output and logs to troubleshoot failed automation tasks and understand what went wrong.
- Relaunch failed jobs to recover from temporary failures and complete necessary automation tasks. |
| Inventory management | Tools to query your inventory for host details, check group membership, and verify system facts. | Operators can:

- View and browse inventories across environments to understand which systems they are managing with automation.
- Manage group assignments to target automation to specific sets of systems.
- View hosts that are configured for automation. |
| System monitoring | Tools to retrieve job logs, troubleshoot failed tasks, and check the health of your automation environment. | Administrators can:

- Perform platform status and health checks across all services to identify issues and ensure the automation platform is running correctly.
- Monitor service health through the platform gateway to ensure all platform components are functioning correctly.
- Audit user activity and generate reports to ensure compliance and identify potential security issues. |
| User management | Tools to allow the AI agent to administer access and organizational structure within the Ansible Automation Platform. | Administrators can:

- Use natural-language prompts to provision users and enforce hierarchy, rather than manually navigating the UI.
- Create, modify, and delete users and teams to manage access to the Ansible Automation Platform and support organizational changes.
- Configure role-based access control to ensure users have the appropriate permissions for their responsibilities while maintaining security.
- View team memberships and structure to see who else in their organization is working on automation. |
| Security/compliance | Tools that enable the AI agent to act as a security operator, managing sensitive credentials and verifying platform integrity without exposing raw secrets. | Operators can:

- View available credentials to understand what authentication options are available for their automation jobs.


Administrators can:

- Manage credentials and security policies to ensure secure access to external systems while maintaining proper governance.
- Manage custom credential types for seamless integration with third-party applications. |
| Platform configuration | Tools that enable organization administrators and developers to inspect and tune the Ansible Automation Platform infrastructure itself. | Administrators can:

- Manage system settings across all components to configure the platform in line with the organizational requirements and policies.
- Manage and track licenses to ensure compliance with licensing terms and optimize license utilization.


Developers can:

- Tune execution environments to optimize the runtime performance of their automation content. |


