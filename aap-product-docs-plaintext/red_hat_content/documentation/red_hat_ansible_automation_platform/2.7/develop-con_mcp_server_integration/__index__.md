# MCP server integration

An MCP server implements Model Context Protocol (MCP) for a specific backend such as a REST API, various services, databases, and other external systems. The MCP server exposes its operations as discoverable tools that AI agents or large language models (LLMs) can call.

MCP servers are integrated into execution environments (EEs) using a robust Ansible plugin framework. This setup allows Ansible playbooks to call MCP servers directly. A crucial design strategy is the ephemeral nature of these servers, meaning they exist only for the duration of the job execution.

The core requirement for enabling MCP support involves securely installing the required MCP server software into the execution environment during the build process, typically using the `ansible-builder` command.

You can configure MCP servers in two ways:

- **For embedded (local) MCP servers**: The EE image must explicitly include the MCP server binaries or libraries installed on the image path. This setup enables the execution environment to discover and start the specific embedded server required for the job.
- **For remote (external) MCP servers**: The EE build process facilitates defining remote connection details in a manifest file contained within the EE. This manifest informs the core MCP collection plugin on how to connect, typically pointing to a specific remote URL using an HTTP connection.


