+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_self_service_supported_platforms"
template = "docs/aem-title.html"
title = "Supported platforms - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_self_service_supported_platforms/aem-page/install-ref_self_service_supported_platforms.html"
last_crumb = "Supported platforms"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Supported platforms"
oversized = "false"
page_slug = "install-ref_self_service_supported_platforms"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-ref_self_service_supported_platforms"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_self_service_supported_platforms/toc/toc.json"
type = "aem-page"
+++

# Supported platforms

Ansible automation portal supports installation using a Helm chart on OpenShift Container Platform.

- For information about the Ansible automation portal lifecycle and supported platfoms, see the [Ansible Automation Platform Ansible automation portal lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page on the Red Hat customer portal.
- For information about the Ansible automation portal support policy, see the [Ansible Automation Platform Ansible automation portal support policy](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-support-policy) page on the Red Hat customer portal.

## Interactive demonstration

You can explore the functionality of Ansible automation portal in an interactive demonstration:

- Launch the [Ansible automation portal interactive demo](https://interact.redhat.com/share/RZM69zpDpc5ymd63pMQv).

### Prerequisites

Review the mandatory subscriptions, permissions, and platform access required before starting the installation. Fulfilling these needs helps ensure a successful deployment.

- You have a valid subscription to Red Hat Ansible Automation Platform.
- You have access to an instance of Red Hat Ansible Automation Platform 2.6 with the appropriate permissions to create an OAuth application.
- You have access to an OpenShift Container Platform instance with the appropriate permissions within your project to create an application.
- You have installed `oc`, the OpenShift command-line interface (CLI) tool, on your local machine. You can use `oc` commands in your terminal to interact with your OpenShift cluster.
- You have installed Helm 3.10 or newer. Helm is a package manager for applications on OpenShift Container Platform.

### Pre-installation configuration

You can deploy Ansible automation portal from a Helm chart on OpenShift Container Platform.

Helm is a tool that simplifies deployment of applications on Red Hat OpenShift Container Platform clusters. Helm uses a packaging format called Helm charts. A Helm chart is a package of files that define how an application is deployed and managed on OpenShift. The Helm chart for Ansible automation portal is available in the OpenShift Helm catalog.
