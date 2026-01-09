# 13. Ansible Automation Platform Resource Operator
## 13.5. Create custom resources for Resource Operator
### 13.5.6. Creating an automation controller workflow template custom resource




A workflow job template links together a sequence of disparate resources to track the full set of jobs that were part of the release process as a single unit.

For more information see the [Workflow job templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-workflow-job-templates) section of the _Using automation execution_ guide.

**Procedure**

- Create a workflow template on automation controller by creating a workflow template custom resource:


```
apiVersion: tower.ansible.com/v1alpha1    kind: WorkflowTemplate    metadata:      name: workflowtemplate-sample    spec:      connection_secret: controller-access      name: ExampleTowerWorkflow      description: Example Workflow Template      organization: Default      inventory: Demo Inventory      workflow_nodes:      - identifier: node101        unified_job_template:          name: Demo Job Template          inventory:            organization:              name: Default          type: job_template      - identifier: node102        unified_job_template:          name: Demo Job Template          inventory:            organization:              name: Default          type: job_template
```




