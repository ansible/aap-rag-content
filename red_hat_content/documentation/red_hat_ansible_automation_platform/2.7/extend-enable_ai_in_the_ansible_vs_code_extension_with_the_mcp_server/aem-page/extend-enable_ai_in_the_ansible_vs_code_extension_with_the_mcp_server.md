+++
title = "Enable the MCP server through the VS Code command palette - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-enable_the_vs_code_extension_ai_assistant/", "Enable the VS Code extension AI assistant"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server/aem-page/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server.html"
last_crumb = "Enable the MCP server through the VS Code command palette"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Enable the MCP server through the VS Code command palette"
oversized = "false"
page_slug = "extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server/toc/toc.json"
type = "aem-page"
+++

# Enable the MCP server through the VS Code command palette

Enable the AI assistant through the MCP server for Red Hat Ansible Automation Platform so that you can create new content with the Ansible VS Code extension.

## Before you begin

- VS Code is installed and running.
- The GitHub Copilot extension is installed, running, and enabled in Agent Mode.
- The Ansible VS Code extension is installed.

## Procedure

To enable the server through the command palette:

1.  In VS Code, click into the command palette at the top of the window, or type `Ctrl+Shift+P` or `Cmd+Shift+P`.
2.  Type and select **Ansible: Enable Ansible Development Tools MCP Server**. A message confirms that you have successfully enabled the MCP server and that it is now available for AI assistants that support MCP.
3.  In the command palette, find and select **MCP: List servers**. Find the entry for **Ansible Development Tools MCP Server**.
4.  Select **Ansible Development Tools MCP Server**to start the server. Verify that the server has started by looking for `Discovered 10 tools` in your VS Code output window.
