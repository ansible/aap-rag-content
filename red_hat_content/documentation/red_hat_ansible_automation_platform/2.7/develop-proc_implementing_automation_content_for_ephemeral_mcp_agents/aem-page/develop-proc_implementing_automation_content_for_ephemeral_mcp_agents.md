+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_implementing_automation_content_for_ephemeral_mcp_agents"
title = "Implement automation content for ephemeral MCP agents - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_devtools_intro/", "Create, test, and deploy automation content with ansible-dev-tools"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_implementing_automation_content_for_ephemeral_mcp_agents/aem-page/develop-proc_implementing_automation_content_for_ephemeral_mcp_agents.html"
last_crumb = "Implement automation content for ephemeral MCP agents"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Implement automation content for ephemeral MCP agents"
oversized = "false"
page_slug = "develop-proc_implementing_automation_content_for_ephemeral_mcp_agents"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_implementing_automation_content_for_ephemeral_mcp_agents"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_implementing_automation_content_for_ephemeral_mcp_agents/toc/toc.json"
type = "aem-page"
+++

# Implement automation content for ephemeral MCP agents

Create an Ansible playbook that uses the execution environment (EE) setup so that ephemeral MCP servers are provisioned during Ansible Automation Platform controller job creation.

## Before you begin

- You have securely stored all access credentials necessary for MCP plugin use exclusively within the Ansible Automation Platform credential store.
- The execution environment (EE) image is configured to include the necessary MCP server component, which is typically accomplished by selecting a collection with specialized roles during the EE build process.

## About this task

You can safely use AI as an operational assistant, which can take assigned actions in your enterprise platform. Ephemeral MCP servers are provisioned only for the duration of the job execution.

## Procedure

1.  Create the `execution-environment.yml` definition file, which specifies a step to install the MCP server components:
  

```yaml
---
version: 3

    images:
  base_image:
    name: ansible-automation-platform-26/ee-minimal-rhel9:latest
dependencies:
  galaxy: requirements.yml

    options:
  package_manager_path: /usr/bin/microdnf

    additional_build_steps:
  append_final: |
    RUN ansible-playbook ansible.mcp_builder.install_mcp -e mcp_servers=github_mcp -e github_mcp_mode=remote
```
    The example definition file specifies the required MCP server, so that the necessary dependencies are pulled into the file.

    During the EE build process the MCP server software is installed into the EE.

  - For embedded servers, include the MCP server binaries or libraries explicitly on the EE image path.
  - For remote servers, define remote connection details in a manifest file within the EE.

2.  Write custom Ansible content:
  

```yaml
---
- name: Example Github MCP server interaction
  hosts: github_mcp
  tasks:
    - name: Create a Github repository
      ansible.mcp.run_tool:
        name: create_repository
        args:
          name: my-github-repository
          autoInit: true
```
    The playbook syntax for invoking MCP plugins is intuitive and aligns with existing Ansible module patterns.

   Important:
      You must configure the `ansible.mcp.mcp` connection plugin to use the `ansible.mcp` collection. For example, set the `ansible_mcp_server_name` custom-defined configuration variable to the name of a server in the `mcpserver.json` manifest file.

    Your playbook might use inventory variables, such as setting the connection plugin to `ansible_connection: ansible.mcp.mcp`, along with required timeout values like `ansible_connect_timeout: 30` and `ansible_command_timeout: 30`.

3.  Create and configure credentials in Ansible Automation Platform:
      The required credentials vary based on which MCP server you are using. For example, the GitHub MCP server requires a GitHub Personal Access Token, which you set in the `MCP_BEARER_TOKEN` environment variable.

  1.  Create a custom credential type in Ansible Automation Platform.
  
![Creating a custom credential type in Ansible Automation Platform](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/mcp-agents-create-credential-type.png)  

  2.  Create a new credential and use the custom credential type you created.
  
![Creating a credential with the custom credential type](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/mcp-agents-create-credential.png)  
        The examples show how to set up the required credential structures in the Ansible Automation Platform credential store. This includes defining the relevant fields and the injector configuration needed to pass the secret as an environment variable (for example, `MCP_BEARER_TOKEN: "{{ token }}"`).

4.  Create a new host and configure the connection variables.
  
![Creating a host with MCP connection variables](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/mcp-agents-create-host.png)  

5.  Launch the relevant job in the Ansible Automation Platform controller GUI.

## Results

The MCP server is provisioned ephemerally for the duration of the job execution. Upon job completion or failure, no residual data, services, or security artifacts remain.

## What to do next

**Troubleshooting**

To manage the health of the MCP servers, the Ansible Automation Platform environment emphasizes governance and auditability, allowing you to trace workflow success and failures.

All MCP plugin invocations and credential usage events are logged and auditable through Ansible Automation Platform audit trail systems, including the job ID, user, and timestamp, along with Ansible eventstream data. This tracking supports governance requirements for enterprise compliance.

The system ensures that secrets are never hardcoded into playbooks or visible in execution logs; they are masked automatically. This robust auditing assists in identifying security issues or operational problems during task execution.
