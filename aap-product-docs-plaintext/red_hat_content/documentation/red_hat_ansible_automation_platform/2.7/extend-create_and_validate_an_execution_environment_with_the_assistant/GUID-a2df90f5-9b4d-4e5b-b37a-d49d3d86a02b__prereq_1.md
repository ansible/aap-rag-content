# Create and validate an execution environment with the assistant
## Before you begin

- VS Code is installed and running.
- The GitHub Copilot Extension is installed and active.
- The Ansible VS Code extension is installed.
- The MCP server for Red Hat Ansible Automation Platform is enabled. Ensure the setting `ansible.mcpServer.enabled` is set to `true`.
- Ansible Development Tools are installed through the assistant (`adt_check_env`) or manually.

## Procedure

1.  In the Copilot chat window, enter a prompt describing your execution environment requirements. For example:


```
Create an execution environment definition file. Use ee-minimal as the base, include ansible.builtin and the community.general collection, add git as a system package, and tag it as webserver-ee:1.0.
```
In response, the assistant triggers the `define_and_build_execution_env` tool to formulate a prompt using your requirements and the internal `ee-rules.md` resource. Note:
No file is created in this step. The assistant prepares the context for accurate YAML generation.

2.  Instruct the assistant to create the execution environment file. For example:


```
Now generate the execution-environment.yml content based on the prompt you received.
```
The assistant calls the tool again, this time with the `generatedYaml` parameter. The tool validates the generated YAML against the execution environment schema.

