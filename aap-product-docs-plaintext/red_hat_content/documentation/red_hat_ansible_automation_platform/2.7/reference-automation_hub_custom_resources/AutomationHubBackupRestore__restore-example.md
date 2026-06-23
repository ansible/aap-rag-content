# Automation hub custom resources
## AutomationHubBackup and AutomationHubRestore [automationhub.ansible.com/v1beta1]
### Example AutomationHubRestore custom resource

```
apiVersion: automationhub.ansible.com/v1beta1
kind: AutomationHubRestore
metadata:
name: hub-restore
spec:
deployment_name: my-hub
backup_name: hub-backup
```
