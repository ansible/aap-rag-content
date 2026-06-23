# Create a custom resource for Resource Operator
## Create an automation controller workflow custom resource

Workflows enable you to configure a sequence of disparate job templates (or workflow templates) that may or may not share inventory, playbooks, or permissions. For more information see [Workflows in automation controller](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflows#controller-workflows "Workflows enable you to configure a sequence of disparate job templates (or workflow templates) that might or might not share inventory, playbooks, or permissions.") .

### About this task

### Procedure

Create a workflow on automation controller by creating a workflow custom resource:

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleWorkflow
metadata:
name: workflow
spec:
inventory: Demo Inventory
workflow_template_name: Demo Job Template
connection_secret: aap-access
runner_pull_policy: IfNotPresent
```

