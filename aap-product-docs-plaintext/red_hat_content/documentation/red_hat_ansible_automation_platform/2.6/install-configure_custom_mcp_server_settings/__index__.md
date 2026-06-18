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
