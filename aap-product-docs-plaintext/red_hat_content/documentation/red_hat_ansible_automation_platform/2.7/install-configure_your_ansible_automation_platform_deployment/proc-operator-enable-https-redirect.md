# Configure your Ansible Automation Platform deployment
## Enable HTTPS redirect for single sign-on

HTTPS redirect for SAML, allows you to log in once and access all of the platform gateway without needing to reauthenticate.

### Before you begin

- You have successfully configured SAML in the gateway from the Ansible Automation Platform Operator. Refer to [Configuring SAML authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_saml#controller-set-up-SAML "SAML allows the exchange of authentication and authorization data between an Identity Provider (IdP) and a Service Provider (SP). Ansible Automation Platform is a SAML SP that you can configure to talk with one or more SAML IdPs to authenticate users.") for help with this.

### About this task

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Go to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select **All Instances** and go to your **AnsibleAutomationPlatform** instance.
5.  Click the ⋮ icon and then select Edit AnsibleAutomationPlatform.
6.  In the **YAML view** paste the following YAML code under the `spec:` section:


```
spec:
extra_settings:
- setting: REDIRECT_IS_HTTPS
value: '"True"'
```

7.  Click Save.

### Results

After you have added the `REDIRECT_IS_HTTPS` setting, wait for the pod to redeploy automatically. You can verify this setting makes it into the pod by running:

```
oc exec -it <gateway-pod-name> -- grep REDIRECT /etc/ansible-automation-platform/gateway/settings.py
```

