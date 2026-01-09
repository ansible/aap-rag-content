# 5. Developing Ansible content
## 5.2. Installing and configuring the Ansible VS Code extension
### 5.2.3. Configuring the Ansible VS Code extension




Configure third-party LLM providers, such as IBM watsonx Code Assistant or Google Gemini, within the Ansible VS Code extension.

**Prerequisites**

- You have installed the Ansible VS Code extension v25.12.3.
- You have obtained a valid API key for your chosen third-party LLM provider.


**Procedure**

1. Open the VS Code application.
1. From the Activity bar, click the **Extensions** icon![Extensions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/7d3e99e2c8c192205eee349f07f39c7e/extensions-icon-vscode.png)
.
1. From the Installed Extensions list, select **Ansible** .
1. From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings** .
1. Select **Ansible Lightspeed** settings, and specify the following information:


| UI field | Description |
| --- | --- |
| Ansible Lightspeed: Enabled | Select this checkbox to enable the Red Hat Ansible Lightspeed service. |
| Ansible Lightspeed: Provider | Select the active AI service for code generation.

Choose the AI provider from the following options:

-  `    wca` : (Default setting) Uses IBM watsonx Code Assistant as the AI provider.
-  `    google` : Uses Google Gemini as the AI provider. |
| Ansible Lightspeed: Model Name | Specify the specific AI model version to use for code generation:

- For IBM watsonx Code Assistant: (Required) The IBM watsonx Code Assistant model name or ID that you want to use for code generation.
- For Google Gemini: (Optional) The system applies a recommended default model if left blank. |
| Ansible Lightspeed: Api Key | Specify the secret credential required to authenticate requests with third-party model providers.

- For IBM watsonx Code Assistant: (Optional) This field is not used for the IBM WCA provider. IBM watsonx Code Assistant relies on a separate OAuth2 login flow via the Red Hat portal.
- For Google Gemini: (Required) Paste your active Google Gemini API key into this field. This token authorizes the extension to send prompts to Google’s servers. |
| Ansible Lightspeed: Api Endpoint | Specify the destination URL for network requests sent by the Ansible VS Code extension.

- For IBM watsonx Code Assistant: (Required) This field allows modification of the service URL for IBM watsonx Code Assistant connections. The default URL is `    https://c.ai.ansible.redhat.com` .
- For Google Gemini: (Not configurable) This setting is not configurable when using the Google provider. The extension automatically manages the correct endpoint URL for Google services internally. |
| Ansible Lightspeed Suggestions: Enabled | Toggle the automatic display of inline code completions within the Ansible VS Code editor. Inline suggestions are currently available for the IBM watsonx Code Assistant provider only. |
| Ansible Lightspeed: Timeout | Define the maximum duration the Ansible VS Code extension waits for a server response. The default timeout for API calls is 3000 milliseconds. |


Your settings are automatically saved in VS Code.

Note
If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.



**Additional resources**

-  [Troubleshooting Ansible Visual Studio Code extension errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#ref-troubleshooting-vscode_troubleshooting-lightspeed)


