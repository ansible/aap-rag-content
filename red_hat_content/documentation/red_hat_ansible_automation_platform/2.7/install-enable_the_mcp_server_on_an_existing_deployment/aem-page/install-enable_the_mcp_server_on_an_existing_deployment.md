+++
template = "docs/aem-title.html"
title = "Enable the MCP server on an existing OCP deployment - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-enable_the_mcp_server_on_an_existing_deployment"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-enable_the_mcp_server_on_an_existing_deployment/aem-page/install-enable_the_mcp_server_on_an_existing_deployment.html"
last_crumb = "Enable the MCP server on an existing OCP deployment"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Enable the MCP server on an existing OCP deployment"
oversized = "false"
page_slug = "install-enable_the_mcp_server_on_an_existing_deployment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-enable_the_mcp_server_on_an_existing_deployment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-enable_the_mcp_server_on_an_existing_deployment/toc/toc.json"
type = "aem-page"
+++

# Enable the MCP server on an existing OCP deployment

You can enable the MCP server on an existing Ansible Automation Platform deployment by editing the `AnsibleAutomationPlatform` custom resource.

## Before you begin

- You have installed the Ansible Automation Platform Operator.
- You have a deployed `AnsibleAutomationPlatform` instance.

## Procedure

1. In the OpenShift Container Platform web console, navigate to Operators> (and then)Installed Operators.
2. Select the Ansible Automation Platform Operator.
3. On the All Instances tab, locate your `AnsibleAutomationPlatform` instance, click the options menu, and select Edit AnsibleAutomationPlatform.
      In the YAML view, add the following under `spec`:

```yaml
spec:
  mcp:
    disabled: false
```

4. Click Save.

## Results

To verify that the MCP server is enabled:

- Under Workloads> (and then)Pods, confirm that the MCP server pod shows a Running status.
- Under Networking> (and then)Routes, a route with a name ending in `-mcp` appears in the list.
