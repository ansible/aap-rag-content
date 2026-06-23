# Manage your Ansible dev environment
## Understand your automation with the AI assistant
### Procedure

1.  Open the playbook you want to investigate in the VS Code editor.
2.  In the Copilot chat window, enter a prompt instructing the AI agent to analyze dependencies. For example:


```
Analyze my web server playbook and tell me which Ansible collections are being used.
```
The assistant then analyzes the content and identifies:
- Collections: Which collections are required (for example,` ansible.builtin`, `community.general`).
- Modules: Specific modules utilized within the tasks.
- FQCN Compliance: The assistant verifies if the automations are referenced using their Fully Qualified Collection Names (FQCN)

