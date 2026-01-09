# 12. Ansible Automation Platform Resource Operator
## 12.5. Create custom resources for Resource Operator
### 12.5.2. Creating a JobTemplate custom resource




A job template is a definition and set of parameters for running an Ansible job. For more information see the [Job Templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-job-templates) section of the _Using automation execution_ guide.

**Procedure**

- Create a job template on automation controller by creating a JobTemplate custom resource:


```
apiVersion: tower.ansible.com/v1alpha1    kind: JobTemplate    metadata:      name: jobtemplate-4    spec:      connection_secret: controller-access      job_template_name: ExampleJobTemplate4      job_template_project: Demo Project      job_template_playbook: hello_world.yml      job_template_inventory: Demo Inventory
```




