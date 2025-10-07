# 8. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 8.7. Ansible Automation Platform post-upgrade steps
### 8.7.1. Key considerations for migrating admin users




Upgrades from Ansible Automation Platform 2.4 to 2.5 allows for the migration of administrators for each component with their existing component-level admin privileges maintained. However, escalation of privileges to platform gateway administrator is not automatic during the upgrade process. This ensures a secure privilege escalation process that can be customized to meet the organization’s specific needs.

**Component-level admin privileges are retained:** Administrators for automation controller and automation hub will retain their existing admin privileges for those respective services post-upgrade. For example, an admin of automation controller will continue to have full administration privileges for automation controller resources.

**Escalation to platform gateway admin must be manually configured post-upgrade:** During the upgrade process, admin privileges for individual services are not automatically translated to platform administrator privileges. Escalation to platform gateway admin must be granted by the platform administrator after upgrade and migration. Each service admin retains the original scope of their access until the access is changed.

As a platform administrator, you can escalate a user’s privileges by selecting the **Ansible Automation Platform Administrator** checkbox. Only a platform administrator can escalate privileges.

Note
Users previously designated as automation controller or automation hub administrators are labeled as **Normal** in the **User type** column of the Users list view. This is a mischaracterization. You can verify that these users have, in fact, retained their service level administrator privileges, by editing the account:



