+++
title = "Automation hub custom resources - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-automation_hub_custom_resources"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansible_automation_platform_custom_resources/", "Ansible Automation Platform custom resources"]]
category = "Reference"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-automation_hub_custom_resources/aem-page/reference-automation_hub_custom_resources.html"
last_crumb = "Automation hub custom resources"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Automation hub custom resources"
oversized = "false"
page_slug = "reference-automation_hub_custom_resources"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/reference-automation_hub_custom_resources"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-automation_hub_custom_resources/toc/toc.json"
type = "aem-page"
+++

# Automation hub custom resources

The automation hub operator provides custom resources for deploying, configuring, and protecting a standalone automation hub instance on OpenShift Container Platform.

The `AutomationHub` custom resource deploys and configures automation hub independently of the full Ansible Automation Platform deployment. Automation hub provides a centralized location for managing Ansible content collections, execution environments, and container images. Use this custom resource when you need to manage automation hub as a standalone component rather than through the `AnsibleAutomationPlatform` resource.

The `AutomationHubBackup` and `AutomationHubRestore` custom resources manage data protection for standalone automation hub deployments. A backup captures the hub database, content, and configuration. A restore recreates the hub from a previously created backup.

## AutomationHub [automationhub.ansible.com/v1beta1]

The `AutomationHub` custom resource deploys and configures a standalone automation hub instance for managing Ansible content collections, execution environments, and container images.

### Description

| **API Group**   | `automationhub.ansible.com` |
| --------------- | --------------------------- |
| **API Version** | `v1beta1`                   |
| **Kind**        | `AutomationHub`             |
| **Scope**       | Namespaced                  |

### Specification

| Field                           | Type   | Description                                                                                                                        | Default        |
| ------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `image_pull_policy`             | String | Image pull policy for automation hub pods. Options: `Always`, `Never`, `IfNotPresent`.                                             | `IfNotPresent` |
| `postgres_configuration_secret` | String | Name of a Kubernetes secret containing external PostgreSQL connection details for the automation hub database.                     | -              |
| `storage_type`                  | String | Storage backend type for automation hub content. Options: `file`, `S3`, `azure`.                                                   | -              |
| `file_storage_storage_class`    | String | Kubernetes storage class for file-based storage. Must support `ReadWriteMany` access mode. Required when `storage_type` is `file`. | -              |
| `file_storage_size`             | String | Size of the persistent volume for file-based storage, for example `50Gi`. Required when `storage_type` is `file`.                  | -              |
| `object_storage_s3_secret`      | String | Name of a Kubernetes secret containing S3-compatible object storage credentials. Required when `storage_type` is `S3`.             | -              |
| `object_storage_azure_secret`   | String | Name of a Kubernetes secret containing Azure Blob Storage credentials. Required when `storage_type` is `azure`.                    | -              |
| `pulp_settings`                 | Object | Custom Pulp configuration settings as key-value pairs, for example `MAX_PAGE_SIZE` or `cache_enabled`.                             | -              |
| `api`                           | Object | Automation hub API pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                          | 1 replica      |
| `content`                       | Object | Automation hub content pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                      | 1 replica      |
| `worker`                        | Object | Automation hub worker pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                       | 1 replica      |
| `web`                           | Object | Automation hub web pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                          | 1 replica      |
| `redis`                         | Object | Automation hub Redis pod configuration. Contains `replicas` (Integer) and `resource_requirements` (Object).                        | 1 replica      |

### Example custom resource

```
apiVersion: automationhub.ansible.com/v1beta1
kind: AutomationHub
metadata:
  name: my-hub
spec:
  storage_type: S3
  object_storage_s3_secret: my-s3-secret
  pulp_settings:
    MAX_PAGE_SIZE: 501
    cache_enabled: true
  api:
    replicas: 2
  content:
    replicas: 2
```

## AutomationHubBackup and AutomationHubRestore [automationhub.ansible.com/v1beta1]

The `AutomationHubBackup` and `AutomationHubRestore` custom resources manage backup and restore operations for standalone automation hub deployments.

### AutomationHubBackup

| **API Group**   | `automationhub.ansible.com` |
| --------------- | --------------------------- |
| **API Version** | `v1beta1`                   |
| **Kind**        | `AutomationHubBackup`       |
| **Scope**       | Namespaced                  |

### AutomationHubBackup spec

| Field                         | Type    | Description                                                          | Default |
| ----------------------------- | ------- | -------------------------------------------------------------------- | ------- |
| `deployment_name`             | String  | Name of the`AutomationHub` instance to back up. Required.            | -       |
| `no_log`                      | Boolean | Suppress logging of sensitive data during the backup process.        | `true`  |
| `backup_pvc`                  | String  | Name of the persistent volume claim (PVC) to use for backup storage. | -       |
| `backup_storage_class`        | String  | Kubernetes storage class for the backup PVC.                         | -       |
| `backup_storage_requirements` | String  | Storage size for the backup PVC, for example`15Gi`.                  | -       |
| `create_backup_pvc`           | Boolean | Set to`true` to have the operator create the PVC automatically.      | `false` |

### Example AutomationHubBackup custom resource

```
apiVersion: automationhub.ansible.com/v1beta1
kind: AutomationHubBackup
metadata:
  name: hub-backup
spec:
  deployment_name: my-hub
  backup_pvc: hub-backup-pvc
  backup_storage_requirements: 25Gi
  create_backup_pvc: true
```

### AutomationHubRestore

| **API Group**   | `automationhub.ansible.com` |
| --------------- | --------------------------- |
| **API Version** | `v1beta1`                   |
| **Kind**        | `AutomationHubRestore`      |
| **Scope**       | Namespaced                  |

### AutomationHubRestore spec

| Field             | Type    | Description                                                          | Default |
| ----------------- | ------- | -------------------------------------------------------------------- | ------- |
| `deployment_name` | String  | Name of the`AutomationHub` instance to restore. Required.            | -       |
| `backup_name`     | String  | Name of the`AutomationHubBackup` resource to restore from. Required. | -       |
| `no_log`          | Boolean | Suppress logging of sensitive data during the restore process.       | `true`  |

### Example AutomationHubRestore custom resource

```
apiVersion: automationhub.ansible.com/v1beta1
kind: AutomationHubRestore
metadata:
  name: hub-restore
spec:
  deployment_name: my-hub
  backup_name: hub-backup
```
