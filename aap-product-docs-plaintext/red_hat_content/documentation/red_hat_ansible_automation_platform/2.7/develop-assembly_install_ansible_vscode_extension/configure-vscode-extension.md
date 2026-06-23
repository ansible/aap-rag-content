# Install and configure the Ansible VS Code extension
## Configure the Ansible VS Code extension

Configure third-party LLM providers, such as IBM watsonx Code Assistant or Google Gemini, within the Ansible VS Code extension.

### Before you begin

- You have installed the Ansible VS Code extension v25.12.3.
- You have obtained a valid API key for your chosen third-party LLM provider.

### Procedure

1.  Open the VS Code application.
2.  From the Activity bar, click the **Extensions** icon ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/extensions-icon-vscode.png).
3.  From the Installed Extensions list, select **Ansible**.
4.  From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings**.
5.  Select **Ansible Lightspeed** settings, and specify the following information:
| UI field                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Ansible Lightspeed: Enabled             | <br>Select this checkbox to enable the Red Hat Ansible Lightspeed service.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br>Ansible Lightspeed: Provider            | <br>Select the active AI service for code generation.<br>Choose the AI provider from the following options:<br>  `wca`: (Default setting) Uses IBM watsonx Code Assistant as the AI provider.  `google`: Uses Google Gemini as the AI provider.                                                                                                                                                                                                                                                      |
| <br>Ansible Lightspeed: Model Name          | <br>Specify the specific AI model version to use for code generation:<br>  For IBM watsonx Code Assistant: (Required) The IBM watsonx Code Assistant model name or ID that you want to use for code generation.  For Google Gemini: (Optional) The system applies a recommended default model if left blank.                                                                                                                                                                                         |
| <br>Ansible Lightspeed: Api Key             | <br>Specify the secret credential required to authenticate requests with third-party model providers.<br>  For IBM watsonx Code Assistant: (Optional) This field is not used for the IBM WCA provider. IBM watsonx Code Assistant relies on a separate OAuth2 login flow via the Red Hat portal.  For Google Gemini: (Required) Paste your active Google Gemini API key into this field. This token authorizes the extension to send prompts to Google’s servers.                                    |
| <br>Ansible Lightspeed: Api Endpoint        | <br>Specify the destination URL for network requests sent by the Ansible VS Code extension.<br>  For IBM watsonx Code Assistant: (Required) This field allows modification of the service URL for IBM watsonx Code Assistant connections. The default URL is `https://c.ai.ansible.redhat.com`.  For Google Gemini: (Not configurable) This setting is not configurable when using the Google provider. The extension automatically manages the correct endpoint URL for Google services internally. |
| <br>Ansible Lightspeed Suggestions: Enabled | <br>Toggle the automatic display of inline code completions within the Ansible VS Code editor. Inline suggestions are currently available for the IBM watsonx Code Assistant provider only.                                                                                                                                                                                                                                                                                                          |
| <br>Ansible Lightspeed: Timeout             | <br>Define the maximum duration the Ansible VS Code extension waits for a server response. The default timeout for API calls is 3000 milliseconds.                                                                                                                                                                                                                                                                                                                                                   |

### Results

Your settings are automatically saved in VS Code.

Note:

If your organization recently subscribed to the Red Hat Ansible Automation Platform, it might take a few hours for Red Hat Ansible Lightspeed to detect the new subscription. In VS Code, use the **Refresh** button in the Ansible extension from the Activity bar to check again.

