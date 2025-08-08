# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 3.3.5. Creating and deploying a Red Hat Ansible Lightspeed instance




Use this procedure to create and deploy a Red Hat Ansible Lightspeed instance to your namespace.

**Prerequisites**

- You have created connection secrets for both Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.


**Procedure**

1. Go to Red Hat OpenShift Container Platform.
1. SelectOperators→Installed Operators.
1. From the **Projects** list, select the namespace where you want to install the Red Hat Ansible Lightspeed instance and where you created the connection secrets.
1. Locate and select the **Ansible Automation Platform (provided by Red Hat)** operator that you installed earlier.
1. SelectAll instances→Create new.
1. From the **Create new** list, select the **Ansible Lightspeed** modal.
1. Ensure that you have selected **Form view** as the configuration mode.
1. Provide the following information:


1.  **Name** : Enter a unique name for your Red Hat Ansible Lightspeed instance.
1.  **Secret where the authentication information can be found** : Select the authentication secret that you created to connect to the Red Hat Ansible Automation Platform.
1.  **Secret where the model configuration can be found** : Select the model secret that you created to connect to IBM watsonx Code Assistant.

1. Optional: If you created a bundle secret to trust a custom Certificate Authority, select the `    bundle_cacert_secret` fromAdvanced→Bundle CA Certificate Secretlist.
1. Click **Create** .

The Red Hat Ansible Lightspeed instance takes a few minutes to deploy to your namespace. After the installation status is displayed as **Successful** , the Ansible Lightspeed portal URL is available underNetworking→Routesin Red Hat OpenShift Container Platform.




**Additional resources**

-  [Troubleshooting Red Hat Ansible Lightspeed on-premise deployment errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#ref-troubleshooting-lightspeed-onpremise-config_troubleshooting-lightspeed)


