# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.5. Changing the permissions of the Ansible MCP server post deployment




If you changed the permissions of the Ansible MCP server after it was created and deployed, you must delete the **AnsibleMCPServer** custom resource and recreate it.

**Prerequisites**

- You have a deployed an Ansible MCP server on an operator-based installation of Ansible Automation Platform.


**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Go to the resources tab underInstalled Operators→aap-operator.v2.6.0-, and then select **AnsibleMCPServer** details.
1. Under **Resources** , search for the **AnsibleMCPServer** custom resource.
1. Select the active **AnsibleMCPServer** instance. An active AnsibleMCPServer instance is identified by the `    -mcp` suffix appended to the Ansible Automation Platform custom resource name.
1. Select the **Settings menu** on the right side of the instance, and then click **Delete AnsibleMCPServer** .

After the reconciliation process completes, the existing MCP server instance is deleted, and a new Ansible MCP server instance is created.




**Verification**

1. Navigate toWorkloads→Deployments.
1. Check that the deployment you created is listed there. For example: `    aap-mcp` .
1. Check one of the pod’s logs and verify there are no errors.


