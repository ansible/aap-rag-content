+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-enable_the_mcp_server_through_the_vs_code_settings_menu"
title = "Enable the MCP server through the VS Code settings menu - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-enable_the_vs_code_extension_ai_assistant/", "Enable the VS Code extension AI assistant"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-enable_the_mcp_server_through_the_vs_code_settings_menu/aem-page/extend-enable_the_mcp_server_through_the_vs_code_settings_menu.html"
last_crumb = "Enable the MCP server through the VS Code settings menu"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Enable the MCP server through the VS Code settings menu"
oversized = "false"
page_slug = "extend-enable_the_mcp_server_through_the_vs_code_settings_menu"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-enable_the_mcp_server_through_the_vs_code_settings_menu"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-enable_the_mcp_server_through_the_vs_code_settings_menu/toc/toc.json"
type = "aem-page"
+++

# Enable the MCP server through the VS Code settings menu

Take the following steps to enable the MCP server through the VS Code settings menu.

## Procedure

1.  In VS Code, select the **Extensions** icon ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/vscode-extensions-icon.png) in the left menu.
2.  Find the Ansible extension and click the **Settings** wheel ![settings wheel](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/settings-icon-ansible-vscode-extension.png).
3.  Select **Settings** from the menu that appears.
4.  In the Settings window, select Extensions> (and then)Ansible> (and then)MCP Server.
5.  Click the checkbox next to **Enable the Ansible Development Tools MCP server for AI integration**. A message confirms that the MCP server is enabled.
6.  Find and select **MCP: List servers**in the command palette.
7.  Select **Ansible Development Tools MCP Server** to start the server. Verify that the server has started by looking for `Discovered 10 tools` in your VS Code output window.
