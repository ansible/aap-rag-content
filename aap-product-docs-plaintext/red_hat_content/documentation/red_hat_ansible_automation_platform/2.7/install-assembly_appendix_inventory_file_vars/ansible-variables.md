# Inventory file variables
## Ansible variables

The following variables control how Ansible Automation Platform interacts with remote hosts.

*Table 1. Ansible variables*

| Variable                       | Description                                                                                                                                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ansible_connection`           | The connection plugin used for the task on the target host. This can be the name of any Ansible connection plugin.<br>SSH protocol types are `smart`, `ssh`, or `paramiko`. You can also use `local` to run tasks on the control node itself.<br>Default = `smart` |
| `ansible_host`                 | The IP address or name of the target host to use instead of `inventory_hostname`.                                                                                                                        |
| `ansible_password`             | The password to authenticate to the host.<br>Do not store this variable in plain text. Always use a vault.                                                                                               |
| `ansible_port`                 | The connection port number.<br>The default for SSH is `22`.                                                                                                                                              |
| `ansible_scp_extra_args`       | This setting is always appended to the default `scp` command line.                                                                                                                                       |
| `ansible_sftp_extra_args`      | This setting is always appended to the default `sftp` command line.                                                                                                                                      |
| `ansible_shell_executable`     | This sets the shell that the Ansible controller uses on the target machine and overrides the executable in `ansible.cfg` which defaults to `/bin/sh`.                                                    |
| `ansible_shell_type`           | The shell type of the target system.<br>Do not use this setting unless you have set the `ansible_shell_executable` to a non-Bourne (sh) compatible shell. By default commands are formatted using sh-style syntax. Setting this to `csh` or `fish` causes commands executed on target systems to follow the syntax of those shells instead. |
| `ansible_ssh_common_args`      | This setting is always appended to the default command line for `sftp`, `scp`, and `ssh`. Useful to configure a `ProxyCommand` for a certain host or group.                                              |
| `ansible_ssh_executable`       | This setting overrides the default behavior to use the system `ssh`. This can override the `ssh_executable` setting in `ansible.cfg`.                                                                    |
| `ansible_ssh_extra_args`       | This setting is always appended to the default `ssh` command line.                                                                                                                                       |
| `ansible_ssh_pipelining`       | Determines if SSH `pipelining` is used.<br>This can override the `pipelining` setting in `ansible.cfg`. If using SSH key-based authentication, the key must be managed by an SSH agent.                  |
| `ansible_ssh_private_key_file` | Private key file used by SSH.<br>Useful if using multiple keys and you do not want to use an SSH agent.                                                                                                  |
| `ansible_user`                 | The user name to use when connecting to the host.<br>Do not change this variable unless `/bin/sh` is not installed on the target machine or cannot be run from sudo.                                     |
| `inventory_hostname`           | This variable takes the hostname of the machine from the inventory script or the Ansible configuration file. You cannot set the value of this variable. Because the value is taken from the configuration file, the actual runtime hostname value can vary from what is returned by this variable. |

