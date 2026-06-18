+++
title = "Automation controller custom resources - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-automation_controller_custom_resources"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansible_automation_platform_custom_resources/", "Ansible Automation Platform custom resources"]]
category = "Reference"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/reference-automation_controller_custom_resources/aem-page/reference-automation_controller_custom_resources.html"
last_crumb = "Automation controller custom resources"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Automation controller custom resources"
oversized = "false"
page_slug = "reference-automation_controller_custom_resources"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/reference-automation_controller_custom_resources"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/reference-automation_controller_custom_resources/toc/toc.json"
type = "aem-page"
+++

# Automation controller custom resources

The automation controller operator provides custom resources for deploying, configuring, and protecting a standalone automation controller instance on OpenShift Container Platform.

The `AutomationController` custom resource deploys and configures automation controller independently of the full Ansible Automation Platform deployment. Use this custom resource when you need to manage automation controller as a standalone component rather than through the `AnsibleAutomationPlatform` resource.

The `AutomationControllerMeshIngress` custom resource creates a mesh ingress hop node inside the OpenShift cluster. This enables remote execution nodes outside the cluster to connect to automation controller through the automation mesh network.

The `AutomationControllerBackup` and `AutomationControllerRestore` custom resources manage data protection for standalone automation controller deployments. A backup captures the controller database and configuration. A restore recreates the controller from a previously created backup.

## AutomationController and AutomationControllerMeshIngress [automationcontroller.ansible.com]

The `AutomationController` custom resource deploys and configures a standalone automation controller instance. The `AutomationControllerMeshIngress` custom resource creates a mesh ingress hop node inside the OpenShift cluster for automation mesh connectivity.

### AutomationController

| **API Group**   | `automationcontroller.ansible.com` |
| --------------- | ---------------------------------- |
| **API Version** | `v1beta1`                          |
| **Kind**        | `AutomationController`             |
| **Scope**       | Namespaced                         |

### AutomationController spec

The `spec` fields for the `AutomationController` custom resource.

| Field                                  | Type    | Description                                                                                                           | Default                               |
| -------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `image_pull_policy`                    | String  | Image pull policy for automation controller pods. Options: `Always`, `Never`, `IfNotPresent`.                         | `IfNotPresent`                        |
| `postgres_configuration_secret`        | String  | Name of a Kubernetes secret containing external PostgreSQL connection details for the automation controller database. | -                                     |
| `route_tls_termination_mechanism`      | String  | TLS termination mechanism for the automation controller route.                                                        | -                                     |
| `uwsgi_processes`                      | Integer | Number of uWSGI worker processes for the web pod.                                                                     | `2`                                   |
| `termination_grace_period_seconds`     | Integer | Grace period in seconds for running jobs to complete before the pod terminates.                                       | -                                     |
| `ee_extra_env`                         | String  | Extra environment variables to pass to execution environment pods.                                                    | -                                     |
| `extra_settings`                       | Array   | List of additional automation controller settings as name-value pairs.                                                | -                                     |
| `task_affinity`                        | Object  | Kubernetes pod affinity rules for the task pod.                                                                       | -                                     |
| `web_affinity`                         | Object  | Kubernetes pod affinity rules for the web pod.                                                                        | -                                     |
| `task_resource_requirements`           | Object  | Kubernetes resource requests and limits for the task pod.                                                             | cpu: 100m/1000m, memory: 150Mi/1200Mi |
| `web_resource_requirements`            | Object  | Kubernetes resource requests and limits for the web pod.                                                              | cpu: 100m/200m, memory: 200Mi/1600Mi  |
| `ee_resource_requirements`             | Object  | Kubernetes resource requests and limits for execution environment pods.                                               | cpu: 100m/1000m, memory: 64Mi/500Mi   |
| `redis_resource_requirements`          | Object  | Kubernetes resource requests and limits for the automation controller Redis pod.                                      | cpu: 50m/100m, memory: 64Mi/200Mi     |
| `rsyslog_resource_requirements`        | Object  | Kubernetes resource requests and limits for the rsyslog pod.                                                          | cpu: 100m/500m, memory: 128Mi/250Mi   |
| `init_container_resource_requirements` | Object  | Kubernetes resource requests and limits for init containers.                                                          | cpu: 100m/500m, memory: 128Mi/200Mi   |

