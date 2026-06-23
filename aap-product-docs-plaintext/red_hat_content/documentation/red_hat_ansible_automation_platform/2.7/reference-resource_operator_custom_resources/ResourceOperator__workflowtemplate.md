# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### WorkflowTemplate

Creates a workflow job template that links together a sequence of job templates on the automation controller.

| Field               | Type   | Description                                                                                                                                                               | Default |
| ------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `connection_secret` | String | Name of the Kubernetes secret containing the platform gateway connection details. Required.                                                                               | -       |
| `name`              | String | Display name for the workflow template.                                                                                                                                   | -       |
| `description`       | String | Description of the workflow template.                                                                                                                                     | -       |
| `organization`      | String | Organization the workflow template belongs to.                                                                                                                            | -       |
| `inventory`         | String | Default inventory for the workflow template.                                                                                                                              | -       |
| `workflow_nodes`    | Array  | List of workflow nodes defining the sequence of jobs. Each node contains an `identifier` and a `unified_job_template` object with `name`, `type`, and `inventory` fields. | -       |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: WorkflowTemplate
metadata:
name: workflowtemplate-sample
spec:
connection_secret: aap-access
name: ExampleWorkflow
organization: Default
inventory: Demo Inventory
workflow_nodes:
- identifier: node101
unified_job_template:
name: Demo Job Template
type: job_template
- identifier: node102
unified_job_template:
name: Demo Job Template
type: job_template
```

