# Restore your Ansible Automation Platform deplopyment
## Restore from a persistent volume claim (PVC)

A persistent volume claim (PVC) is a storage volume that stores data for automation hub and automation controller applications.

### Before you begin

- You have an existing PVC containing a backup.
- You have installed the Ansible Automation Platform Operator on Red Hat OpenShift Container Platform.

### About this task

These PVCs are independent of the applications and persist even if an application is deleted. You can restore data from a PVC as an alternative to recovering from an **Ansible Automation Platform** backup.

For more information see the [Finding and deleting PVCs](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_your_ansible_automation_platform_deployment#proc-find-delete-PVCs "A persistent volume claim (PVC) is a storage volume used to store data that automation hub and automation controller applications use.") section of the *Installing on OpenShift Container Platform* guide.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Go to your **All Instances** tab, and click Create New.
5.  Select **Ansible Automation Platform Restore** from the list.
6.  For **Name** enter the name for the recovery deployment.
7.  For **New Ansible Automation Platform Name** enter the new name for your Ansible Automation Platform instance.
8.  For **Backup Source** select **PVC**.   1.  **Backup PVC:** Enter the name of your PVC.
2.  **Backup Directory:** Enter the path to your backup directory on your PVC.
9.  For **Backup name** enter the name you chose when creating the backup.
10.  Under **YAML view** paste in the following example:


```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformRestore
metadata:
name: aap
spec:
deployment_name: aap
backup_source: PVC
backup_pvc: aap-backup-claim
backup_dir: '/backups/aap-openshift-backup-2025-06-23-18:28:29'

controller:
backup_source: PVC
backup_pvc: aap-controller-backup-claim
backup_dir: '/backups/tower-openshift-backup-2025-06-23-182910'

hub:
backup_source: PVC
backup_pvc: aap-hub-backup-claim
backup_dir: '/backups/openshift-backup-2025-06-23-182853'
storage_type: file

eda:
backup_source: PVC
backup_pvc: aap-eda-backup-claim
backup_dir: '/backups/eda-openshift-backup-2025-06-23-18:29:11'
```

11.  Click Create.

### Results

Your backup restores under the **AnsibleAutomationPlatformRestores** tab.

Note:

The recovery is not complete until all the resources are successfully restored. Depending on the size of your database this can take some time.

1. Go to Workloads> (and then)Pods.
2. Confirm that all pods are in a **Running** or **Completed** state.

