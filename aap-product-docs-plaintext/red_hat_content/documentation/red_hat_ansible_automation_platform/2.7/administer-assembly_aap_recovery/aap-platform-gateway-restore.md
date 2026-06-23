# Restore your Ansible Automation Platform deplopyment
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

