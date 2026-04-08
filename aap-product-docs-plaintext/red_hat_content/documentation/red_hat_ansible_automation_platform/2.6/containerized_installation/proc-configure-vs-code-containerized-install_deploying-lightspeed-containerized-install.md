# 6. Deploying Red Hat Ansible Lightspeed on containerized Ansible Automation Platform
## 6.5. Configuring the Ansible VS Code extension




If you deployed the Ansible Lightspeed coding assistant, you must also configure the Ansible VS Code extension with the generated Ansible Lightspeed URL. This configuration enables the Ansible users in your organization to use the Ansible Lightspeed coding assistant to create Ansible content.

**Prerequisites**

- You have installed VS Code version 1.70.1 or later.
- Your organization administrator has configured an IBM watsonx Code Assistant model for your organization.
- Your network or firewall configuration permits ingress traffic on port 8447. This port is required for containerized installations to connect IBM watsonx Code Assistant with the Ansible VS Code extension, which then provides access to the Ansible Lightspeed coding assistant.


**Procedure**

1. Open the VS Code application.
1. From the Activity bar, click the **Extensions** icon![Extensions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Containerized_installation-en-US/images/7d3e99e2c8c192205eee349f07f39c7e/extensions-icon-vscode.png)
.
1. From the Installed Extensions list, select **Ansible** .
1. From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings** .
1. Select **Ansible Lightspeed** settings, and specify the following information:


1. Ensure that the **Enable Ansible Lightspeed with watsonx Code Assistant inline suggestions** checkbox is selected.
1. In the **URL for Ansible Lightspeed** field, verify that you have the following URL: `        https://&lt;node.ansible.com&gt;:8447` .
1. Select the **Enable Ansible Lightspeed with watsonx Code Assistant inline suggestions** checkbox.

1. Optional: If you want to use the custom model instead of the default model, in the **Model ID Override** field, enter the custom model ID. The **model-override** setting enables you to override the default model and use the custom model, after your organization administrator has created a custom model and has shared the model ID with you separately.

Your settings are automatically saved in VS Code.

Note
If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.






**Next steps**

- After you configure the Ansible VS Code extension with the generated Ansible Lightspeed URL, you can use the Ansible VS Code extension and start developing Ansible content.


1.  [Log in to Red Hat Ansible Lightspeed through the Ansible VS Code extension](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/developing-ansible-content_lightspeed-user-guide#login-vscode-extension_developing-ansible-content) .
1.  [Develop Ansible content](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/developing-ansible-content_lightspeed-user-guide) .



