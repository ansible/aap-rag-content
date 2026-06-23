# Event-Driven Ansible custom resources
## EDABackup and EDARestore [eda.ansible.com/v1alpha1]
### EDARestore spec

| Field             | Type    | Description                                                    | Default |
| ----------------- | ------- | -------------------------------------------------------------- | ------- |
| `deployment_name` | String  | Name of the`EDA` instance to restore. Required.                | -       |
| `backup_name`     | String  | Name of the`EDABackup` resource to restore from. Required.     | -       |
| `no_log`          | Boolean | Suppress logging of sensitive data during the restore process. | `true`  |

