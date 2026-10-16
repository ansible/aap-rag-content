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
