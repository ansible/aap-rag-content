# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### AnsibleJob

Launches a job or workflow job template on the automation controller instance specified in the connection secret.

| Field                    | Type    | Description                                                                                              | Default |
| ------------------------ | ------- | -------------------------------------------------------------------------------------------------------- | ------- |
| `connection_secret`      | String  | Name of the Kubernetes secret containing the platform gateway connection details. Required.              | -       |
| `job_template_name`      | String  | Name of the job template to launch. Specify either this or `workflow_template_name`.                     | -       |
| `workflow_template_name` | String  | Name of the workflow job template to launch. Specify either this or `job_template_name`.                 | -       |
| `inventory`              | String  | Name of the inventory to use. Prompt on launch must be enabled on the template.                          | -       |
| `extra_vars`             | Object  | Extra variables to pass to the job as key-value pairs. Prompt on launch must be enabled on the template. | -       |
| `job_tags`               | String  | Comma-separated list of tags to run, for example `"provision,install,configuration"`.                    | -       |
| `skip_tags`              | String  | Comma-separated list of tags to skip, for example `"configuration,restart"`.                             | -       |
| `runner_image`           | String  | Container image for the runner pod.                                                                      | -       |
| `runner_version`         | String  | Version of the runner image to use.                                                                      | -       |
| `job_ttl`                | Integer | Time to live in seconds for the job resource after completion.                                           | -       |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleJob
metadata:
generateName: demo-job-1
spec:
connection_secret: aap-access
job_template_name: Demo Job Template
inventory: Demo Inventory
extra_vars:
test_var: test
job_tags: "provision,install"
```

