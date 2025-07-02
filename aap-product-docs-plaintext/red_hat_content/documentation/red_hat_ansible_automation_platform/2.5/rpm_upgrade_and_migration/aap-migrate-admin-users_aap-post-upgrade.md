# 3. Ansible Automation Platform post-upgrade steps
## 3.1. Migrating admin users




Upgrades from Ansible Automation Platform 2.4 to 2.5 allows for the migration of administrators for each component with their existing component-level admin privileges maintained. However, escalation of privileges to platform gateway administrator is not automatic during the upgrade process. This ensures a secure privilege escalation process that can be customized to meet the organization’s specific needs.

**Prerequisites**

- Review current admin roles for the individual services in your current deployment.
- Confirm the users who will require platform gateway admin rights post-upgrade.


