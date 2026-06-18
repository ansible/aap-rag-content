+++
title = "Create and integrate custom MCP Servers in execution environments - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-create_and_integrate_custom_mcp_servers_in_execution_environments"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments/", "Define, create, and build execution environments"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-create_and_integrate_custom_mcp_servers_in_execution_environments/aem-page/administer-create_and_integrate_custom_mcp_servers_in_execution_environments.html"
last_crumb = "Create and integrate custom MCP Servers in execution environments"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Create and integrate custom MCP Servers in execution environments"
oversized = "false"
page_slug = "administer-create_and_integrate_custom_mcp_servers_in_execution_environments"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-create_and_integrate_custom_mcp_servers_in_execution_environments"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-create_and_integrate_custom_mcp_servers_in_execution_environments/toc/toc.json"
type = "aem-page"
+++

# Create and integrate custom MCP Servers in execution environments

Integrate custom *Model Context Protocol* (MCP) servers into execution environments using the `ansible.mcp_builder` framework to automate installation, configuration, and lifecycle management.

Note:

Individual MCP server implementations (including the reference examples for AWS, Azure, and GitHub) are Dev Preview and unsupported. Your organization is responsible for the MCP servers you choose to integrate.

**Preparing your environment**

Before you begin, ensure you have the following:

- ansible-builder : Version 3.1 or later installed on your build system. Install it using     `dnf install ansible-builder`.

- ansible-core: : Version 2.16 or later.

- Access to a base Execution Environment image, for example, ee-minimal-rhel9 from the Red Hat registry.

- The `ansible.mcp_builder` collection (version 1.0.3 or later), installed using:     `ansible-galaxy collection install ansible.mcp_builder`.

- The `ansible.mcp` collection (a required dependency), installed using:     `ansible-galaxy collection install ansible.mcp`.

- Familiarity with Ansible roles, collections, and execution environment definitions.

## Evaluate MCP servers before installation

To protect your execution environment from vulnerabilities, evaluate *Model Context protocol* (MCP) servers before installation by auditing code, pinning versions, enforcing read-only modes, and verifying permissions

Before including an MCP server in your execution environment:

- **Review the source code**: MCP servers can execute arbitrary operations on your infrastructure. Audit the server code before installing, especially for servers from community or third-party sources.

- **Pin to specific versions**: Use explicit version numbers in your registry metadata rather than latest. `cfn_mcp_version: "1.0.19"`

     This ensures reproducible builds and prevents unexpected behavior from upstream changes.

- **Use read-only mode where available**: Many MCP servers support a read-only flag that prevents mutating operations:
  

```
cfn_mcp_registry:
  - name: "awslabs.cfn-mcp-server"
    type: "stdio"
    lang: "pypi"
    args: ["--readonly"]
    description: "AWS CloudFormation MCP Server (read-only)"
```

- **Review required permissions**: Understand what permissions each MCP server needs. For example, the CloudFormation MCP server requires `cloudcontrol:*` and `cloudformation:*` IAM permissions. Grant only the minimum permissions needed.

### Understand the MCP builder framework

`ansible.mcp_builder` collection provides a reusable framework for installing MCP servers inside execution environments. Rather than manually scripting installation steps in your container build, you define a role with metadata about your MCP server, and the framework handles the rest.

To automate the installation and lifecycle management of your servers, you must understand how the `ansible.mcp_builder` framework operates.

The framework consists of three main components:

- The common role (`ansible.mcp_builder.common`) provides shared installation logic for MCP servers. Based on the language specified in your role's registry metadata, the common role automatically:
  * Installs the appropriate language runtime (Go, Node.js, or Python/uv) if not already present.
  * Downloads and installs the MCP server package from the correct source (PyPI, npm, or Git).
  * Generates a unified manifest file (`/opt/mcp/mcpservers.json`) listing all available MCP servers.
  * Creates the mcp_manage utility for listing, querying, and running installed MCP servers
