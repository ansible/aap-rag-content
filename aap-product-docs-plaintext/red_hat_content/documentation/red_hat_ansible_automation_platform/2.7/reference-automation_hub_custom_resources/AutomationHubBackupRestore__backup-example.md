# Automation hub custom resources
## AutomationHubBackup and AutomationHubRestore [automationhub.ansible.com/v1beta1]
### Example AutomationHubBackup custom resource

```
apiVersion: automationhub.ansible.com/v1beta1
kind: AutomationHubBackup
metadata:
name: hub-backup
spec:
deployment_name: my-hub
backup_pvc: hub-backup-pvc
backup_storage_requirements: 25Gi
create_backup_pvc: true
```

