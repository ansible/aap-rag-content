# AnsibleAutomationPlatformBackup and AnsibleAutomationPlatformRestore [aap.ansible.com/v1alpha1]
## Example restore custom resource

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformRestore
metadata:
name: restore-myaap
spec:
deployment_name: myaap
backup_name: custom-backup
```
