# 4. Setting up Red Hat Ansible Lightspeed for your organization
## 4.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 4.3.3. Creating a model configuration secret




You must create a configuration secret to connect to an IBM watsonx Code Assistant model, which can be either an on-premise deployment or a cloud deployment.

**Prerequisites**

- You have installed the Ansible Automation Platform operator 2.5.0-0.1753402603 or later on the Red Hat OpenShift Container Platform.
- You have created an OAuth application in the automation controller.
- You have obtained an API key and a model ID from IBM watsonx Code Assistant.

For information about obtaining an API key and model ID from IBM watsonx Code Assistant, see the [IBM watsonx Code Assistant documentation](https://cloud.ibm.com/docs/watsonx-code-assistant) . For information about installing IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data, see the [watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data documentation](https://www.ibm.com/docs/en/software-hub/5.1.x?topic=services-watsonx-code-assistant-red-hat-ansible-lightspeed) .




**Procedure**

1. Go to the Red Hat OpenShift Container Platform.
1. SelectWorkloads→Secrets.
1. ClickCreate→Key/value secret.
1. From the **Projects** list, select the namespace that you created when you installed the Red Hat Ansible Automation Platform operator.
1. ClickCreate→Key/value secret.
1. In **Secret name** , enter a unique name for the secret. For example, `    model-aiconnect` .
1. Add the following keys and their associated values individually:

| Key | Value |
| --- | --- |
|  `username` |  _For on-premise deployment only_

Enter the username you use to connect to an IBM Cloud Pak for Data deployment. |
|  `model_type` | Enter one of the following values per your IBM watsonx Code Assistant model:

- For on-premise deployment (IBM Cloud Pak for Data): `    wca-onprem`
- For cloud deployment (IBM Cloud): `    wca` |
|  `model_url` | Enter the URL of the IBM watsonx Code Assistant model. For cloud deployment, the model URL could be `https://api.dataplatform.cloud.ibm.com` . |
|  `model_api_key` | Enter the API key of your IBM watsonx Code Assistant model that was generated during the model installation. |
|  `model_id` | Enter the ID of your IBM watsonx Code Assistant model. |
|  `model_verify_ssl` |  _Optional, and supported on Ansible Automation Platform 2.5 and later_

This key controls whether the SSL certificate of the IBM watsonx Code Assistant model is verified.

Default = `true` |
|  `model_enable_anonymization` |  _Optional and supported on Ansible Automation Platform 2.5.250730 and later_

This key controls whether the anonymization of Personally Identifiable Information (PII) is enabled. PII information includes passwords, IP addresses, email addresses, and other sensitive data. When is enabled, users' personal information is modified to some generic values to protect their data and reduce the risk of data leaks.

You can turn off anonymization by setting the value to `false` to retain all original information entered by users and improve the quality of the answers. Disabling anonymization for Ansible Lightspeed hybrid deployments (the model is in IBM watsonx Code Assistant on IBM Cloud) results in users' PII being sent to IBM Cloud.

Default = `true` |


Important
Ensure that you do not accidentally add any whitespace characters (extra line, space, and so on) to the value fields. If there are any extra or erroneous characters in the secret, the connection to IBM watsonx Code Assistant fails.




1. Click **Create** .

After you create the model configuration secret, you must update the YAML file of the Ansible Automation Platform operator.




