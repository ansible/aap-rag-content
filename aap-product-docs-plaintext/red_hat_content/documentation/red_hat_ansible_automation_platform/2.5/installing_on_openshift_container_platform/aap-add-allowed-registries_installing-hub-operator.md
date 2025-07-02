# 3. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 3.3. Configuring automation hub on Red Hat OpenShift Container Platform web console
### 3.3.6. Adding allowed registries to the automation controller image configuration




Before you can deploy a container image in automation hub, you must add the registry to the `allowedRegistries` in the automation controller image configuration. To do this you can copy and paste the following code into your automation controller image YAML.

**Procedure**

1. Log in to **Red Hat OpenShift Container Platform** .
1. Navigate toHome→Search.
1. Select the **Resources** drop-down list and type "Image".
1. Select **Image (config,openshift.io/v1)** .
1. ClickClusterunder the **Name** heading.
1. Select theYAMLtab.
1. Paste in the following under spec value:


```
spec:      registrySources:        allowedRegistries:        - quay.io        - registry.redhat.io        - image-registry.openshift-image-registry.svc:5000        - &lt;OCP route for your automation hub&gt;
```


1. ClickSave.


