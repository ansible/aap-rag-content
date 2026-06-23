# Create and integrate custom MCP Servers in execution environments
## Create a custom MCP server role
### About this task

This procedure uses the AWS CloudFormation MCP Server (`awslabs.cfn-mcp-server`) as a working example.

### Procedure

1.  Create the collection directory structure and a new Ansible collection to hold your custom MCP role:


```
mkdir -p collections/ansible_collections/myorg/mcp_cfn/roles/cfn_mcp/{defaults,tasks,meta}
mkdir -p collections/ansible_collections/myorg/mcp_cfn/playbooks
touch collections/ansible_collections/myorg/mcp_cfn/galaxy.yml
touch collections/ansible_collections/myorg/mcp_cfn/README.md
touch collections/ansible_collections/myorg/mcp_cfn/LICENSE
touch collections/ansible_collections/myorg/mcp_cfn/roles/cfn_mcp/meta/main.yml
```
The directory structure will look like this:

```
collections/ansible_collections/myorg/mcp_cfn/
├── galaxy.yml
├── README.md
├── LICENSE
├── playbooks/
│   └── install_cfn_mcp.yml
└── roles/
└── cfn_mcp/
├── defaults/
│   └── main.yml
├── tasks/
│   └── main.yml
└── meta/
└── main.yml

```

2.  Define the collection metadata by creating `galaxy.yml` at the root of your collection:


```
# galaxy.yml
---
namespace: myorg
name: mcp_cfn
version: 1.0.19
readme: README.md
authors:
- Your Name
description: Custom MCP role for AWS CloudFormation MCP Server
license_file: LICENSE
tags:
- mcp
- aws
- cloudformation
dependencies:
ansible.mcp_builder: ">=1.0.3"

```
The dependencies field ensures that the `ansible.mcp_builder` collection is installed alongside your collection.

3.  Define the role registry metadata by creating `roles/cfn_mcp/defaults/main.yml ` with the registry definition for your MCP server:


```
# roles/cfn_mcp/defaults/main.yml
---
cfn_mcp_registry:
- name: "awslabs.cfn-mcp-server"
type: "stdio"
lang: "pypi"
args: []
description: "AWS CloudFormation MCP Server - manage AWS resources via Cloud Control API"

cfn_mcp_version: "1.0.19"


```
The registry variable must follow the naming convention `<role_name>_registry`. The fields are:

| Field       | Required | Description                                                       |
| ----------- | -------- | ----------------------------------------------------------------- |
| name        | Yes      | The executable name or package name of the MCP server.            |
| type        | Yes      | Transport type: stdio for local servers, http for remote servers. |
| lang        | Yes      | Installation method: pypi, npm, or go.                            |
| args        | Yes      | List of default arguments passed to the server on startup.        |
| description | Yes      | Human-readable description shown in`mcp_manage` list.             |
| package     | No       | The package name if different from name (used for npm packages).  |
The version variable must follow the naming convention `<role_name>_version`.

For Go-based servers built from source, you also need build-related variables in defaults, as follows:

```
myrole_build_repo: "https://github.com/example/my-mcp-server.git"
myrole_build_repo_branch: "main"
myrole_build_path: "example/build"

```

4.  Create the role tasks by creating `roles/cfn_mcp/tasks/main.yml`:


```
# roles/cfn_mcp/tasks/main.yml
---
- name: Include install manager tasks
ansible.builtin.include_role:
name: ansible.mcp_builder.common
tasks_from: install_manager

- name: Update MCP servers manifest
ansible.builtin.include_role:
name: ansible.mcp_builder.common
tasks_from: generate_manifest

- name: Verify CloudFormation MCP installation
ansible.builtin.command:
cmd: mcp_manage run {{ common_package_name }} --help
changed_when: false
register: cfn_mcp_verify_result
failed_when: false

- name: Display verification status (success)
ansible.builtin.debug:
msg: "CloudFormation MCP Server installed and verified successfully."
when:
- cfn_mcp_verify_result.rc is defined
- cfn_mcp_verify_result.rc == 0

- name: Display verification status (failure)
ansible.builtin.debug:
msg: "CloudFormation MCP Server verification failed. Check logs for details."
when:
- cfn_mcp_verify_result.rc is defined
- cfn_mcp_verify_result.rc != 0
```
The two `include_role` tasks are the minimum required. The `install_manager` task reads your registry metadata and installs the MCP server by using the appropriate method. The generate_manifest task adds the server to the `mcpservers.json` manifest.

The verification step is optional but recommended. It confirms the installed server is callable.

5.  Create the role metadata by creating `roles/cfn_mcp/meta/main.yml`:


```
# roles/cfn_mcp/meta/main.yml
---
galaxy_info:
role_name: "cfn_mcp"
author: "Your Name"
description: "Installs the AWS CloudFormation MCP server"
license: "GPL-3.0-or-later"
min_ansible_version: "2.16.0"
platforms:
- name: EL
versions:
- "9"
galaxy_tags:
- mcp
- aws
- cloudformation

collections:
- ansible.mcp_builder
```

6.  Create the installation playbook `playbooks/install_cfn_mcp.yml`:


```
# playbooks/install_cfn_mcp.yml
---
- name: Install custom CloudFormation MCP Server
hosts: localhost
connection: local
gather_facts: false

tasks:
- name: Ensure base functionality
ansible.builtin.include_role:
name: ansible.mcp_builder.common
public: true

- name: Install CloudFormation MCP Server
ansible.builtin.include_role:
name: myorg.mcp_cfn.cfn_mcp

- name: Fix ownership of all MCP installations for runtime user
ansible.builtin.file:
path: "{{ common_mcp_base_path }}"
state: directory
recurse: true
owner: "{{ common_runtime_user }}"
group: "{{ common_runtime_user }}"
```
Important:
The first task must include `ansible.mcp_builder.common` with `public: true`. This initializes the framework and makes shared variables (such as `common_mcp_base_path`) available to later tasks. The ownership fix at the end ensures the MCP server files are accessible by the non-root runtime user inside the execution environment.
Note:
The dev preview `ansible.mcp_builder.install_mcp` playbook only supports roles within the `ansible.mcp_builder` namespace. Custom roles in your own collection namespace require their own playbook, as shown above.

7.  Build your collection into a distributable tar file:
`cd collections/ansible_collections/myorg/mcp_cfn`
`ansible-galaxy collection build --output-path /path/to/output/`
This produces a file: `myorg-mcp_cfn-1.0.19.tar.gz. `

