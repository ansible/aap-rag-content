+++
title = "Install Ansible Builder to create or edit execution environments - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_installing_builder"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_installing_builder/", "Install Ansible Builder to create or edit execution environments"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_installing_builder/aem-page/install-proc_installing_builder.html"
last_crumb = "Install Ansible Builder to create or edit execution environments"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install Ansible Builder to create or edit execution environments"
oversized = "false"
page_slug = "install-proc_installing_builder"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_installing_builder"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_installing_builder/toc/toc.json"
type = "aem-page"
+++

# Install Ansible Builder to create or edit execution environments

Install Ansible Builder to create custom execution environments that contain the dependencies and collections required for your automation content. You need a valid Red Hat subscription and Podman installed on your RHEL system.

## Before you begin

- You have installed the Podman container runtime.
- You have valid subscriptions attached on the host. With a valid subscription you can access the subscription-only resources needed to install `ansible-builder`, and ensures that the necessary repository for `ansible-builder` is automatically enabled. See [Attaching your Red Hat Ansible Automation Platform subscription](/documentation/en-us/red_hat_ansible_automation_platform/2.6/plan-proc_attaching_subscriptions "You must have valid subscriptions on all nodes before installing Red Hat Ansible Automation Platform.") for more information. Note:
      To install the developer tools without consuming a managed node subscription, you can use MCT4589-Red Hat Ansible Developer, Standard (10 Managed Nodes), which is available at no cost. This subscription requires the approval of the Ansible Business Unit.

## Procedure

 Run the following command to install Ansible Builder and activate your Ansible Automation Platform repo:

```
#  dnf install --enablerepo=ansible-automation-platform-*aap-version*-for-rhel-*rhel-version*-x86_64-rpms
  ansible-builder
```
Replace *aap-version* with your Ansible Automation Platform version and *rhel-version* with your Red Hat Enterprise Linux major version.
