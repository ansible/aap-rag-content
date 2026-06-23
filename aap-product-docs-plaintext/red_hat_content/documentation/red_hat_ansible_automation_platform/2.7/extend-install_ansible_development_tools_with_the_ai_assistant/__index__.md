# Install Ansible Development Tools with the AI assistant

If you do not have Ansible Development Tools installed, you can instruct the assistant to install them.

## Procedure

1.  Open GitHub Copilot Chat.
2.  Enter the prompt:


```



```
The assistant then triggers the `adt_check_env` tool.
The system:
- Checks if ADT is already installed. If so, it will report: "ADT (`ansible-dev-tools`) is already installed".
- If ADT is not installed, it will attempt installation via `pip` or `pipx`.
If ADT is not already installed, the AI assistant chooses a package manager (`pip` or `pipx`) and installs ADT automatically.

