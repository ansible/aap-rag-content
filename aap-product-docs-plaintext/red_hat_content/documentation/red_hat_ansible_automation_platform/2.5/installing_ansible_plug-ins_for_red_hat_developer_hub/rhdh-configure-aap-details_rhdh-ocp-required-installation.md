# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.5. Required configuration
### 2.5.5. Configuring Ansible Automation Platform details




The Ansible plug-ins query your Ansible Automation Platform subscription status with the controller API using a token.

Note
The Ansible plug-ins continue to function regardless of the Ansible Automation Platform subscription status.



**Procedure**

1. Create a Personal Access Token (PAT) with “Read” scope in automation controller, following the [Applications](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication#assembly-controller-applications) section of _Access management and authentication_ .
1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add your Ansible Automation Platform details to `    app-config-rhdh.yaml` .


1. Set the `        baseURL` key with your automation controller URL.
1. Set the `        token` key with the generated token value that you created in Step 1.
1. Set the `        checkSSL` key to `        true` or `        false` .

If `        checkSSL` is set to `        true` , the Ansible plug-ins verify whether the SSL certificate is valid.


```
data:          app-config-rhdh.yaml: |            ...            ansible:            ...              rhaap:                baseUrl: '&lt;https://MyControllerUrl&gt;'                token: '&lt;AAP Personal Access Token&gt;'                checkSSL: true
```





Note
You are responsible for protecting your Red Hat Developer Hub installation from external and unauthorized access. Manage the backend authentication key like any other secret. Meet strong password requirements, do not expose it in any configuration files, and only inject it into configuration files as an environment variable.



