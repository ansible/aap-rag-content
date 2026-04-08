# 2. Creating Red Hat Ansible Automation Platform backup resources
## 2.1. Back up your Ansible Automation Platform deployment




Regularly backing up your **Ansible Automation Platform** deployment is vital to protect against unexpected data loss and application errors. **Ansible Automation Platform** hosts any enabled components (such as, automation controller, automation hub, and Event-Driven Ansible), when you back up **Ansible Automation Platform** the operator will also back up these components.

Note
Ansible Automation Platform Operator creates a PersistentVolumeClaim (PVC) for your Ansible Automation Platform Backup automatically. You can use your own pre-created PVC by using the `backup_pvc` spec and specifying your PVC.



**Prerequisites**

- You must be authenticated on OpenShift cluster.
- You have installed Ansible Automation Platform Operator on the cluster.
- You have deployed a **Ansible Automation Platform** instance using the Ansible Automation Platform Operator.


**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Go to your **All Instances** tab, and clickCreate New.
1. Select **Ansible Automation Platform Backup** from the list.

Note
When creating the **Ansible Automation Platform Backup** resource it also creates backup resources for each of the nested components that are enabled.




1. In the **Name** field, enter a name for the backup.
1. In the **Deployment name** field, enter the name of the deployed Ansible Automation Platform instance being backed up. For example if your Ansible Automation Platform deployment must be backed up and the deployment name is aap, enter 'aap' in the **Deployment name** field.
1. ClickCreate. This results in an **AnsibleAutomationPlatformBackup** resource similar to the following:


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatformBackup    metadata:      name: backup      namespace: aap    spec:      no_log: true      deployment_name: aap
```

**Verification**

To verify that your backup was successful you can:



1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Click **All Instances** .


The **All Instances** page displays the main backup and the backups for each component with the name you specified when creating your backup resource. The status for the following instances must be either **Running** or **Successful** :

- AnsibleAutomationPlatformBackup
- AutomationControllerBackup
- EDABackup
- AutomationHubBackup


