# 12. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 12.8. Discovering custom resource definition configuration parameters




The Ansible Automation Platform Operator manages multiple custom resources (CRs), each with its own configuration parameters. Use the `oc explain` command to discover all available configuration options for the `AnsibleAutomationPlatform` CR and its nested components.

**Procedure**

1. To see all available configuration parameters for a top-level CR, run:


```
oc explain ansibleautomationplatform.spec
```


1. To view specific nested sections, query them directly:


```
oc explain automationcontroller.spec.postgres_configuration_secret    oc explain automationcontroller.spec.route_tls_termination_mechanism
```


1. To explore all nested fields at once, use the `    --recursive` flag:


```
oc explain automationcontroller.spec --recursive
```




