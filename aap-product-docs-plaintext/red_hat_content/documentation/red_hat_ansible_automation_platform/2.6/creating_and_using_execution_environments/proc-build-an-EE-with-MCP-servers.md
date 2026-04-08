# 6. Using automation execution environments with Red Hat Model Context Protocol (MCP) servers
## 6.3. Building an execution environment with MCP servers




The ansible.mcp_builder collection is designed to run as a step in building an execution environment, allowing you to deploy multiple MCP servers from various sources (npm packages, PyPI packages, and compiled Go binaries) in a single environment.

**Procedure**

1. The collection must be listed as a galaxy dependency in the `    execution-environment.yml` file, either directly listed or passed using a `    requirements.yml` file.
1. To select MCP servers to install, use the `    -e` flag with the `    mcp_servers` variable. Servers are selected by their exact role name, for example, `    github_mcp` .

**Example `    execution-environment.yml` configuration** :


```
version: 3        images:      base_image:        name: ansible-automation-platform-25/ee-minimal-rhel9:latest    dependencies:      galaxy: requirements.yml        options:      package_manager_path: /usr/bin/microdnf        additional_build_steps:      append_final: |        RUN ansible-playbook ansible.mcp_builder.install_mcp -e mcp_servers=github_mcp -e github_mcp_mode=remote
```


1. Run this command inside the directory containing the execution environment definition file:

`    ansible-builder build --tag my-mcp-ee:latest`

This approach allows you to create custom execution environments with only the MCP servers you need.




