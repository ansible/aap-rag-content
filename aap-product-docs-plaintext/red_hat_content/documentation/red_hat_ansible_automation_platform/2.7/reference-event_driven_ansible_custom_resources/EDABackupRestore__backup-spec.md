# Event-Driven Ansible custom resources
## EDABackup and EDARestore [eda.ansible.com/v1alpha1]
### EDABackup spec

| Field                         | Type    | Description                                                          | Default |
| ----------------------------- | ------- | -------------------------------------------------------------------- | ------- |
| `deployment_name`             | String  | Name of the`EDA` instance to back up. Required.                      | -       |
| `no_log`                      | Boolean | Suppress logging of sensitive data during the backup process.        | `true`  |
| `backup_pvc`                  | String  | Name of the persistent volume claim (PVC) to use for backup storage. | -       |
| `backup_storage_class`        | String  | Kubernetes storage class for the backup PVC.                         | -       |
| `backup_storage_requirements` | String  | Storage size for the backup PVC, for example`7Gi`.                   | -       |
| `create_backup_pvc`           | Boolean | Set to`true` to have the operator create the PVC automatically.      | `false` |

