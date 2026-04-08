# 5. Validate and debug content with the AI assistant
## 5.2. Validate content with the AI assistant




Ask the AI assistant to analyze the current playbook without modifying it. This identifies specific rule violations and potential errors. If errors are found, `ansible_lint` has autofix functionality, enabling it to suggest changes, and, with your permission, implement those changes in your code.

**Procedure**

1. Open the playbook file in the VS Code editor.
1. Open the Copilot chat window.
1. In the chat window, enter a natural language prompt such as:


-  _Validate my webserver playbook to check for any issues_ .

This triggers the `        ansible-lint` tool in check-only mode. The assistant displays a list of the issues it found, including Rule IDs, line numbers, and descriptions of the errors (for example, missing FQCN, or YAML formatting issues).

The assistant will ask " _Would you like ansible-lint to apply automatic fixes?_ ” You must grant the AI assistant permission to make any changes to your code.



1. Enter “yes” or “no” depending on whether you want the assistant to apply the suggested changes.
1. Select the option to **allow** or **skip** to grant the assistant permission to make changes.


1. If you select **allow** , the AI assistant will update your code.
1. If you select **skip** , the AI assistant will output a list of issues and the suggested fix for each.



