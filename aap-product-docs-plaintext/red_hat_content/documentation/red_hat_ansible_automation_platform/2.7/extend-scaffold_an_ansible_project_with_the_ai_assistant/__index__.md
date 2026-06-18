# Scaffold an Ansible project with the AI assistant

Use the MCP server for Red Hat Ansible Automation Platform through the Ansible VS Code extension to generate a new project structure, and to create and scaffold new content such as playbooks or collections.

## Before you begin

- The Ansible VS Code extension is installed, running, and enabled in Agent Mode.
- The MCP server for Red Hat Ansible Automation Platform is enabled in the Ansible VS Code extension.
- Ansible Development Tools are installed.

## About this task

Use the AI assistant to ensure that your project aligns with best practices and organizational standards without manually creating boilerplate code. You can also generate and view Ansible best practices and coding guidelines.

## Procedure

1.  Open the Copilot chat window by clicking the GitHub Copilot icon in the VS Code sidebar.
2.  Enter a prompt requesting Ansible best practices. For example:


```
Show me Ansible best practices and coding guidelines so that I can write high-quality playbooks.
```
This triggers the `ansible_content_best_practices `tool, which will display the guidelines for you to read within the editor.

3.  Enter a prompt requesting The Zen of Ansible. For example:


```
Show me The Zen of Ansible.
```
This triggers the `zen_of_ansible` tool, which will list Zen of Ansible principles for you to read within the editor.

## Create the project structure

Enter a prompt in natural language to trigger the project creation tool. When prompted, `ansible-creator` works in the background to generate the directory structure.

### Procedure

1.  In the Copilot chat window, enter a prompt specifying the project name and type. For example:


```
Create a new Ansible playbook project called 'webserver-deployment'.
```
This triggers the `create_ansible_projects`tool.

The extension executes `ansible-creator init playbook`and generates the content.

2.  Verify that the generated structure is consistent with the standard layout by navigating to the VS Code Explorer view and locating the new directory (`webserver-deployment`)
3.  Confirm the presence of standard artifacts like:
1.  Initial playbook files.
2.  Recommended configuration files (such as `ansible.cfg` or `inventory`).

### Scaffold content

If you need to generate specific content within that project using specific templates (such as a playbook or execution environment), you can continue the conversation.

#### Procedure

-  For a playbook project, enter the following prompt:


```
Following best practices, help me create a playbook called 'webserver'.
```

-  For an execution environment, enter the following prompt:


```
Create an execution environment definition file using Fedora minimal as the base.
```
