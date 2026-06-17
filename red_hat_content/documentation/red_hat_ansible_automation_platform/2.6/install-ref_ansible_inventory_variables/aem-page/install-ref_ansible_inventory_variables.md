+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_ansible_inventory_variables"
template = "docs/aem-title.html"
title = "Ansible variables - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_appendix_inventory_file_vars/", "Inventory file variables"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_ansible_inventory_variables/aem-page/install-ref_ansible_inventory_variables.html"
last_crumb = "Ansible variables"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Ansible variables"
oversized = "false"
page_slug = "install-ref_ansible_inventory_variables"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-ref_ansible_inventory_variables"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-ref_ansible_inventory_variables/toc/toc.json"
type = "aem-page"
+++

# Ansible variables

The following variables control how Ansible Automation Platform interacts with remote hosts.

*Table 1. Ansible variables*

| Variable                            | Description                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `ansible_connection`           | <br>The connection plugin used for the task on the target host. This can be the name of any Ansible connection plugin.<br>SSH protocol types are `smart`, `ssh`, or `paramiko`. You can also use `local` to run tasks on the control node itself.<br>Default = `smart`                                                                          |
| <br> `ansible_host`                 | <br>The IP address or name of the target host to use instead of `inventory_hostname`.                                                                                                                                                                                                                                                           |
| <br> `ansible_password`             | <br>The password to authenticate to the host.<br>Do not store this variable in plain text. Always use a vault.                                                                                                                                                                                                                                  |
| <br> `ansible_port`                 | <br>The connection port number.<br>The default for SSH is `22`.                                                                                                                                                                                                                                                                                 |
| <br> `ansible_scp_extra_args`       | <br>This setting is always appended to the default `scp` command line.                                                                                                                                                                                                                                                                          |
| <br> `ansible_sftp_extra_args`      | <br>This setting is always appended to the default `sftp` command line.                                                                                                                                                                                                                                                                         |
| <br> `ansible_shell_executable`     | <br>This sets the shell that the Ansible controller uses on the target machine and overrides the executable in `ansible.cfg` which defaults to `/bin/sh`.                                                                                                                                                                                       |
| <br> `ansible_shell_type`           | <br>The shell type of the target system.<br>Do not use this setting unless you have set the `ansible_shell_executable` to a non-Bourne (sh) compatible shell. By default commands are formatted using sh-style syntax. Setting this to `csh` or `fish` causes commands executed on target systems to follow the syntax of those shells instead. |
| <br> `ansible_ssh_common_args`      | <br>This setting is always appended to the default command line for `sftp`, `scp`, and `ssh`. Useful to configure a `ProxyCommand` for a certain host or group.                                                                                                                                                                                 |
| <br> `ansible_ssh_executable`       | <br>This setting overrides the default behavior to use the system `ssh`. This can override the `ssh_executable` setting in `ansible.cfg`.                                                                                                                                                                                                       |
| <br> `ansible_ssh_extra_args`       | <br>This setting is always appended to the default `ssh` command line.                                                                                                                                                                                                                                                                          |
| <br> `ansible_ssh_pipelining`       | <br>Determines if SSH `pipelining` is used.<br>This can override the `pipelining` setting in `ansible.cfg`. If using SSH key-based authentication, the key must be managed by an SSH agent.                                                                                                                                                     |
| <br> `ansible_ssh_private_key_file` | <br>Private key file used by SSH.<br>Useful if using multiple keys and you do not want to use an SSH agent.                                                                                                                                                                                                                                     |
| <br> `ansible_user`                 | <br>The user name to use when connecting to the host.<br>Do not change this variable unless `/bin/sh` is not installed on the target machine or cannot be run from sudo.                                                                                                                                                                        |
| <br> `inventory_hostname`           | <br>This variable takes the hostname of the machine from the inventory script or the Ansible configuration file. You cannot set the value of this variable. Because the value is taken from the configuration file, the actual runtime hostname value can vary from what is returned by this variable.                                          |
