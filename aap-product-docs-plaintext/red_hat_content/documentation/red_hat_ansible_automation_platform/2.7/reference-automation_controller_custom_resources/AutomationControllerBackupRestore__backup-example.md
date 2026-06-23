# Automation controller custom resources
## AutomationControllerBackup and AutomationControllerRestore [automationcontroller.ansible.com]
### Example AutomationControllerBackup custom resource

```
apiVersion: automationcontroller.ansible.com/v1beta1
kind: AutomationControllerBackup
metadata:
name: controller-backup
spec:
deployment_name: my-controller
backup_pvc: controller-backup-pvc
backup_storage_requirements: 15Gi
create_backup_pvc: true
```

