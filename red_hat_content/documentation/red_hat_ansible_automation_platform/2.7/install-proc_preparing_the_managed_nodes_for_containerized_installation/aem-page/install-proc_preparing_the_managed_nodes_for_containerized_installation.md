+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_preparing_the_managed_nodes_for_containerized_installation"
template = "docs/aem-title.html"
title = "Prepare the managed nodes - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_preparing_the_managed_nodes_for_containerized_installation/aem-page/install-proc_preparing_the_managed_nodes_for_containerized_installation.html"
last_crumb = "Prepare the managed nodes"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Prepare the managed nodes"
oversized = "false"
page_slug = "install-proc_preparing_the_managed_nodes_for_containerized_installation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_preparing_the_managed_nodes_for_containerized_installation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_preparing_the_managed_nodes_for_containerized_installation/toc/toc.json"
type = "aem-page"
+++

# Prepare the managed nodes

Managed nodes, or hosts, are the devices managed by Ansible Automation Platform. To ensure a secure containerized setup, create a dedicated user on each node for Ansible Automation Platform to use when connecting and running tasks.

## Procedure

1.  Log in to the host as the root user.
2.  Create a new user. Replace `<username>` with the username you want, for example `aap`.

```
$ sudo adduser <username>
```

3.  Set a password for the new user. Replace `<username>` with the username you created.

```
$ sudo passwd <username>
```

4.  Configure the user to run `sudo` commands. For a secure and maintainable installation, configure `sudo` privileges for the installation user in a dedicated file within the `/etc/sudoers.d/` directory.

  1.  Create a dedicated `sudoers` file for the user:
  

```
$ sudo visudo -f /etc/sudoers.d/<username>
```

  2.  Add the following line to the file, replacing `<username>` with the username you created:
  

```
<username> ALL=(ALL) NOPASSWD: ALL
```

  3.  Save and exit the file.
