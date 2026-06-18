+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_devtools_install_rpm"
template = "docs/aem-title.html"
title = "Install Ansible development tools from an RPM package - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_devtools_install/", "Install Ansible development tools"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_devtools_install_rpm/aem-page/install-proc_devtools_install_rpm.html"
last_crumb = "Install Ansible development tools from an RPM package"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Install Ansible development tools from an RPM package"
oversized = "false"
page_slug = "install-proc_devtools_install_rpm"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_devtools_install_rpm"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_devtools_install_rpm/toc/toc.json"
type = "aem-page"
+++

# Install Ansible development tools from an RPM package

Ansible development tools are available as an RPM package for Red Hat Enterprise Linux. Install the tools on your local RHEL system using a package manager.

## Before you begin

- You have installed a supported version of Red Hat Enterprise Linux.
- You have registered your system with Red Hat Subscription Manager.
- You have installed a containerization platform, for example Podman or Docker.

## Procedure

1.  Run the following command to check whether Simple Content Access (SCA) is enabled:
  

```shell
$ sudo subscription-manager status
```
    If Simple Content Access is enabled, the output contains the following message:

```
Content Access Mode is set to Simple Content Access.
```
  1.  If Simple Content Access is not enabled, attach the Red Hat Ansible Automation Platform SKU:
  

```shell
$ sudo subscription-manager attach --pool=<sku-pool-id>
```

2.  Install Ansible development tools with the following command:
  

```shell
$ sudo dnf install
  --enablerepo=ansible-automation-platform-*aap-version*-for-rhel-*rhel-version*-x86_64-rpms ansible-dev-tools
```
    Replace *aap-version* with your Ansible Automation Platform version and *rhel-version* with your Red Hat Enterprise Linux major version.

## Results

1. Verify that the Ansible development tools have been installed:

```shell
$ rpm -aq | grep ansible-dev-tools
```
     If the installation was successful, the output shows the `ansible-dev-tools` package and its version number, for example:



```
ansible-dev-tools-25.8.3-1.el9ap.noarch
```

2. On successful installation, you can view the help documentation for the `ansible-creator` utility:

```
$ ansible-creator --help

    usage: ansible-creator [-h] [--version] command ...

    The fastest way to generate all your ansible content.

    Positional arguments:
   command
    add           Add resources to an existing Ansible project.
    init          Initialize a new Ansible project.

    Options:
   --version      Print ansible-creator version and exit.
   -h     --help  Show this help message and exit
```
