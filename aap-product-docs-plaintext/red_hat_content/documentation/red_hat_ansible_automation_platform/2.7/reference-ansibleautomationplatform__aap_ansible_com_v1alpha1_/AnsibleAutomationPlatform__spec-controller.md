# AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]
## spec.controller

Configuration for the automation controller component. In addition to the fields listed here, this section accepts all fields from `AutomationController.spec`. For the full list of available fields, see [AutomationController spec](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-automation_controller_custom_resources#AutomationControllerAndMeshIngress__controller-spec).

| Field      | Type    | Description                                                                                      | Default |
| ---------- | ------- | ------------------------------------------------------------------------------------------------ | ------- |
| `disabled` | Boolean | Set to`true` to disable the automation controller component.                                     | `false` |
| `name`     | String  | Name of an existing`AutomationController` custom resource to register with the platform gateway. | -       |

