# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.1. Upgrade prerequisites
### 2.1.4. User privileges




- Ensure a dedicated non-root user is configured on the Red Hat Enterprise Linux host.


- This user requires sudo or other Ansible supported privilege escalation (sudo is recommended) to perform administrative tasks during the installation.
- This user is responsible for the installation of RPM Ansible Automation Platform.
- You can obtain root access either through the sudo command, or through privilege escalation. You can de-escalate privileges from root to users such as AWX, PostgreSQL, Event-Driven Ansible, or Pulp.
- An NTP client is configured on each node.



**Additional resources**

-  [Attaching your Red Hat Ansible Automation Platform subscription](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/assembly-platform-install-overview#proc-attaching-subscriptions)
-  [Backup and restore Red Hat Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_upgrade/controller-backup-and-restore)
-  [Clustering](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/controller-clustering)
-  [Planning your upgrade](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/index)
-  [Planning your installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/index)


