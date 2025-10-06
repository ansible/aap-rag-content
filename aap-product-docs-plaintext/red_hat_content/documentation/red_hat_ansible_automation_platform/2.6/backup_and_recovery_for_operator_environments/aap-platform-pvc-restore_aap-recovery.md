# 3. Recovering a Red Hat Ansible Automation Platform deployment
## 3.2. Recovering your Ansible Automation Platform deployment from a PVC




A persistent volume claim (PVC) is a storage volume that stores data for automation hub and automation controller applications. These PVCs are independent of the applications and persist even if an application is deleted. You can restore data from a PVC as an alternative to recovering from an **Ansible Automation Platform** backup.

For more information see the [Finding and deleting PVCs](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index#proc-find-delete-PVCs_installing-controller-operator) section of the _Installing on OpenShift Container Platform_ guide.

**Prerequisites**

- You have an existing PVC containing a backup.
- You have installed the Ansible Automation Platform Operator on Red Hat OpenShift Container Platform.


**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Go to your **All Instances** tab, and clickCreate New.
1. Select **Ansible Automation Platform Restore** from the list.
1. For **Name** enter the name for the recovery deployment.
1. For **New Ansible Automation Platform Name** enter the new name for your Ansible Automation Platform instance.
1. For **Backup Source** select **PVC** .


1.  **Backup PVC:** Enter the name of your PVC.
1.  **Backup Directory:** Enter the path to your backup directory on your PVC.

1. For **Backup name** enter the name you chose when creating the backup.
1. Under **YAML view** paste in the following example:


```
---    apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatformRestore    metadata:      name: aap    spec:      deployment_name: aap      backup_source: PVC      backup_pvc: aap-backup-claim      backup_dir: '/backups/aap-openshift-backup-2025-06-23-18:28:29'          controller:        backup_source: PVC        backup_pvc: aap-controller-backup-claim        backup_dir: '/backups/tower-openshift-backup-2025-06-23-182910'          hub:        backup_source: PVC        backup_pvc: aap-hub-backup-claim        backup_dir: '/backups/openshift-backup-2025-06-23-182853'        storage_type: file          eda:        backup_source: PVC        backup_pvc: aap-eda-backup-claim        backup_dir: '/backups/eda-openshift-backup-2025-06-23-18:29:11'
```


1. ClickCreate.


**Verification**

Your backups restore under the **AnsibleAutomationPlatformRestores** tab.


Note
The recovery is not complete until all the resources are successfully restored. Depending on the size of your database this this can take some time.



1. Go toWorkloads→Pods.
1. Confirm that all pods are in a **Running** or **Completed** state.


**Additional resources**

-  [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index)


