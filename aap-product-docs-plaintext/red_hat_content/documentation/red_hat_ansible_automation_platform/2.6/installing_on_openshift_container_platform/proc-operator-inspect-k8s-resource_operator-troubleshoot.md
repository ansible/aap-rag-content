# 14. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 14.5. Inspecting a OpenShift Container Platform resource




To inspect a OpenShift Container Platform resource, you must use the `oc` command to get a summary or the full YAML definition of the resource.

**Procedure**

1. To view a human-readable summary of a resource, run:


```
oc describe -n &lt;namespace&gt; &lt;resource&gt; &lt;resource-name&gt;
```


1. To view the complete YAML definition of a resource, use the `    -o yaml` flag:


```
oc get -n &lt;namespace&gt; &lt;resource&gt; &lt;resource-name&gt; -o yaml
```


- For example, to get the YAML for the `        automationcontroller` custom resource, run:


```
oc get -n aap automationcontroller aap -o yaml
```





