# 2. Upgrading to Red Hat Ansible Automation Platform 2.5
## 2.1. Prerequisites




- Upgrades to Ansible Automation Platform 2.5 include the [platform gateway](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ref-aap-components#con-about-platform-gateway_planning) . Ensure you review the [2.5 Network ports and protocols](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ref-network-ports-protocols_planning) for architectural changes and [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models) for information on opinionated deployment models.
- You have reviewed the [centralized Redis](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ha-redis_planning#gw-centralized-redis_planning) instance offered by Ansible Automation Platform for both standalone and clustered topologies.
- Prior to upgrading your Red Hat Ansible Automation Platform, ensure you have reviewed [Planning your installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation) for a successful upgrade. You can then download the desired version of the Ansible Automation Platform installer, configure the inventory file in the installation bundle to reflect your environment, and then run the installer.
- Prior to upgrading your Red Hat Ansible Automation Platform, ensure you have upgraded to automation controller 2.5 or later.
- When upgrading to Ansible Automation Platform 2.5, you must use RPM installer version 2.5-11 or later. If you use an older installer, the installation might fail. If you encounter a failed installation using an older version of the installer, rerun the installation with RPM installer version 2.5-11 or later.


