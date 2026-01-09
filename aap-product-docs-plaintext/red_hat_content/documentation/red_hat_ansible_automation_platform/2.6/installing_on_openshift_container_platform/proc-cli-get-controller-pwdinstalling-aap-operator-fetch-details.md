# 2. Installing Red Hat Ansible Automation Platform gateway on Red Hat OpenShift Container Platform
## 2.4. Accessing platform gateway through the OpenShift Container Platform CLI
### 2.4.2. Fetching the platform gateway password




The YAML block for the platform gateway instance in the `AnsibleAutomationPlatform` object assigns values to the _name_ and _admin_user_ keys.

**Procedure**

1. Use these values in the following command to fetch the password for the platform gateway instance.


```
oc get secret/&lt;your instance name&gt;-&lt;admin_user&gt;-password -o yaml
```


1. The default value for _admin_user_ is `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">admin</span></em></span>` . Modify the command if you changed the admin username in the `    AnsibleAutomationPlatform` object.

The following example retrieves the password for a platform gateway object called `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">example</span></em></span>` :


```
oc get secret/example-admin-password -o yaml
```

The base64 encoded password for the platform gateway instance is listed in the `    metadata` field in the output:


```
$ oc get secret/example-admin-password -o yaml        apiVersion: v1    data:      password: ODzLODzLODzLODzLODzLODzLODzLODzLODzLODzLODzL    kind: Secret    metadata:      labels:        app.kubernetes.io/component: aap        app.kubernetes.io/name: example        app.kubernetes.io/operator-version: ""        app.kubernetes.io/part-of: example      name: example-admin-password      namespace: ansible-automation-platform
```




