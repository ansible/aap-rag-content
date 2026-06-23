# Troubleshoot your Operator-based deployment of Ansible Automation Platform
## Inspect a OpenShift Container Platform resource

To inspect a OpenShift Container Platform resource, you must use the `oc` command to get a summary or the full YAML definition of the resource.

### Procedure

1.  To view a human-readable summary of a resource, run:


```
oc describe -n <namespace> <resource> <resource-name>
```

2.  To view the complete YAML definition of a resource, use the `-o yaml` flag:


```
oc get -n <namespace> <resource> <resource-name> -o yaml
```
- For example, to get the YAML for the `automationcontroller` custom resource, run:

```
oc get -n aap automationcontroller aap -o yaml
```

