# 7. Troubleshooting
## 7.2. Troubleshooting Red Hat Ansible Lightspeed on-premise deployment errors
### 7.2.4. Cannot connect to the Ansible Lightspeed service due to SSL connection error




If you are using self-signed certificates on the model server, you might encounter SSL certification verification errors, causing the connection between Ansible Lightspeed service and the model server to fail. The following error message is displayed:

```
Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED]
certificate verify failed: self signed certificate in certificate chain (_ssl.c:1006)'))
```

To resolve this error, use one of the following workarounds based on your Red Hat Ansible Automation Platform version:

**For Red Hat Ansible Automation Platform 2.5:**

Specify the optional key/value pair as `model_verify_ssl=true` in the model secret to connect to an IBM watsonx Code Assistant model. For details about the procedure, see [Creating connection secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#create-connection-secrets_configuring-lightspeed-onpremise) .


**For Red Hat Ansible Automation Platform 2.4:**

You can disable the SSL protection between the model server and the Ansible Lightspeed service. For example, you can disable the SSL protection when you are on a testing environment. To disable the SSL protection, you must add the following extra setting in the Red Hat Ansible Lightspeed Custom Resource Definition (CRD) YAML file under the `spec:` section:


```
extra_settings:
- setting: ANSIBLE_AI_MODEL_MESH_API_VERIFY_SSL
value: false
```

Reenabling the SSL protection
You must re-enable the SSL protection when deploying on a production environment. To re-enable the SSL protection, simply remove the extra setting from the YAML file.



**Procedure**

1. Go to the Red Hat OpenShift Container Platform.
1. SelectOperators→Installed Operators.
1. From the **Projects** list, select the namespace that you created when you installed the Red Hat Ansible Automation Platform operator.
1. Locate and select the **Ansible Automation Platform (provided by Red Hat)** operator that you installed earlier.
1. Select the **Ansible Lightspeed** tab.
1. Find and select the instance you want to update.
1. Select the **YAML** tab. The editor switches to a YAML editor view.
1. Scroll and find the spec: section, and add the following parameter under the `    spec:` section:


```
extra_settings:        - setting: ANSIBLE_AI_MODEL_MESH_API_VERIFY_SSL          value: false
```


1. Click **Save** .
1. Restart the automation controller pods to apply the revised YAML.
Perform the following steps:


1. From the Red Hat OpenShift Container Platform, selectWorkloads→Pods.
1. Locate and select the Ansible Lightspeed pod that you updated.
1. Click the **Edit** icon beside the pod and select **Delete Pod** .
The select pod gets deleted and a new pod gets created.



