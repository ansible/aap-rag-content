# AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]
## Resource requirements object

All `resource_requirements` fields follow the standard Kubernetes resource specification pattern with `requests` and `limits`.

| Field             | Type   | Description                                                | Default             |
| ----------------- | ------ | ---------------------------------------------------------- | ------------------- |
| `requests.cpu`    | String | Minimum CPU allocation for the pod, for example`100m`.     | Varies by component |
| `requests.memory` | String | Minimum memory allocation for the pod, for example`256Mi`. | Varies by component |
| `limits.cpu`      | String | Maximum CPU the pod can consume, for example`500m`.        | Varies by component |
| `limits.memory`   | String | Maximum memory the pod can consume, for example`1000Mi`.   | Varies by component |

