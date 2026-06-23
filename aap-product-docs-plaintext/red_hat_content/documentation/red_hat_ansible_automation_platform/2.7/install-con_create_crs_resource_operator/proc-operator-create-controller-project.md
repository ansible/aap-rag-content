# Create a custom resource for Resource Operator
## Create an automation controller project custom resource

A Project is a logical collection of Ansible playbooks, represented in automation controller. For more information see [Logically group playbooks with projects](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_projects "A project is a logical collection of Ansible playbooks, represented in automation controller.").

### About this task

### Procedure

Create a project on automation controller by creating an automation controller project custom resource:

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleProject
metadata:
name: git
spec:
repo: https://github.com/ansible/ansible-tower-samples
branch: main
name: ProjectDemo-git
scm_type: git
organization: Default
description: demoProject
connection_secret: aap-access
runner_pull_policy: IfNotPresent
```

