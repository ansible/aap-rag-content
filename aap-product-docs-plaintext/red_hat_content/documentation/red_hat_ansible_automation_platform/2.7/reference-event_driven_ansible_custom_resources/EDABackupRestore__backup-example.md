# Event-Driven Ansible custom resources
## EDABackup and EDARestore [eda.ansible.com/v1alpha1]
### Example EDABackup custom resource

```
apiVersion: eda.ansible.com/v1alpha1
kind: EDABackup
metadata:
name: eda-backup
spec:
deployment_name: my-eda
backup_pvc: eda-backup-pvc
backup_storage_requirements: 7Gi
create_backup_pvc: true
```

