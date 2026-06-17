# 2. Creating Red Hat Ansible Automation Platform backup resources
## 2.2. Define custom backup Persistent Volume Claims

Define custom Persistent Volume Claims (PVCs) to control backup storage allocation for each Ansible Automation Platform component. Specify unique PVC names, storage classes, and volume sizes at both global and component levels to differentiate between backup runs.

**Prerequisites**

- You have an active Red Hat Ansible Automation Platform deployment on OpenShift Container Platform.
- You have the `oc` CLI tool installed and cluster administrator access.

**Procedure**

1. Create a backup YAML file, for example `custom-pvc-backup.yaml`, that defines the `backup_pvc` and `create_backup_pvc` parameters for each component:

apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformBackup
metadata:
name: aapbackup
spec:
backup_pvc: custom-aap-backup-pvc 1
backup_storage_class: nfs-local-rwx
backup_storage_requirements: 7Gi
create_backup_pvc: true 2
deployment_name: aap
controller: 3
backup_pvc: custom-controller-backup-pvc
backup_resource_requirements:
limits:
cpu: "4"
memory: 8Gi
requests:
cpu: "2"
memory: 4Gi
backup_storage_class: standard-csi
backup_storage_requirements: 7Gi
create_backup_pvc: true
eda:
backup_pvc: custom-eda-backup-pvc
backup_storage_class: standard-csi
backup_storage_requirements: 7Gi
create_backup_pvc: true
hub:
backup_pvc: custom-hub-backup-pvc
backup_storage_class: nfs-local-rwx
backup_storage_requirements: 7Gi
create_backup_pvc: true



[1](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/backup_and_recovery_for_operator_environments/index#CO1-1)
Sets a custom PVC name for the platform gateway backup.

[2](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/backup_and_recovery_for_operator_environments/index#CO1-2)
When set to `true`, the operator creates the PVC automatically if it does not already exist.

[3](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/backup_and_recovery_for_operator_environments/index#CO1-3)
Component-level settings override the global values for `backup_pvc`, `backup_storage_class`, and `backup_storage_requirements`. Each component can define its own `backup_pvc` to create a uniquely named PVC.

2. Apply the configuration:

$ oc apply -f custom-pvc-backup.yaml

**Verification**

- Confirm that the PVCs were created:

$ oc get pvc -n <namespace>

The output displays the custom PVCs for each component:

NAME                             STATUS   VOLUME       CAPACITY   ACCESS MODES   STORAGECLASS
custom-aap-backup-pvc            Bound    pv-aap       7Gi        RWX            nfs-local-rwx
custom-controller-backup-pvc     Bound    pv-ctrl      7Gi        RWO            standard-csi
custom-eda-backup-pvc            Bound    pv-eda       7Gi        RWO            standard-csi
custom-hub-backup-pvc            Bound    pv-hub       7Gi        RWX            nfs-local-rwx

