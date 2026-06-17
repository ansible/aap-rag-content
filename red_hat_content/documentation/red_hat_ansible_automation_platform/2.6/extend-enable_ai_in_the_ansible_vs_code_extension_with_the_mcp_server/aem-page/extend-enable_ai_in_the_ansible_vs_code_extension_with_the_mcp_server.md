+++
title = "Enable AI in the Ansible VS Code extension with the MCP server - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server/", "Enable AI in the Ansible VS Code extension with the MCP server"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server/aem-page/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server.html"
last_crumb = "Enable AI in the Ansible VS Code extension with the MCP server"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Enable AI in the Ansible VS Code extension with the MCP server"
oversized = "false"
page_slug = "extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/extend-enable_ai_in_the_ansible_vs_code_extension_with_the_mcp_server/toc/toc.json"
type = "aem-page"
+++

# Enable AI in the Ansible VS Code extension with the MCP server

Enable the AI assistant through the MCP server for Red Hat Ansible Automation Platform so that you can create new content with the Ansible VS Code extension.

## Before you begin

- VS Code is installed and running.
- The GitHub Copilot extension is installed, running, and enabled in Agent Mode.
- The Ansible VS Code extension is installed.

## About this task

As an automation developer, you can enable the MCP (Model context protocol) server through the Ansible VS Code extension. Doing so empowers Ansible devtools to give customized suggestions tuned specifically to your working environment.

You can enable the MCP server for Red Hat Ansible Automation Platform through the **command palette** or the **Settings menu** in VS Code.

## Procedure

To enable the server through the command palette:

1.  In VS Code, click into the command palette at the top of the window, or type `Ctrl+Shift+P` or `Cmd+Shift+P`.
2.  Type and select **Ansible: Enable Ansible Development Tools MCP Server**. A message confirms that you have successfully enabled the MCP server and that it is now available for AI assistants that support MCP.
3.  In the command palette, find and select **MCP: List servers**. Find the entry for **Ansible Development Tools MCP Server**.
4.  Select **Ansible Development Tools MCP Server**to start the server. Verify that the server has started by looking for `Discovered 10 tools` in your VS Code output window.

## Enable the MCP server through the settings menu

Take the following steps to enable the MCP server through the VS Code settings menu.

### Procedure

1.  In VS Code, select the **Extensions** icon ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/vscode-extensions-icon.png) in the left menu.
2.  Find the Ansible extension and click the **Settings** wheel ![settings wheel](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/settings-icon-ansible-vscode-extension.png).
3.  Select **Settings** from the menu that appears.
4.  In the Settings window, select Extensions> (and then)Ansible> (and then)MCP Server.
5.  Click the checkbox next to **Enable the Ansible Development Tools MCP server for AI integration**. A message confirms that the MCP server is enabled.
6.  Find and select **MCP: List servers**in the command palette.
7.  Select **Ansible Development Tools MCP Server** to start the server. Verify that the server has started by looking for `Discovered 10 tools` in your VS Code output window.

### Disable the server

You can disable the MCP server from the VS Code command palette or the settings menu.

#### Procedure

-  To disable the server from the command palette, find and select **Disable Ansible Development Tools MCP Server**.
-  To disable the server from the settings menu, click the **Settings** wheel ![settings wheel](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/settings-icon-ansible-vscode-extension.png)in the Ansible VS Code extension, navigate to Extensions> (and then)Ansible> (and then)MCP Server and un-check the checkbox next to **Enable the Ansible MCP server for AI integration**.
