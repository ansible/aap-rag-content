+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_custom_mcp_server_settings"
template = "docs/aem-title.html"
title = "Configure custom MCP server settings - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_custom_mcp_server_settings/aem-page/install-configure_custom_mcp_server_settings.html"
last_crumb = "Configure custom MCP server settings"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure custom MCP server settings"
oversized = "false"
page_slug = "install-configure_custom_mcp_server_settings"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-configure_custom_mcp_server_settings"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_custom_mcp_server_settings/toc/toc.json"
type = "aem-page"
+++

# Configure custom MCP server settings

The `extra_settings` variable allows you to pass a list of custom setting and value pairs to the MCP server for Red Hat Ansible Automation Platform within the `mcp` section of the `AnsibleAutomationPlatform` custom resource.

## Before you begin

- You have installed the Ansible Automation Platform Operator.
- You have deployed the MCP server for Red Hat Ansible Automation Platform on your operator-based installation.

## Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Go to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select All Instances and go to your Ansible Automation Platform instance.
5.  Click the ⋮ icon and then select Edit Ansible Automation Platform.
6.  In the YAML view, locate the `spec.mcp` section.
7.  Add the `extra_settings`list under the existing `mcp`section. The following example configures the default page size for list-type API responses:
  

```
spec:
  mcp:
    disabled:false
    allow_write_operations:false
    extra_settings:
      - setting:DEFAULT_PAGE_SIZE value:"25"
```

8.  Click Save.

## What to do next

The MCP server pod restarts with the updated configuration. To verify the new setting, query a list-type API endpoint through your AI agent and confirm that the response returns the expected number of results per page.
