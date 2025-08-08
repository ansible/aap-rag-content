# 4. Developing Ansible content
## 4.2. Installing and configuring the Ansible VS Code extension
### 4.2.3. Configuring the Ansible VS Code extension




You can configure the Ansible VS Code extension to enable Red Hat Ansible Lightspeed and specify it’s portal URL and IBM watsonx Code Assistant model ID.

**Prerequisites**

- Your organization administrator has configured an IBM watsonx Code Assistant model for your organization.


**Procedure**

1. Open the VS Code application.
1. From the Activity bar, click the **Extensions** icon![Extensions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/7d3e99e2c8c192205eee349f07f39c7e/extensions-icon-vscode.png)
.
1. From the Installed Extensions list, select **Ansible** .
1. From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings** .
1. Select **Ansible Lightspeed** settings, and specify the following information:


1. Ensure that the **Enable Ansible Lightspeed with watsonx Code Assistant inline suggestions** checkbox is selected.
1. In the **URL for Ansible Lightspeed** field, verify that you have the following URL: `        https://c.ai.ansible.redhat.com/` .
1. Select the **Enable Ansible Lightspeed with watsonx Code Assistant inline suggestions** checkbox.

1. Optional: If you want to use the custom model instead of the default model, in the **Model ID Override** field, enter the custom model ID. The **model-override** setting enables you to override the default model and use the custom model, after your organization administrator has created a custom model and has shared the model ID with you separately.

Your settings are automatically saved in VS Code.




The following illustration displays the configured settings for the Ansible VS Code extension:


<span id="idm139976452410448"></span>
**Figure 4.1. Configured settings for the Ansible VS Code extension**

![Configured settings for the Ansible VS Code extension](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/f0217e74e4b417bd4f6ae02ad6acb8c8/lightspeed-vs-code-settings.png)




Note
If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.



**Additional resources**

-  [Troubleshooting Ansible Visual Studio Code extension errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#ref-troubleshooting-vscode_troubleshooting-lightspeed)


