+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_running_setup_script"
title = "Run the setup script - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_platform_install_overview/", "Install RPM-based Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_running_setup_script/aem-page/install-proc_running_setup_script.html"
last_crumb = "Run the setup script"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Run the setup script"
oversized = "false"
page_slug = "install-proc_running_setup_script"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_running_setup_script"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_running_setup_script/toc/toc.json"
type = "aem-page"
+++

# Run the setup script

Run the installation program setup script after updating the inventory file with all the required parameters to begin the installation and configuration of the platform.

## About this task

 **RPM installer**

## Procedure

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

## Results

Installation of Red Hat Ansible Automation Platform will begin.
