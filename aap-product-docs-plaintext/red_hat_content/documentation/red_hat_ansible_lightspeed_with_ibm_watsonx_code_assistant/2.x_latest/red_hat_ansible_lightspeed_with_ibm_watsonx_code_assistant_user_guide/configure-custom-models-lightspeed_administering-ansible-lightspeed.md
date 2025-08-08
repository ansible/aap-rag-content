# 5. Administering the Ansible Lightspeed Service
## 5.3. Configuring custom models
### 5.3.4. Configuring Red Hat Ansible Lightspeed to use custom models




After you create and deploy a custom model in IBM watsonx Code Assistant, you must configure Red Hat Ansible Lightspeed so that you can use the custom model for your organization.

You can specify one of the following configurations for using the custom model:

-  **Enable access for all users in your organization**

You can configure a custom model as the default model for your organization. All users in your organization can use the custom model.


-  **Enable access for select Ansible users in your organization**

Using the **model-override** setting in the Ansible VS Code extension, select Ansible users can tune their Ansible Lightspeed service to use a custom model instead of the default model. For example, If you are using Red Hat Ansible Lightspeed as both an organization administrator and an end user, you can test the custom model for select Ansible users before making it available for all users in your organization.




**Procedure**

Choose one of the following configurations for your custom model:


-  **Configure the custom model for all Ansible users in your organization**


1. Log in to the [Ansible Lightspeed with IBM watsonx Code Assistant Hybrid Cloud Console](https://console.redhat.com/preview/ansible/seats-administration) as an organization administrator.
1. Specify the model ID of the custom model:


1. Click **Model Settings** .
1. Under **Model ID** , click **Add Model ID** . A screen to enter the **Model ID** is displayed.
1. Enter the **Model ID** of the custom model.
1. Optional: Click **Test model ID** to validate the model ID.
1. Click **Save** .


-  **Configure the custom model for select Ansible users in your organization**


1. Log in to the VS Code application using your Red Hat account.
1. From the Activity bar, click the **Extensions** icon![Extensions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/7d3e99e2c8c192205eee349f07f39c7e/extensions-icon-vscode.png)
.
1. From the Installed Extensions list, select **Ansible** .
1. From the **Ansible** extension page, click the **Settings** icon and select **Extension Settings** .
1. From the list of settings, select **Ansible Lightspeed** .
1. In the **Model ID Override** field, enter the model ID of the custom model.

Your settings are automatically saved in VS Code, and you can now use the custom model.





