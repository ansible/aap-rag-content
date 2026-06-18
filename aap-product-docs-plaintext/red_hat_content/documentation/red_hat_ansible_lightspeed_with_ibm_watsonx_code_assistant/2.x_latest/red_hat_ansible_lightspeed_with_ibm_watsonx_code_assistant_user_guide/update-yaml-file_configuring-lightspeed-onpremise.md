# 4. Setting up Red Hat Ansible Lightspeed for your organization
## 4.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 4.3.4. Updating the YAML file of the Ansible Automation Platform operator

After you create the model configuration secret, you must update the YAML file of the Ansible Automation Platform operator to use the secret.

**Procedure**

1. Go to the Red Hat OpenShift Container Platform.

2. Select Operators → Installed Operators.

3. From the list of installed operators, select the **Ansible Automation Platform** operator.

4. Locate and select the **Ansible Automation Platform** custom resource, and then click the required app.

5. Select the **YAML** tab.

6. Scroll the text to find the `Lightspeed` category, and add the following details under the `spec:` section:

```
spec:
lightspeed:
disabled: false
model_config_secret_name: <Name of the model configuration secret that you recently created.>
```

7. Click **Save**. The Ansible Lightspeed service takes a few minutes to set up.

