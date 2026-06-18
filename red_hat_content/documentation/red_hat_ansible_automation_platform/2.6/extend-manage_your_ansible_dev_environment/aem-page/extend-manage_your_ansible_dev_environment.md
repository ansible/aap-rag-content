+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-manage_your_ansible_dev_environment"
title = "Manage your Ansible dev environment - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server/", "Enable AI in the Ansible VS Code extension with the MCP server"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/extend-manage_your_ansible_dev_environment/aem-page/extend-manage_your_ansible_dev_environment.html"
last_crumb = "Manage your Ansible dev environment"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Manage your Ansible dev environment"
oversized = "false"
page_slug = "extend-manage_your_ansible_dev_environment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/extend-manage_your_ansible_dev_environment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/extend-manage_your_ansible_dev_environment/toc/toc.json"
type = "aem-page"
+++

# Manage your Ansible dev environment

Use the AI assistant to help you understand what is happening in your own environment without having to leave the editor.

## Before you begin

- VS Code is open with the Ansible VS Code Extension active.
- The Ansible MCP Server is enabled.
- GitHub Copilot is active.

## About this task

You can ask the AI assistant to list the automations (collections and tools) available in your local environment. This way, you can verify what tools are available to you before starting development.

## Procedure

1.  In the GitHub Copilot chat window, enter a natural language prompt to check the environment. For example:
  1.  `Check my Ansible environment and tell me what's installed.`
  2.  `What collections are installed?`
  The AI assistant triggers the `ade_environment_info` tool.

2.  Review the output, which displays:
  1.  Ansible Version: The core version installed.
  2.  Ansible Lint Version: Confirmation of the linting tool status.
  3.  Installed Collections: A list of collections available for use (such as `amazon.aws`, `ansible.posix`).
  4.  Python Environment: Details about the active virtual environment.

## Understand your automation with the AI assistant

If you are working with an existing playbook and need to understand its components, you can ask the assistant to analyze the file.

### Procedure

1.  Open the playbook you want to investigate in the VS Code editor.
2.  In the Copilot chat window, enter a prompt instructing the AI agent to analyze dependencies. For example:
  

```
Analyze my web server playbook and tell me which Ansible collections are being used.
```
  The assistant then analyzes the content and identifies:
  - Collections: Which collections are required (for example,` ansible.builtin`, `community.general`).
  - Modules: Specific modules utilized within the tasks.
  - FQCN Compliance: The assistant verifies if the automations are referenced using their Fully Qualified Collection Names (FQCN)

### List available Ansible MCP tools

To discover other automation tasks the assistant can perform with the MCP server, you can query the toolset directly.

#### Procedure

1.  In the GitHub Copilot chat window, enter the following prompt:
  

```
What Ansible tools are available through MCP?
```
The assistant then triggers the `list_available_tools` function.

2.  The assistant returns a list of tools, including:
  1.  `zen_of_ansible`
  2.  `ansible_content_best_practices`
  3.  `list_available_tools`
  4.  `ansible_lint`
  5.  `ansible_navigator`
  6.  `ade_environment_info`
  7.  `ade_setup_environment`
  8.  `adt_check_env`
  9.  `create_ansible_projects`
  10.  `define_and_build_execution_env`
