# 1. Red Hat Ansible Automation Platform 2.6 upgrades
## 1.1. Ansible Automation Platform upgrades




You can upgrade your Ansible Automation Platform installation from version 2.4 or 2.5 to 2.6 using the supported upgrade paths. Review the available upgrade paths and required steps to ensure a successful upgrade of your Ansible Automation Platform environment.

Important
Upgrade from Event-Driven Ansible 2.5 to 2.6 is supported; however, upgrade from Event-Driven Ansible 2.4 to 2.6 is not supported. If you are upgrading from Ansible Automation Platform 2.4 to 2.6 and you have deployed Event-Driven Ansible, you must first remove the Event-Driven Ansible 2.4 database and then upgrade your platform to 2.6. For information about the procedure, see [Removing Event-Driven Ansible 2.4 database](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#proc-removing-eda-db_aap-upgrading-platform) .



Before beginning your upgrade be sure to review the prerequisites and upgrade planning sections of this guide.

|  **Supported upgrade path** |  **Steps to upgrade** |
| --- | --- |
| Ansible Automation Platform 2.4 to 2.6 | 1.  [Back up the platform using automation installer](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/controller-backup-and-restore#backup-using-automation-installer) .
1.  [Download the installation package](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#con-choosing-obtaining-installer_aap-upgrading-platform) .
1.  [Set up your inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#editing-inventory-file-for-updates_aap-upgrading-platform) to match your installation environment. See [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models) for a list of example inventory files.
1.  [Remove Event-Driven Ansible 2.4 database](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#proc-removing-eda-db_aap-upgrading-platform) , if you deployed Event-Driven Ansible.
1.  [Run the 2.6 installation program](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#proc-running-setup-script-for-updates) over your current Ansible Automation Platform instance. |
| Ansible Automation Platform 2.5 to 2.6 | 1.  [Back up the platform using automation installer](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/controller-backup-and-restore#backup-using-automation-installer) .
1.  [Download the installation package](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#con-choosing-obtaining-installer_aap-upgrading-platform) .
1.  [Set up your inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#editing-inventory-file-for-updates_aap-upgrading-platform) to match your installation environment. See [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models) for a list of example inventory files.
1.  [Run the 2.6 installation program](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#proc-running-setup-script-for-updates) over your current Ansible Automation Platform instance. |
|  [Automation controller and automation hub 2.4 and Event-Driven Ansible 2.6 with unified UI upgrades](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#upgrade-controller-hub-eda-unified-ui_aap-upgrading-platform) | Upgrade the 2.4 services (using inventory file to only specify automation controller and automation hub VMs) to get them to the initial version of Ansible Automation Platform 2.6.

After all the services are at the same version, run a 2.6 upgrade on all the services. |


