+++
title = "Automation portal operator - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-automation_portal_operator"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-automation_portal_operator/aem-page/whats_new-automation_portal_operator.html"
last_crumb = "Automation portal operator"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Automation portal operator"
oversized = "false"
page_slug = "whats_new-automation_portal_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-automation_portal_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-automation_portal_operator/toc/toc.json"
type = "aem-page"
+++

# Automation portal operator

The automation portal operator deploys and manages Ansible automation portal on OpenShift using a declarative custom resource.

The automation portal operator follows a compose-via-CRD pattern with two operators working together. The automation portal operator reads the `AutomationPortal` custom resource, validates credentials, generates plugin configuration, and creates a custom resource. The Red Hat Developer Hub (RHDH) Operator reads the custom resource and creates the Deployment, Service, Route, and PostgreSQL database. When you create an `AutomationPortal` custom resource, the operator automatically installs the RHDH Operator if it is not already present on the cluster.

The operator reports five status conditions on the `AutomationPortal` custom resource. The overall `Ready` condition is `True` only when all other conditions are `True`.

For more information, see *Install automation portal on OpenShift using the operator*.
