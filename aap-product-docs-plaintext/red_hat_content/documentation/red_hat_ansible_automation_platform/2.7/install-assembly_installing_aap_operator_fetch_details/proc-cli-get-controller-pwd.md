# Access Ansible Automation Platform through the CLI
## Fetch the platform gateway password

The YAML block for the platform gateway instance in the `AnsibleAutomationPlatform` object assigns values to the *name* and *admin_user* keys.

### About this task

### Procedure

1.  Use these values in the following command to fetch the password for the platform gateway instance.

```
oc get secret/<your instance name>-<admin_user>-password -o yaml
```

2.  The default value for *admin_user* is `admin`. Modify the command if you changed the admin username in the `AnsibleAutomationPlatform` object. The following example retrieves the password for a platform gateway object called `example`:

```
oc get secret/example-admin-password -o yaml
```
The base64 encoded password for the platform gateway instance is listed in the `metadata` field in the output:

```
$ oc get secret/example-admin-password -o yaml

apiVersion: v1
data:
password: ODzLODzLODzLODzLODzLODzLODzLODzLODzLODzLODzL
kind: Secret
metadata:
labels:
app.kubernetes.io/component: aap
app.kubernetes.io/name: example
app.kubernetes.io/operator-version: ""
app.kubernetes.io/part-of: example
name: example-admin-password
namespace: ansible-automation-platform
```

