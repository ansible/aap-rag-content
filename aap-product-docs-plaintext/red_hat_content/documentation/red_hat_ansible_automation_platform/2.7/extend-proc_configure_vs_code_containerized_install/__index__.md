# Configure the Ansible VS Code extension

If you deployed the Ansible Lightspeed coding assistant, you must also configure the Ansible VS Code extension with the generated Ansible Lightspeed URL. This configuration enables the Ansible users in your organization to use the Ansible Lightspeed coding assistant to create Ansible content.

## Before you begin

- You have installed VS Code version 1.70.1 or later.
- Your organization administrator has configured an IBM watsonx Code Assistant model for your organization.
- Your network or firewall configuration permits ingress traffic on port 8447. This port is required for containerized installations to connect IBM watsonx Code Assistant with the Ansible VS Code extension, which then provides access to the Ansible Lightspeed coding assistant.

## About this task

## Procedure

1.  Open the VS Code application.
2.  From the Activity bar, click the **Extensions** icon ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/extensions-icon-vscode.png).
3.  From the Installed Extensions list, select **Ansible**.
4.  From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings**.
5.  Select **Ansible Lightspeed** settings, and specify the following information:
1.  Ensure that the **Enable Ansible Lightspeed with watsonx Code Assistant inline suggestions** checkbox is selected.
2.  In the **URL for Ansible Lightspeed** field, verify that you have the following URL: `https://<node.ansible.com>:8447`.
3.  Select the **Enable Ansible Lightspeed with watsonx Code Assistant inline suggestions** checkbox.
6.  Optional: If you want to use the custom model instead of the default model, in the **Model ID Override** field, enter the custom model ID. The **model-override** setting enables you to override the default model and use the custom model, after your organization administrator has created a custom model and has shared the model ID with you separately. Your settings are automatically saved in VS Code.

Note:
If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.

## What to do next

- After you configure the Ansible VS Code extension with the generated Ansible Lightspeed URL, you can use the Ansible VS Code extension and start developing Ansible content.   1. [Log in to Red Hat Ansible Lightspeed through the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension#login-vscode-extension "After installing and configuring the VS Code extension, you can log in to the Ansible Lightspeed service.").
2. [Develop Ansible content](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_developing_ansible_content#developing-ansible-content "As an automation developer, you can use Red Hat Ansible Lightspeed to implement your organization’s automation strategy. Red Hat Ansible Lightspeed can help you create and use custom automation content.").
