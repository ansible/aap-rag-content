# Set up Red Hat Ansible Lightspeed on-premise deployment
## Configure Ansible VS Code extension for Red Hat Ansible Lightspeed on-premise deployment

To access the on-premise deployment of Red Hat Ansible Lightspeed, all Ansible users within your organization must install the Ansible Visual Studio (VS) Code extension in their VS Code editor, and configure the extension to connect to the on-premise deployment.

### Before you begin

- You have installed VS Code version 1.70.1 or later.

### Procedure

1.  Obtain the URL of your Ansible Lightspeed instance:
1.  In Red Hat OpenShift Container Platform, select Networking> (and then)Routes and locate the Red Hat Ansible Lightspeed instance that was created.
2.  From the **Location** column, copy the URL of your Ansible Lightspeed instance. The URL will be in the following format: `https://<lightspeed_route>/complete/aap/`

2.  Open the VS Code application.
3.  From the **Activity** bar, click the **Extensions** icon.
4.  From the **Installed Extensions** list, select **Ansible**.
5.  From the **Ansible** extension page, click the **Settings** icon (![Settings icon](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/settings-icon-ansible-vscode-extension.png)) and select **Extension Settings**.
6.  Select **Ansible Lightspeed** settings and specify the following information:

- In the **URL for Ansible Lightspeed** field, enter the **Route URL** of the Red Hat Ansible Lightspeed on-premise deployment. Ansible users must have Ansible Automation Platform controller credentials. After configuring Ansible VS Code extension to connect to Red Hat Ansible Lightspeed on-premise deployment, you must [log in to Ansible Lightspeed through the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension#login-vscode-extension "After installing and configuring the VS Code extension, you can log in to the Ansible Lightspeed service.").

Note:
If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.

