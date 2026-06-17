+++
title = "MCP server integration - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_mcp_server_integration"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_devtools_intro/", "Create, test, and deploy automation content with ansible-dev-tools"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_mcp_server_integration/aem-page/develop-con_mcp_server_integration.html"
last_crumb = "MCP server integration"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "MCP server integration"
oversized = "false"
page_slug = "develop-con_mcp_server_integration"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-con_mcp_server_integration"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_mcp_server_integration/toc/toc.json"
type = "aem-page"
+++

# MCP server integration

An MCP server implements Model Context Protocol (MCP) for a specific backend such as a REST API, various services, databases, and other external systems. The MCP server exposes its operations as discoverable tools that AI agents or large language models (LLMs) can call.

MCP servers are integrated into execution environments (EEs) using a robust Ansible plugin framework. This setup allows Ansible playbooks to call MCP servers directly. A crucial design strategy is the ephemeral nature of these servers, meaning they exist only for the duration of the job execution.

The core requirement for enabling MCP support involves securely installing the required MCP server software into the execution environment during the build process, typically using the `ansible-builder` command.

You can configure MCP servers in two ways:

- **For embedded (local) MCP servers**: The EE image must explicitly include the MCP server binaries or libraries installed on the image path. This setup enables the execution environment to discover and start the specific embedded server required for the job.
- **For remote (external) MCP servers**: The EE build process facilitates defining remote connection details in a manifest file contained within the EE. This manifest informs the core MCP collection plugin on how to connect, typically pointing to a specific remote URL using an HTTP connection.


## Supported MCP servers

To use MCP servers, you must specify the required MCP support information in your EE definitions. This configuration pulls the necessary dependencies into your EE YAML file. The following MCP servers are currently targeted for support:

- **AWS Core MCP**: Serves as a starting point for working across Amazon MCPs.
- **AWS Cloud Control API MCP**: Provides the execution layer for AWS resource management.
- **GitHub MCP**: Used for testing and validation, often targeting remote server connections.

## Dependencies

Dependencies are incorporated into the EE YAML when you create the definition files. For example, the demonstration jobs target scenarios like AWS EC2 and VPC management, GitHub repository, and pull request operations.
