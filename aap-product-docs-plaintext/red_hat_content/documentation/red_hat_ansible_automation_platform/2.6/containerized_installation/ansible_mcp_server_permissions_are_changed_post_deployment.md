# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.5. Troubleshooting Ansible MCP server errors
### 7.5.3. Ansible MCP server permissions are changed post deployment




**Issue** : If you changed the permissions of the Ansible MCP server after it was created and deployed, you must delete the **AnsibleMCPServer** custom resource and recreate it.

**Workaround** : Perform the following steps:

1. Navigate to the Ansible Automation Platform portal.
1. Under **Resources** , search for the **AnsibleMCPServer** custom resource.
1. Select the active **AnsibleMCPServer** instance. An active AnsibleMCPServer instance is identified by the `    -mcp` suffix appended to the Ansible Automation Platform custom resource name.
1. Select the **Settings menu** (3-dot menu icon) on the right side of the instance, then click **Delete AnsibleMCPServer** .
1. After the reconciliation process is completed, the existing Ansible MCP server instance is deleted and a new Ansible MCP server instance is created.


