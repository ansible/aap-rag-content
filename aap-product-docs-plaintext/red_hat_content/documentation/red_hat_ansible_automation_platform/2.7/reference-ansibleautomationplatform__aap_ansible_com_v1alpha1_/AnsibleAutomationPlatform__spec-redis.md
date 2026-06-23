# AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]
## spec.redis

Configuration for the platform Redis pods.

| Field                   | Type    | Description                                                                                                                                                                                                                                                                  | Default            |
| ----------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `replicas`              | Integer | Number of Redis pod replicas.                                                                                                                                                                                                                                                | `1`                |
| `resource_requirements` | Object  | Kubernetes resource requests and limits for the Redis pods. See[Resource requirements object](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__resource-requirements). | See defaults table |

