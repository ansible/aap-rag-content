# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 3.3.3. Creating an OAuth application




Use this procedure to create an OAuth application for your Red Hat Ansible Lightspeed on-premise deployment.

**Prerequisites**

- You have an operational Ansible automation controller instance.


**Procedure**

1. Log in to the automation controller as an administrator.
1. Under **Administration** , clickApplications→Add.
1. Enter the following information:


1.  **Name** : Specify a unique name for your application.
1.  **Organization** : Select a preferred organization.
1.  **Authorization grant type** : Select **Authorization code** .
1.  **Redirect URIs** : Enter a temporary URL for now, for example, `        <a class="link" href="https://temp/">https://temp/</a>` .

The exact Red Hat Ansible Lightspeed application URL is generated after the on-premise deployment is completed. After the deployment is completed, you must change the Redirect URI to point to the generated Red Hat Ansible Lightspeed application URL. For more information, see [Updating the Redirect URIs](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#update-redirect-uri_configuring-lightspeed-onpremise) .


1. From the **Client type** list, select **Confidential** .

1. Click **Save** .

A pop-up window is displayed along with the generated application client ID and client secret.


1. Copy and save both the generated client ID and client secret for future use.

Important
This is the only time the pop-up window is displayed. Therefore, ensure that you copy both the client ID and client secret, as you need these tokens to create connections secrets for Red Hat Ansible Automation Platform and IBM watsonx Code Assistant both.



The following image is an example of the generated client ID and client secret:

![{Example of a generated client ID and client secret](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/337b2725d0b16ee1ffa5111384a41c8b/popup-window-client-ID-secret.png)





**Additional resources**

-  [Troubleshooting Red Hat Ansible Lightspeed on-premise deployment errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#ref-troubleshooting-lightspeed-onpremise-config_troubleshooting-lightspeed)


