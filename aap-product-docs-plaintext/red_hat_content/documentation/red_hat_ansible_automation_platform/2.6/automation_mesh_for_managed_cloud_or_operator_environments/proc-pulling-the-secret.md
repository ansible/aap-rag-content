# 2. Automation mesh for operator-based Red Hat Ansible Automation Platform
## 2.8. Pulling the secret for OpenShift Container Platform deployments




Note
This does not apply to Ansible Automation Platform on Microsoft Azure.



If you are using the default execution environment provided with automation controller to run on remote execution nodes, you must add a pull secret in automation controller that contains the credential for pulling the execution environment image.

To do this, create a pull secret on the automation controller namespace and configure the `ee_pull_credentials_secret` parameter in the Operator as follows:

**Procedure**

1. Create a secret using the following command:


```
oc create secret generic ee-pull-secret \         --from-literal=username=&lt;username&gt; \         --from-literal=password=&lt;password&gt; \         --from-literal=url=registry.redhat.io
```


1. Add `    ee_pull_credentials_secret` and `    ee-pull-secret` to the specification by editing the deployment specification:


```
oc edit automationcontrollers aap-controller-o yaml
```

and add the following:


```
spec      ee_pull_credentials_secret=ee-pull-secret
```


1. To manage instances from the automation controller UI, you must have System Administrator or System Auditor permissions.


