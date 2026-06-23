# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### JobTemplate

Creates a job template on the automation controller.

| Field                    | Type   | Description                                                                                 | Default |
| ------------------------ | ------ | ------------------------------------------------------------------------------------------- | ------- |
| `connection_secret`      | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -       |
| `job_template_name`      | String | Name of the job template to create.                                                         | -       |
| `job_template_project`   | String | Name of the project to associate with the job template.                                     | -       |
| `job_template_playbook`  | String | Name of the playbook file to run.                                                           | -       |
| `job_template_inventory` | String | Name of the inventory to associate with the job template.                                   | -       |


**Example:**

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

