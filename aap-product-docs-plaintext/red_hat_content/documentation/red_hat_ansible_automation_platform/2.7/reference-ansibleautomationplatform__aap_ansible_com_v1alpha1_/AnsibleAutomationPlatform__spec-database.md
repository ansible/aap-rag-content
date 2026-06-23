# AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]
## spec.database

Configuration for the platform database.

| Field                   | Type   | Description                                                                                                                                                                                                                                                                                                                               | Default            |
| ----------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `database_secret`       | String | Name of a Kubernetes secret containing external database connection details. Required when using an external database instead of the operator-deployed database.                                                                                                                                                                          | -                  |
| `resource_requirements` | Object | Kubernetes resource requests and limits for the operator-deployed database pod. Ignored when using an external database. See[Resource requirements object](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__resource-requirements). | See defaults table |

