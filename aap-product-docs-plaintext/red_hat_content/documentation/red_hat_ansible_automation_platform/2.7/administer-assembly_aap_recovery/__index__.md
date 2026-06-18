# Restore your Ansible Automation Platform deplopyment

If you lose information on your system or experience issues with an upgrade, you can use the backup resources of your deployment instances. Use the following procedures to recover your Ansible Automation Platform deployment files.

## Restore Ansible Automation Platform

**Ansible Automation Platform** manages any enabled components (such as, automation controller, automation hub, and Event-Driven Ansible), when you recover **Ansible Automation Platform** you also restore these components.

### Before you begin

- You must be authenticated with an OpenShift cluster.
- You have installed the Ansible Automation Platform Operator on the cluster.
- The **AnsibleAutomationPlatformBackups** deployment is available in your cluster.

### About this task

To restore Ansible Automation Platform Operator, create a single **AnsibleAutomationPlatformRestore** resource. This resource creates and manages the restore objects for each platform component:

- AutomationControllerRestore
- AutomationHubRestore
- EDARestore

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Go to your **All Instances** tab, and click Create New.
5.  Select **Ansible Automation Platform Restore** from the list.
6.  For **Name** enter the name for the recovery deployment.
7.  For **New Ansible Automation Platform Name** enter the new name for your Ansible Automation Platform instance.
8.  **Backup Source** defaults to **CR**.
9.  For **Backup name** enter the name you chose when creating the backup.
10.  Click Create.

### Results

Your backup restores under the **AnsibleAutomationPlatformRestores** tab.

Note:

The recovery is not complete until all the resources are successfully restored. Depending on the size of your database this can take some time.

To verify that your recovery was successful you can:

1. Go to Workloads> (and then)Pods.
2. Confirm that all pods are in a **Running** or **Completed** state.

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

## Restore from an external database

You can restore an external database on Red Hat OpenShift Container Platform using the Operator. Use the following procedure to restore from an external database.

### Before you begin

- You have an external database.
- You have installed the Ansible Automation Platform Operator on OpenShift Container Platform.

### About this task

Important:

Restoring from an external database force drops the database, which overrides your existing external database.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Go to your **All Instances** tab, and click Create New.
5.  Select **Ansible Automation Platform Restore** from the list.
6.  For **Name** enter the name for the recovery deployment.
7.  For **New Ansible Automation Platform Name** enter the new name for your Ansible Automation Platform instance.   - If restoring to the same name Ansible Automation Platform then you must add `force_drop_db: true` to drop the database on restore.

8.  **Backup Source** defaults to **CR**.
9.  For **Backup name** enter the name you chose when creating the backup. Under **YAML view** paste in the following example:


```
---
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformRestore
metadata:
name: aaprestore
spec:
deployment_name: aap
backup_name: aapbackup
controller:
force_drop_db: true
```

10.  Click Create.

### Results

Your backup restores under the **AnsibleAutomationPlatformRestores** tab.

Note:

The recovery is not complete until all the resources are successfully restored. Depending on the size of your database this can take some time.

To verify that your recovery was successful you can:

1. Go to Workloads> (and then)Pods.
2. Confirm that all pods are in a **Running** or **Completed** state.
