+++
title = "Integrate Model Context Protocol (MCP) servers through execution environment builder - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_mcp_server_integration"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_mcp_server_integration_1/", "MCP server integration"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_mcp_server_integration/aem-page/develop-ref_mcp_server_integration.html"
last_crumb = "Integrate Model Context Protocol (MCP) servers through execution environment builder"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Integrate Model Context Protocol (MCP) servers through execution environment builder"
oversized = "false"
page_slug = "develop-ref_mcp_server_integration"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_mcp_server_integration"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_mcp_server_integration/toc/toc.json"
type = "aem-page"
+++

# Integrate Model Context Protocol (MCP) servers through execution environment builder

Execution environment builder supports the optional integration of a Model Context Protocol (MCP) server. MCP servers expose automation actions to AI assistants or other cognitive services.

## Supported MCP servers

If you select an MCP server, execution environment builder automatically handles the necessary configuration files and dependencies. This Ansible automation portal feature generates execution environment definition files for building an execution environment with your selected MCP servers.

Execution environment builder currently supports the following MCP servers:

- GitHub
- AWS
  * AWS CCAPI
  * AWS CDK
  * AWS IAM
  * AWS Core
- Azure
