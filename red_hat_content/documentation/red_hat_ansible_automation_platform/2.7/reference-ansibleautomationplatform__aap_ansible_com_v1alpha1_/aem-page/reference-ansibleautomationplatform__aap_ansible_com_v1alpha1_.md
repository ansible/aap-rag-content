+++
title = "AnsibleAutomationPlatform [aap.ansible.com/v1alpha1] - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansible_automation_platform_custom_resources/", "Ansible Automation Platform custom resources"]]
category = "Reference"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_/aem-page/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_.html"
last_crumb = "AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]"
oversized = "false"
page_slug = "reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_/toc/toc.json"
type = "aem-page"
+++

# AnsibleAutomationPlatform [aap.ansible.com/v1alpha1]

The `AnsibleAutomationPlatform` custom resource is the top-level resource for deploying and managing Ansible Automation Platform on OpenShift Container Platform. It configures all components, including automation controller, automation hub, Event-Driven Ansible, and the platform gateway.

## Description

| **API Group**   | `aap.ansible.com`           |
| --------------- | --------------------------- |
| **API Version** | `v1alpha1`                  |
| **Kind**        | `AnsibleAutomationPlatform` |
| **Scope**       | Namespaced                  |

## Specification

The top-level `spec` fields for the `AnsibleAutomationPlatform` custom resource.

| Field                  | Type    | Description                                                                                                                                                                                                                                          | Default        |
| ---------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `no_log`               | Boolean | Development setting to enable additional logging output.                                                                                                                                                                                             | `false`        |
| `image_pull_policy`    | String  | Image pull policy for all platform pods. Options:`Always`,`Never`,`IfNotPresent`.                                                                                                                                                                    | `IfNotPresent` |
| `bundle_cacert_secret` | String  | Name of a Kubernetes secret containing custom CA certificates to trust.                                                                                                                                                                              | -              |
| `redis_mode`           | String  | Redis deployment mode. Set to`cluster` to enable Redis cluster mode.                                                                                                                                                                                 | -              |
| `api`                  | Object  | Configuration for the platform gateway API pods. See[spec.api](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__spec-api).                     | -              |
| `redis`                | Object  | Configuration for the platform Redis pods. See[spec.redis](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__spec-redis).                       | -              |
| `database`             | Object  | Configuration for the platform database. See[spec.database](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__spec-database).                   | -              |
| `controller`           | Object  | Configuration for the automation controller component. See[spec.controller](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__spec-controller). | -              |
| `eda`                  | Object  | Configuration for the Event-Driven Ansible component. See[spec.eda](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__spec-eda).                | -              |
| `hub`                  | Object  | Configuration for the automation hub component. See[spec.hub](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__spec-hub).                      | -              |
| `lightspeed`           | Object  | Configuration for the Ansible Lightspeed component. See[spec.lightspeed](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__spec-lightspeed).    | -              |

## spec.api

Configuration for the platform gateway API pods.

| Field                   | Type    | Description                                                                                                                                                                                                                                                                        | Default            |
| ----------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `replicas`              | Integer | Number of gateway API pod replicas.                                                                                                                                                                                                                                                | `1`                |
| `resource_requirements` | Object  | Kubernetes resource requests and limits for the gateway API pods. See[Resource requirements object](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__resource-requirements). | See defaults table |

## spec.redis

Configuration for the platform Redis pods.

| Field                   | Type    | Description                                                                                                                                                                                                                                                                  | Default            |
| ----------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `replicas`              | Integer | Number of Redis pod replicas.                                                                                                                                                                                                                                                | `1`                |
| `resource_requirements` | Object  | Kubernetes resource requests and limits for the Redis pods. See[Resource requirements object](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__resource-requirements). | See defaults table |

## spec.database

Configuration for the platform database.

