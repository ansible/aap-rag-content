# 2. Upgrading to Red Hat Ansible Automation Platform 2.5
## 2.6. Removing Event-Driven Ansible 2.4 database




Ansible Automation Platform 2.5 supports upgrades from Ansible Automation Platform 2.4 environments for all components, except for Event-Driven Ansible. Database migrations between Event-Driven Ansible 2.4 and Event-Driven Ansible 2.5 are not compatible.

If you are upgrading from Ansible Automation Platform 2.4 to 2.5, you must first remove the Event-Driven Ansible 2.4 database. A new Event-Driven Ansible 2.5 database gets created automatically after the upgrade. You can then reconnect Automation Decisions (Event-Driven Ansible controller) to Automation Execution (automation controller) to run rulebook activations.

**Procedure**

1. Shut down the old Event-Driven Ansible 2.4 host.
1. Log in to your database host with a user that has superuser privileges.

`    # psql -h &lt;hostname&gt; -U &lt;username&gt;`


1. When prompted, enter your password.
1. Delete the existing Event-Driven Ansible 2.4 database by using the following command:

`    DROP DATABASE automationedacontroller`


1. When prompted, reenter your password.


**Next steps**

1.  [Run the Ansible Automation Platform installer setup script](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-running-setup-script-for-updates) .
1. After the upgrade is completed, reconnect Automation Decisions (Event-Driven Ansible controller) to Automation Execution (automation controller) to run rulebook activations successfully.


