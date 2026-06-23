# Automation controller custom resources
## AutomationControllerBackup and AutomationControllerRestore [automationcontroller.ansible.com]
### AutomationControllerRestore spec

| Field             | Type    | Description                                                                  | Default |
| ----------------- | ------- | ---------------------------------------------------------------------------- | ------- |
| `deployment_name` | String  | Name of the `AutomationController` instance to restore. Required.            | -       |
| `backup_name`     | String  | Name of the `AutomationControllerBackup` resource to restore from. Required. | -       |
| `no_log`          | Boolean | Suppress logging of sensitive data during the restore process.               | `true`  |

