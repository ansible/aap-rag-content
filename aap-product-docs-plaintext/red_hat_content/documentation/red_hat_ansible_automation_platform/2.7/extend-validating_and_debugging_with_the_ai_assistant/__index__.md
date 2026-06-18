# Validate and debug with the AI assistant

Use the AI assistant to validate playbooks in real time, identify issues before execution, and automatically apply fixes.

## Before you begin

- VS Code is open and Ansible VS Code extension is active.
- The MCP server for Red Hat Ansible Automation Platform is enabled.
- You have an Ansible playbook open in the editor (for example, `playbooks/webserver.yml`).

## About this task

First, ask the AI assistant to analyze the current playbook without modifying it. This identifies specific rule violations and potential errors.

If errors are found, `ansible_lint` has autofix functionality, enabling it to suggest changes, and, with your permission, implement those changes in your code.

## Procedure

1.  Open the playbook file in the VS Code editor.
2.  In the Copilot chat window, enter a natural language prompt such as:


```
Validate my webserver playbook to check for any issues.
```
The assistant triggers the `ansible_lint`tool in check-only mode.

The assistant displays a list of the issues it found, including Rule IDs, line numbers, and descriptions of the errors (for example, missing FQCN, or YAML formatting issues).

The assistant will ask if you would like `ansible-lint` to apply automatic fixes. You must grant the AI assistant permission to make any changes to your code.

3.  Enter "yes" or "no" depending on whether you want the assistant to apply the suggested changes.
4.  Select the option to allow or to skip to grant the assistant permission to make changes.
If you select allow, the assistant updates your code.

If you select skip, the assistant outputs a list of issues and the suggested fix for each.

## Auto-fix errors

You can prompt the AI assistant to auto-fix errors that `ansible_lint`finds.

### Procedure

1.  In the GitHub Copilot chat window, enter the following prompt:


```
Run ansible_lint on my webserver playbook and apply automatic fixes.
```
The assistant triggers the `ansible_lint`tool wiht the `fix:true` parameter.

2.  The tool then processes the file and applies corrections for issues such as:
1.  FQCN (Fully Qualified Collection Name): Converting short module names to fully qualified ones.
2.  Formatting: Correcting YAML indentation and Jinja2 expression spacing.
3.  Ordering: Fixing key ordering within tasks.

### What to do next

When the AI agent completes the auto fixes, confirm the updates by taking the following steps. 1. Either verify in the chat window that the AI has displayed the **fixed content**, or confirm that the file has been updated.
2. Review your open file in the editor. Changes (such as updated module names) should be reflected immediately in the code.

## Implement fixes

### Procedure

1.  Review the assistant's response. It should highlight sections of the code that have errors or that could be improved. The analysis might include:
1.  Identification of Anti-patterns: Flagging inefficient or insecure practices.
2.  Failure Analysis: Explaining logical errors that could cause runtime failures.
3.  Best Practice Gaps: Noting where the code deviates from the "prescriptive rule sets" derived from Ansible content best practices.
After reviewing the errors, ask the assistant to generate the specific code required to fix them.

2.  Prompt the assistant to provide a solution. For example:
1.  `How do I fix this error?`
2.  `Refactor this task to follow best practices`
The assistant generates a corrected code block, ensuring it conforms to best practice recommendations (such as correct indentation, valid parameters, and proper module usage).

### What to do next

After applying the suggested changes, verify that there are no further issues.

1. Apply the changes to your playbook.
2. (Optional) Ask the assistant to confirm the new structure. For example, you can ask `Does this look correct now?`
3. The assistant might trigger `ansible_lint `again or perform a final static check to ensure the debugging session resolved the issues.
