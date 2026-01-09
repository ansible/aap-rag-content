# Chapter 6. Red Hat Ansible Automation Platform credential




When Event-Driven Ansible controller is deployed on Ansible Automation Platform 2.6, you can create a Red Hat Ansible Automation Platform credential to connect to automation controller through the use of an automation controller URL and a username and password.

After it has been created, you can attach the Red Hat Ansible Automation Platform credential to a rulebook and use it to run rulebook activations. These credentials provide a simple way to configure communication between automation controller and Event-Driven Ansible controller, enabling your rulebook activations to launch job templates.

Note
If you deployed Event-Driven Ansible controller with Ansible Automation Platform 2.4, you probably used controller tokens to connect automation controller and Event-Driven Ansible controller. These controller tokens have been deprecated in Ansible Automation Platform 2.6. To delete deprecated controller tokens and the rulebook activations associated with them, complete the following procedures starting with [Replacing controller tokens in Ansible Automation Platform 2.6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-set-up-rhaap-credential-type#replacing-controller-tokens) before proceeding with [Setting up a Red Hat Ansible Automation Platform credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-set-up-rhaap-credential-type#eda-set-up-rhaap-credential) .



