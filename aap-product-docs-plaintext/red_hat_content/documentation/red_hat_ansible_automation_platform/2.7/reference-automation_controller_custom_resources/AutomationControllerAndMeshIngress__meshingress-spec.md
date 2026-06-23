# Automation controller custom resources
## AutomationController and AutomationControllerMeshIngress [automationcontroller.ansible.com]
### AutomationControllerMeshIngress spec

The `spec` fields for the `AutomationControllerMeshIngress` custom resource.

| Field             | Type   | Description                                                                                                                                      | Default |
| ----------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `deployment_name` | String | Name of the `AutomationController` instance to attach the mesh ingress to. Required. Must be in the same namespace as the mesh ingress resource. | -       |

