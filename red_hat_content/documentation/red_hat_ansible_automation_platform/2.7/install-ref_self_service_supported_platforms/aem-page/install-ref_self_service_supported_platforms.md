+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_self_service_supported_platforms"
title = "Supported platforms for Ansible automation portal - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_self_service_supported_platforms/aem-page/install-ref_self_service_supported_platforms.html"
last_crumb = "Supported platforms for Ansible automation portal"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Supported platforms for Ansible automation portal"
oversized = "false"
page_slug = "install-ref_self_service_supported_platforms"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_self_service_supported_platforms"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_self_service_supported_platforms/toc/toc.json"
type = "aem-page"
+++

# Supported platforms for Ansible automation portal

Ansible automation portal supports deployment on OpenShift Container Platform and Red Hat Enterprise Linux, and maintains compatibility across Ansible Automation Platform 2.5, 2.6, and 2.7.

## Ansible Automation Platform version compatibility

Ansible automation portal operates on an independent, asynchronous release schedule from the core platform. A given release of Ansible automation portal remains compatible with multiple Ansible Automation Platform releases.

*Table 1. Ansible automation portal compatibility matrix*

| Component                          | Supported versions                                                                                          |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Ansible Automation Platform        | Versions 2.5, 2.6, and 2.7                                                                                  |
| OpenShift Container Platform       | Version 4.14 and later (Helm chart; Operator available in version 2.7)                                      |
| Red Hat Enterprise Linux appliance | Red Hat Enterprise Linux 9.4 and later deployed on KVM, Red Hat OpenShift Virtualization, or VMware vSphere |

Note:

Ansible automation portal connects to Ansible Automation Platform 2.5, 2.6, and 2.7 instances. For OpenShift Helm deployments connecting to an Ansible Automation Platform 2.5 instance, see the self-service automation portal documentation published on the Red Hat Customer Portal. For RHEL appliance deployments, use the version-agnostic deployment instructions in this guide.

## Lifecycle and support policies

For additional details regarding support tiers, release milestones, and platform maintenance:

- For information about the Ansible automation portal lifecycle and supported platforms, see the [Ansible Automation Platform Ansible automation portal lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page on the Red Hat Customer Portal.
- For information about the Ansible automation portal support policy, see the [Ansible Automation Platform Ansible automation portal support policy](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-support-policy) page on the Red Hat Customer Portal.
