+++
title = "Plug-in delivery method - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/con_self_service_choose_plugin_delivery"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/con_self_service_choose_plugin_delivery/aem-page/con_self_service_choose_plugin_delivery.html"
last_crumb = "Plug-in delivery method"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Plug-in delivery method"
oversized = "false"
page_slug = "con_self_service_choose_plugin_delivery"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/con_self_service_choose_plugin_delivery"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/con_self_service_choose_plugin_delivery/toc/toc.json"
type = "aem-page"
+++

# Plug-in delivery method

Ansible automation portal supports two plug-in delivery methods. Use OCI container delivery for new installations, or plan to migrate from the deprecated HTTP plug-in registry.

- **OCI container delivery (recommended):** Ansible automation portal pulls an Open Container Initiative (OCI) image from `registry.redhat.io` that contains the Ansible plug-ins. Use this method for new installations and production deployments.
- **HTTP plug-in registry (deprecated):** You deploy an in-cluster HTTP service that hosts plug-in tarball files. This method is deprecated and will be removed in a future release of Ansible Automation Platform. If you already use this method, plan to migrate to OCI container delivery.


Important:

Set `redhat-developer-hub.global.pluginMode` to `oci`. The chart default is `tarball`. Before you install, confirm your environment is supported on the Ansible automation portal lifecycle page (portal version, Ansible Automation Platform compatibility, and OpenShift Container Platform compatibility).

Note:

For a disconnected cluster, complete the prerequisites in this guide, then continue with the disconnected installation guide.
