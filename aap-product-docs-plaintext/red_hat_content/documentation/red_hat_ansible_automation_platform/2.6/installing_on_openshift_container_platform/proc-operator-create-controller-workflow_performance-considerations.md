# 11. Ansible Automation Platform Resource Operator
## 11.5. Creating custom resources for Resource Operator
### 11.5.5. Creating an automation controller workflow custom resource




Workflows enable you to configure a sequence of disparate job templates (or workflow templates) that may or may not share inventory, playbooks, or permissions. For more information see the [Workflows in automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-workflows) section of the _Using automation execution_ guide.

**Procedure**

- Create a workflow on automation controller by creating a workflow custom resource:


```
apiVersion: tower.ansible.com/v1alpha1    kind: AnsibleWorkflow    metadata:      name: workflow    spec:      inventory: Demo Inventory      workflow_template_name: Demo Job Template      connection_secret: controller-access      runner_pull_policy: IfNotPresent
```




