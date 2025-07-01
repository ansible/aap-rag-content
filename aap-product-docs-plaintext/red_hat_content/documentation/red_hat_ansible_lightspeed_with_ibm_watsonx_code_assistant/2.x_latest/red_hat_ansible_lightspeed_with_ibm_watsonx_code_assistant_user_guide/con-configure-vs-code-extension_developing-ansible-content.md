# 4. Developing Ansible content
## 4.2. Installing and configuring the Ansible VS Code extension




Red Hat Ansible Lightspeed with IBM watsonx Code Assistant is integrated with the Ansible Visual Studio (VS) Code extension in VS Code. The Ansible VS Code extension, with Red Hat Ansible Lightspeed features enabled, automatically collects recommendations, usage telemetry, and Ansible YAML file state through automated events.

To access Red Hat Ansible Lightspeed, all Ansible users must install and configure the Ansible VS Code extension in their VS Code. The Ansible VS Code extension uses the Ansible-specific IBM watsonx Granite model configured in the Red Hat Ansible Lightspeed administrator portal as the default mode for all users in your organization.

You can also use a custom, fine-tuned model if your organization administrator has created a custom model and has shared the model ID with you separately. Use the **model-override** setting in the Ansible VS Code extension to override the default model, and use the custom model instead. Using a custom model enables you to improve the code recommendation experience and tune the model to your organizational automation patterns. For example, if you are using Red Hat Ansible Lightspeed both as an organization administrator and a user, you can test the custom model for select Ansible users before making it available for all users in your organization. For more information, see [Configuring custom models](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#configure-custom-models_administering-ansible-lightspeed) .

