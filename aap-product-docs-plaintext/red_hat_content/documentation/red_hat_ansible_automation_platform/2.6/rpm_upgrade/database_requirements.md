# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.1. Upgrade prerequisites
### 2.1.3. Database requirements




- Ansible Automation Platform can work with two varieties of database:


- Database installed with Ansible Automation Platform - This database consists of a PostgreSQL installation done as part of an Ansible Automation Platform installation using PostgreSQL packages provided by Red Hat.
- Customer provided or configured database - This is an external database that is provided by the customer, whether on bare metal, virtual machine, container, or cloud hosted service. Ansible Automation Platform requires customer provided (external) database to have ICU support.

- PostgreSQL user passwords are hashed with SCRAM-SHA-256 secure hashing algorithm before storing in the database.
- Ensure that you back up your Ansible Automation Platform environment before upgrading in case any issues occur. See [Backup and restore](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/controller-backup-and-restore) and [Backup and recovery for operator environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/backup_and_recovery_for_operator_environments) for the specific topology of the environment.


