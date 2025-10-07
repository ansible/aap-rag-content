# 2. Automating Network Intrusion Detection and Prevention Systems (IDPS) with Ansible Automation Platform
## 2.2. Automating your IDPS rules with Ansible Automation Platform




To automate your IDPS, use the `ids_rule` role to create and change Snort rules. Snort uses rule-based language that analyzes your network traffic and compares it against the given rule set.

The following lab environment demonstrates what an Ansible security automation integration would look like. A machine called “Attacker” simulates a potential attack pattern on the target machine on which the IDPS is running.

Keep in mind that a real world setup will feature other vendors and technologies.

![Sample Ansible security automation integration](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Implementing_security_automation-en-US/images/f5cb6d84f8a90de47f4d5180fc043f67/security-ids-sample-demo.png)


