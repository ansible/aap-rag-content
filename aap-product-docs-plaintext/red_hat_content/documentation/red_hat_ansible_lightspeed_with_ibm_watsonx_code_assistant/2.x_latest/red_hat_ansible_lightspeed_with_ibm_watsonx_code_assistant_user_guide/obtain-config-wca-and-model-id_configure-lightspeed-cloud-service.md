# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.2. Setting up Red Hat Ansible Lightspeed cloud service
### 3.2.2. Configuring Red Hat Ansible Lightspeed cloud service




Use this procedure to configure the Red Hat Ansible Lightspeed cloud service.

**Prerequisites**

- You have obtained an API key and a model ID from IBM watsonx Code Assistant that you want to use in Red Hat Ansible Lightspeed.

For information about how to obtain an API key and model ID from IBM watsonx Code Assistant, see the [IBM watsonx Code Assistant documentation](https://cloud.ibm.com/docs/watsonx-code-assistant) .




**Procedure**

1. Log in to the [Ansible Lightspeed portal](https://c.ai.ansible.redhat.com/) as an organization administrator.
1. From the login screen, click **Admin Portal** .
1. Specify the API key of your IBM watsonx Code Assistant instance:


1. Under **IBM Cloud API Key** , click **Add API key** . A screen to enter the **API Key** is displayed.
1. Enter the API Key.
1. Optional: Click **Test** to validate the API key.
1. Click **Save** .

1. Specify the model ID of the model that you want to use:


1. Click **Model Settings** .
1. Under **Model ID** , click **Add Model ID** . A screen to enter the **Model Id** is displayed.
1. Enter the **Model ID** that you obtained in the previous procedure as the default model for your organization.
1. Optional: Click **Test model ID** to validate the model ID.
1. Click **Save** .

When the API key and model ID is successfully validated, Red Hat Ansible Lightspeed is connected to your IBM watsonx Code Assistant instance.





**Additional resources**

-  [Troubleshooting Red Hat Ansible Lightspeed configuration errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#troubleshooting-lightspeed-config_troubleshooting-lightspeed)


