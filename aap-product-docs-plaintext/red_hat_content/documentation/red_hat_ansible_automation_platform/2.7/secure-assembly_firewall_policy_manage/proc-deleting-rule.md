# Manage firewall policies and rules with security automation
## Delete a firewall rule

Use the acl_manager role to delete a security rule.

### Before you begin

- You have installed Ansible 2.9 or later
- You have access to the firewall MGMT servers to enforce the new policies

### Procedure

1.  Install the acl_manager role using the ansible-galaxy command:
`$ ansible-galaxy install ansible_security.acl_manager`

2.  Using the CLI, create a new playbook with the acl_manger role and set the parameters, for example, source object, destination object, access rule between the two objects:


```
- name: delete block list entry
hosts: checkpoint
connection: httpapi

- include_role:
name: acl_manager
Tasks_from: unblock_ip
vars:
source_ip: 192.168.0.10
destination_ip: 192.168.0.11
ansible_network_os: checkpoint
```

3.  Run the playbook:
`$ ansible-navigator run --ee false <playbook.yml>`:


![Playbook with deleted firewall rule](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/security-delete-rule.png)

4.  You have deleted the firewall rule. Access the MGMT server and verify that the new security policy has been removed.
