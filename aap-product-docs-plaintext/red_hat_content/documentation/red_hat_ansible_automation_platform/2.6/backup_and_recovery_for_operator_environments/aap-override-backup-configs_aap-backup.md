# 2. Creating Red Hat Ansible Automation Platform backup resources
## 2.3. Custom backup configurations for specific components

You can override the global backup configuration for specific components, such as automation controller, private automation hub, or Event-Driven Ansible controller. This enables each component to use its own storage class, PVC name, storage size, or resource limits during the backup process.

**Example: Overriding component backup settings**

In this backup custom resource, each component has a unique PVC name and storage class:

apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformBackup
metadata:
name: custom-backup
spec:
deployment_name: myaap
no_log: false
backup_storage_class: rook-cephfs 1
hub:
backup_pvc: custom-hub-backup-pvc 2
backup_storage_requirements: 25Gi
backup_storage_class: rook-cephfs
create_backup_pvc: true
no_log: false
controller:
backup_pvc: custom-controller-backup-pvc
backup_storage_requirements: 15Gi
backup_storage_class: rook-block 3
create_backup_pvc: true
no_log: false
eda:
backup_pvc: custom-eda-backup-pvc
backup_storage_requirements: 7Gi
backup_storage_class: rook-block
create_backup_pvc: true
no_log: false

[1](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/backup_and_recovery_for_operator_environments/index#CO2-1)
The global `backup_storage_class` applies to the platform gateway. Components that do not specify their own `backup_storage_class` inherit this value.

[2](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/backup_and_recovery_for_operator_environments/index#CO2-2)
Each component can define its own `backup_pvc` to create a uniquely named PVC. Set `create_backup_pvc: true` to have the operator create the PVC automatically.

[3](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/backup_and_recovery_for_operator_environments/index#CO2-3)
Component-level values, such as `backup_storage_class: rook-block`, override the global setting for that component.

