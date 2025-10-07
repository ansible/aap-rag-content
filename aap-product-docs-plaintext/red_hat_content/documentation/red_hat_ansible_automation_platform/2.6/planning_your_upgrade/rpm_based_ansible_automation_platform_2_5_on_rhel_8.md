# 3. Support matrix for upgrade scenarios
## 3.2. RPM-based upgrade scenarios
### 3.2.3. RPM-based Ansible Automation Platform 2.5 on RHEL 8




| Source | Target | Process |
| --- | --- | --- |
| RPM-based Ansible Automation Platform 2.5 on RHEL 8 | RPM-based Ansible Automation Platform 2.6 on RHEL 9 | 1.  [Backup your deployment of 2.5 RPM](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-scenario#con-backup-aap_platform-install-scenario) on RHEL 8, then restore to a RHEL 9 environment running a fresh installation of RPM 2.5.
1.  [Upgrade your RPM deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_upgrade) from 2.5 to 2.6. |
| RPM-based Ansible Automation Platform 2.5 on RHEL 8 | Container-based Ansible Automation Platform 2.6 on RHEL 9 | 1.  [Backup your deployment of 2.5 RPM](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-scenario#con-backup-aap_platform-install-scenario) on RHEL 8, then restore to a RHEL 9 environment running a fresh installation of RPM 2.5.
1.  [Upgrade your RPM deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_upgrade) from 2.5 to 2.6.
1.  [Migrate your RPM deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/ansible_automation_platform_migration) 2.6 to a container deployment 2.6. |
| RPM-based Ansible Automation Platform 2.5 on RHEL 8 | Container-based Ansible Automation Platform 2.6 on RHEL 10 | 1.  [Backup your deployment of 2.5 RPM](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-scenario#con-backup-aap_platform-install-scenario) on RHEL 8, then restore to a RHEL 9 environment running a fresh installation of RPM 2.5.
1.  [Upgrade your RPM deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_upgrade) from 2.5 to 2.6.
1.  [Migrate your RPM deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/ansible_automation_platform_migration) 2.6 to a container deployment 2.6.
1.  [Backup your deployment of container 2.6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/aap-containerized-installation#backing-up-containerized-ansible-automation-platform) on RHEL 9, then restore to a RHEL 10 environment running a fresh container installation 2.6. |
| RPM-based Ansible Automation Platform 2.5 on RHEL 8 | Ansible Automation Platform on OpenShift Container Platform 2.6 | 1.  [Backup your deployment of 2.5 RPM](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-scenario#con-backup-aap_platform-install-scenario) on RHEL 8, then restore to a RHEL 9 environment running a fresh installation of RPM 2.5.
1.  [Upgrade your RPM deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_upgrade) from 2.5 to 2.6.
1.  [Migrate your RPM deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/ansible_automation_platform_migration) 2.6 to Ansible Automation Platform on OpenShift Container Platform 2.6. |


