+++
title = "MCP server variables - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-mcp_server_variables"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_inventory_file_vars/", "Inventory file variables"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-mcp_server_variables/aem-page/install-mcp_server_variables.html"
last_crumb = "MCP server variables"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "MCP server variables"
oversized = "false"
page_slug = "install-mcp_server_variables"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-mcp_server_variables"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-mcp_server_variables/toc/toc.json"
type = "aem-page"
+++

# MCP server variables

Inventory file variables for the MCP server for Red Hat Ansible Automation Platform.

| Variable name                   | Descriptions                                                                                                                                                                                                                                                                         | Required or Optional | Default |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | ------- |
| `mcp_allow_write_operations`    | Controls the operational access level of the MCP server. Set to `true` to grant the external AI tool read-write permissions, which authorizes the AI agent to execute job templates, manage resources, and apply infrastructure changes. Set to `false` to enforce read-only access. | Optional             | `false` |
| `mcp_ignore_certificate_errors` | Controls whether the MCP server bypasses SSL/TLS certificate validation when connecting to the Ansible Automation Platform API. Set to `true` if Ansible Automation Platform uses a self-signed certificate.                                                                         | Optional             | `false` |
| `mcp_tls_cert`                  | Path to the TLS certificate file for the MCP server.                                                                                                                                                                                                                                 | Optional             | n/a     |
| `mcp_tls_key`                   | Path to the TLS key file for the MCP server                                                                                                                                                                                                                                          | Optional             | n/a     |
| `mcp_extra_settings`            | <br>A list of additional configuration settings to pass to the MCP server. For example, set `DEFAULT_PAGE_SIZE` to control the number of results returned by list-type API responses:<br>`mcp_extra_settings: [{setting: DEFAULT_PAGE_SIZE,value:"25"}]`                             | Optional             | n/a     |