- Your custom role defines metadata about the MCP server you want to install. At minimum, it includes:
  * A registry variable that specifies the server name, transport type, language, and description.
  * A tasks file that invokes the common role's `install_manager` and `generate_manifest`tasks.
- A playbook ties your custom role into the build process. This playbook is called by ansible-builder during the execution environment container build.

**Select an installation method**

| Language | Install method                                        | Example servers                                   |
| -------- | ----------------------------------------------------- | ------------------------------------------------- |
| pypi     | Installed with uv tool install from PyPI              | AWS CloudFormation MCP, AWS Core MCP, AWS IAM MCP |
| npm      | Installed with npm install from the npm registry      | Azure MCP                                         |
| go       | Built from source with go build from a Git repository | GitHub MCP                                        |

## Track configurations with the MCP servers manifest

Understand how the MCP servers manifest registers and automatically merges multiple server installations into the `/opt/mcp/mcpservers.json` file so that you can effectively track and verify your execution environment configurations.

All installed MCP servers are registered in `/opt/mcp/mcpservers.json`. This file follows the mcp.json format established by VS Code, with each server entry containing:

```
 {
    "server-name": {
        "type": "stdio",
        "command": "/opt/mcp/bin/server-name",
        "args": [],
        "description": "Description of the MCP server"
    }
}
```
For remote (HTTP-based) MCP servers, the entry uses url instead of command:

```
{
    "server-name": {
        "type": "http",
        "url": "https://remote-server:12345",
        "args": [],
        "description": "Remote MCP server"
    }
}
```
When multiple playbooks install MCP servers into the same execution environment, the manifest merges automatically. Each subsequent installation appends its entries to the existing manifest without overwriting previous entries.

## Create a custom MCP server role

Develop a custom Ansible role to automate the installation, configuration, and management of your specific custom Model Context Protocol (MCP) server for seamless integration into execution environments.

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

## Build an execution environment with your dev preview MCP server

Use the ansible-builder tool to compile and build an execution environment container image that incorporates your dev preview Model Context Protocol (MCP) server role and its dependencies.

### Procedure

1.  Create a working directory for the execution environment build and copy in the required collection tarballs:
  

```
mkdir -p ee-build/
cp myorg-mcp_cfn-1.0.19.tar.gz ee-build/
cp ansible-mcp_builder-1.0.3.tar.gz ee-build/  # if using a local copy

```

2.  Create `ee-build/requirements.yml ` listing your collections:
  

```
# requirements.yml
---
collections:
  - name: ansible.mcp_builder
    source: /build/configs/ansible-mcp_builder-1.0.3.tar.gz
    type: file
  - name: myorg.mcp_cfn
    source: /build/configs/myorg-mcp_cfn-1.0.19.tar.gz
    type: file
  - name: ansible.mcp

```
  Note:
  The `/build/configs/` path prefix is required. During the execution environment container build, ansible-builder copies files specified in additional_build_files into the build context under `_build/<dest>/`, which is then mounted at `/build/ ` inside the container.
    If your collections are published to Ansible Galaxy or automation hub, you can reference them by name instead of local paths:

```
 # requirements.yml (published collections)
---
collections:
  - name: ansible.mcp_builder
  - name: myorg.mcp_cfn
  - name: ansible.mcp
```

3.  Create `ee-build/execution-environment.yml`:
  

```
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
  - src: myorg-mcp_cfn-1.0.19.tar.gz
    dest: configs

    additional_build_steps:
  append_final: |
    RUN ansible-playbook myorg.mcp_cfn.install_cfn_mcp
```
    Where:

    `additional_build_files`: Copies your collection tarballs into the container build context so they can be referenced during the build.

    `options.package_manager_path`: Set to `/usr/bin/microdnf ` for ee-minimal-rhel9, or `/usr/bin/dnf ` for UBI9-based images.

    `additional_build_steps.append_final`: Runs your installation playbook in the final build stage, after collections are installed.

