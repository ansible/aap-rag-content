# 1. Red Hat Ansible Automation Platform 2.5 upgrades
## 1.1. Ansible Automation Platform upgrades




Currently, it is possible to perform Ansible Automation Platform upgrades using one of the following supported upgrade paths.

Important
Upgrading from Event-Driven Ansible 2.4 is not supported. If you are upgrading from Ansible Automation Platform 2.4 to 2.5 and you have deployed Event-Driven Ansible, you must first remove the Event-Driven Ansible 2.4 database and then upgrade your platform to 2.5. For information about the procedure, see [Removing Event-Driven Ansible 2.4 database](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-removing-eda-db_aap-upgrading-platform) .



Before beginning your upgrade be sure to review the prerequisites and upgrade planning sections of this guide.

|  **Supported upgrade path** |  **Steps to upgrade** |
| --- | --- |
| Ansible Automation Platform 2.4 to 2.5 |  [Download the installation package](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-choosing-obtaining-installer_aap-upgrading-platform) .

[Set up your inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#editing-inventory-file-for-updates_aap-upgrading-platform) to match your installation environment. See [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models) for a list of example inventory files.

[Back up your Ansible Automation Platform instance](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-backup-aap_aap-upgrading-platform) .

[Remove Event-Driven Ansible 2.4 database](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-removing-eda-db_aap-upgrading-platform) , if you deployed Event-Driven Ansible.

[Run the 2.5 installation program](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-running-setup-script-for-updates) over your current Ansible Automation Platform instance.

[Link your existing service level accounts](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#account-linking_aap-post-upgrade) to a single unified platform account. |
| Ansible Automation Platform 2.5 to 2.5.x |  [Download the installation package](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-choosing-obtaining-installer_aap-upgrading-platform) .

[Set up your inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#editing-inventory-file-for-updates_aap-upgrading-platform) to match your installation environment. See [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models) for a list of example inventory files.

[Back up your Ansible Automation Platform instance](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-backup-aap_aap-upgrading-platform) .

[Run the 2.5 installation program](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-running-setup-script-for-updates) over your current Ansible Automation Platform instance. |
|  [Automation controller and automation hub 2.4 and Event-Driven Ansible 2.5 with unified UI upgrades](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#upgrade-controller-hub-eda-unified-ui_aap-upgrading-platform) | Upgrade the 2.4 services (using inventory file to only specify automation controller and automation hub VMs) to get them to the initial version of AAP 2.5.

After all the services are at the same version, run a 2.5 upgrade on all the services |


