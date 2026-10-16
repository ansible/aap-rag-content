# Install containerized Ansible Automation Platform

Run the `install` playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.

## Before you begin

- You have prepared the Red Hat Enterprise Linux host
- You have created the installation user
- You have downloaded Ansible Automation Platform
- You have configured the inventory file
- You have set the host `umask` to `022` or `002` for this installation
- You are logged in to the Red Hat Enterprise Linux host as your non-root user

For guidance on the umask requirement, see [Ensure compliance with host-level security controls](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_compliance_profile_considerations#con-compliance-profile-considerations "You can use Ansible Automation Platform to manage systems where security controls have been applied to managed RHEL nodes to meet the requirements of a compliance profile such as CIS, PCI/DSS, the DISA STIG, or similar.").

## Procedure

1. Go to the installation directory on your Red Hat Enterprise Linux host.
2. Run the `install` playbook:


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
