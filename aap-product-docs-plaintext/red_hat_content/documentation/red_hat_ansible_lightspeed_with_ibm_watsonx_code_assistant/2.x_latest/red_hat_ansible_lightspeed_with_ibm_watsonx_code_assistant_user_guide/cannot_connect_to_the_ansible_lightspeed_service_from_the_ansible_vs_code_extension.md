# 7. Troubleshooting
## 7.2. Troubleshooting Red Hat Ansible Lightspeed on-premise deployment errors
### 7.2.3. Cannot connect to the Ansible Lightspeed service from the Ansible VS Code extension




The following scenarios are possible:

- The log-in attempt fails with the following error message:

`    Enable lightspeed services from settings to use the feature.`

This error indicates that Ansible Lightspeed is not enabled in the Ansible VS Code extension. To resolve this error, perform the following tasks:


1. Open the VS Code application.
1. From the **Activity** bar, click the **Extensions** icon.
1. From the **Installed Extensions** list, select **Ansible** .
1. From the **Ansible** extension page, click the **Settings** icon (![Settings icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/a965b5f084413665a18b604849646b2a/settings-icon-ansible-vscode-extension.png)
) and select **Extension Settings** .
1. Select **Ansible Lightspeed** settings and then select the **Enable Ansible Lightspeed** checkbox.

- You are redirected to an incorrect Ansible Lightspeed instance on clicking theConnectbutton.

This error indicates an incorrect route URL was used while configuring the Ansible Lightspeed service in Ansible VS Code extension. Ensure that you have configured the correct value in the route URL without any suffix. For more information, see [Configuring Ansible VS Code extension for Red Hat Ansible Lightspeed on-premise deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#configure-vscode-extension-onpremise-deployment_configuring-lightspeed-onpremise) .


- Cannot request code recommendations

The following error message is displayed:

`    An error occurred attempting to complete your request. Please try again later.`

This error indicates that the Ansible Lightspeed service is not running or is running with issues. Please check the Lightspeed service logs (the pod with suffix `    -api` ) for more details and error codes.


- Cannot request code recommendations

The following error message is displayed:

`    The IBM watsonx Code Assistant is unavailable. Please try again later.`

or:

`    IBM watsonx Code Assistant Model ID is invalid. Please contact your administrator.`

This error indicates that the model secret contains incorrect values. To resolve this error, ensure that you have not accidentally added any whitespace characters (extra line, space, and so on) to the `    username` , `    model_url` , and `    model_api_key` parameters in the model connection secret. For more information, see [Creating connection secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .




