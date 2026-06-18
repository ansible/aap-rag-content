+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_choosing_installation_type"
template = "docs/aem-title.html"
title = "Choose an installation type - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_choosing_installation_type/aem-page/install-con_choosing_installation_type.html"
last_crumb = "Choose an installation type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Choose an installation type"
oversized = "false"
page_slug = "install-con_choosing_installation_type"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-con_choosing_installation_type"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_choosing_installation_type/toc/toc.json"
type = "aem-page"
+++

# Choose an installation type

Containerized Ansible Automation Platform supports two installation types: online and disconnected. Review the requirements for each to decide which is appropriate for your environment.

## Online installation

An online installation pulls container images directly from Red Hat registries during the installation process.

 **Requirements:**

- An active internet connection on all Ansible Automation Platform nodes
- A Red Hat registry service account with credentials (`registry_username` and `registry_password`)
- Network access to Red Hat registries (registry.redhat.io)


For online installation instructions, see *Prepare the installation* in the related information section.

## Disconnected (bundled) installation

A disconnected installation uses a pre-packaged bundle that includes all container images and dependencies. This installation type is designed for air-gapped or restricted network environments.

 **Requirements:**

- Local RPM repository configured with required dependencies
- No internet connection required during installation
- Red Hat registry credentials are not required


For disconnected installation instructions, see *Install in a disconnected environment* in the related information section.
