# AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]
## spec.eda

Configuration for the Event-Driven Ansible component. In addition to the fields listed here, this section accepts all fields from `EDA.spec`. For the full list of available fields, see [EDA spec](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-event_driven_ansible_custom_resources#EDA__spec).

| Field      | Type    | Description                                                                     | Default |
| ---------- | ------- | ------------------------------------------------------------------------------- | ------- |
| `disabled` | Boolean | Set to`true` to disable the Event-Driven Ansible component.                     | `false` |
| `name`     | String  | Name of an existing`EDA` custom resource to register with the platform gateway. | -       |

