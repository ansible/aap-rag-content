# AnsibleAutomationPlatformBackup and AnsibleAutomationPlatformRestore [aap.ansible.com/v1alpha1]
## Component backup overrides

Each component section (`hub`, `controller`, `eda`) supports the following fields to override global backup settings.

| Field                         | Type    | Description                                                                                | Default               |
| ----------------------------- | ------- | ------------------------------------------------------------------------------------------ | --------------------- |
| `backup_pvc`                  | String  | Name of the PVC for this component's backup. Overrides the global`backup_pvc`.             | Inherited from global |
| `backup_storage_requirements` | String  | Storage size for this component's backup PVC, for example`25Gi`.                           | Inherited from global |
| `backup_storage_class`        | String  | Storage class for this component's backup PVC. Overrides the global`backup_storage_class`. | Inherited from global |
| `create_backup_pvc`           | Boolean | Set to `true` to have the operator create the PVC automatically.                           | `false`               |
| `no_log`                      | Boolean | Suppress logging of sensitive data for this component. Overrides the global `no_log`.      | Inherited from global |

