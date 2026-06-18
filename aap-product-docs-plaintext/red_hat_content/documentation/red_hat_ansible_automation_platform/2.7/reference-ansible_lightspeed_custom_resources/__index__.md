# Ansible Lightspeed custom resources

The Ansible Lightspeed operator provides a custom resource for deploying and configuring the Ansible Lightspeed AI assistant service on OpenShift Container Platform.

The `AnsibleLightspeed` custom resource deploys and configures Ansible Lightspeed independently of the full Ansible Automation Platform deployment. Ansible Lightspeed provides AI-powered assistance for Ansible content creation. Use this custom resource when you need to manage Ansible Lightspeed as a standalone component rather than through the `AnsibleAutomationPlatform` resource.

## AnsibleLightspeed [lightspeed.ansible.com/v1alpha1]

The `AnsibleLightspeed` custom resource deploys and configures the Ansible Lightspeed AI assistant service.

### Description

| **API Group**   | `lightspeed.ansible.com` |
| --------------- | ------------------------ |
| **API Version** | `v1alpha1`               |
| **Kind**        | `AnsibleLightspeed`      |
| **Scope**       | Namespaced               |

### Specification

| Field                      | Type    | Description                                                                                                                                      | Default |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `disabled`                 | Boolean | Set to `true` to disable the Ansible Lightspeed component.                                                                                       | `true`  |
| `database`                 | Object  | Database configuration. Contains`database_secret` (String) specifying the name of a Kubernetes secret with external database connection details. | -       |
| `auth_config_secret_name`  | String  | Name of a Kubernetes secret containing authentication configuration for Ansible Lightspeed.                                                      | -       |
| `model_config_secret_name` | String  | Name of a Kubernetes secret containing model configuration for Ansible Lightspeed.                                                               | -       |

### Example custom resource

```
apiVersion: lightspeed.ansible.com/v1alpha1
kind: AnsibleLightspeed
metadata:
name: my-lightspeed
spec:
disabled: false
auth_config_secret_name: lightspeed-auth-config
model_config_secret_name: lightspeed-model-config
database:
database_secret: lightspeed-db-secret
```
