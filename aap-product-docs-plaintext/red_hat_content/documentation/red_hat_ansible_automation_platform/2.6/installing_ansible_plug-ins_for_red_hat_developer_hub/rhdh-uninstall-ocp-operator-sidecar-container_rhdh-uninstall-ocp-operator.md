# 7. Uninstalling an Operator installation on OpenShift Container Platform
## 7.3. Uninstalling the sidecar container




To remove the sidecar container for Ansible development tools from the developer-hub pod, you must modify the base ConfigMap for the Red Hat Developer Hub deployment.

**Procedure**

1. In the OpenShift console, select the **Topology** view.
1. Click **More actions ⋮** on the developer-hub instance and select **Edit backstage** to edit the base ConfigMap.
1. Select the **YAML** tab.
1. In the editing pane, remove the `    containers` block for the sidecar container from the `    spec.deployment.patch.spec.template.spec` block:


```
...    spec:      deployment:        patch:          spec:            template:              spec:                containers:                  - command:                      - adt                      - server                    image: ghcr.io/ansible/community-ansible-dev-tools:latest                    imagePullPolicy: always                    ports:                      - containerPort: 8000                        protocol: TCP                    terminationMessagePolicy: file
```


1. ClickSave.


