# Chapter 2. Upgrading to Red Hat Ansible Automation Platform 2.6




To upgrade your Red Hat Ansible Automation Platform, start by reviewing [Planning your upgrade](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade) to ensure a successful upgrade. You can then download the desired version of the Ansible Automation Platform installer, configure the inventory file in the installation bundle to reflect your environment, and then run the installer.

Important
In Ansible Automation Platform 2.6, while the automation controller’s API remains for backward compatibility, new installations must use the platform gateway API for managing organizations, teams, and users. Using the legacy API will introduce a delay of up to 15 minutes before changes are synchronized to all components, including Event-Driven Ansible controller.



