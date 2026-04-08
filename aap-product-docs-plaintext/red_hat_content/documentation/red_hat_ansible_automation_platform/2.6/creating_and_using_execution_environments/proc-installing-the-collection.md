# 6. Using automation execution environments with Red Hat Model Context Protocol (MCP) servers
## 6.2. Installing the MCP Builder Collection




Install or upgrade the `ansible.mcp_builder` collection through the Ansible Galaxy command-line tool or a requirements file. Use the collection to deploy and manage MCP servers within an execution environment.

**Prequisites**

- ansible-core: 2.18.0+
- Python: 3.11+


**Collections**

-  `    ansible.mcp` for execution of MCP servers.


**External dependencies**

- ansible-builder for building execution environments
- podman or docker for container runtime
- Fedora/RHEL base image for use in execution environment builds


**Procedure**

1. Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

`    ansible-galaxy collection install ansible.mcp_builder`


1. You can also include it in a `    requirements.yml` file and install it with `    ansible-galaxy collection install -r requirements.yml` , using the format:


```
collections:     	 - name: ansible.mcp_builder
```


1. To upgrade the collection to the latest available version, run:

`    ansible-galaxy collection install ansible.mcp_builder --upgrade`


1. You can also install a specific version of the collection. Use the following syntax to install version 1.0.0:

`    ansible-galaxy collection install ansible.mcp_builder:==1.0.0`

See [Using Ansible collections](https://docs.ansible.com/projects/ansible/devel/collections_guide/index.html) for more details.


1. After installation, the collection provides:

MCP Server Manifest ( `    /opt/mcp/mcpservers.json` ) - JSON file describing all installed MCP servers


1. Servers are installed into the execution environment using the ansible. `    mcp_builder.install_mcp` playbook.
1. To select which servers to install, their exact role names, for example, `    github_mcp` , are passed using the `    -e mcp_servers` variable during the build.
1. The `    ansible.mcp_builder.common` role sets up the generic build environment, detects dependencies, and handles the installation of servers from various sources, including Go, npm, and PyPI.


