# Event-Driven Ansible custom resources
## EDA [eda.ansible.com/v1alpha1]
### Specification

| Field                          | Type   | Description                                                                                                                                      | Default    |
| ------------------------------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `automation_server_url`        | String | URL of the automation controller instance for Event-Driven Ansible to connect to.                                                                | -          |
| `automation_server_ssl_verify` | String | Enable or disable SSL verification for the automation controller connection. Set to`no` to disable.                                              | `yes`      |
| `database`                     | Object | Database configuration. Contains`database_secret` (String) specifying the name of a Kubernetes secret with external database connection details. | -          |
| `api`                          | Object | Event-Driven Ansible API pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                                    | 1 replica  |
| `ui`                           | Object | Event-Driven Ansible UI pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                                     | 1 replica  |
| `scheduler`                    | Object | Event-Driven Ansible scheduler pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                              | 1 replica  |
| `default_worker`               | Object | Event-Driven Ansible default worker pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                         | 1 replica  |
| `activation_worker`            | Object | Event-Driven Ansible activation worker pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                      | 1 replica  |
| `event_stream`                 | Object | Event-Driven Ansible event stream pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                           | 1 replica  |
| `worker`                       | Object | Event-Driven Ansible worker pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                                 | 2 replicas |

