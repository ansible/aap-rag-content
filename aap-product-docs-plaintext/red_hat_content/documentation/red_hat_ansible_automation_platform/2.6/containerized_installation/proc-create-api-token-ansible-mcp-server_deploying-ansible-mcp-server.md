# 7. Deploying Ansible MCP server on Ansible Automation Platform
## 7.3. Creating an API token for the Ansible MCP server




Create an API token for your Ansible Automation Platform instance, so you can use it to connect with your preferred AI agent. The AI tool will inherit the user’s permissions for API token-based authentication.

**Prerequisites**

- Your organization administrator has deployed an Ansible MCP server.


**Procedure**

1. From the navigation panel, selectAccess Management→Users.
1. Select the username for your user profile to configure OAuth 2 tokens.
1. Select the **Tokens** tab. When no tokens are present, the **Tokens** screen prompts you to add them.
1. Click **Create token** , and provide the following details:


-  **Application** : Enter the name of the application with which you want to associate your token. Alternatively, you can search for it by clicking **Browse** . This opens a separate window that enables you to choose from the available options. Select **Name** from the filter list to filter by name if the list is extensive.

Note
To create a Personal Access Token (PAT) that is not linked to any application, leave the **Application** field blank.




-  **Description** : (Optional) Provide a short description for your token.
-  **Scope** : (Required) Specify the level of access you want this token to have. The scope of an OAuth 2 token can be set as one of the following:


-  **Write** : Allows requests sent with this token to add, edit, and delete resources in the system.
-  **Read** : Limits actions to read only. The write scope includes the read scope.


1. Click **Create token** . The token information is displayed.
1. On the token information page that appears, click the **Copy icon** and save the token for future use.

Important
This will be the only time the token is displayed. Therefore, ensure that you save the token for future use.






**Verification**

You can verify that the application now shows the user with the appropriate token by selecting the **Tokens** tab on the **Application Details** page:


1. From the navigation panel, selectAccess Management→OAuth Applications.
1. Select the application you want to verify from the **Applications** list view.
1. Select the **Tokens** tab.

Your token should be displayed in the list of tokens associated with the application you chose.




**Next step**

-  [Connect an external AI agent to the Ansible MCP server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#proc-connect-ai-agent-ansible-mcp-server_deploying-ansible-mcp-server)


