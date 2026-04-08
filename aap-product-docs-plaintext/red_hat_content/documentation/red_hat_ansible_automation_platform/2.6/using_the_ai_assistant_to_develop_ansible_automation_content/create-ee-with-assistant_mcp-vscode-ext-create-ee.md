# 6. Create and validate an execution environment with the AI assistant
## 6.2. Create an execution environment definition file with the AI assistant




To create an execution environment, first prompt the AI assistant to generate a definition file that defines the environment.

**Procedure**

1. Enter a prompt describing your execution environment requirements in the Copilot chat window. For example:


-  _Create an execution environment definition file. Use `        ee-minimal` as the base, include `        ansible.builtin` and the `        community.general` collection, add git as a system package, and tag it as `webserver-ee:1.0`_

In response, the assistant triggers the `        define_and_build_execution_env tool` to formulate a prompt using your requirements and the internal `        ee-rules.md` resource.

Note
No file is created in this step. The assistant prepares the context for accurate YAML generation.





1. Instruct the assistant to create the execution environment file. For example:


-  _Generate the execution-environment.yml content based on the prompt you received_ .

The assistant then calls the tool again, this time with the `        generatedYaml` parameter. The tool validates the generated YAML against the execution environmentschema.





**Verification**

If successful, the assistant confirms the creation of `execution-environment.yml` and displays the validation status.


