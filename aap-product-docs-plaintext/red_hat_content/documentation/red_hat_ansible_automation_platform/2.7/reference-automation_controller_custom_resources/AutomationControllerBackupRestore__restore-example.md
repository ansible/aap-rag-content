# Automation controller custom resources
## AutomationControllerBackup and AutomationControllerRestore [automationcontroller.ansible.com]
### Example AutomationControllerRestore custom resource

```
apiVersion: automationcontroller.ansible.com/v1beta1
kind: AutomationControllerRestore
metadata:
name: controller-restore
spec:
deployment_name: my-controller
backup_name: controller-backup
```
