+++
title = "Back up your Ansible Automation Platform deployment - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_aap_backup"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_aap_backup_recovery/", "Back up and restore in an OpenShift environment"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_aap_backup/aem-page/administer-assembly_aap_backup.html"
last_crumb = "Back up your Ansible Automation Platform deployment"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Back up your Ansible Automation Platform deployment"
oversized = "false"
page_slug = "administer-assembly_aap_backup"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_aap_backup"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_aap_backup/toc/toc.json"
type = "aem-page"
+++

# Back up your Ansible Automation Platform deployment

Backing up your Red Hat Ansible Automation Platform deployment involves creating backup resources for your deployed instances.

Use the following procedures to create backup resources for your Red Hat Ansible Automation Platform deployment. We recommend taking backups before upgrading the Ansible Automation Platform Operator. Take a backup regularly in case you want to restore the platform to a previous state.

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

## Define custom backup Persistent Volume Claims

Define a custom Persistent Volume Claims (PVCs) to control backup storage allocation for each Ansible Automation Platform component. Specify unique PVC names, storage classes, and volume sizes at both global and component levels to differentiate between backup runs.

### Before you begin

- You have an active Red Hat Ansible Automation Platform deployment on OpenShift Container Platform.
- You have the `oc` CLI tool installed and cluster administrator access.

### Procedure

1.  Create a backup YAML file, for example `custom-pvc-backup.yaml`) , that defines `backup_pvc` and `create_backup_pvc` parameters for each component:
  

```none
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformBackup
metadata:
  name: aapbackup
spec:
  backup_pvc: custom-aap-backup-pvc (a)
  backup_storage_class: nfs-local-rwx
  backup_storage_requirements: 7Gi
  create_backup_pvc: true (b)
  deployment_name: aap
  controller: (c)
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
```

  1. Sets a custom PVC name for the platform gateway backup.
  2. When set to `true`, the operator creates the PVC automatically if it does not already exist.
  3. Component-level settings override the global values for `backup_pvc`, `backup_storage_class`, and `backup_storage_requirements`. Each component can define its own `backup_pvc` to create a uniquely named PVC.

2.  Apply the configuration:
  

```none
oc apply -f custom-pvc-backup.yaml
```

### Results

Confirm that the PVCs were created:

```none
oc get pvc -n <namespace>
```
The output displays the custom PVCs for each component:

| Name                                 | Status        | Volume              | Capacity    | Access Modes | Storage class         |
| ------------------------------------ | ------------- | ------------------- | ----------- | ------------ | --------------------- |
| ``` custom-aap-backup-pvc ```        | ``` Bound ``` | ``` pv-aap  ```     | ``` 7Gi ``` | ``` RWX  ``` | ``` nfs-local-rwx ``` |
| ``` custom-controller-backup-pvc ``` | ``` Bound ``` | ``` pv-ctrl     ``` | ``` 7Gi ``` | ``` RWO ```  | ``` standard-csi ```  |
| ``` custom-eda-backup-pvc     ```    | ``` Bound ``` | ``` pv-eda  ```     | ``` 7Gi ``` | ``` RWO ```  | ``` standard-csi ```  |
| ``` custom-hub-backup-pvc  ```       | ``` Bound ``` | ``` pv-hub  ```     | ``` 7Gi ``` | ``` RWX  ``` | ``` nfs-local-rwx ``` |

## Custom backup configurations for specific components

You can override the global backup configuration for specific components, such as automation controller, private automation hub, or Event-Driven Ansible controller. This enables each component to use its own storage class, PVC name, storage size, or resource limits during the backup process.

**Example: Overriding component resources**

In this backup custom resource, each component has a unique PVC name and storage class::

```none
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformBackup
metadata:
  name: custom-backup
spec:
  deployment_name: myaap
  no_log: false
  backup_storage_class: rook-cephfs <1>
  hub:
 backup_pvc: custom-hub-backup-pvc <2>
    backup_storage_requirements: 25Gi
    backup_storage_class: rook-cephfs
    create_backup_pvc: true
    no_log: false
  controller:
    backup_pvc: custom-controller-backup-pvc
    backup_storage_requirements: 15Gi  
    backup_storage_class: rook-block <3>
    create_backup_pvc: true
    no_log: false
  eda:
 backup_pvc: custom-eda-backup-pvc
    backup_storage_requirements: 7Gi
    backup_storage_class: rook-block
    create_backup_pvc: true
    no_log: false
```


1.      The global `backup_storage_class` applies to the platform gateway. Components that do not specify their own `backup_storage_class` inherit this value.

2.      Each component can define its own `backup_pvc` to create a uniquely named PVC. Set `create_backup_pvc: true` to have the operator create the PVC automatically.

3.      Component-level values, such as `backup_storage_class: rook-block`, override the global setting for that component.

## Resolve naming conflicts when deploying an Automation Controller custom resource

If your `AutomationController` customer resource matches an existing deployment, perform the following steps to resolve the issue.

### About this task

The name specified for the new `AutomationController` custom resource must not match an existing deployment or the recovery process will fail. Persistent volume claims (PVCs) and Secrets remain after a deployment is deleted. If you want to reuse the same name you must delete previous PVCs and Secrets before creating a new custom resource.

### Procedure

1.  Delete the existing `AutomationController` and the associated postgres PVC:
  

```
oc delete automationcontroller <YOUR_DEPLOYMENT_NAME> -n <YOUR_NAMESPACE>

    oc delete pvc postgres-13-<YOUR_DEPLOYMENT_NAME>-13-0 -n <YOUR_NAMESPACE>
```

2.  Use `AutomationControllerRestore` with the same deployment_name in it:
  

```
oc apply -f restore.yaml
```
