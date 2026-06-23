# Deploy the MCP server on Ansible Automation Platform
## Create an API token for the MCP server
### Troubleshoot MCP server errors

This section contains information to help you diagnose and resolve issues with deploying the MCP server for Red Hat Ansible Automation Platform and connecting it to an external AI agent.

#### API output format rejected with 406 Status Code

**Issue**: Ansible Automation Platform rejects an API request (for example, retrieving job stdout) with an HTTP `406` status code if the MCP server’s requested output is not in `JSON` format.

**Workaround**: To obtain the output in a specific format, instruct your AI tool to use `JSON` format first. You can then transform the `JSON` output into your desired format.

#### User requests rejected with 400 status code

**Issue**: The MCP server may reject user requests from the external AI tool with `400 Bad Request` status code. This error is encountered when the Ansible Automation Platform uses a self-signed certificate.

**Workaround**: Configure the MCP server to ignore certificate errors using the following steps:

- For container-based installation: Set the value of variable `mcp_ignore_certificate_errors` to `true`.

- For operator-based installation:     Add the `IGNORE_CERTIFICATE_ERRORS` setting to the `mcp:` section of **AnsibleAutomationPlatform** custom resource in the following format:



```none
spec:
mcp:
extra_settings:
- setting: IGNORE_CERTIFICATE_ERRORS
value: true
```

#### MCP server permissions are changed post deployment

**Issue**: If you changed the permissions of the MCP server after it was created and deployed, you must delete the **AnsibleMCPServer** custom resource and recreate it.

**Workaround**: Perform the following steps:

1. Navigate to the Ansible Automation Platform portal.
2. Under **Resources**, search for the **AnsibleMCPServer** custom resource.
3. Select the active **AnsibleMCPServer** instance. An active AnsibleMCPServer instance is identified by the `-mcp` suffix appended to the Ansible Automation Platform custom resource name.
4. Select the **Settings menu** (3-dot menu icon) on the right side of the instance, then click **Delete AnsibleMCPServer**.
5. After the reconciliation process is completed, the existing MCP server instance is deleted and a new MCP server instance is created.
