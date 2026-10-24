+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_reinstalling_containerized_aap"
template = "docs/aem-title.html"
title = "Reinstall containerized Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_reinstalling_containerized_aap/aem-page/install-proc_reinstalling_containerized_aap.html"
last_crumb = "Reinstall containerized Ansible Automation Platform"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Reinstall containerized Ansible Automation Platform"
oversized = "false"
page_slug = "install-proc_reinstalling_containerized_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_reinstalling_containerized_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_reinstalling_containerized_aap/toc/toc.json"
type = "aem-page"
+++

# Reinstall containerized Ansible Automation Platform

Reinstall a containerized deployment after uninstalling and preserving the database.

## Procedure

Follow the steps in [Install containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_installing_containerized_aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.") and include the existing secret key value in the playbook command:

```
$ ansible-playbook -i inventory ansible.containerized_installer.install -e controller_secret_key=<secret_key_value>
```
