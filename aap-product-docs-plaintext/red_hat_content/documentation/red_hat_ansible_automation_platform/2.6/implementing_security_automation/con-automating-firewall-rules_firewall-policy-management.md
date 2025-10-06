# 1. Firewall policy management with Ansible security automation
## 1.2. Automate firewall rules




Ansible security automation enables you to automate various firewall policies that require a series of actions across various products. You can use an Ansible role, such as the [acl_manager](https://github.com/ansible-security/acl_manager) role to manage your _Access Control Lists_ (ACLs) for many firewall devices such as blocking or unblocking an IP or URL. Roles let you automatically load related vars, files, tasks, handlers, and other Ansible artifacts based on a known file structure. After you group your content in roles, you can easily reuse them and share them with other users.

The following lab environment is a simplified example of a real-world enterprise security architecture, which can be more complex and include additional vendor-specific tools. This is a typical incident response scenario where you receive an intrusion alert and immediately execute a playbook with the acl_manger role that blocks the attacker’s IP address.

Your entire team can use Ansible security automation to address investigations, threat hunting, and incident response all on one platform. [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible) provides you with certified content collections that are easy to consume and reuse within your security team.

![Simplified security lab environment](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Implementing_security_automation-en-US/images/a72895b73b84aa49356c8aae2334eacb/security-lab-environment.png)


**Additional resources**

[roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#roles)


