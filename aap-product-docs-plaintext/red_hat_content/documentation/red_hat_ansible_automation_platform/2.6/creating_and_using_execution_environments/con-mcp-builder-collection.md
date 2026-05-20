# 6. Create and integrate custom MCP Servers in execution environments
## 6.2. Understand the MCP builder framework

The `ansible.mcp_builder` collection provides a reusable framework for installing MCP servers inside execution environments. Rather than manually scripting installation steps in your container build, you define a role with metadata about your MCP server, and the framework handles the rest.

To automate the installation and lifecycle management of your servers, you must understand how the `ansible.mcp_builder` framework operates.

**How the framework works**

The framework consists of three main components:

- The common role ( `ansible.mcp_builder.common` ) provides shared installation logic for MCP servers. Based on the language specified in your role’s registry metadata, the common role automatically:


- Installs the appropriate language runtime (Go, Node.js, or Python/uv) if not already present.
- Downloads and installs the MCP server package from the correct source (PyPI, npm, or Git).
- Generates a unified manifest file (`/opt/mcp/mcpservers.json/opt/mcp/ mcpservers.json`) listing all available MCP servers.
- Creates the `mcp_manage` utility for listing, querying, and running installed MCP servers

- Your custom role defines metadata about the MCP server you want to install. At minimum, it includes:


- A registry variable that specifies the server name, transport type, language, and description.
- A tasks file that invokes the common role’s `install_manager` and `generate_manifest` tasks.

- A playbook ties your custom role into the build process. This playbook is called by ansible-builder during the execution environment container build.

**Selecting an installation method**

The framework supports three installation methods, selected by the `lang` field in your registry metadata:

| <br>  Language | <br>  Install method | <br>  Example servers |
| --- | --- | --- |
| <br>  pyoi | <br>  Installed with uv tool install from PyPI | <br>  AWS CloudFormation MCP, AWS Core MCP, AWS IAM MCP |
| <br>  npm | <br>  Installed with npm from the npm registry | <br>  Azure MCP |
| <br>  go | <br>  Built from source with go build from a Git repository | <br>  GitHub MCP |

