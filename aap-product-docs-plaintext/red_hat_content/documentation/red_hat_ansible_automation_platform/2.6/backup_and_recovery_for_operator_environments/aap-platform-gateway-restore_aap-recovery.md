# 3. Recovering a Red Hat Ansible Automation Platform deployment
## 3.1. Recovering your Ansible Automation Platform deployment

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
2. Navigate to Operators → Installed Operators.
3. Select your Ansible Automation Platform Operator deployment.
4. Go to your **All Instances** tab, and click Create New.
5. Select **Ansible Automation Platform Restore** from the list.
6. For **Name** enter the name for the recovery deployment.
7. For **New Ansible Automation Platform Name** enter the new name for your Ansible Automation Platform instance.
8. **Backup Source** defaults to **CR**.
9. For **Backup name** enter the name you chose when creating the backup.
10. Click Create.

**Verification**

Your backup restores under the **AnsibleAutomationPlatformRestores** tab.

Note

The recovery is not complete until all the resources are successfully restored. Depending on the size of your database this can take some time.

To verify that your recovery was successful you can:

1. Go to Workloads → Pods.
2. Confirm that all pods are in a **Running** or **Completed** state.

**Additional resources**

- [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/installing_on_openshift_container_platform/index)