| Field                   | Type   | Description                                                                                                                                                                                                                                                                                                                               | Default            |
| ----------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `database_secret`       | String | Name of a Kubernetes secret containing external database connection details. Required when using an external database instead of the operator-deployed database.                                                                                                                                                                          | -                  |
| `resource_requirements` | Object | Kubernetes resource requests and limits for the operator-deployed database pod. Ignored when using an external database. See[Resource requirements object](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansibleautomationplatform__aap_ansible_com_v1alpha1_#AnsibleAutomationPlatform__resource-requirements). | See defaults table |

## spec.controller

Configuration for the automation controller component. In addition to the fields listed here, this section accepts all fields from `AutomationController.spec`. For the full list of available fields, see [AutomationController spec](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-automation_controller_custom_resources#AutomationControllerAndMeshIngress__controller-spec).

| Field      | Type    | Description                                                                                      | Default |
| ---------- | ------- | ------------------------------------------------------------------------------------------------ | ------- |
| `disabled` | Boolean | Set to`true` to disable the automation controller component.                                     | `false` |
| `name`     | String  | Name of an existing`AutomationController` custom resource to register with the platform gateway. | -       |

## spec.eda

Configuration for the Event-Driven Ansible component. In addition to the fields listed here, this section accepts all fields from `EDA.spec`. For the full list of available fields, see [EDA spec](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-event_driven_ansible_custom_resources#EDA__spec).

| Field      | Type    | Description                                                                     | Default |
| ---------- | ------- | ------------------------------------------------------------------------------- | ------- |
| `disabled` | Boolean | Set to`true` to disable the Event-Driven Ansible component.                     | `false` |
| `name`     | String  | Name of an existing`EDA` custom resource to register with the platform gateway. | -       |

## spec.hub

Configuration for the automation hub component. In addition to the fields listed here, this section accepts all fields from `AutomationHub.spec`. For the full list of available fields, see [AutomationHub spec](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-automation_hub_custom_resources#AutomationHub__spec).

| Field      | Type    | Description                                                                               | Default |
| ---------- | ------- | ----------------------------------------------------------------------------------------- | ------- |
| `disabled` | Boolean | Set to`true` to disable the automation hub component.                                     | `false` |
| `name`     | String  | Name of an existing`AutomationHub` custom resource to register with the platform gateway. | -       |

## spec.lightspeed

Configuration for the Ansible Lightspeed component. In addition to the fields listed here, this section accepts all fields from `AnsibleLightspeed.spec`. For the full list of available fields, see [AnsibleLightspeed spec](/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansible_lightspeed_custom_resources#AnsibleLightspeed__spec).

| Field      | Type    | Description                                               | Default |
| ---------- | ------- | --------------------------------------------------------- | ------- |
| `disabled` | Boolean | Set to`true` to disable the Ansible Lightspeed component. | `true`  |

## Resource requirements object

All `resource_requirements` fields follow the standard Kubernetes resource specification pattern with `requests` and `limits`.

| Field             | Type   | Description                                                | Default             |
| ----------------- | ------ | ---------------------------------------------------------- | ------------------- |
| `requests.cpu`    | String | Minimum CPU allocation for the pod, for example`100m`.     | Varies by component |
| `requests.memory` | String | Minimum memory allocation for the pod, for example`256Mi`. | Varies by component |
| `limits.cpu`      | String | Maximum CPU the pod can consume, for example`500m`.        | Varies by component |
| `limits.memory`   | String | Maximum memory the pod can consume, for example`1000Mi`.   | Varies by component |

## Default resource requirements

The following table lists the default resource requests and limits for each component.

| Component               | CPU request | Memory request | CPU limit | Memory limit |
| ----------------------- | ----------- | -------------- | --------- | ------------ |
| `api` (gateway)         | 100m        | 256Mi          | 500m      | 1000Mi       |
| `redis` (platform)      | 100m        | 256Mi          | 500m      | 500Mi        |
| `database`              | 100m        | 256Mi          | 500m      | 800Mi        |
| `controller.task`       | 100m        | 150Mi          | 1000m     | 1200Mi       |
| `controller.web`        | 100m        | 200Mi          | 200m      | 1600Mi       |
| `controller.ee`         | 100m        | 64Mi           | 1000m     | 500Mi        |
| `controller.redis`      | 50m         | 64Mi           | 100m      | 200Mi        |
| `controller.rsyslog`    | 100m        | 128Mi          | 500m      | 250Mi        |
| `controller.init`       | 100m        | 128Mi          | 500m      | 200Mi        |
| `eda.api`               | 50m         | 350Mi          | 500m      | 400Mi        |
| `eda.ui`                | 25m         | 64Mi           | 500m      | 150Mi        |
| `eda.scheduler`         | 50m         | 200Mi          | 500m      | 250Mi        |
| `eda.worker`            | 25m         | 200Mi          | 250m      | 250Mi        |
| `eda.default_worker`    | 25m         | 200Mi          | 500m      | 400Mi        |
| `eda.activation_worker` | 25m         | 150Mi          | 500m      | 400Mi        |
| `eda.event_stream`      | 25m         | 150Mi          | 100m      | 300Mi        |
| `hub.api`               | 150m        | 256Mi          | 800m      | 500Mi        |
| `hub.content`           | 150m        | 256Mi          | 800m      | 1200Mi       |
| `hub.worker`            | 150m        | 256Mi          | 800m      | 400Mi        |
| `hub.web`               | 100m        | 256Mi          | 500m      | 300Mi        |
| `hub.redis`             | 100m        | 250Mi          | 300m      | 400Mi        |

## Example custom resource

The following example shows a basic `AnsibleAutomationPlatform` custom resource with an external database, S3 storage for automation hub, and Event-Driven Ansible SSL verification disabled:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: aap
spec:
  database:
    database_secret: postgres-config-gateway
  eda:
    automation_server_ssl_verify: 'no'
  hub:
    storage_type: 's3'
    object_storage_s3_secret: 'example-galaxy-object-storage'
```