4.  Run ansible-builder to build your execution environment image:
  

```
cd ee-build/
ansible-builder build -t my-cfn-mcp-ee:latest -f execution-environment.yml -v 3
```
    The build process:

  1. Installs the base execution environment image dependencies.
  2. Installs the `ansible.mcp_builder`, `myorg.mcp_cfn` , and `ansible.mcp ` collections.
  3. Runs your installation playbook, which installs the MCP server and generates the manifest.
    A successful build produces output ending with:

```
Successfully tagged localhost/my-cfn-mcp-ee:latest
Complete! The build context can be found at: /path/to/ee-build/context

```

## Combine custom and dev preview MCP servers

Integrate both custom-developed and dev-preview Model Context Protocol (MCP) servers within a single execution environment to use comprehensive automation capabilities.

To include both dev preview MCP servers from `ansible.mcp_builder` (such as `aws_ccapi_mcp`) and your custom role in the same execution environment, chain multiple playbook calls in `additional_build_steps`:

```
additional_build_steps:
  append_final: |
    RUN ansible-playbook ansible.mcp_builder.install_mcp -e mcp_servers=aws_ccapi_mcp
    RUN ansible-playbook myorg.mcp_cfn.install_cfn_mcp

```
The manifest file merges automatically. The second playbook appends its entries to the existing `mcpservers.json` created by the first.

### Test and verify your MCP server

Verify your MCP server configuration by listing registered servers, inspecting the generated JSON manifest, and testing container connectivity with Podman.

**Testing your MCP server in the execution environment**

After building the execution environment, verify that your MCP server is correctly installed and functional.

**List the MCP servers registered in the manifest:**

`podman run --rm my-cfn-mcp-ee:latest mcp_manage list`

Expected output:

```
Available MCP servers:
  - awslabs.cfn-mcp-server (type: stdio, path: /opt/mcp/bin/awslabs.cfn-mcp-server)
```

**Verify the manifest file**

Inspect the generated manifest directly:

 `podman run --rm my-cfn-mcp-ee:latest cat /opt/mcp/mcpservers.json`

Expected output:

```
{
    "awslabs.cfn-mcp-server": {
        "args": [],
        "command": "/opt/mcp/bin/awslabs.cfn-mcp-server",
        "description": "AWS CloudFormation MCP Server - manage AWS resources via Cloud Control API",
        "type": "stdio"
    }
}

```

**Test server connectivity**

Run the MCP server with `--help` to confirm it is callable:

 `podman run --rm my-cfn-mcp-ee:latest mcp_manage run awslabs.cfn-mcp-server --help`

For servers that require credentials (such as AWS), pass environment variables:

```
podman run --rm \
  -e AWS_PROFILE=my-profile \
  -e AWS_REGION=us-east-1 \
  -v ~/.aws:/home/runner/.aws:ro \
  my-cfn-mcp-ee:latest \
  mcp_manage run awslabs.cfn-mcp-server
```

## Configure remote MCP servers

If you need to bypass local installation and dynamically choose your deployment mode at build time, configure your role to reference a remote MCP server via HTTP.

**Add a remote server to your role**

To define a remote MCP server, set the type to http in your registry metadata:

```
 # roles/cfn_mcp/defaults/main.yml (remote mode example)
---
cfn_mcp_registry:
  - name: "awslabs.cfn-mcp-server"
    type: "http"
    lang: "pypi"
    path: "https://my-mcp-host.example.com:8443/cfn"
    args: []
    description: "Remote AWS CloudFormation MCP Server"

cfn_mcp_version: "latest"
```
When type is http, the framework only registers the server in the manifest with its URL.

**Support both modes**

The GitHub MCP role in `ansible.mcp_builder` demonstrates a pattern for supporting both embedded and remote modes. You can adopt this pattern by:

1. Creating a `vars/remote.yml` file with the remote registry definition.
2. Loading it conditionally in your tasks:

