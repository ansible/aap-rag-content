# 2. Hardening Ansible Automation Platform
## 2.3. Initial configuration




Granting access to certain parts of Ansible Automation Platform increases security risk.

Apply the following practices to help secure access:

- Minimize access to system administrative accounts. There is a difference between the user interface (web interface) and access to the infrastructure nodes that Ansible Automation Platform is running on. A system administrator or super user can access, edit, and disrupt any system application. Anyone with root access to Ansible Automation Platform infrastructure nodes has the potential ability to decrypt stored credentials, so minimizing access to system administrative accounts is crucial for maintaining a secure system.
- Minimize local system access. Ansible Automation Platform infrastructure nodes should not require local user access except for administrative purposes. Non-administrator users should not have access to the Ansible Automation Platform infrastructure nodes.
- Enforce separation of duties. Different components of automation might need to access a system at different levels. Use different keys or credentials for each component so that the effect of any one key or credential vulnerability is minimized.
- In the Ansible Automation Platform UI, any account with “system administrator” privileges can edit, change, and update any inventory or automation resource. Restrict these account privileges to the minimum set of users necessary for Ansible Automation Platform administration and maintenance.


