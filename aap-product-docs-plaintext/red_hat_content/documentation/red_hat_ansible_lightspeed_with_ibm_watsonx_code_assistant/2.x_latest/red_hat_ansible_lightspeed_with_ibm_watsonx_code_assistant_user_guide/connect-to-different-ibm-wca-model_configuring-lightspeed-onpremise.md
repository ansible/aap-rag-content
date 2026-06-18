# 4. Setting up Red Hat Ansible Lightspeed for your organization
## 4.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 4.3.6. Connecting to a different IBM watsonx Code Assistant model

After you have set up the Red Hat Ansible Lightspeed on-premise deployment successfully, you can modify the deployment if you want to connect to another IBM watsonx Code Assistant model.

For example, you connected to the default IBM watsonx Code Assistant model but now want to connect to a custom model instead. To connect to another IBM watsonx Code Assistant model, you must create new connection secrets, and then update the connection secrets and parameters on an existing Ansible Automation Platform operator.

**Prerequisites**

- You have set up a Red Hat Ansible Lightspeed on-premise deployment.
- You have obtained an API key and a model ID of the IBM watsonx Code Assistant model you want to connect to.
- You have created a new model configuration secret for the IBM watsonx Code Assistant model that you want to connect to. For information about creating a model configuration secrets, see [Creating a model configuration secret](#create-connection-secrets_configuring-lightspeed-onpremise "4.3.3.&nbsp;Creating a model configuration secret").

**Procedure**

1. Go to the Red Hat OpenShift Container Platform.

2. Select Operators → Installed Operators.

3. From the list of installed operators, select the **Ansible Automation Platform** operator.

4. Locate and select the **Ansible Automation Platform** custom resource, and then click the required app.

5. Select the **YAML** tab.

6. Scroll the text to find the `spec` section under `Lightspeed` category. For example:

```
spec:
lightspeed:
disabled: false
model_config_secret_name: <Name of the model configuration secret that you recently created.>
```

7. Replace the `model_config_secret_name` value with the name of the IBM watsonx Code Assistant that you want to connect to.

8. Click **Save**.

The new Ansible Lightspeed pods are created. After the new pods are running successfully, the old Ansible Lightspeed pods are terminated.

