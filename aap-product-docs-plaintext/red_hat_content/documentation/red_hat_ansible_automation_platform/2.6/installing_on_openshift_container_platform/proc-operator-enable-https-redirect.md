# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.1. Configuring platform gateway on Red Hat OpenShift Container Platform web console
### 5.1.3. Enabling HTTPS redirect for single sign-on (SSO) for platform gateway on OpenShift Container Platform




HTTPS redirect for SAML, allows you to log in once and access all of the platform gateway without needing to reauthenticate.

**Prerequisites**

- You have successfully configured SAML in the gateway from the Ansible Automation Platform Operator. Refer to [Configuring SAML authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#controller-set-up-SAML) for help with this.


**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Go toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select **All Instances** and go to your **AnsibleAutomationPlatform** instance.
1. Click the ⋮ icon and then selectEdit AnsibleAutomationPlatform.
1. In the **YAML view** paste the following YAML code under the `    spec:` section:


```
spec:      extra_settings:        - setting: REDIRECT_IS_HTTPS          value: '"True"'
```


1. ClickSave.


**Verification**

After you have added the `REDIRECT_IS_HTTPS` setting, wait for the pod to redeploy automatically. You can verify this setting makes it into the pod by running:


```
oc exec -it &lt;gateway-pod-name&gt; -- grep REDIRECT /etc/ansible-automation-platform/gateway/settings.py
```

