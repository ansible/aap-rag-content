+++
title = "Deploy Ansible Automation Platform - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_install_aap_gateway"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_install_aap_gateway/aem-page/install-assembly_install_aap_gateway.html"
last_crumb = "Deploy Ansible Automation Platform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Deploy Ansible Automation Platform"
oversized = "false"
page_slug = "install-assembly_install_aap_gateway"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_install_aap_gateway"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_install_aap_gateway/toc/toc.json"
type = "aem-page"
+++

# Deploy Ansible Automation Platform

As a namespace administrator, you can use Ansible Automation Platform gateway to manage Ansible Automation Platform components in your OpenShift environment.

The Ansible Automation Platform gateway uses the Ansible Automation Platform custom resource to manage and integrate the following Ansible Automation Platform components into a unified user interface:

- Automation controller
- Automation hub
- Event-Driven Ansible
- Red Hat Ansible Lightspeed (This feature is disabled by default, you must opt in to use it.)


Before you can deploy the platform gateway you must have Ansible Automation Platform Operator installed in a namespace. If you have not installed Ansible Automation Platform Operator see **Installing the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform**.

If you have the Ansible Automation Platform Operator and some or all of the Ansible Automation Platform components installed see **Deploying the platform gateway with existing Ansible Automation Platform components** for how to proceed.
