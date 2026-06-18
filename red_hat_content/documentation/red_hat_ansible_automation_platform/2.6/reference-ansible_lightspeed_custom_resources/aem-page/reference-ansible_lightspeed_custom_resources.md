+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansible_lightspeed_custom_resources"
title = "Ansible Lightspeed custom resources - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/reference-ansible_automation_platform_custom_resources/", "Ansible Automation Platform custom resources"]]
category = "Reference"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-ansible_lightspeed_custom_resources/aem-page/reference-ansible_lightspeed_custom_resources.html"
last_crumb = "Ansible Lightspeed custom resources"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Ansible Lightspeed custom resources"
oversized = "false"
page_slug = "reference-ansible_lightspeed_custom_resources"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/reference-ansible_lightspeed_custom_resources"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/reference-ansible_lightspeed_custom_resources/toc/toc.json"
type = "aem-page"
+++

# Ansible Lightspeed custom resources

The Ansible Lightspeed operator provides a custom resource for deploying and configuring the Ansible Lightspeed AI assistant service on OpenShift Container Platform.

The `AnsibleLightspeed` custom resource deploys and configures Ansible Lightspeed independently of the full Ansible Automation Platform deployment. Ansible Lightspeed provides AI-powered assistance for Ansible content creation. Use this custom resource when you need to manage Ansible Lightspeed as a standalone component rather than through the `AnsibleAutomationPlatform` resource.

## AnsibleLightspeed [lightspeed.ansible.com/v1alpha1]

The `AnsibleLightspeed` custom resource deploys and configures the Ansible Lightspeed AI assistant service.

### Description

| **API Group**   | `lightspeed.ansible.com` |
| --------------- | ------------------------ |
| **API Version** | `v1alpha1`               |
| **Kind**        | `AnsibleLightspeed`      |
| **Scope**       | Namespaced               |

### Specification

| Field                      | Type    | Description                                                                                                                                      | Default |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `disabled`                 | Boolean | Set to `true` to disable the Ansible Lightspeed component.                                                                                       | `true`  |
| `database`                 | Object  | Database configuration. Contains`database_secret` (String) specifying the name of a Kubernetes secret with external database connection details. | -       |
| `auth_config_secret_name`  | String  | Name of a Kubernetes secret containing authentication configuration for Ansible Lightspeed.                                                      | -       |
| `model_config_secret_name` | String  | Name of a Kubernetes secret containing model configuration for Ansible Lightspeed.                                                               | -       |

### Example custom resource

```
apiVersion: lightspeed.ansible.com/v1alpha1
kind: AnsibleLightspeed
metadata:
  name: my-lightspeed
spec:
  disabled: false
  auth_config_secret_name: lightspeed-auth-config
  model_config_secret_name: lightspeed-model-config
  database:
    database_secret: lightspeed-db-secret
```
