# 1. Firewall policy management with Ansible security automation
## 1.2. Automate firewall rules
### 1.2.1. Creating a new firewall rule




Use the acl_manager role to create a new firewall rule for blocking a source IP address from accessing a destination IP address.

**Prerequisites**

- You have installed the latest version of ansible-core.
- You have access to the Check Point Management server to enforce the new policies


**Procedure**

1. Install the acl_manager role using the ansible-galaxy command.

`    $ ansible-galaxy install ansible_security.acl_manager`


1. Create a new playbook and set the following parameter. For example, source object, destination object, access rule between the two objects and the actual firewall you are managing, such as Check Point:


```
- name: block IP address      hosts: checkpoint      connection: httpapi          tasks:        - include_role:            name: acl_manager            tasks_from: block_ip          vars:            source_ip: 172.17.13.98            destination_ip: 192.168.0.10            ansible_network_os: checkpoint
```


1. Run the playbook `    $ ansible-navigator run --ee false &lt;playbook.yml&gt;` .

![Playbook with new firewall rule](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Implementing_security_automation-en-US/images/6a7ae50190e836aa7996993f39f2b25c/security-create-rule.png)





**Verification**

You have created a new firewall rule that blocks a source IP address from accessing a destination IP address. Access the MGMT server and verify that the new security policy has been created.


