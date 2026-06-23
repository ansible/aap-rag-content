# AnsibleAutomationPlatformBackup and AnsibleAutomationPlatformRestore [aap.ansible.com/v1alpha1]
## Example backup custom resource

The following example shows a backup custom resource with per-component overrides for PVC names, storage sizes, and storage classes:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformBackup
metadata:
name: custom-backup
spec:
deployment_name: myaap
no_log: false
backup_storage_class: rook-cephfs
hub:
backup_pvc: custom-hub-backup-pvc
backup_storage_requirements: 25Gi
backup_storage_class: rook-cephfs
create_backup_pvc: true
no_log: false
controller:
backup_pvc: custom-controller-backup-pvc
backup_storage_requirements: 15Gi
backup_storage_class: rook-block
create_backup_pvc: true
no_log: false
eda:
backup_pvc: custom-eda-backup-pvc
backup_storage_requirements: 7Gi
backup_storage_class: rook-block
create_backup_pvc: true
no_log: false
```

