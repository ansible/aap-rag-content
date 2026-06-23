# Create a custom resource for Resource Operator
## Create an automation controller workflow template custom resource

A workflow job template links together a sequence of disparate resources to track the full set of jobs that were part of the release process as a single unit.

### About this task

For more information see [Workflow job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflow_job_templates "A workflow job template links together a sequence of disparate resources that tracks the full set of jobs that were part of the release process as a single unit.") .

### Procedure

Create a workflow template on automation controller by creating a workflow template custom resource:

```
apiVersion: tower.ansible.com/v1alpha1
kind: WorkflowTemplate
metadata:
name: workflowtemplate-sample
spec:
connection_secret: aap-access
name: ExampleTowerWorkflow
description: Example Workflow Template
organization: Default
inventory: Demo Inventory
workflow_nodes:
- identifier: node101
unified_job_template:
name: Demo Job Template
inventory:
organization:
name: Default
type: job_template
- identifier: node102
unified_job_template:
name: Demo Job Template
inventory:
organization:
name: Default
type: job_template
```

