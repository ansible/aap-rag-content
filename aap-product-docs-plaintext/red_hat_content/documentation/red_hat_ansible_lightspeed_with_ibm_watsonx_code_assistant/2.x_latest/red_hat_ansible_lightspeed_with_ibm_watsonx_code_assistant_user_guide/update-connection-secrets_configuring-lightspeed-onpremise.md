# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 3.3.8. Updating connection secrets on an existing Red Hat Ansible Automation Platform operator




After you have set up the Red Hat Ansible Lightspeed on-premise deployment successfully, you can modify the deployment if you want to connect to another IBM watsonx Code Assistant model. For example, you connected to the default IBM watsonx Code Assistant model but now want to connect to a custom model instead. To connect to another IBM watsonx Code Assistant model, you must create new connection secrets, and then update the connection secrets and parameters on an existing Red Hat Ansible Automation Platform operator.

**Prerequisites**

- You have set up a Red Hat Ansible Lightspeed on-premise deployment.
- You have obtained an API key and a model ID of the IBM watsonx Code Assistant model you want to connect to.
- You have created new authorization and model connection secrets for the IBM watsonx Code Assistant model that you want to connect to. For information about creating authorization and model connection secrets, see [Creating connection secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .


**Procedure**

1. Go to the Red Hat OpenShift Container Platform.
1. SelectOperators→Installed Operators.
1. From the **Projects** list, select the namespace where you installed the Red Hat Ansible Lightspeed instance.
1. Locate and select the **Ansible Automation Platform (provided by Red Hat)** operator that you installed earlier.
1. Select the **Ansible Lightspeed** tab.
1. Find and select the instance you want to update.
1. ClickActions→Edit AnsibleLightspeed. The editor switches to a text or YAML view.
1. Scroll the text to find the `    spec:` section.

![Setting to update the connection secrets](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/f27efb09ff28f30c224be4759ba208dd/update-connection-secrets.png)
)


1. Find the entry for the secret you have changed and saved under a new name.
1. Change the name of the secrets to the new secrets.
1. Click **Save** .

The new AnsibleLightspeed Pods are created. After the new pods are running successfully, the old AnsibleLightspeed Pods are terminated.




**Additional resources**

-  [Troubleshooting Red Hat Ansible Lightspeed on-premise deployment errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#ref-troubleshooting-lightspeed-onpremise-config_troubleshooting-lightspeed)


