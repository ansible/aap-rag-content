# 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform
## 3.3. Adding a sidecar container for Ansible development tools to the RHDH Operator Custom Resource




Add a sidecar container for Ansible development tools in the Developer Hub pod. To do this, you must modify the base ConfigMap for the Red Hat Developer Hub deployment.

**Procedure**

1. In the OpenShift console, select the **Topology** view.
1. Click **More actions ⋮** on the developer-hub instance and select **Edit backstage** to open the **Backstage details** page.
1. Select the **YAML** tab.
1. In the editing pane, add a `    containers` block in the `    spec.deployment.patch.spec.template.spec` block:


```
apiVersion: rhdh.redhat.com/v1alpha4    kind: Backstage    metadata:      name: developer-hub    spec:      deployment:        patch:          spec:            template:              spec:                containers:                  - command:                      - adt                      - server                    image: registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest                    imagePullPolicy: always                    ports:                      - containerPort: 8000                        protocol: TCP                    terminationMessagePolicy: file
```


1. ClickSave.

Note
If you want to add extra environment variables to your deployment, you can add them in the `    spec.application.extraEnvs` block:


```
spec:      application:        ...        extraEnvs:          envs:            - name: &lt;env_variable_name&gt;              value: &lt;env_variable_value&gt;
```






