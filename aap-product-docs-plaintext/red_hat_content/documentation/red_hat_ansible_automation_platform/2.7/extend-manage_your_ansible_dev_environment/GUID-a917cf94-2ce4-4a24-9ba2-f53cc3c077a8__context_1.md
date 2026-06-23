# Manage your Ansible dev environment
## About this task

You can ask the AI assistant to list the automations (collections and tools) available in your local environment. This way, you can verify what tools are available to you before starting development.

## Procedure

1.  In the GitHub Copilot chat window, enter a natural language prompt to check the environment. For example:
1.  `Check my Ansible environment and tell me what's installed.`
2.  `What collections are installed?`
The AI assistant triggers the `ade_environment_info` tool.

2.  Review the output, which displays:
1.  Ansible Version: The core version installed.
2.  Ansible Lint Version: Confirmation of the linting tool status.
3.  Installed Collections: A list of collections available for use (such as `amazon.aws`, `ansible.posix`).
4.  Python Environment: Details about the active virtual environment.

