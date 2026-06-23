# Create and validate an execution environment with the assistant
## Generate an execution environment definition from an existing playbook
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
