+++
title = "Download Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_downloading_containerized_aap"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_downloading_containerized_aap/aem-page/install-proc_downloading_containerized_aap.html"
last_crumb = "Download Ansible Automation Platform"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Download Ansible Automation Platform"
oversized = "false"
page_slug = "install-proc_downloading_containerized_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_downloading_containerized_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_downloading_containerized_aap/toc/toc.json"
type = "aem-page"
+++

# Download Ansible Automation Platform

Choose the installation program you need based on your Red Hat Enterprise Linux environment internet connectivity and download the installation program to your Red Hat Enterprise Linux host.

## Before you begin

- You have logged in to the Red Hat Enterprise Linux host as your non-root user.

## Procedure

1.  Download the latest version of containerized Ansible Automation Platform from the [Ansible Automation Platform download page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software).   1.  For online installations: **Ansible Automation Platform 2.7 Containerized Setup**
  2.  For offline or bundled installations: **Ansible Automation Platform 2.7 Containerized Setup Bundle**
2.  Copy the installation program `.tar.gz` file and the optional manifest `.zip` file onto your Red Hat Enterprise Linux host. Use the `scp` command to securely copy the files. The basic syntax for `scp` is:

```
scp [options] <path_to_source_file> <path_to_destination>
```
    For example, use the following `scp` command to copy the installation program `.tar.gz` file to an AWS EC2 instance with a private key (replace the placeholder `<>` values with your actual information):

```
scp -i <path_to_private_key> ansible-automation-platform-containerized-setup-<version_number>.tar.gz ec2-user@<remote_host_ip_or_hostname>:<path_to_destination>
```

3.  Decide where you want the installation program to reside on the file system. This is your installation directory.   1.  The installation creates installation-related files under this location and requires at least 15 GB for the initial installation.
4.  Unpack the installation program `.tar.gz` file into your installation directory, and go to the unpacked directory.   1.  To unpack the online installer:
  

```
$ tar xfvz ansible-automation-platform-containerized-setup-<version_number>.tar.gz
```

  2.  To unpack the offline or bundled installer:
  

```
$ tar xfvz ansible-automation-platform-containerized-setup-bundle-<version_number>-<arch_name>.tar.gz
```
