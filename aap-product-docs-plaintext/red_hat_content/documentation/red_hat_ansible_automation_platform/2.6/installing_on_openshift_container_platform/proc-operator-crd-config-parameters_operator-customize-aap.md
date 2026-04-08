# 4. Customizing your Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 4.2. Discovering custom resource definition configuration parameters




The Ansible Automation Platform Operator manages multiple custom resources (CRs), each with its own configuration parameters. Use the `oc explain` command to discover all available configuration options for the `AnsibleAutomationPlatform` CR and its nested components.

**Procedure**

1. To see all available configuration parameters for a top-level CR, run:


```
oc explain ansibleautomationplatform.spec
```


1. To view component-specific configuration options nested under the Ansible Automation Platform CR, query them through the component section:


```
oc explain ansibleautomationplatform.spec.controller.postgres_configuration_secret    oc explain ansibleautomationplatform.spec.controller.route_tls_termination_mechanism    oc explain ansibleautomationplatform.spec.hub.storage_type    oc explain ansibleautomationplatform.spec.eda.automation_server_url
```


1. To explore all nested fields for a specific component, use the `    --recursive` flag:


```
oc explain ansibleautomationplatform.spec.controller --recursive    oc explain ansibleautomationplatform.spec.hub --recursive    oc explain ansibleautomationplatform.spec.eda --recursive
```

Note
You can also query individual component CRs directly if needed:


```
oc explain automationcontroller.spec    oc explain automationhub.spec    oc explain eda.spec
```

However, when configuring components through the Ansible Automation Platform CR (recommended approach), use the nested paths shown above.






