# 4. Setting up Red Hat Ansible Lightspeed for your organization
## 4.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 4.3.4. Updating the YAML file of the Ansible Automation Platform operator




After you create the model configuration secret, you must update the YAML file of the Ansible Automation Platform operator to use the secret.

**Procedure**

1. Go to the Red Hat OpenShift Container Platform.
1. SelectOperators→Installed Operators.
1. From the list of installed operators, select the **Ansible Automation Platform** operator.
1. Locate and select the **Ansible Automation Platform** custom resource, and then click the required app.
1. Select the **YAML** tab.
1. Scroll the text to find the `    Lightspeed` category, and add the following details under the `    spec:` section:


```
spec:      lightspeed:        disabled: false        model_config_secret_name: &lt;Name of the model configuration secret that you recently created.&gt;
```


1. Click **Save** . The Ansible Lightspeed service takes a few minutes to set up.


