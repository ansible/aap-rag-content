# Deploy the MCP server on Ansible Automation Platform
## Deploy the MCP server for Red Hat Ansible Automation Platform on an operator-based installation

As an organization administrator, you can deploy and configure the MCP server on an operator-based installation of Ansible Automation Platform. Use the following procedure to deploy and configure the MCP server.

### Before you begin

- You have a valid Ansible Automation Platform subscription.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform as an administrator.
2.  Navigate to the namespace where you want to install the MCP server.
3.  Select Operators> (and then)Installed Operators.
4.  From the list of installed operators, select **Ansible Automation Platform**.
5.  In the Ansible Automation Platform tile, click **Create instance**.
6.  From the **Configure via** field, select the **Form** view, then provide the instance name. For example, `aap-mcp`.
7.  Select the **YAML** view, and under the `spec:` section, add the `mcp` component:


```
spec:
mcp:
disabled: false
allow_write_operations: false
```

8.  Use the `allow_write_operations` variable to configure the operational access level of the MCP server:
9.  Click **Create**. the MCP server is created.
10.  Optional: If you changed the permissions of the MCP server after it was created and deployed, you must delete the **AnsibleMCPServer** custom resource and recreate it. Perform the following steps:

1.  Go to the Ansible Automation Platform portal.
2.  Under **Resources**, search for the **AnsibleMCPServer** custom resource.
3.  Select the active **AnsibleMCPServer** instance. An active AnsibleMCPServer instance is identified by the `-mcp` suffix appended to the Ansible Automation Platform custom resource name.
4.  Select the **Settings menu** on the right side of the instance, and then click **Delete AnsibleMCPServer**.
5.  After the reconciliation process completes, the existing MCP server instance is deleted, and a new MCP server instance is created.

### Results

1. Navigate to Workloads> (and then)Deployments.
2. Check that the deployment you created is listed there. For example: `aap-mcp`.
3. Check one of the pod’s logs and verify there are no errors.

### What to do next

1. Obtain the following information:
- **Ansible Automation Platform login screen URL**:
1. Navigate to Networking> (and then)Routes.
2. For the Ansible Automation Platform deployment, click the **Copy icon** in the **Location** field. This is the URL of the Ansible Automation Platform login screen.
- **Ansible Automation Platform administrator password**:
1. Navigate to Workloads> (and then)Secrets and click `aap-admin-password`.
2. Click **Reveal values** and then use the **Copy** icon to save the Ansible Automation Platform administrator password for future use.
- **MCP server URL**:
1. Navigate to Networking> (and then)Routes.
2. For the deployment you recently created (`aap-mcp`), click the **Copy** icon from the **Location** field. This is the URL required to configure your AI agent to connect to the MCP server.
2. [Create an API token for the MCP server](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#proc-create-api-token-ansible-mcp-server "Create an API token for your Ansible Automation Platform instance, so you can use it to connect with your preferred AI agent. The AI tool will inherit the user’s permissions for API token-based authentication.").

