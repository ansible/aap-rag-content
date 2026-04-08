# 1. Set up your development environment with the MCP server-enabled Ansible VS Code extension
## 1.2. Run environment diagnostics




Use the AI assistant to assess your local environment to understand what tools, versions, and collections are currently installed.

**Procedure**

1. Open GitHub Copilot chat.
1. Enter a prompt in natural language asking the AI assistant what is installed in your environment. For example:


1.  _Check my Ansible environment and tell me what’s installed_ .
1.  _What collections are installed_ ?

The assistant then triggers the `        ade_environment_info` tool.



1. Review the output, which typically includes:


1. Workspace path and Python version
1. Virtual environment status
1. Ansible Automation Platform and `        ansible_lint` versions
1. A list of installed collections
1. The installation status of Ansible development tools (ADT).



