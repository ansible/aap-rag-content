# 14. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 14.4. Configuring log verbosity




You can enable task output for debugging on any custom resources (CRs) by setting `no_log` to `false` in the component section of the `AnsibleAutomationPlatform` CR.

The logs then show output for any failed tasks that originally had `no_log` set to `true` . All Ansible Automation Platform components (automation controller, automation hub, and Event-Driven Ansible) support the `no_log` setting.

**Procedure**

1. Edit the Ansible Automation Platform CR and set the `    no_log` field to `    false` for the component you want to debug.

For automation controller:


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: myaap    spec:      controller:        no_log: false
```

For automation hub:


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: myaap    spec:      hub:        no_log: false
```

For Event-Driven Ansible:


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: myaap    spec:      eda:        no_log: false
```

Note
This might expose sensitive data in the logs. On production clusters, this value must generally be set to `    true` unless you are actively debugging an issue.




1. To increase the Ansible Playbook verbosity from the operator, set the verbosity level using an annotation on the Ansible Automation Platform CR:


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: myaap      annotations:        ansible.sdk.operatorframework.io/verbosity: "4"    spec:      # ... component configuration ...
```




