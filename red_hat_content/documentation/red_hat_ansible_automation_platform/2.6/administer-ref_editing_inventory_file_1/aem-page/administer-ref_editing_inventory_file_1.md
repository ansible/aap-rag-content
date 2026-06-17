+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-ref_editing_inventory_file_1"
title = "Edit the inventory file - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_install_mesh/", "Scale with automation mesh in a containerized or VM environment"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-ref_editing_inventory_file_1/aem-page/administer-ref_editing_inventory_file_1.html"
last_crumb = "Edit the inventory file"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Edit the inventory file"
oversized = "false"
page_slug = "administer-ref_editing_inventory_file_1"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-ref_editing_inventory_file_1"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-ref_editing_inventory_file_1/toc/toc.json"
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

 **For online installations**

```
cd <path-to-source-file>/ansible-automation-platform-containerized-setup-<version_number>
```
 **For offline or bundled installations**

```
cd <path-to-source-file/ansible-automation-platform-containerized-setup-bundle-<version_number>-<arch_name>
```


1. Open the `inventory` file with a text editor.

2. Edit the `inventory` file parameters to specify your installation scenario. For containerized installation, see [Configuring the inventory file](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_configuring_inventory_file#configuring-inventory-file "You can control the installation of Ansible Automation Platform with inventory files. Inventory files define the host details, certificate details, and component-specific settings needed to customize the installation.")

## Run the setup script

Run the installation program setup script after updating the inventory file with all the required parameters to begin the installation and configuration of the platform.

### About this task

 **RPM installer**

### Procedure

 Run the `setup.sh` script

```
$ sudo ./setup.sh
```


Note:

If you are running the setup as a non-root user with `sudo` privileges, you can use the following command:

```
$ ANSIBLE_BECOME_METHOD='sudo'
ANSIBLE_BECOME=True ./setup.sh
```

### Results

Installation of Red Hat Ansible Automation Platform will begin.

### What to do next

If you want to add additional nodes to your automation mesh after the initial setup, edit the inventory file to add the new node, then rerun the `setup.sh` script.

 **Containerized installer**

For information on installing containerized Ansible Automation Platform, see [Installing containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_installing_containerized_aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.")

## Import a CA certificate

A Certificate Authority (CA) verifies and signs individual node certificates in an automation mesh environment. You can provide your own CA by specifying the path to the certificate and the private RSA key file in the `inventory` file of your Red Hat Ansible Automation Platform installer.

### About this task

Note:

The Ansible Automation Platform installation program generates a CA if you do not provide one.

### Procedure

1.  Open the `inventory` file for editing.
2.  Add the `mesh_ca_keyfile` variable and specify the full path to the private RSA key (`.key`).
3.  Add the `mesh_ca_certfile` variable and specify the full path to the CA certificate file (`.crt`).
4.  Save the changes to the inventory file.

```
[all:vars]
mesh_ca_keyfile=/tmp/<mesh_CA>.key
mesh_ca_certfile=/tmp/<mesh_CA>.crt
```

5.  With the CA files added to the inventory file, run the installation program to apply the CA.

### Results

This process copies the CA to the to `/etc/receptor/tls/ca/` directory on each control and execution node on your mesh network.
