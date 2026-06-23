# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### AnsibleInstanceGroup

Creates an instance group on the automation controller for organizing and managing execution capacity.

| Field                | Type   | Description                                                                                 | Default        |
| -------------------- | ------ | ------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`  | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -              |
| `name`               | String | Display name for the instance group.                                                        | -              |
| `runner_pull_policy` | String | Image pull policy for the runner pod.                                                       | `IfNotPresent` |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleInstanceGroup
metadata:
name: my-instance-group
spec:
connection_secret: aap-access
name: production-instances
```
