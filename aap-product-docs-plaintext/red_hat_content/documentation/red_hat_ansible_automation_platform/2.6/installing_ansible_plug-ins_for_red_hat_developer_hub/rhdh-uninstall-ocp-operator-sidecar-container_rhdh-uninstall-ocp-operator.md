# 7. Uninstalling an Operator installation on OpenShift Container Platform
## 7.3. Uninstalling the sidecar container




To remove the sidecar container for Ansible development tools from the developer-hub pod, you must modify the base ConfigMap for the Red Hat Developer Hub deployment.

**Procedure**

1. In the OpenShift console, select the **Topology** view.
1. Click **More actions ⋮** on the developer-hub instance and select **Edit backstage** to edit the base ConfigMap.
1. Select the **YAML** tab.
1. In the editing pane, remove the `    containers` block for the sidecar container from the `    spec.deployment.patch.spec.template.spec` block:


```
...    spec:      deployment:        patch:          spec:            template:              spec:                containers:                  - command:                      - adt                      - server                    image: registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest                    imagePullPolicy: always                    ports:                      - containerPort: 8000                        protocol: TCP                    terminationMessagePolicy: file
```


1. ClickSave.
1. If you used OCI delivery, delete the registry auth secret:


```
oc delete secret &lt;deployment-name&gt;-dynamic-plugins-registry-auth
```


1. If you used the HTTP plug-in registry, remove the plug-in registry application:


```
oc delete all -l app=plugin-registry
```