### Example AutomationController custom resource

```
apiVersion: automationcontroller.ansible.com/v1beta1
kind: AutomationController
metadata:
  name: my-controller
spec:
  uwsgi_processes: 4
  task_resource_requirements:
    requests:
      cpu: 200m
      memory: 512Mi
    limits:
      cpu: 2000m
      memory: 2Gi
  web_resource_requirements:
    requests:
      cpu: 200m
      memory: 512Mi
    limits:
      cpu: 1000m
      memory: 2Gi
```

### AutomationControllerMeshIngress

| **API Group**   | `automationcontroller.ansible.com` |
| --------------- | ---------------------------------- |
| **API Version** | `v1alpha1`                         |
| **Kind**        | `AutomationControllerMeshIngress`  |
| **Scope**       | Namespaced                         |

### AutomationControllerMeshIngress spec

The `spec` fields for the `AutomationControllerMeshIngress` custom resource.

| Field             | Type   | Description                                                                                                                                      | Default |
| ----------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `deployment_name` | String | Name of the `AutomationController` instance to attach the mesh ingress to. Required. Must be in the same namespace as the mesh ingress resource. | -       |

### Example AutomationControllerMeshIngress custom resource

```
apiVersion: automationcontroller.ansible.com/v1alpha1
kind: AutomationControllerMeshIngress
metadata:
  name: my-mesh-ingress
  namespace: aap
spec:
  deployment_name: my-controller
```

## AutomationControllerBackup and AutomationControllerRestore [automationcontroller.ansible.com]

The `AutomationControllerBackup` and `AutomationControllerRestore` custom resources manage backup and restore operations for standalone automation controller deployments.

### AutomationControllerBackup

| **API Group**   | `automationcontroller.ansible.com` |
| --------------- | ---------------------------------- |
| **API Version** | `v1beta1`                          |
| **Kind**        | `AutomationControllerBackup`       |
| **Scope**       | Namespaced                         |

### AutomationControllerBackup spec

| Field                         | Type    | Description                                                          | Default |
| ----------------------------- | ------- | -------------------------------------------------------------------- | ------- |
| `deployment_name`             | String  | Name of the `AutomationController` instance to back up. Required.    | -       |
| `no_log`                      | Boolean | Suppress logging of sensitive data during the backup process.        | `true`  |
| `backup_pvc`                  | String  | Name of the persistent volume claim (PVC) to use for backup storage. | -       |
| `backup_storage_class`        | String  | Kubernetes storage class for the backup PVC.                         | -       |
| `backup_storage_requirements` | String  | Storage size for the backup PVC, for example `15Gi`.                 | -       |
| `create_backup_pvc`           | Boolean | Set to `true` to have the operator create the PVC automatically.     | `false` |

### Example AutomationControllerBackup custom resource

```
apiVersion: automationcontroller.ansible.com/v1beta1
kind: AutomationControllerBackup
metadata:
  name: controller-backup
spec:
  deployment_name: my-controller
  backup_pvc: controller-backup-pvc
  backup_storage_requirements: 15Gi
  create_backup_pvc: true
```

### AutomationControllerRestore

| **API Group**   | `automationcontroller.ansible.com` |
| --------------- | ---------------------------------- |
| **API Version** | `v1beta1`                          |
| **Kind**        | `AutomationControllerRestore`      |
| **Scope**       | Namespaced                         |

### AutomationControllerRestore spec

| Field             | Type    | Description                                                                  | Default |
| ----------------- | ------- | ---------------------------------------------------------------------------- | ------- |
| `deployment_name` | String  | Name of the `AutomationController` instance to restore. Required.            | -       |
| `backup_name`     | String  | Name of the `AutomationControllerBackup` resource to restore from. Required. | -       |
| `no_log`          | Boolean | Suppress logging of sensitive data during the restore process.               | `true`  |

### Example AutomationControllerRestore custom resource

```
apiVersion: automationcontroller.ansible.com/v1beta1
kind: AutomationControllerRestore
metadata:
  name: controller-restore
spec:
  deployment_name: my-controller
  backup_name: controller-backup
```
