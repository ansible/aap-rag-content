# 6. Create and integrate custom MCP Servers in execution environments
## 6.5. Build an execution environment with your custom MCP server

Use the ansible-builder tool to compile and build an execution environment container image that incorporates your custom Model Context Protocol (MCP) server role and its dependencies.

**Procedure**

1. Create a working directory for the execution environment build and copy in the required collection tarballs:

`mkdir -p ee-build/``cp myorg-mcp_cfn-1.0.0.tar.gz ee-build/``cp ansible-mcp_builder-1.0.3.tar.gz ee-build/ # if using a local copy`

2. Create `ee-build/requirements.yml` listing your collections:

# requirements.yml
---
collections:
- name: ansible.mcp_builder
source: /build/configs/ansible-mcp_builder-1.0.3.tar.gz
type: file
- name: myorg.mcp_cfn
source: /build/configs/myorg-mcp_cfn-1.0.0.tar.gz
type: file
- name: ansible.mcp


Note
The `/build/configs/` path prefix is required. During the execution environment container build, ansible-builder copies files specified in `additional_build_files` into the build context under `_build/<dest>/`, which is then mounted at `/build/` inside the container.

If your collections are published to Ansible Galaxy or automation hub, you can reference them by name instead of local paths:

# requirements.yml (published collections)
---
collections:
- name: ansible.mcp_builder
- name: myorg.mcp_cfn
- name: ansible.mcp

3. Create `ee-build/execution-environment.yml` with this content:

# execution-environment.yml
---
version: 3

images:
base_image:
name: registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel9:latest

dependencies:
galaxy: requirements.yml

options:
package_manager_path: /usr/bin/microdnf

additional_build_files:
- src: ansible-mcp_builder-1.0.3.tar.gz
dest: configs
- src: myorg-mcp_cfn-1.0.0.tar.gz
dest: configs

additional_build_steps:
append_final: |
RUN ansible-playbook myorg.mcp_cfn.install_cfn_mcp

Where


- `additional_build_files`: Copies your collection tarballs into the container build context so they can be referenced during the build.
- `additional_build_steps.append_final`: Runs your installation playbook in the final build stage, after collections are installed.
- `options.package_manager_path`: Set to `/usr/bin/microdnf` for `ee-minimal-rhel9`, or `/usr/bin/dnf` for UBI9-based images.

4. Run ansible-builder to build your execution environment image:

`cd ee-build/``ansible-builder build -t my-mcp-ee:latest -f execution-environment.yml -v 3`

The build process will:


1. Install the base execution environment image dependencies.

2. Install the `ansible.mcp_builder`, `myorg.mcp_cfn`, and `ansible.mcp` collections.

3. Run your installation playbook, which installs the MCP server and generates the manifest.

A successful build produces output ending with:

Successfully tagged localhost/my-cfn-mcp-ee:latest
Complete! The build context can be found at: /path/to/ee-build/context

