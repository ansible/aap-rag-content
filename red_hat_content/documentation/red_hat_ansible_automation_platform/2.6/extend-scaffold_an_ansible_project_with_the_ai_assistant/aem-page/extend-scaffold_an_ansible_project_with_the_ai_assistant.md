+++
template = "docs/aem-title.html"
title = "Scaffold an Ansible project with the AI assistant - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-scaffold_an_ansible_project_with_the_ai_assistant"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server/", "Enable AI in the Ansible VS Code extension with the MCP server"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/extend-scaffold_an_ansible_project_with_the_ai_assistant/aem-page/extend-scaffold_an_ansible_project_with_the_ai_assistant.html"
last_crumb = "Scaffold an Ansible project with the AI assistant"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Scaffold an Ansible project with the AI assistant"
oversized = "false"
page_slug = "extend-scaffold_an_ansible_project_with_the_ai_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/extend-scaffold_an_ansible_project_with_the_ai_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/extend-scaffold_an_ansible_project_with_the_ai_assistant/toc/toc.json"
type = "aem-page"
+++

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
