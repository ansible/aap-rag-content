# 3. Recovering a Red Hat Ansible Automation Platform deployment
## 3.3. Recovering your Ansible Automation Platform deployment from an external database




You can restore an external database on Red Hat OpenShift Container Platform using the Operator. Use the following procedure to restore from an external database.

Important
Restoring from an external database force drops the database, which overrides your existing external database.



**Prerequisites**

- You have an external database.
- You have installed the Ansible Automation Platform Operator on OpenShift Container Platform.


**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Go to your **All Instances** tab, and clickCreate New.
1. Select **Ansible Automation Platform Restore** from the list.
1. For **Name** enter the name for the recovery deployment.
1. For **New Ansible Automation Platform Name** enter the new name for your Ansible Automation Platform instance.


- If restoring to the same name Ansible Automation Platform then you must add `        force_drop_db: true` to drop the database on restore.

1.  **Backup Source** defaults to **CR** .
1. For **Backup name** enter the name you chose when creating the backup. Under **YAML view** paste in the following example:


```
---    apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatformRestore    metadata:      name: aaprestore    spec:      deployment_name: aap      backup_name: aapbackup      controller:        force_drop_db: true
```


1. ClickCreate.


**Verification**

Your backup restores under the **AnsibleAutomationPlatformRestores** tab.


Note
The recovery is not complete until all the resources are successfully restored. Depending on the size of your database this can take some time.



To verify that your recovery was successful you can:

1. Go toWorkloads→Pods.
1. Confirm that all pods are in a **Running** or **Completed** state.


**Additional resources**

-  [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index)


