# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### AnsibleWorkflow

Creates a workflow on the automation controller.

| Field                    | Type   | Description                                                                                 | Default        |
| ------------------------ | ------ | ------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`      | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -              |
| `workflow_template_name` | String | Name of the workflow template.                                                              | -              |
| `inventory`              | String | Name of the inventory to associate with the workflow.                                       | -              |
| `runner_pull_policy`     | String | Image pull policy for the runner pod.                                                       | `IfNotPresent` |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleWorkflow
metadata:
name: workflow
spec:
connection_secret: aap-access
workflow_template_name: Demo Job Template
inventory: Demo Inventory
```

