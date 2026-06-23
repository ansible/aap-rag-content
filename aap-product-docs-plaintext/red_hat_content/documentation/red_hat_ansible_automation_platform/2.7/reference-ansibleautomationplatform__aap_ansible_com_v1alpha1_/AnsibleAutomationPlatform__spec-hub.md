# AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]
## spec.hub

Configuration for the automation hub component. In addition to the fields listed here, this section accepts all fields from `AutomationHub.spec`. For the full list of available fields, see [AutomationHub spec](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-automation_hub_custom_resources#AutomationHub__spec).

| Field      | Type    | Description                                                                               | Default |
| ---------- | ------- | ----------------------------------------------------------------------------------------- | ------- |
| `disabled` | Boolean | Set to`true` to disable the automation hub component.                                     | `false` |
| `name`     | String  | Name of an existing`AutomationHub` custom resource to register with the platform gateway. | -       |

