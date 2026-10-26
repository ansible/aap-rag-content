+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-understand_the_automation_portal_operator"
title = "Understand the automation portal operator - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-understand_the_automation_portal_operator/aem-page/install-understand_the_automation_portal_operator.html"
last_crumb = "Understand the automation portal operator"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Understand the automation portal operator"
oversized = "false"
page_slug = "install-understand_the_automation_portal_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-understand_the_automation_portal_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-understand_the_automation_portal_operator/toc/toc.json"
type = "aem-page"
+++

# Understand the automation portal operator

The automation portal operator deploys and manages Ansible automation portal on OpenShift using a declarative custom resource.

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

## How the operator works

The automation portal operator follows a compose-via-CRD pattern with two operators working together:

- **Automation portal operator** — reads the `AutomationPortal` custom resource, validates credentials, generates plugin configuration, and creates a custom resource.
- **Red Hat Developer Hub (RHDH) Operator** — reads the custom resource and creates the Deployment, Service, Route, and PostgreSQL database.

When you create an `AutomationPortal` custom resource, the operator automatically installs the RHDH Operator if it is not already present on the cluster.

For details on the acceptable usage and support scope for Red Hat Developer Hub with automation portal, refer to the *Ansible automation portal Support Policy* article.

## Status conditions

The operator reports five status conditions on the `AutomationPortal` custom resource. The overall `Ready` condition is `True` only when all other conditions are `True`.

| Condition           | True                                               | False                                     |
| ------------------- | -------------------------------------------------- | ----------------------------------------- |
| `RHDHOperatorReady` | RHDH Operator installed,`Backstage` CRD registered | RHDH Operator missing or installing       |
| `SecretsValid`      | All referenced Secrets exist with required keys    | Secret missing, key missing, or key empty |
| `PluginsConfigured` | Dynamic plugins ConfigMap generated                | Configuration generation failed           |
| `BackstageReady`    | Automation portal deployment healthy and serving   | Automation portal pods not ready          |
| `Ready`             | All conditions True                                | One or more conditions False              |
