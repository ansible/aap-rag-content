# Back up your Ansible Automation Platform deployment
## Back up your Ansible Automation Platform deployment

Regularly backing up your **Ansible Automation Platform** deployment is vital to protect against data loss. When you back up the platform, the operator automatically backs up all enabled components, including automation controller, automation hub, and Event-Driven Ansible.

### Before you begin

- You must be authenticated on OpenShift cluster.
- You have installed Ansible Automation Platform Operator on the cluster.
- You have deployed a **Ansible Automation Platform** instance using the Ansible Automation Platform Operator.

### About this task

Note:

Ansible Automation Platform Operator creates a PersistentVolumeClaim (PVC) for your Ansible Automation Platform Backup automatically. You can use your own pre-created PVC by using the `backup_pvc` spec and specifying your PVC.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Go to your **All Instances** tab, and click Create New.
5.  Select **Ansible Automation Platform Backup** from the list. Note:
When creating the **Ansible Automation Platform Backup** resource it also creates backup resources for each of the nested components that are enabled.

6.  In the **Name** field, enter a name for the backup.
7.  In the **Deployment name** field, enter the name of the deployed Ansible Automation Platform instance being backed up. For example if your Ansible Automation Platform deployment must be backed up and the deployment name is aap, enter 'aap' in the **Deployment name** field.
8.  Click Create. This results in an **AnsibleAutomationPlatformBackup** resource similar to the following:


```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformBackup
metadata:
name: backup
namespace: aap
spec:
no_log: true
deployment_name: aap
```

### Results

To verify that your backup was successful you can:

1. Log in to Red Hat OpenShift Container Platform.
2. Navigate to Operators> (and then)Installed Operators.
3. Select your Ansible Automation Platform Operator deployment.
4. Click **All Instances**.


The **All Instances** page displays the main backup and the backups for each component with the name you specified when creating your backup resource. The status for the following instances must be either **Running** or **Successful**:

- AnsibleAutomationPlatformBackup
- AutomationControllerBackup
- EDABackup
- AutomationHubBackup

