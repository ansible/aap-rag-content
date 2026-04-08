# 1. Set up your development environment with the MCP server-enabled Ansible VS Code extension
## 1.4. Configure Ansible development tools with the AI assistant




After installing Ansible development tools, you can use the MCP server-enabled AI assistant in the Ansible VS Code extension to configure your workspace, including:

- Setting up a virtual environment.
- Installing specific Python versions.
- Adding Ansible collections.


**Procedure**

1. Open GitHub Copilot chat.
1. In the chat window, enter a natural language prompt instructing the AI assistant to set up the configuration you want. For example:

_Set up a complete Ansible development environment with Python 3.11, and install the collections amazon.aws and ansible.posix_ .

The assistant triggers the `    ade_setup_environment` tool, and the system automatically performs the following configuration steps:


- Create a virtual environment: The assistant creates a virtual environment ( `        venv/` ) in your workspace.
- Install core tools: The assistant installs `        ansible-core` and `        ansible-lint` in the new virtual environment.
- Install collections: The assistant installs the requested collections ( `        amazon.aws` , `        ansible.posix` ) and their dependencies.
- Check for conflicts: The assistant checks for conflicting packages and verifies `        ansible-lint` status.

1. Review the output in the Copilot chat. When setup is complete, the assistant confirms that the environment is set up, and gives instructions on activating the environment. For example:


1. To activate, run `        source &lt;path&gt;/venv/bin/activate`
1. To deactivate, run `        deactivate` .



**Verification**

Verify that configuration was successful by asking the AI assistant to check the environment status again. For example:


_Check my environment again to confirm that everything is set up correctly_ .

The `ade_environment_info` tool runs and confirms the Python version, virtual environment path, and installed collections in its output.

