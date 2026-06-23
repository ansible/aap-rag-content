# Automation controller custom resources
## AutomationController and AutomationControllerMeshIngress [automationcontroller.ansible.com]
### AutomationController spec

The `spec` fields for the `AutomationController` custom resource.

| Field                                  | Type    | Description                                                                                                           | Default                               |
| -------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `image_pull_policy`                    | String  | Image pull policy for automation controller pods. Options: `Always`, `Never`, `IfNotPresent`.                         | `IfNotPresent`                        |
| `postgres_configuration_secret`        | String  | Name of a Kubernetes secret containing external PostgreSQL connection details for the automation controller database. | -                                     |
| `route_tls_termination_mechanism`      | String  | TLS termination mechanism for the automation controller route.                                                        | -                                     |
| `uwsgi_processes`                      | Integer | Number of uWSGI worker processes for the web pod.                                                                     | `2`                                   |
| `termination_grace_period_seconds`     | Integer | Grace period in seconds for running jobs to complete before the pod terminates.                                       | -                                     |
| `ee_extra_env`                         | String  | Extra environment variables to pass to execution environment pods.                                                    | -                                     |
| `extra_settings`                       | Array   | List of additional automation controller settings as name-value pairs.                                                | -                                     |
| `task_affinity`                        | Object  | Kubernetes pod affinity rules for the task pod.                                                                       | -                                     |
| `web_affinity`                         | Object  | Kubernetes pod affinity rules for the web pod.                                                                        | -                                     |
| `task_resource_requirements`           | Object  | Kubernetes resource requests and limits for the task pod.                                                             | cpu: 100m/1000m, memory: 150Mi/1200Mi |
| `web_resource_requirements`            | Object  | Kubernetes resource requests and limits for the web pod.                                                              | cpu: 100m/200m, memory: 200Mi/1600Mi  |
| `ee_resource_requirements`             | Object  | Kubernetes resource requests and limits for execution environment pods.                                               | cpu: 100m/1000m, memory: 64Mi/500Mi   |
| `redis_resource_requirements`          | Object  | Kubernetes resource requests and limits for the automation controller Redis pod.                                      | cpu: 50m/100m, memory: 64Mi/200Mi     |
| `rsyslog_resource_requirements`        | Object  | Kubernetes resource requests and limits for the rsyslog pod.                                                          | cpu: 100m/500m, memory: 128Mi/250Mi   |
| `init_container_resource_requirements` | Object  | Kubernetes resource requests and limits for init containers.                                                          | cpu: 100m/500m, memory: 128Mi/200Mi   |

