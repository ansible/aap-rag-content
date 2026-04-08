# 6. Using automation execution environments with Red Hat Model Context Protocol (MCP) servers
## 6.1. MCP Builder Collection




The `mcp_builder_collection` is a collection of Ansible roles and playbooks designed to facilitate the integration and management of Model Context Protocol (MCP) servers within Ansible execution environments built using Ansible Builder.

This collection provides tools to streamline the process of configuring MCP servers, ensuring that they are properly set up to interact with Large Language Models (LLMs) and other AI systems.

Roles

| Name | Description |
| --- | --- |
|  `ansible.mcp_builder.common` | Sets up a generic MCP build environment with automatic dependency detection and installs MCP servers from multiple sources (Go, npm, PyPI) |
|  `ansible.mcp_builder.aws_ccapi_mcp` | Installs the [AWS Cloud Control MCP server](https://awslabs.github.io/mcp/servers/ccapi-mcp-server) from PyPI |
|  `ansible.mcp_builder.aws_cdk_mcp` | Installs the [AWS CDK MCP server](https://awslabs.github.io/mcp/servers/cdk-mcp-server) from PyPI |
|  `ansible.mcp_builder.aws_core_mcp` | Installs the AWS [Core MCP server](https://awslabs.github.io/mcp/servers/core-mcp-server) from PyPI with dynamic proxy server strategy |
|  `ansible.mcp_builder.aws_iam_mcp` | Installs the AWS [IAM MCP server](https://awslabs.github.io/mcp/servers/core-mcp-server) from PyPI |
|  `ansible.mcp_builder.azure_mcp` | Installs the [Azure MCP server](https://awslabs.github.io/mcp/servers/azure-mcp-server) from npm to interact with Azure resources |
|  `ansible.mcp_builder.github_mcp` | Installs the [GitHub MCP server](https://github.com/github/github-mcp-server) with support for local (build from source) and remote modes |


**Playbooks**

| Name | Description |
| --- | --- |
|  `ansible.mcp_builder.install_mcp` | Installs selected MCP servers |


