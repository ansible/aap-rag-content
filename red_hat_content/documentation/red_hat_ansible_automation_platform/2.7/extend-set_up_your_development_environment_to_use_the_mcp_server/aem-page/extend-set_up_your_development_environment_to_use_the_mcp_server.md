+++
title = "Set up your development environment to use the MCP server - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-set_up_your_development_environment_to_use_the_mcp_server"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server/", "Enable AI in the Ansible VS Code extension with the MCP server"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-set_up_your_development_environment_to_use_the_mcp_server/aem-page/extend-set_up_your_development_environment_to_use_the_mcp_server.html"
last_crumb = "Set up your development environment to use the MCP server"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Set up your development environment to use the MCP server"
oversized = "false"
page_slug = "extend-set_up_your_development_environment_to_use_the_mcp_server"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-set_up_your_development_environment_to_use_the_mcp_server"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-set_up_your_development_environment_to_use_the_mcp_server/toc/toc.json"
type = "aem-page"
+++

# Set up your development environment to use the MCP server

Use the Ansible AI assistant to query your environment to understand what tools you have installed, and to install `ansible-dev-tools` and set up your development environment.

## Before you begin

The latest version of Python is installed.

## About this task

First, run environment diagnostics. Use the AI assistant to assess your local environment to understand what tools, versions, and collections are currently installed.

## Procedure

1.  Open GitHub Copilot Chat.
2.  Enter a natural language prompt such as:
  1.  `Check my Ansible environment and tell me what's installed.`
  2.  `What collections are installed?`
  The assistant will trigger the `ade_environment_info` tool.

3.  Review the output, which typically includes:
  1.  Workspace path and Python version
  2.  Virtual Environment status
  3.  A list of Installed Collections.
  4.  The installation status of Ansible Development Tools (ADT).
