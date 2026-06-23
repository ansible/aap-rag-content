# Automate network intrusion detection and prevention systems
## Automate your IDPS rules with Ansible Automation Platform

To automate your IDPS, use the `ids_rule` role to create and change Snort rules. Snort uses rule-based language that analyzes your network traffic and compares it against the given rule set.

The following lab environment demonstrates what an Ansible security automation integration would look like. A machine called “Attacker” simulates a potential attack pattern on the target machine on which the IDPS is running.

Keep in mind that a real world setup will feature other vendors and technologies.


![Sample Ansible security automation integration](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/security-ids-sample-demo.png)

