# 5. Validate and debug content with the AI assistant
## 5.3. Auto-fixing errors with the AI assistant




You can also prompt the AI assistant to automatically fix errors that `ansible_lint` finds.

**Procedure**

1. In the GitHub Copilot chat window, enter the following prompt:


-  _Run `        ansible-lint` on my webserver playbook and apply automatic fixes_ .

The automated workflow triggers the `        ansible_lint` tool with the `        fix: true` parameter.



1. The `    ansible_lint` tool then processes the file and applies corrections for issues such as:


- Converting short module names to fully qualified ones.
- Correcting YAML indentation and Jinja2 expression spacing.
- Fixing key ordering within tasks.



**Verification**

When the AI assistant completes the auto fixes, confirm the updates by taking the following steps.


- Either verify in the chat window that the AI assistant has displayed the fixed content, or confirm that the file has been updated.
- Review your open file in the editor. Changes (such as updated module names) should be reflected immediately in the code.


