+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-event_driven_ansible_custom_resources"
template = "docs/aem-title.html"
title = "Event-Driven Ansible custom resources - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansible_automation_platform_custom_resources/", "Ansible Automation Platform custom resources"]]
category = "Reference"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-event_driven_ansible_custom_resources/aem-page/reference-event_driven_ansible_custom_resources.html"
last_crumb = "Event-Driven Ansible custom resources"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Event-Driven Ansible custom resources"
oversized = "false"
page_slug = "reference-event_driven_ansible_custom_resources"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/reference-event_driven_ansible_custom_resources"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-event_driven_ansible_custom_resources/toc/toc.json"
type = "aem-page"
+++

# Event-Driven Ansible custom resources

The Event-Driven Ansible operator provides custom resources for deploying, configuring, and protecting a standalone Event-Driven Ansible instance on OpenShift Container Platform.

The `EDA` custom resource deploys and configures Event-Driven Ansible independently of the full Ansible Automation Platform deployment. Event-Driven Ansible enables event-driven automation workflows by connecting event sources to automation actions. Use this custom resource when you need to manage Event-Driven Ansible as a standalone component rather than through the `AnsibleAutomationPlatform` resource.

The `EDABackup` and `EDARestore` custom resources manage data protection for standalone Event-Driven Ansible deployments. A backup captures the Event-Driven Ansible database and configuration. A restore recreates the deployment from a previously created backup.

## EDA [eda.ansible.com/v1alpha1]

The `EDA` custom resource deploys and configures a standalone Event-Driven Ansible instance for event-driven automation workflows.

### Description

| **API Group**   | `eda.ansible.com` |
| --------------- | ----------------- |
| **API Version** | `v1alpha1`        |
| **Kind**        | `EDA`             |
| **Scope**       | Namespaced        |

### Specification

| Field                          | Type   | Description                                                                                                                                      | Default    |
| ------------------------------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `automation_server_url`        | String | URL of the automation controller instance for Event-Driven Ansible to connect to.                                                                | -          |
| `automation_server_ssl_verify` | String | Enable or disable SSL verification for the automation controller connection. Set to`no` to disable.                                              | `yes`      |
| `database`                     | Object | Database configuration. Contains`database_secret` (String) specifying the name of a Kubernetes secret with external database connection details. | -          |
| `api`                          | Object | Event-Driven Ansible API pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                                    | 1 replica  |
| `ui`                           | Object | Event-Driven Ansible UI pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                                     | 1 replica  |
| `scheduler`                    | Object | Event-Driven Ansible scheduler pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                              | 1 replica  |
| `default_worker`               | Object | Event-Driven Ansible default worker pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                         | 1 replica  |
| `activation_worker`            | Object | Event-Driven Ansible activation worker pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                      | 1 replica  |
| `event_stream`                 | Object | Event-Driven Ansible event stream pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                           | 1 replica  |
| `worker`                       | Object | Event-Driven Ansible worker pod configuration. Contains`replicas` (Integer) and`resource_requirements` (Object).                                 | 2 replicas |

### Example custom resource

```
apiVersion: eda.ansible.com/v1alpha1
kind: EDA
metadata:
  name: my-eda
spec:
  automation_server_ssl_verify: 'no'
  api:
    replicas: 2
  activation_worker:
    replicas: 2
  event_stream:
    replicas: 2
```

## EDABackup and EDARestore [eda.ansible.com/v1alpha1]

The `EDABackup` and `EDARestore` custom resources manage backup and restore operations for standalone Event-Driven Ansible deployments.

### EDABackup

| **API Group**   | `eda.ansible.com` |
| --------------- | ----------------- |
| **API Version** | `v1alpha1`        |
| **Kind**        | `EDABackup`       |
| **Scope**       | Namespaced        |

### EDABackup spec

| Field                         | Type    | Description                                                          | Default |
| ----------------------------- | ------- | -------------------------------------------------------------------- | ------- |
| `deployment_name`             | String  | Name of the`EDA` instance to back up. Required.                      | -       |
| `no_log`                      | Boolean | Suppress logging of sensitive data during the backup process.        | `true`  |
| `backup_pvc`                  | String  | Name of the persistent volume claim (PVC) to use for backup storage. | -       |
| `backup_storage_class`        | String  | Kubernetes storage class for the backup PVC.                         | -       |
| `backup_storage_requirements` | String  | Storage size for the backup PVC, for example`7Gi`.                   | -       |
| `create_backup_pvc`           | Boolean | Set to`true` to have the operator create the PVC automatically.      | `false` |

### Example EDABackup custom resource

```
apiVersion: eda.ansible.com/v1alpha1
kind: EDABackup
metadata:
  name: eda-backup
spec:
  deployment_name: my-eda
  backup_pvc: eda-backup-pvc
  backup_storage_requirements: 7Gi
  create_backup_pvc: true
```

### EDARestore

| **API Group**   | `eda.ansible.com` |
| --------------- | ----------------- |
| **API Version** | `v1alpha1`        |
| **Kind**        | `EDARestore`      |
| **Scope**       | Namespaced        |

### EDARestore spec

| Field             | Type    | Description                                                    | Default |
| ----------------- | ------- | -------------------------------------------------------------- | ------- |
| `deployment_name` | String  | Name of the`EDA` instance to restore. Required.                | -       |
| `backup_name`     | String  | Name of the`EDABackup` resource to restore from. Required.     | -       |
| `no_log`          | Boolean | Suppress logging of sensitive data during the restore process. | `true`  |

### Example EDARestore custom resource

```
apiVersion: eda.ansible.com/v1alpha1
kind: EDARestore
metadata:
  name: eda-restore
spec:
  deployment_name: my-eda
  backup_name: eda-backup
```
