+++
template = "docs/aem-title.html"
title = "Install containerized Ansible Automation Platform - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_installing_containerized_aap"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_installing_containerized_aap/aem-page/install-proc_installing_containerized_aap.html"
last_crumb = "Install containerized Ansible Automation Platform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install containerized Ansible Automation Platform"
oversized = "false"
page_slug = "install-proc_installing_containerized_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_installing_containerized_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_installing_containerized_aap/toc/toc.json"
type = "aem-page"
+++

# Install containerized Ansible Automation Platform

Run the `install` playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.

## Before you begin

- You have prepared the Red Hat Enterprise Linux host
- You have prepared the managed nodes
- You have downloaded Ansible Automation Platform
- You have configured the inventory file
- You are logged in to the Red Hat Enterprise Linux host as your non-root user

## Procedure

1.  Go to the installation directory on your Red Hat Enterprise Linux host.
2.  Run the `install` playbook:
  

```
ansible-playbook -i <inventory_file_name> ansible.containerized_installer.install
```
    For example:

```
ansible-playbook -i inventory ansible.containerized_installer.install
```
    You can add additional parameters to the installation command as needed:

```
ansible-playbook -i <inventory_file_name> -e @<vault_file_name> --ask-vault-pass -K -v ansible.containerized_installer.install
```
    For example:

```
ansible-playbook -i inventory -e @vault.yml --ask-vault-pass -K -v  ansible.containerized_installer.install
```
  - `-i <inventory_file_name>` - The inventory file to use for the installation.
  - `-e @<vault_file_name> --ask-vault-pass` - (Optional) If you are using a vault to store sensitive variables, add this to the installation command.
  - `-K` - (Optional) If your privilege escalation (becoming root) requires you to enter a password, add this to the installation command. You are then prompted for the BECOME password.
  - `-v` - (Optional) You can use increasing verbosity, up to 4 (`-vvvv`) to see installation process details. This can significantly increase installation time. Use it only as needed or when requested by Red Hat support.

## Results

- After the installation completes, verify that you can access Ansible Automation Platform which is available by default at the following URL:

```
https://<gateway_node>:443
```

- Log in as the admin user with the credentials you created for `gateway_admin_username` and `gateway_admin_password`.
- The default ports and protocols used for Ansible Automation Platform are 80 (HTTP) and 443 (HTTPS). You can customize the ports with the following variables:

```
envoy_http_port=80
envoy_https_port=443
```

- If you want to disable HTTPS, set `envoy_disable_https` to `true`:

```
envoy_disable_https: true
```
