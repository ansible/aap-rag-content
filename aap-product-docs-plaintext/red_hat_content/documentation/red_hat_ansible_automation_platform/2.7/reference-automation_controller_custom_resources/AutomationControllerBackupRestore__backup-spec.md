# Automation controller custom resources
## AutomationControllerBackup and AutomationControllerRestore [automationcontroller.ansible.com]
### AutomationControllerBackup spec

| Field                         | Type    | Description                                                          | Default |
| ----------------------------- | ------- | -------------------------------------------------------------------- | ------- |
| `deployment_name`             | String  | Name of the `AutomationController` instance to back up. Required.    | -       |
| `no_log`                      | Boolean | Suppress logging of sensitive data during the backup process.        | `true`  |
| `backup_pvc`                  | String  | Name of the persistent volume claim (PVC) to use for backup storage. | -       |
| `backup_storage_class`        | String  | Kubernetes storage class for the backup PVC.                         | -       |
| `backup_storage_requirements` | String  | Storage size for the backup PVC, for example `15Gi`.                 | -       |
| `create_backup_pvc`           | Boolean | Set to `true` to have the operator create the PVC automatically.     | `false` |

