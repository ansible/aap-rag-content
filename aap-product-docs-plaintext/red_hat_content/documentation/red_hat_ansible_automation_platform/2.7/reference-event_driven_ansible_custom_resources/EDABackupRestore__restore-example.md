# Event-Driven Ansible custom resources
## EDABackup and EDARestore [eda.ansible.com/v1alpha1]
### Example EDARestore custom resource

```
apiVersion: eda.ansible.com/v1alpha1
kind: EDARestore
metadata:
name: eda-restore
spec:
deployment_name: my-eda
backup_name: eda-backup
```
