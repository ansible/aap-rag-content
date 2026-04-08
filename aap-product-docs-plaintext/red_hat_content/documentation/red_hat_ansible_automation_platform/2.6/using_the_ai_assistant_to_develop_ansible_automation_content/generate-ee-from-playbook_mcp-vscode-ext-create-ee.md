# 6. Create and validate an execution environment with the AI assistant
## 6.3. Generate an execution environment from an existing playbook




Prompt the AI assistant to inspect an existing playbook to determine the necessary collections and dependencies for a new execution environment based on the playbook.

**Procedure**

1. Open the playbook you want to analyze in the VS Code editor.
1. In the Copilot chat window, prompt the assistant to analyze the playbook. For example:


-  _Analyze my current playbook, determine the necessary collections, and generate an execution environment definition file that includes them_ .

1. Review the output and confirm that the assistant has imported collections (for example, `    community.general` , `    amazon.aws` ) required by the tasks in your playbook.


