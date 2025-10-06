# 2. New features and enhancements
## 2.7. Installation updates
### 2.7.3. RPM installation




Updated system requirements for RPM installation of Ansible Automation Platform 2.6 include:

- Ansible Automation Platform RPM installer was deprecated in 2.5 and will be removed in Ansible Automation Platform 2.7. The RPM installer will be supported for RHEL 9 during the lifecycle of Ansible Automation Platform 2.6 to support migrations to existing supported topologies. See the [support matrix](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-support-matrix) for more information on upgrade and migration paths.
- Red Hat Enterprise Linux 9.2 operating system requirement was updated to 9.4 or later minor versions of Red Hat Enterprise Linux 9. Red Hat Enterprise Linux 8 is no longer supported.
- Red Hat Enterprise Linux 10 is not supported for RPM installations. See [support matrix](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-support-matrix) for more information on supported upgrade and migration paths.
- PostgreSQL 16 and 17 are now supported for customer-provided (external) databases.

Note
External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15.






For more information, see [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/platform-system-requirements) in _RPM installation_ .

