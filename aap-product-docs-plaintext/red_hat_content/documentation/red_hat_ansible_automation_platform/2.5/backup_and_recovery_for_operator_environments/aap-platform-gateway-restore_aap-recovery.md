# 3. Recovering a Red Hat Ansible Automation Platform deployment
## 3.1. Recovering your Ansible Automation Platform deployment




**Ansible Automation Platform** manages any enabled components (such as, automation controller, automation hub, and Event-Driven Ansible), when you recover **Ansible Automation Platform** you also restore these components.

In previous versions of the Ansible Automation Platform Operator, it was necessary to create a restore object for each component of the platform. Now, you create a single **AnsibleAutomationPlatformRestore** resource, which creates and manages the other restore objects:

- AutomationControllerRestore
- AutomationHubRestore
- EDARestore


**Prerequisites**

- You must be authenticated with an OpenShift cluster.
- You have installed the Ansible Automation Platform Operator on the cluster.
- The **AnsibleAutomationPlatformBackups** deployment is available in your cluster.


**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Go to your **All Instances** tab, and clickCreate New.
1. Select **Ansible Automation Platform Restore** from the list.
1. For **Name** enter the name for the recovery deployment.
1. For **New Ansible Automation Platform Name** enter the new name for your Ansible Automation Platform instance.
1.  **Backup Source** defaults to **CR** .
1. For **Backup name** enter the name your chose when creating the backup.
1. ClickCreate.


Your backups starts restoring under the **AnsibleAutomationPlatformRestores** tab.

Note
The recovery is not complete until all the resources are successfully restored. Depending on the size of your database this this can take some time.



**Verification**

To verify that your recovery was successful you can:


1. Go toWorkloads→Pods.
1. Confirm that all pods are in a **Running** or **Completed** state.


