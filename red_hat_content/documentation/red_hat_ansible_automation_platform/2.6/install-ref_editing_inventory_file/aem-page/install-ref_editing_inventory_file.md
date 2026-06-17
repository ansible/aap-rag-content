+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_editing_inventory_file"
title = "Edit the inventory file - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_platform_install_overview/", "Install RPM-based Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_editing_inventory_file/aem-page/install-ref_editing_inventory_file.html"
last_crumb = "Edit the inventory file"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Edit the inventory file"
oversized = "false"
page_slug = "install-ref_editing_inventory_file"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-ref_editing_inventory_file"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_editing_inventory_file/toc/toc.json"
type = "aem-page"
+++

# Edit the inventory file

You can use the Ansible Automation Platform installer inventory file to specify your installation scenario.

## For an RPM installation

 *Procedure*

 **RPM installed package**

```
$ cd /opt/ansible-automation-platform/installer/
```
 **Bundled installer**

```
$ cd ansible-automation-platform-setup-bundle-<latest-version>
```
 **Online installer**

```
$ cd ansible-automation-platform-setup-<latest-version>
```

## For online installations

1. Open the `inventory` file with a text editor.

2. Edit the `inventory` file parameters to specify your installation scenario. For containerized installation, see [Configuring the inventory file](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_configuring_inventory_file#configuring-inventory-file "You can control the installation of Ansible Automation Platform with inventory files. Inventory files define the host details, certificate details, and component-specific settings needed to customize the installation.")

You can use one of the supported Installation scenario examples as the basis for your `inventory` file.
