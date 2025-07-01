# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 3.3.1. Overview




This section provides information about the system requirements, prerequisites, and the process for setting up a Red Hat Ansible Lightspeed on-premise deployment.

#### 3.3.1.1. Deployment models




You can use one of the following modes of deployment:

-  **On-premise deployment**

Both Red Hat Ansible Lightspeed and the IBM watsonx Code Assistant model (IBM Cloud Pak for Data) are on-premise deployments. Telemetry data is not collected for an on-premise mode of deployment.


-  **Hybrid deployment**

Red Hat Ansible Lightspeed is an on-premise deployment, while IBM watsonx Code Assistant model is a cloud deployment. For hybrid deployments, telemetry data is gathered and can be accessed from the Admin dashboard.

A hybrid deployment model provides the following benefits:


- Enables you to set up an on-premise deployment of Red Hat Ansible Lightspeed, with an option to use an IBM watsonx Code Assistant model that is on either an on-premise environment or a cloud environment.
- Provides the freedom and flexibility to choose an environment that best suits your organizational needs.
- Enables organizations to use the Ansible Automation Platform for user authentication, instead of logging into the Red Hat cloud.
- Enables organizations to deploy the Ansible Automation Platform in their preferred region.



#### 3.3.1.2. System requirements




Your system must meet the following minimum system requirements to install and run the Red Hat Ansible Lightspeed on-premise deployment.

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 5 GB |
| CPU | 1 |
| Local disk | 40 GB |


To see the rest of the Red Hat Ansible Automation Platform system requirements, see the [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/platform-system-requirements) section of _Planning your installation_ .

Note
You must also have installed IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data. The installation includes a base model that you can use to set up your Red Hat Ansible Lightspeed on-premise deployment. For installation information, see the [watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data documentation](https://www.ibm.com/docs/en/software-hub/5.1.x?topic=services-watsonx-code-assistant-red-hat-ansible-lightspeed) .



#### 3.3.1.3. Prerequisites




- You have installed Red Hat Ansible Automation Platform on your Red Hat OpenShift Container Platform environment.
- You have administrator privileges for Red Hat Ansible Automation Platform.
- You have installed IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data.
- Your system meets the minimum system requirements to set up Red Hat Ansible Lightspeed on-premise deployment.
- You have obtained an API key and a model ID from IBM watsonx Code Assistant.

For information about obtaining an API key and model ID from IBM watsonx Code Assistant, see the [IBM watsonx Code Assistant documentation](https://cloud.ibm.com/docs/watsonx-code-assistant) . For information about installing IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data, see the [watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data documentation](https://www.ibm.com/docs/en/software-hub/5.1.x?topic=services-watsonx-code-assistant-red-hat-ansible-lightspeed) .


- You have an existing external PostgreSQL database configured for the Red Hat Ansible Automation Platform, or have a database created for you when configuring the Red Hat Ansible Lightspeed on-premise deployment.


#### 3.3.1.4. Process for configuring a Red Hat Ansible Lightspeed on-premise deployment




Perform the following tasks to install and configure a Red Hat Ansible Lightspeed on-premise deployment:

1.  [Install the Red Hat Ansible Automation Platform operator](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#install-aap-lightspeed-operator_configuring-lightspeed-onpremise)
1.  [Create an OAuth application](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-oauth-app_configuring-lightspeed-onpremise)
1.  [Create connections secrets for Red Hat Ansible Automation Platform and IBM watsonx Code Assistant both](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise)
1.  [Create and deploy a Red Hat Ansible Lightspeed instance](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-lightspeed-instance_configuring-lightspeed-onpremise)
1.  [Update the Redirect URI to connect to your Red Hat Ansible Lightspeed on-premise deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#update-redirect-uri_configuring-lightspeed-onpremise)
1.  [Install and configure Ansible Visual Studio Code extension to connect to Red Hat Ansible Lightspeed on-premise deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#configure-vscode-extension-onpremise-deployment_configuring-lightspeed-onpremise)
1. Optional: If you want to connect to a different IBM watsonx Code Assistant, [update the connection secrets on an existing Red Hat Ansible Automation Platform operator](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#update-connection-secrets_configuring-lightspeed-onpremise)
1. Optional: [Monitor your Red Hat Ansible Lightspeed on-premise deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#monitor-lightspeed-onpremise-deployment_configuring-lightspeed-onpremise)
1. Optional: [Use the Ansible Lightspeed REST API to build custom automation development and tooling workflow outside of VS Code](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#use-rest-api_configuring-lightspeed-onpremise)


