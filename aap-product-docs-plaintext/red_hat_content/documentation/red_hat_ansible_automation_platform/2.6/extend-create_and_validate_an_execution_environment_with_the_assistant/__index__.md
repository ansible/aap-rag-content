# Create and validate an execution environment with the assistant

To create an execution environment, first generate a definition file that defines the environment.

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

## What to do next

If successful, the assistant confirms the file creation and displays the validation status.

## Generate an execution environment definition from an existing playbook

Use the AI assistant to inspect an existing playbook to determine the necessary collections and dependencies for a new execution environment based on the playbook.

### Procedure

1.  In the VS Code editor, open the playbook you intend to analyze.
2.  In the Copilot chat window, ask the assistant to analyze the playbook. For example:


```
Analyze my current playbook, determine the necessary collections, and generate an execution environment definition file that includes them
```

3.  Review the output and confirm that the assistant has imported collections (for example, `community.general`, `amazon.aws`) required by the tasks in your playbook.

### What to do next

Follow the previous procedure to create an execution environment definition file. The resulting `execution-environment.yml `will automatically populate the dependencies section with the identified collections.

### Validate an execution environment file

Use the AI assistant to validate an existing definition file against the schema and Ansible best practices.

#### Before you begin

- The `execution-environment.yml`file is open in the editor.
- Copilot chat is active.

#### Procedure

1.  Ask the assistant to validate your execution environment file. For example:


```
Check if my execution-environment.yml file is valid and follows best practices
```
The assistant then analyzes the file structure against the execution environment v3 schema and rules. It verifies required sections (for example, `version`, `images`, `dependencies`) and identifies missing fields or incorrect formatting.

2.  Review the assessment to confirm that it includes your requirements.

#### Build the execution environment with the assistant

After the definition file is created and validated, you can prompt the assistant for the specific commands to build the image.

##### Before you begin

- A container runtime like Podman is installed.
- Copilot chat is active and your execution environment file is open in the editor.

##### Procedure

1.  Ask the assistant for build instructions. For example:


```
How do I build this execution environment? What are the next steps?
```
This prompts the assistant to generate an `ansible-builder` command tailored to your file and tag.

2.  Copy the build command that was generated and run it in your VS Code terminal. An example command might look like this:


```
ansible-builder build --file execution-environment.yml --context ./context --tag webserver-ee:1.0 -vvv.
```
