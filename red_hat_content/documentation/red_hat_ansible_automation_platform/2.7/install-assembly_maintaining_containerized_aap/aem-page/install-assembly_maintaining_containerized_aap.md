+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_maintaining_containerized_aap"
title = "Maintain containerized Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_maintaining_containerized_aap/aem-page/install-assembly_maintaining_containerized_aap.html"
last_crumb = "Maintain containerized Ansible Automation Platform"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Maintain containerized Ansible Automation Platform"
oversized = "false"
page_slug = "install-assembly_maintaining_containerized_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-assembly_maintaining_containerized_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_maintaining_containerized_aap/toc/toc.json"
type = "aem-page"
+++

# Maintain containerized Ansible Automation Platform

Update, backup, restore, uninstall, or reinstall containerized Ansible Automation Platform deployments to support your automation infrastructure.

## Uninstall containerized Ansible Automation Platform

Uninstall your container-based installation of Ansible Automation Platform.

### Before you begin

- You have logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.

### Procedure

1.  If you intend to reinstall Ansible Automation Platform and want to use the preserved databases, you must collect the existing secret keys:
  1.  First, list the available secrets:
  

```
$ podman secret list
```

  2.  Next, collect the secret keys by running the following command:
  

```
$ podman secret inspect --showsecret <secret_key_variable> | jq -r .[].SecretData
```
        For example:

```
$ podman secret inspect --showsecret controller_secret_key | jq -r .[].SecretData
```

2.  Run the `uninstall` playbook:
  

```
$ ansible-playbook -i inventory ansible.containerized_installer.uninstall
```
  - This stops all systemd units and containers and then deletes all resources used by the containerized installer such as:
    * configuration and data directories and files
    * systemd unit files
    * Podman containers and images
    * RPM packages
  - To keep container images, set the `container_keep_images` parameter to `true`.

```
$ ansible-playbook -i inventory ansible.containerized_installer.uninstall -e container_keep_images=true
```

  - To keep PostgreSQL databases, set the `postgresql_keep_databases` parameter to `true`.

```
$ ansible-playbook -i inventory ansible.containerized_installer.uninstall -e postgresql_keep_databases=true
```

## Reinstall containerized Ansible Automation Platform

Reinstall a containerized deployment after uninstalling and preserving the database.

### Procedure

 Follow the steps in [Install containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_installing_containerized_aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.") and include the existing secret key value in the playbook command:

```
$ ansible-playbook -i inventory ansible.containerized_installer.install -e controller_secret_key=<secret_key_value>
```
