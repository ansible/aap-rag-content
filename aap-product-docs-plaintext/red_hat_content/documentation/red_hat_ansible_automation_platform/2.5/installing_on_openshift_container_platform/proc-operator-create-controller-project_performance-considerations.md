# 11. Ansible Automation Platform Resource Operator
## 11.5. Creating custom resources for Resource Operator
### 11.5.3. Creating an automation controller project custom resource




A Project is a logical collection of Ansible playbooks, represented in automation controller. For more information see the [Projects](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-projects) section of the _Using automation execution_ guide.

**Procedure**

- Create a project on automation controller by creating an automation controller project custom resource:


```
apiVersion: tower.ansible.com/v1alpha1    kind: AnsibleProject    metadata:      name: git    spec:      repo: https://github.com/ansible/ansible-tower-samples      branch: main      name: ProjectDemo-git      scm_type: git      organization: Default      description: demoProject      connection_secret: controller-access      runner_pull_policy: IfNotPresent
```




