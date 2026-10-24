+++
template = "docs/aem-title.html"
title = "Install automation portal on OpenShift using the operator - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_using_the_operator"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_using_the_operator/aem-page/install-install_automation_portal_on_openshift_using_the_operator.html"
last_crumb = "Install automation portal on OpenShift using the operator"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Install automation portal on OpenShift using the operator"
oversized = "false"
page_slug = "install-install_automation_portal_on_openshift_using_the_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_using_the_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_using_the_operator/toc/toc.json"
type = "aem-page"
+++

# Install automation portal on OpenShift using the operator

Install Ansible automation portal on OpenShift Container Platform using the automation portal operator. This installation method is available as a Technology Preview.

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

The automation portal operator automates the deployment and configuration of Ansible automation portal on OpenShift. The operator manages the full lifecycle of the automation portal, including installation, configuration, and upgrades.

The operator follows a compose-via-CRD pattern. It generates portal-specific configuration and creates a custom resource that reconciles into a running automation portal deployment.
