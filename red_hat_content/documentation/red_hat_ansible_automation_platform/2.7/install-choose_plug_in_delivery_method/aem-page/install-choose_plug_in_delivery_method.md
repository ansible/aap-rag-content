+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-choose_plug_in_delivery_method"
title = "Plug-in delivery method - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-choose_plug_in_delivery_method/aem-page/install-choose_plug_in_delivery_method.html"
last_crumb = "Plug-in delivery method"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Plug-in delivery method"
oversized = "false"
page_slug = "install-choose_plug_in_delivery_method"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-choose_plug_in_delivery_method"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-choose_plug_in_delivery_method/toc/toc.json"
type = "aem-page"
+++

# Plug-in delivery method

Ansible plug-ins for Red Hat Developer Hub support two delivery methods. Select the method that fits your environment.

Ansible automation portal supports two plug-in delivery methods:

- **OCI container delivery (recommended)**: Ansible automation portal automatically pulls an Open Container Initiative (OCI) container from `registry.redhat.io` that contains the plug-ins. Use this method for new installations.
- **HTTP plug-in registry (deprecated)**: Manually create an HTTP plug-in registry that hosts plug-in tarball files. This method is deprecated and will be removed in a future release of Ansible Automation Platform. Existing installations that use this method should migrate to OCI container delivery.


Note:

If you are installing Ansible automation portal in a disconnected or air-gapped OpenShift Container Platform environment, complete the pre-installation configuration in this chapter and then follow the procedures in the disconnected installation chapter. The disconnected installation chapter includes additional steps for mirroring container images, configuring registry authentication, and installing the Helm chart in isolated environments.
