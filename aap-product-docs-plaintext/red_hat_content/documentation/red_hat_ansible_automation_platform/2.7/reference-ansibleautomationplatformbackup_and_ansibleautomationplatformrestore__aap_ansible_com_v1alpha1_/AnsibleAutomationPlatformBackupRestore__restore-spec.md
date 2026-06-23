# AnsibleAutomationPlatformBackup and AnsibleAutomationPlatformRestore [aap.ansible.com/v1alpha1]
## AnsibleAutomationPlatformRestore spec

The `spec` fields for the `AnsibleAutomationPlatformRestore` custom resource.

| Field             | Type    | Description                                                                      | Default |
| ----------------- | ------- | -------------------------------------------------------------------------------- | ------- |
| `deployment_name` | String  | Name of the`AnsibleAutomationPlatform` instance to restore. Required.            | -       |
| `backup_name`     | String  | Name of the`AnsibleAutomationPlatformBackup` resource to restore from. Required. | -       |
| `no_log`          | Boolean | Suppress logging of sensitive data during the restore process.                   | `true`  |

