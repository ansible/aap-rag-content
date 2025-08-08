# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 3.3.4. Creating connection secrets




You must create an authorization secret to connect to Red Hat Ansible Automation Platform, and a model secret to connect to IBM watsonx Code Assistant. If you need to trust a custom Certificate Authority, you must create a bundle secret.

**Prerequisites**

- You have installed the Ansible Automation Platform operator on the Red Hat OpenShift Container Platform.
- You have created an OAuth application in the automation controller.
- You have obtained an API key and a model ID from IBM watsonx Code Assistant.

For information about obtaining an API key and model ID from IBM watsonx Code Assistant, see the [IBM watsonx Code Assistant documentation](https://cloud.ibm.com/docs/watsonx-code-assistant) . For information about installing IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data, see the [watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data documentation](https://www.ibm.com/docs/en/software-hub/5.1.x?topic=services-watsonx-code-assistant-red-hat-ansible-lightspeed) .




**Procedure**

1. Go to the Red Hat OpenShift Container Platform.
1. SelectWorkloads→Secrets.
1. ClickCreate→Key/value secret.
1. From the **Projects** list, select the namespace that you created when you installed the Red Hat Ansible Automation Platform operator.
1. Create an **authorization secret** to connect to the Red Hat Ansible Automation Platform:


1. ClickCreate→Key/value secret.
1. In **Secret name** , enter a unique name for the secret. For example, `        auth-aiconnect` .
1. Add the following keys and their associated values individually:

| Key | Value |
| --- | --- |
|  `auth_api_url` | Enter the API URL of the automation controller in the following format based on the Ansible Automation Platform version you are using:

- For Ansible Automation Platform 2.4: `    https://&lt;CONTROLLER_SERVER_NAME&gt;/api`
- For Ansible Automation Platform 2.5: `    https://&lt;GATEWAY_SERVER_NAME&gt;` |
|  `auth_api_key` | Enter the client ID of the OAuth application that you recorded earlier. |
|  `auth_api_secret` | Enter the client secret of the OAuth application that you recorded earlier. |
|  `auth_allowed_hosts` | Enter the list of strings representing the host/domain names used by the underlying Django framework to restrict which hosts can access the service. This is a security measure to prevent HTTP Host header attacks. For more information, see [Allowed hosts in django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts) . |
|  `auth_verify_ssl` | Enter the value as `true` . |


Important
Ensure that you do not accidentally add any whitespace characters (extra line, space, and so on) to the value fields. If there are any extra or erroneous characters in the secret, the connection to Red Hat Ansible Automation Platform fails.




1. Click **Create** .

The following image is an example of an authorization secret:

![{Example of an authorization secret](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/628f23b0bdc6327e8bb0a509438e8ddd/aiconnect-auth-secret.png)




1. Similarly, create a **model secret** to connect to an IBM watsonx Code Assistant model:


1. ClickCreate→Key/value secret.
1. In **Secret name** , enter a unique name for the secret. For example, `        model-aiconnect` .
1. Add the following keys and their associated values individually:

| Key | Value |
| --- | --- |
|  `username` | Enter the username you use to connect to your IBM watsonx Code Assistant model. |
|  `model_type` | Enter one of the following values per your IBM watsonx Code Assistant model:

- For on-premise deployment of IBM watsonx Code Assistant model (IBM Cloud Pak for Data): `    wca-onprem`
- For cloud deployment of IBM watsonx Code Assistant model (IBM Cloud): `    wca` |
|  `model_url` | Enter the URL of the IBM watsonx Code Assistant model. |
|  `model_api_key` | Enter the API key of your IBM watsonx Code Assistant model that was generated during the model installation. |
|  `model_id` | Enter the ID of your IBM watsonx Code Assistant model. |
|  `model_verify_ssl` |  _Optional, and supported on Red Hat Ansible Automation Platform 2.5 only_

This key controls whether the SSL certificate of the IBM watsonx Code Assistant model is verified.

Default = `true` |


Important
Ensure that you do not accidentally add any whitespace characters (extra line, space, and so on) to the value fields. If there are any extra or erroneous characters in the secret, the connection to IBM watsonx Code Assistant fails.




1. Click **Create** .



After you create the authorization and model secrets, you must select the secrets when you [create and deploy a Red Hat Ansible Lightspeed instance](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-lightspeed-instance_configuring-lightspeed-onpremise) .

#### 3.3.4.1. Creating a bundle secret to trust a custom Certificate Authority




If you encounter a scenario where you need to trust a custom Certificate Authority, you can customize a few variables for the Red Hat Ansible Lightspeed instance. Trusting a custom Certificate Authority enables the Red Hat Ansible Lightspeed instance to access network services configured with SSL certificates issued locally, such as cloning a project from an internal Git server via HTTPS.

If you encounter the following error when syncing projects, it indicates that you need to customize the variables.

```
fatal: unable to access 'https://private.repo./mine/ansible-rulebook.git': SSL certificate problem: unable to get local issuer certificate
```

**Procedure**

Use one of the following methods to create a custom bundle secret using the CLI:


-  **Using a Certificate Authority secret**

Create a `    bundle_cacert_secret` using the following command:


```
# kubectl create secret generic &lt;resourcename&gt;-custom-certs \        --from-file=bundle-ca.crt=&lt;PATH/TO/YOUR/CA/PEM/FILE&gt;<span id="CO1-1"><!--Empty--></span><span class="callout">1</span>
```

**Where:**

<1>: Path of the self-signed certificate. Modify the file path to point to where your self-signed certificates are stored. The Red Hat Ansible Lightspeed instance looks for the data field `    bundle-ca.crt` in the specified `    bundle_cacert_secret` secret.


The following is an example of a bundle CA certificate:


```
spec:      ...      bundle_cacert_secret: &lt;resourcename&gt;-custom-certs
```


-  **Using the `    kustomization.yaml` configuration file**

Use the following command:


```
secretGenerator:      - name: &lt;resourcename&gt;-custom-certs        files:          - bundle-ca.crt=&lt;path+filename&gt;        options:          disableNameSuffixHash: true
```




After you create the bundle secret, you must select the secret when you [create and deploy a Red Hat Ansible Lightspeed instance](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-lightspeed-instance_configuring-lightspeed-onpremise) .

**Additional resources**

-  [Troubleshooting Red Hat Ansible Lightspeed on-premise deployment errors](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#ref-troubleshooting-lightspeed-onpremise-config_troubleshooting-lightspeed)


