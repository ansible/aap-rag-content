# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### AnsibleProject

Creates a project (a logical collection of Ansible playbooks) on the automation controller.

| Field                | Type   | Description                                                                                 | Default        |
| -------------------- | ------ | ------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`  | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -              |
| `repo`               | String | URL of the source control repository.                                                       | -              |
| `branch`             | String | Branch of the source control repository to use.                                             | -              |
| `name`               | String | Display name for the project in the automation controller.                                  | -              |
| `scm_type`           | String | Source control type, for example `git`.                                                     | -              |
| `organization`       | String | Organization the project belongs to.                                                        | -              |
| `description`        | String | Description of the project.                                                                 | -              |
| `runner_pull_policy` | String | Image pull policy for the runner pod. Options: `Always`, `Never`, `IfNotPresent`.           | `IfNotPresent` |


**Example:**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleProject
metadata:
name: git
spec:
connection_secret: aap-access
repo: https://github.com/ansible/ansible-tower-samples
branch: main
name: ProjectDemo-git
scm_type: git
organization: Default
```

