# Best practices for securing user accounts
## Infrastructure server account planning

For user accounts on the RHEL servers that run Ansible Automation Platform services, follow your organizational policies to determine if individual user accounts should be local or should use an external authentication source.

Only users who have a valid need to perform maintenance tasks on the Ansible Automation Platform components themselves should have access to the underlying RHEL servers, as the servers store configuration files that contain sensitive information, such as encryption keys and service passwords. Because these individuals must have privileged access to support Ansible Automation Platform services, minimizing access to the underlying RHEL servers is critical. Do not grant sudo access to the root account or local Ansible Automation Platform service accounts (awx, pulp, postgres) to untrusted users.

Note:

Some local service accounts are created and managed by the RPM-based installation program. These particular accounts on the underlying RHEL hosts cannot come from an external authentication source.

