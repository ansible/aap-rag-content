# 3. Setting up Red Hat Ansible Lightspeed for your organization
## 3.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 3.3.6. Connecting to a different IBM watsonx Code Assistant model




After you have set up the Red Hat Ansible Lightspeed on-premise deployment successfully, you can modify the deployment if you want to connect to another IBM watsonx Code Assistant model. For example, you connected to the default IBM watsonx Code Assistant model but now want to connect to a custom model instead. To connect to another IBM watsonx Code Assistant model, you must create new connection secrets, and then update the connection secrets and parameters on an existing Ansible Automation Platform operator.

**Prerequisites**

- You have set up a Red Hat Ansible Lightspeed on-premise deployment.
- You have obtained an API key and a model ID of the IBM watsonx Code Assistant model you want to connect to.
- You have created a new model configuration secret for the IBM watsonx Code Assistant model that you want to connect to. For information about creating a model configuration secrets, see [Creating a model configuration secret](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .


**Procedure**

1. Go to the Red Hat OpenShift Container Platform.
1. SelectOperators→Installed Operators.
1. From the list of installed operators, select the **Ansible Automation Platform** operator.
1. Locate and select the **Ansible Automation Platform** custom resource, and then click the required app.
1. Select the **YAML** tab.
1. Scroll the text to find the `    spec` section under `    Lightspeed` category. For example:


```
spec:      lightspeed:        disabled: false        model_config_secret_name: &lt;Name of the model configuration secret that you recently created.&gt;
```


1. Replace the `    model_config_secret_name` value with the name of the IBM watsonx Code Assistant that you want to connect to.
1. Click **Save** .

The new Ansible Lightspeed pods are created. After the new pods are running successfully, the old Ansible Lightspeed pods are terminated.




