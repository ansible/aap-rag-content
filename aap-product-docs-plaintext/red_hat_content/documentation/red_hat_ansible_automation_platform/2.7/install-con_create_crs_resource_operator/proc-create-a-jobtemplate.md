# Create a custom resource for Resource Operator
## Create a JobTemplate custom resource

A job template is a definition and set of parameters for running an Ansible job. For more information see [Standardize and streamline automation with automation job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .").

### About this task

### Procedure

Create a job template on automation controller by creating a JobTemplate custom resource:

```
apiVersion: tower.ansible.com/v1alpha1
kind: JobTemplate
metadata:
name: jobtemplate-4
spec:
connection_secret: aap-access
job_template_name: ExampleJobTemplate4
job_template_project: Demo Project
job_template_playbook: hello_world.yml
job_template_inventory: Demo Inventory
```

