# 1. Set up your development environment with the MCP server-enabled Ansible VS Code extension
## 1.2. Run environment diagnostics

Use the AI assistant to assess your local environment to understand what tools, versions, and collections are currently installed.

**Procedure**

1. Open GitHub Copilot chat.

2. Enter a prompt in natural language asking the AI assistant what is installed in your environment. For example:


1. *Check my Ansible environment and tell me what’s installed*.

2. *What collections are installed*?

The assistant then triggers the `ade_environment_info` tool.

3. Review the output, which typically includes:


1. Workspace path and Python version
2. Virtual environment status
3. Ansible Automation Platform and `ansible_lint` versions
4. A list of installed collections
5. The installation status of Ansible development tools (ADT).

