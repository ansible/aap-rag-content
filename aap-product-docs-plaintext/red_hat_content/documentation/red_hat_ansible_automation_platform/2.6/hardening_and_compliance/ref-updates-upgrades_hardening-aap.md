# 2. Hardening Ansible Automation Platform
## 2.4. Day two operations
### 2.4.2. Updates and upgrades




All upgrades should be no more than two major versions behind what you are currently upgrading to. For example, to upgrade to automation controller 4.3, you must first be on version 4.1.x because there is no direct upgrade path from version 3.8.x or earlier. Refer to [Planning your upgrade](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade) for additional information. To run automation controller 4.3, you must also have Ansible 2.12 or later.

#### 2.4.2.1. Disaster recovery and continuity of operations




Taking regular backups of Ansible Automation Platform is a critical part of disaster recovery planning. Both backups and restores are performed using the installation program, so these actions should be performed from the dedicated installation host described earlier in this document. Refer to the [Back up and restore](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/controller-backup-and-restore) section of the Configuring automation execution documentation for further details on how to perform these operations.

An important aspect of backups is that they contain a copy of the database as well as the secret key used to decrypt credentials stored in the database, so the backup files should be stored in a secure encrypted location. This means that access to endpoint credentials are protected properly. Access to backups should be limited only to Ansible Automation Platform administrators who have root shell access to automation controller and the dedicated installation host.

The two main reasons an Ansible Automation Platform administrator needs to back up their Ansible Automation Platform environment are:

- To save a copy of the data from your Ansible Automation Platform environment, so you can restore it if needed.
- To use the backup to restore the environment into a different set of servers if you’re creating a new Ansible Automation Platform cluster or preparing for an upgrade.


In all cases, the recommended and safest process is to always use the same versions of PostgreSQL and Ansible Automation Platform to back up and restore the environment.

Using some redundancy on the system is highly recommended. If the secrets system is down, the automation controller cannot fetch the information and can fail in a way that would be recoverable once the service is restored. If you believe the SECRET_KEY automation controller generated for you has been compromised and has to be regenerated, you can run a tool from the installation program that behaves much like the automation controller backup and restore tool.

To generate a new secret key, perform the following steps:

1. Backup your Ansible Automation Platform database before you do anything else! See the [Back up and restore](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/controller-backup-and-restore) section of the Configuring automation execution guide,
1. Using the inventory from your install (same inventory with which you run backups/restores), run `    setup.sh -k` .


A backup copy of the previous key is saved in `/etc/tower/` .

