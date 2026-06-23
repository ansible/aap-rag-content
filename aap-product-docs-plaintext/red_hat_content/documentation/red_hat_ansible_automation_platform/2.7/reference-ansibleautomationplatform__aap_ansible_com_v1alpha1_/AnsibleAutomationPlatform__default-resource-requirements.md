# AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]
## Default resource requirements

The following table lists the default resource requests and limits for each component.

| Component               | CPU request | Memory request | CPU limit | Memory limit |
| ----------------------- | ----------- | -------------- | --------- | ------------ |
| `api` (gateway)         | 100m        | 256Mi          | 500m      | 1000Mi       |
| `redis` (platform)      | 100m        | 256Mi          | 500m      | 500Mi        |
| `database`              | 100m        | 256Mi          | 500m      | 800Mi        |
| `controller.task`       | 100m        | 150Mi          | 1000m     | 1200Mi       |
| `controller.web`        | 100m        | 200Mi          | 200m      | 1600Mi       |
| `controller.ee`         | 100m        | 64Mi           | 1000m     | 500Mi        |
| `controller.redis`      | 50m         | 64Mi           | 100m      | 200Mi        |
| `controller.rsyslog`    | 100m        | 128Mi          | 500m      | 250Mi        |
| `controller.init`       | 100m        | 128Mi          | 500m      | 200Mi        |
| `eda.api`               | 50m         | 350Mi          | 500m      | 400Mi        |
| `eda.ui`                | 25m         | 64Mi           | 500m      | 150Mi        |
| `eda.scheduler`         | 50m         | 200Mi          | 500m      | 250Mi        |
| `eda.worker`            | 25m         | 200Mi          | 250m      | 250Mi        |
| `eda.default_worker`    | 25m         | 200Mi          | 500m      | 400Mi        |
| `eda.activation_worker` | 25m         | 150Mi          | 500m      | 400Mi        |
| `eda.event_stream`      | 25m         | 150Mi          | 100m      | 300Mi        |
| `hub.api`               | 150m        | 256Mi          | 800m      | 500Mi        |
| `hub.content`           | 150m        | 256Mi          | 800m      | 1200Mi       |
| `hub.worker`            | 150m        | 256Mi          | 800m      | 400Mi        |
| `hub.web`               | 100m        | 256Mi          | 500m      | 300Mi        |
| `hub.redis`             | 100m        | 250Mi          | 300m      | 400Mi        |

