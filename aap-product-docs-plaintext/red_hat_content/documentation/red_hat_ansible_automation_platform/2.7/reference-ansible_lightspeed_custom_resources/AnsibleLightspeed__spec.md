# Ansible Lightspeed custom resources
## AnsibleLightspeed [lightspeed.ansible.com/v1alpha1]
### Specification

| Field                      | Type    | Description                                                                                                                                      | Default |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `disabled`                 | Boolean | Set to `true` to disable the Ansible Lightspeed component.                                                                                       | `true`  |
| `database`                 | Object  | Database configuration. Contains`database_secret` (String) specifying the name of a Kubernetes secret with external database connection details. | -       |
| `auth_config_secret_name`  | String  | Name of a Kubernetes secret containing authentication configuration for Ansible Lightspeed.                                                      | -       |
| `model_config_secret_name` | String  | Name of a Kubernetes secret containing model configuration for Ansible Lightspeed.                                                               | -       |

