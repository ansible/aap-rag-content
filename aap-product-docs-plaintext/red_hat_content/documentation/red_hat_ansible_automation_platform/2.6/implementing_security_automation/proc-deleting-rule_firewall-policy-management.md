# 1. Firewall policy management with Ansible security automation
## 1.2. Automate firewall rules
### 1.2.2. Deleting a firewall rule




Use the acl_manager role to delete a security rule.

**Prerequisites**

- You have installed Ansible 2.9 or later
- You have access to the firewall MGMT servers to enforce the new policies


**Procedure**

1. Install the acl_manager role using the ansible-galaxy command:

`    $ ansible-galaxy install ansible_security.acl_manager`


1. Using the CLI, create a new playbook with the acl_manger role and set the parameters, for example, source object, destination object, access rule between the two objects:


```
- name: delete block list entry      hosts: checkpoint      connection: httpapi            - include_role:            name: acl_manager            Tasks_from: unblock_ip          vars:            source_ip: 192.168.0.10            destination_ip: 192.168.0.11            ansible_network_os: checkpoint
```


1. Run the playbook `    $ ansible-navigator run --ee false &lt;playbook.yml&gt;` :

![Playbook with deleted firewall rule](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Implementing_security_automation-en-US/images/a28dc750b7226394546e12c4de260beb/security-delete-rule.png)



1. You have deleted the firewall rule. Access the MGMT server and verify that the new security policy has been removed.


**Additional resources**

[Installing roles from Galaxy](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-roles-from-galaxy)


