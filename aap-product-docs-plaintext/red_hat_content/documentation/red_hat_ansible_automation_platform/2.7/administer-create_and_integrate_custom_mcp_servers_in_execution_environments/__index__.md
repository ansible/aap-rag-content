# Create and integrate custom MCP Servers in execution environments

Integrate custom *Model Context Protocol* (MCP) servers into execution environments using the `ansible.mcp_builder` framework to automate installation, configuration, and lifecycle management.

Note:

Individual MCP server implementations (including the reference examples for AWS, Azure, and GitHub) are Dev Preview and unsupported. Your organization is responsible for the MCP servers you choose to integrate.

**Preparing your environment**

Before you begin, ensure you have the following:

- ansible-builder : Version 3.1 or later installed on your build system. Install it using     `dnf install ansible-builder`.

- ansible-core: : Version 2.16 or later.

- Access to a base Execution Environment image, for example, ee-minimal-rhel9 from the Red Hat registry.

- The `ansible.mcp_builder` collection (version 1.0.3 or later), installed using:     `ansible-galaxy collection install ansible.mcp_builder`.

- The `ansible.mcp` collection (a required dependency), installed using:     `ansible-galaxy collection install ansible.mcp`.

- Familiarity with Ansible roles, collections, and execution environment definitions.

