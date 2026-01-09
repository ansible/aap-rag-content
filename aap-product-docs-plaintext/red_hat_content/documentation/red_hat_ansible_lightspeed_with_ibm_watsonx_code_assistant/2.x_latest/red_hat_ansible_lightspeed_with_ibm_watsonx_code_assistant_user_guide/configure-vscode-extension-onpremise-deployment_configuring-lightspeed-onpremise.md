# 4. Setting up Red Hat Ansible Lightspeed for your organization
## 4.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 4.3.5. Configuring Ansible VS Code extension for Red Hat Ansible Lightspeed on-premise deployment




To access the on-premise deployment of Red Hat Ansible Lightspeed, all Ansible users within your organization must install the Ansible Visual Studio (VS) Code extension in their VS Code editor, and configure the extension to connect to the on-premise deployment.

**Prerequisites**

- You have installed VS Code version 1.70.1 or later.


**Procedure**

1. Obtain the URL of your Ansible Lightspeed instance:


1. In Red Hat OpenShift Container Platform, selectNetworking→Routesand locate the Red Hat Ansible Lightspeed instance that was created.
1. From the **Location** column, copy the URL of your Ansible Lightspeed instance.

The URL will be in the following format: `        https://&lt;lightspeed_route&gt;/complete/aap/`



1. Open the VS Code application.
1. From the **Activity** bar, click the **Extensions** icon.
1. From the **Installed Extensions** list, select **Ansible** .
1. From the **Ansible** extension page, click the **Settings** icon (![Settings icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/a965b5f084413665a18b604849646b2a/settings-icon-ansible-vscode-extension.png)
) and select **Extension Settings** .
1. Select **Ansible Lightspeed** settings and specify the following information:


- In the **URL for Ansible Lightspeed** field, enter the **Route URL** of the Red Hat Ansible Lightspeed on-premise deployment. Ansible users must have Ansible Automation Platform controller credentials.

After configuring Ansible VS Code extension to connect to Red Hat Ansible Lightspeed on-premise deployment, you must [log in to Ansible Lightspeed through the Ansible VS Code extension](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#login-vscode-extension_developing-ansible-content) .

Note
If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.







