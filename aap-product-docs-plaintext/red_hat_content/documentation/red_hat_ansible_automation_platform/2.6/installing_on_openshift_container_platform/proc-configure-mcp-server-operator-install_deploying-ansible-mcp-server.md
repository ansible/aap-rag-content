# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.2. Deploying an Ansible MCP server on an operator-based installation




As an organization administrator, you can deploy and configure an Ansible MCP server on an operator-based installation of Ansible Automation Platform 2.6. Use the following procedure to deploy and configure the Ansible MCP server.

**Prerequisites**

- You have a valid Ansible Automation Platform 2.6 subscription.


**Procedure**

1. Log in to Red Hat OpenShift Container Platform as an administrator.
1. Navigate to the namespace where you want to install the MCP server.
1. SelectOperators→Installed Operators.
1. From the list of installed operators, select **Ansible Automation Platform** .
1. In the Ansible Automation Platform tile, click **Create instance** .
1. From the **Configure via** field, select the **Form** view, then provide the instance name. For example, `    aap-mcp` .
1. Select the **YAML** view, and under the `    spec:` section, add the `    mcp` component:


```
spec:      mcp:        disabled: false        allow_write_operations: false
```

Important
Use the `    allow_write_operations` variable to configure the operational access level of the Ansible MCP server:


-  **Read-only access** : Set the variable to `        false` to restrict the AI agent to viewing data only. In this mode, the AI tool can query job statuses and logs, but cannot trigger new automation in the Ansible Automation Platform. The MCP server is set to read-only mode by default.
-  **Read-write access** : Set the variable to `        true` to allow the AI agent to make changes in Ansible Automation Platform, such as executing jobs or modifying the system state.



1. Click **Create** . The Ansible MCP server is created.


**Verification**

1. Navigate toWorkloads→Deployments.
1. Check that the deployment you created is listed there. For example: `    aap-mcp` .
1. Check one of the pod’s logs and verify there are no errors.


**Next steps**

1. Obtain the following information:


-  **Ansible Automation Platform login screen URL** :


1. Navigate toNetworking→Routes.
1. For the Ansible Automation Platform deployment, click the **Copy icon** in the **Location** field. This is the URL of the Ansible Automation Platform login screen.

-  **Ansible Automation Platform administrator password** :


1. Navigate toWorkloads→Secretsand click `            aap-admin-password` .
1. Click **Reveal values** and then use the **Copy** icon to save the Ansible Automation Platform administrator password for future use.

-  **Ansible MCP server URL** :


1. Navigate toNetworking→Routes.
1. For the deployment you recently created ( `            aap-mcp` ), click the **Copy** icon from the **Location** field. This is the URL required to configure your AI agent to connect to the Ansible MCP server.


1.  [Create an API token for the Ansible MCP server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#proc-create-api-token-ansible-mcp-server_deploying-ansible-mcp-server) .


