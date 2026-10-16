+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform"
title = "Install automation portal on OpenShift Container Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/aem-page/install-install_automation_portal_on_openshift_container_platform.html"
last_crumb = "Install automation portal on OpenShift Container Platform"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Install automation portal on OpenShift Container Platform"
oversized = "false"
page_slug = "install-install_automation_portal_on_openshift_container_platform"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/toc/toc.json"
type = "aem-page"
+++

# Install automation portal on OpenShift Container Platform

Install Ansible automation portal on OpenShift Container Platform. Choose the installation method that matches your operational requirements.

## Choose your installation method

Ansible automation portal supports two installation methods on OpenShift Container Platform. For VM-based deployments on RHEL, see *Deploy the Ansible automation portal RHEL appliance*.

| Installation method               | Platform                                       | Lifecycle management                                                         | Disconnected support                                                                | When to use                                                                           |
| --------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Helm chart**                    | OpenShift Container Platform                   | Helm. Manual`helm upgrade` for configuration changes and version updates.    | Yes. Mirror container images and Helm chart packages.                               | You have an existing Helm-based deployment or prefer Helm-based lifecycle management. |
| **Operator** (Technology Preview) | OpenShift Container Platform 4.18 through 4.23 | Operator Lifecycle Manager (OLM). Automated install, upgrade, and uninstall. | Yes. Mirror operator bundle, catalog, and container images to an internal registry. | You want declarative, operator-managed deployments on OpenShift.                      |
