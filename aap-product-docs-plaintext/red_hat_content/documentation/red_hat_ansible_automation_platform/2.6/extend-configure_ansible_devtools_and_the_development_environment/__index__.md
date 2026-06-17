# Configure Ansible DevTools and the development environment

After installing ADT, use the MCP server for Red Hat Ansible Automation Platform to configure your workspace by setting up a virtual environment, installing specific Python versions, and adding necessary Ansible collections.

## Before you begin

- VS Code is open.
- GitHub Copilot Chat is active.

## Procedure

1.  In the Copilot chat window, enter a natural language prompt instructing the AI assistant to set up a particular configuration. For example:


```
Set up a complete Ansible development environment with Python 3.11, and install the collections amazon.aws and ansible.posix
```
The assistant will trigger the `ade_setup_environment`tool. The system will automatically perform the following configuration steps:
- Create a Virtual Environment: The assistant creates a virtual environment (for example, `venv/`) in your workspace.
- Install Core Tools: The assistant installs `ansible-core `and `ansible-lint` in the new virtual environment.
- Install Collections: The assistant installs the requested collections (for example, `amazon.aws`, `ansible.posix`) and their dependencies.
- Check for Conflicts: The assistant checks for conflicting packages and verifies the `ansible-lint` status.

2.  Review the output in the Copilot interface. When it has completed setup, the assistant provides a summary confirming the environment is set up. It also provides instructions on how to activate the environment:
1.  To activate, run: `source <path>/venv/bin/activate`
2.  To deactivate, run: `deactivate`

## What to do next

Verify the configuration was successful by asking the assistant to re-check the environment status. For example:

```
Check my environment again to confirm everything is set up correctly.
```

The `ade_environment_info` tool will run and confirm the Python version, virtual environment path, and installed collections in its output.
