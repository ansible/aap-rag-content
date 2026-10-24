+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_installing_builder"
title = "Install Ansible Builder to create or edit execution environments - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_devtools_install/", "Set up your development environment"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_installing_builder/aem-page/install-proc_installing_builder.html"
last_crumb = "Install Ansible Builder to create or edit execution environments"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Install Ansible Builder to create or edit execution environments"
oversized = "false"
page_slug = "install-proc_installing_builder"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_installing_builder"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_installing_builder/toc/toc.json"
type = "aem-page"
+++

# Install Ansible Builder to create or edit execution environments

Ansible Builder is included in the Ansible development tools package, but you can also install it standalone if you only need to create or manage execution environments. Builder creates custom execution environments that contain the dependencies and collections required for your automation content.

## Before you begin

- You have installed the Podman container runtime.
- You have valid subscriptions attached on the host. With a valid subscription you can access the subscription-only resources needed to install `ansible-builder`, and ensures that the necessary repository for `ansible-builder` is automatically enabled. See [Register your Red Hat Enterprise Linux hosts](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_attaching_subscriptions "You must register all nodes with Red Hat Subscription Management (RHSM) before installing Ansible Automation Platform.") for more information. Note:
      To install the developer tools without consuming a managed node subscription, you can use MCT4589-Red Hat Ansible Developer, Standard (10 Managed Nodes), which is available at no cost. This subscription requires the approval of the Ansible Business Unit.

## Procedure

Run the following command to install Ansible Builder and activate your Ansible Automation Platform repo:

```
#  dnf install --enablerepo=ansible-automation-platform-*aap-version*-for-rhel-*rhel-version*-x86_64-rpms
  ansible-builder
```

Replace *aap-version* with your Ansible Automation Platform version and *rhel-version* with your Red Hat Enterprise Linux major version.
