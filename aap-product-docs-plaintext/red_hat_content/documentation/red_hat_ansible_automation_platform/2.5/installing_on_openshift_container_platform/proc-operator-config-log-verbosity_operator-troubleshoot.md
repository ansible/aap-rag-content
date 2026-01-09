# 13. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 13.4. Configuring log verbosity




You can enable task output for debugging on any custom resources (CRs) by setting `no_log` to `false` in the `spec` section of the CR.

The logs then show output for any failed tasks that originally had `no_log` set to `true` . The following procedure uses automation controller as an example, but every CR listed in the [Core Ansible Automation Platform Resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#ref-operator-core-aap-resources_operator-troubleshoot) section supports `no_log` .

**Procedure**

1. Edit the automation controller CR and set the `    no_log` field to `    false` in the spec.


```
apiVersion: automationcontroller.ansible.com/v1beta1    kind: AutomationController    metadata:      name: controller-demo    spec:      no_log: false
```

Note
This might expose sensitive data in the logs. On production clusters, this value must generally be set to `    true` unless you are actively debugging an issue.




1. To increase the Ansible Playbook verbosity from the operator, set the verbosity level using an annotation:


```
annotations:        ansible.sdk.operatorframework.io/verbosity: "4"
```




