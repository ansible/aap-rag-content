+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansibleautomationplatformbackup_and_ansibleautomationplatformrestore__aap_ansible_com_v1alpha1_"
template = "docs/aem-title.html"
title = "AnsibleAutomationPlatformBackup and AnsibleAutomationPlatformRestore [aap.ansible.com/v1alpha1] - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansible_automation_platform_custom_resources/", "Ansible Automation Platform custom resources"]]
category = "Reference"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-ansibleautomationplatformbackup_and_ansibleautomationplatformrestore__aap_ansible_com_v1alpha1_/aem-page/reference-ansibleautomationplatformbackup_and_ansibleautomationplatformrestore__aap_ansible_com_v1alpha1_.html"
last_crumb = "AnsibleAutomationPlatformBackup and AnsibleAutomationPlatformRestore [aap.ansible.com/v1alpha1]"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "AnsibleAutomationPlatformBackup and AnsibleAutomationPlatformRestore [aap.ansible.com/v1alpha1]"
oversized = "false"
page_slug = "reference-ansibleautomationplatformbackup_and_ansibleautomationplatformrestore__aap_ansible_com_v1alpha1_"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/reference-ansibleautomationplatformbackup_and_ansibleautomationplatformrestore__aap_ansible_com_v1alpha1_"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-ansibleautomationplatformbackup_and_ansibleautomationplatformrestore__aap_ansible_com_v1alpha1_/toc/toc.json"
type = "aem-page"
+++

# AnsibleAutomationPlatformBackup and AnsibleAutomationPlatformRestore [aap.ansible.com/v1alpha1]

The `AnsibleAutomationPlatformBackup` and `AnsibleAutomationPlatformRestore` custom resources manage backup and restore operations for your Ansible Automation Platform deployment on OpenShift Container Platform. You can configure global settings or override them per component.

## AnsibleAutomationPlatformBackup

| **API Group**   | `aap.ansible.com`                 |
| --------------- | --------------------------------- |
| **API Version** | `v1alpha1`                        |
| **Kind**        | `AnsibleAutomationPlatformBackup` |
| **Scope**       | Namespaced                        |

## AnsibleAutomationPlatformBackup spec

The `spec` fields for the `AnsibleAutomationPlatformBackup` custom resource.

| Field                         | Type    | Description                                                                                                                                                                                                                                                                                                                                    | Default |
| ----------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `deployment_name`             | String  | Name of the`AnsibleAutomationPlatform` instance to back up. Required.                                                                                                                                                                                                                                                                          | -       |
| `no_log`                      | Boolean | Suppress logging of sensitive data during the backup process.                                                                                                                                                                                                                                                                                  | `true`  |
| `backup_pvc`                  | String  | Name of the persistent volume claim (PVC) to use for backup storage. This value applies globally to all components unless overridden.                                                                                                                                                                                                          | -       |
| `backup_storage_class`        | String  | Kubernetes storage class for the backup PVC. Applies globally to the platform gateway. Components that do not specify their own`backup_storage_class` inherit this value.                                                                                                                                                                      | -       |
| `backup_storage_requirements` | String  | Storage size for the backup PVC, for example`15Gi`.                                                                                                                                                                                                                                                                                            | -       |
| `hub`                         | Object  | <br>Override backup settings for the automation hub component. See [Component backup overrides](/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansibleautomationplatformbackup_and_ansibleautomationplatformrestore__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatformBackupRestore__backup-component-overrides).    | -       |
| `controller`                  | Object  | Override backup settings for the automation controller component. See [Component backup overrides](/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansibleautomationplatformbackup_and_ansibleautomationplatformrestore__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatformBackupRestore__backup-component-overrides). | -       |
| `eda`                         | Object  | Override backup settings for the Event-Driven Ansible component. See [Component backup overrides](/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansibleautomationplatformbackup_and_ansibleautomationplatformrestore__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatformBackupRestore__backup-component-overrides).  | -       |

## Component backup overrides

Each component section (`hub`, `controller`, `eda`) supports the following fields to override global backup settings.

| Field                         | Type    | Description                                                                                | Default               |
| ----------------------------- | ------- | ------------------------------------------------------------------------------------------ | --------------------- |
| `backup_pvc`                  | String  | Name of the PVC for this component's backup. Overrides the global`backup_pvc`.             | Inherited from global |
| `backup_storage_requirements` | String  | Storage size for this component's backup PVC, for example`25Gi`.                           | Inherited from global |
| `backup_storage_class`        | String  | Storage class for this component's backup PVC. Overrides the global`backup_storage_class`. | Inherited from global |
| `create_backup_pvc`           | Boolean | Set to `true` to have the operator create the PVC automatically.                           | `false`               |
| `no_log`                      | Boolean | Suppress logging of sensitive data for this component. Overrides the global `no_log`.      | Inherited from global |

## Example backup custom resource

The following example shows a backup custom resource with per-component overrides for PVC names, storage sizes, and storage classes:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformBackup
metadata:
  name: custom-backup
spec:
  deployment_name: myaap
  no_log: false
  backup_storage_class: rook-cephfs
  hub:
    backup_pvc: custom-hub-backup-pvc
    backup_storage_requirements: 25Gi
    backup_storage_class: rook-cephfs
    create_backup_pvc: true
    no_log: false
  controller:
    backup_pvc: custom-controller-backup-pvc
    backup_storage_requirements: 15Gi
    backup_storage_class: rook-block
    create_backup_pvc: true
    no_log: false
  eda:
    backup_pvc: custom-eda-backup-pvc
    backup_storage_requirements: 7Gi
    backup_storage_class: rook-block
    create_backup_pvc: true
    no_log: false
```

## AnsibleAutomationPlatformRestore

| **API Group**   | `aap.ansible.com`                  |
| --------------- | ---------------------------------- |
| **API Version** | `v1alpha1`                         |
| **Kind**        | `AnsibleAutomationPlatformRestore` |
| **Scope**       | Namespaced                         |

## AnsibleAutomationPlatformRestore spec

The `spec` fields for the `AnsibleAutomationPlatformRestore` custom resource.

| Field             | Type    | Description                                                                      | Default |
| ----------------- | ------- | -------------------------------------------------------------------------------- | ------- |
| `deployment_name` | String  | Name of the`AnsibleAutomationPlatform` instance to restore. Required.            | -       |
| `backup_name`     | String  | Name of the`AnsibleAutomationPlatformBackup` resource to restore from. Required. | -       |
| `no_log`          | Boolean | Suppress logging of sensitive data during the restore process.                   | `true`  |

## Example restore custom resource

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformRestore
metadata:
  name: restore-myaap
spec:
  deployment_name: myaap
  backup_name: custom-backup
```