```
# roles/cfn_mcp/tasks/main.yml
---
- name: Override registry for remote mode
  ansible.builtin.include_vars:
    file: remote.yml
  when: cfn_mcp_mode | default('local') == 'remote'

- name: Include install manager tasks
  ansible.builtin.include_role:
    name: ansible.mcp_builder.common
    tasks_from: install_manager

- name: Update MCP servers manifest
  ansible.builtin.include_role:
    name: ansible.mcp_builder.common
    tasks_from: generate_manifest

```
You can then select the mode when building the execution environment:

```
additional_build_steps:
  append_final: |
    RUN ansible-playbook myorg.mcp_cfn.install_cfn_mcp -e cfn_mcp_mode=remote

```

## Secure your custom MCP servers

Apply essential security configurations and best practices to safeguard your custom MCP servers, manage credentials securely, and harden your execution environments.

**Managing credentials and secrets**

MCP servers frequently require credentials to interact with cloud providers or external services. Follow these practices:

- **Never embed credentials into the execution environment image**: Credentials embedded during build time persist in the container image layers and can be extracted. Instead, pass credentials at runtime using environment variables or mounted files.

- **Use runtime environment variables**: Pass credentials when launching the execution environment:

```
podman run --rm \
   -e AWS_PROFILE=my-profile \
   -e GITHUB_PERSONAL_ACCESS_TOKEN="$GITHUB_TOKEN" \
   my-mcp-ee:latest …

```

-  **Mount credential files as read-only**: For providers that use credential files (such as AWS), mount them read-only:     ` -v ~/.aws:/home/runner/.aws:ro`

- **In Ansible Automation Platform, use credential types**: When running MCP-enabled execution environments through Ansible Automation Platform, configure credentials through the automation controller credential management system rather than embedding them in playbooks or job templates.

## Use your MCP-enabled execution environment in Ansible Automation Platform

To secure your infrastructure and ensure predictable execution, evaluate MCP servers before installation by auditing code, pinning versions, enabling read-only modes, and enforcing least-privilege permissions.

After building and testing your execution environment locally, you can use it in Ansible Automation Platform.

**Push the image to a registry**

Tag and push your execution environment image to a container registry accessible by your Ansible Automation Platform instance:

```
podman tag my-cfn-mcp-ee:latest registry.example.com/ee/my-cfn-mcp-ee:latest
podman push registry.example.com/ee/my-cfn-mcp-ee:latest

```
If you are using the Private Automation Hub included with Ansible Automation Platform, push to its registry.

### Add the execution environment to Ansible Automation Platform

To execute automation tasks using your custom MCP server, add its execution environment to Ansible Automation Platform by registering the container image path and secure credentials in the administration settings.

#### Procedure

1.  In the navigation panel, select **Automation execution > Administration > Execution Environments**.
2.  Click **Add**.
3.  Enter the image path (for example, `registry.example.com/ee/my-cfn-mcp-ee:latest`).
4.  Configure registry credentials if required.
5.  Save the execution environment.

### Assign to a Job Template

Configure your job template with an MCP-enabled execution environment and credentials to ensure your automation jobs execute correctly.

#### Procedure

1.  In the navigation panel, select `Automation execution > Templates`.
2.  Edit or create a **Job Template**.
3.  In the **Execution Environment** field, select your MCP-enabled execution environment.
4.  Configure any required credentials for the MCP server (such as AWS credentials).
5.  Save and launch the template.

## Debug common issues

Diagnose and resolve initialization failures when your MCP server is unlisted or fails to execute. By systematically verifying build logs, installed files, and manifests, you can identify the root cause of deployment errors and successfully run your server.

### Procedure

1.  Check the build log: Look for errors during the ansible-playbook step of the build output. Common issues include missing dependencies or network access failures during package download.
2.  Inspect the installed files: Verify the binary or script is present:
  `podman run --rm my-cfn-mcp-ee:latest ls -la /opt/mcp/bin/`

