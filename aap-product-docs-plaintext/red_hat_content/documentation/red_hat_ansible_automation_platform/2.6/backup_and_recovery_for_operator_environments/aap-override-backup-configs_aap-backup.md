# 2. Creating Red Hat Ansible Automation Platform backup resources
## 2.3. Custom backup configurations for specific components




You can override the global backup configuration for specific components, such as automation controller, private automation hub, or Event-Driven Ansible controller. This enables each component to use its own storage class, PVC name, storage size, or resource limits during the backup process.

**Example: Overriding component backup settings**

In this backup custom resource, each component has a unique PVC name and storage class:


```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformBackup
metadata:
name: custom-backup
spec:
deployment_name: myaap
no_log: false
backup_storage_class: rook-cephfs<span id="CO2-1"><!--Empty--></span><span class="callout">1</span>hub:
backup_pvc: custom-hub-backup-pvc<span id="CO2-2"><!--Empty--></span><span class="callout">2</span>backup_storage_requirements: 25Gi
backup_storage_class: rook-cephfs
create_backup_pvc: true
no_log: false
controller:
backup_pvc: custom-controller-backup-pvc
backup_storage_requirements: 15Gi
backup_storage_class: rook-block<span id="CO2-3"><!--Empty--></span><span class="callout">3</span>create_backup_pvc: true
no_log: false
eda:
backup_pvc: custom-eda-backup-pvc
backup_storage_requirements: 7Gi
backup_storage_class: rook-block
create_backup_pvc: true
no_log: false
```

