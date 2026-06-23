# Automation hub custom resources
## AutomationHubBackup and AutomationHubRestore [automationhub.ansible.com/v1beta1]
### AutomationHubRestore spec

| Field             | Type    | Description                                                          | Default |
| ----------------- | ------- | -------------------------------------------------------------------- | ------- |
| `deployment_name` | String  | Name of the`AutomationHub` instance to restore. Required.            | -       |
| `backup_name`     | String  | Name of the`AutomationHubBackup` resource to restore from. Required. | -       |
| `no_log`          | Boolean | Suppress logging of sensitive data during the restore process.       | `true`  |