3.  Check the manifest separately from the binary: If `mcp_manage` list shows the server but `mcp_manage` run fails, the manifest was generated but the package installation may have failed silently.
4.  Run the server directly: Bypass `mcp_manage` and call the server binary directly to see raw error output:
   ` podman run --rm my-cfn-mcp-ee:latest /opt/mcp/bin/awslabs.cfn-mcp-server --help`

**Troubleshoot build and runtime errors**

Diagnose and resolve common issues encountered when building, configuring, and integrating custom or built-in Model Context Protocol (MCP) servers within your execution environments.

**Build failures**

| Error                                    | Reason                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Unable to find collection artifact file. | This error occurs when the collection tarball path in requirements.yml does not match the path inside the container. Ensure:   The tarball is listed in `additional_build_files` with a dest value.The source path in `requirements.yml` uses `/build/configs/<filename>` (not the host filesystem path).                                        |
| Package download fails during build      | The execution environment build environment requires network access to download packages from PyPI, npm, or Git repositories. If building behind a proxy, configure proxy settings in your container build environment. If building in an air-gapped environment, you must pre-download packages and include them using`additional_build_files`. |
| Go build fails with "module not found"   | For Go-based MCP servers, ensure the`build_repo` URL and`build_repo_branch` are correct and accessible. The framework clones the repository and runs go mod download before building.                                                                                                                                                            |


**Runtime failures**

| Error                                   | Reason                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mcp_manage`: command not found         | <br>The `mcp_manage` script is installed at `/opt/mcp/mcp_manage` with a symlink at `/usr/local/bin/mcp_manage`. If it is missing, the common role's `generate_management` task may have been skipped.<br>Ensure your playbook includes `ansible.mcp_builder.common` with `public: true` as the first task                                                                         |
| MCP server fails with permission errors | <br>The execution environment runs as user 1000 (non-root). Ensure your playbook includes the ownership fix task:    ``` - name: Fix ownership of all MCP installations for runtime user   ansible.builtin.file:     path: "{{ common_mcp_base_path }}"     state: directory     recurse: true     owner: "{{ common_runtime_user }}"     group: "{{ common_runtime_user }}"   ``` |
| Server listed but not executing         | <br>If `mcp_manage` list shows your server but `mcp_manage` run fails, check:   <br>The binary exists at the path shown in the manifest.Required runtime dependencies are present (for example, `Node.js` for npm-based servers).Environment variables required by the server are passed at container runtime.                                                                     |


**Variable validation errors**

| Error                     | Reason                                                                                                                                                                                                                                                                                        |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Missing registry variable | The common role expects a registry variable named`<role_name>_registry`. Ensure your`defaults/main.yml` follows the naming convention. For a role named x`defaults/main.yml`, the variable must be`cfn_mcp_registry`.                                                                         |
| Invalid language type     | The lang field in the registry must be one of: pypi, npm, or go. Any other value causes the install manager to skip installation. However,`generate_manifest.yml` will fail with`'dict object' has no attribute 'path' (rc=2)` because it expects a variable the skipped installer never set. |


**Understanding support boundaries**

Red Hat provides and supports the following components:

- The `ansible.mcp_builder` collection, including the common role and its installation framework.
- The ansible-builder tool for creating execution environments.
- The execution environment runtime within Ansible Automation Platform.


The following are the customer's responsibility:

- Individual MCP server implementations. Red Hat does not support any specific MCP server, including the reference examples (AWS, Azure, GitHub) provided in the `ansible.mcp_builder` collection. These examples are Dev Preview.
- Custom MCP roles and collections. Your organization owns the creation, testing, and maintenance of custom roles.
- MCP server security. Your organization is responsible for evaluating, auditing, and securing the MCP servers you deploy.
- MCP server credentials and access controls. Configuring and securing access to external services is your responsibility.


If you encounter issues:

- For problems with ansible-builder, the common role, or the execution environment build process, contact Red Hat support.
- For problems with a specific MCP server, contact the MCP server vendor or community.
