# Upgrade the Ansible Automation Platform Operator

To upgrade to the latest version of Ansible Automation Platform Operator on OpenShift Container Platform, you can use the following procedure:

## Before you begin

- Read the [Release notes](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-platform_intro "Ansible Automation Platform unifies comprehensive automation capabilities, a robust ecosystem, and flexible deployment options into one strategic solution. It enables customers to automate and orchestrate workflows across domains for efficient, resilient, and consistent IT operations at scale.") for your target version.


1. For existing deployments only: You must deploy your automation controller and automation hub instances to the same, single namespace before upgrading. For more information see, [Migrating from one namespace to another](https://access.redhat.com/solutions/7092056).
2. Review the [Backup and restore in an OpenShift environment](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_aap_backup_recovery "To safeguard against unexpected data loss and application errors, it is critical that you perform periodic backups of your Red Hat Ansible Automation Platform deployment. In addition to data loss prevention, backups allow you to fall back to a different deployment state.") section and backup your services:
- AutomationControllerBackup
- AutomationHubBackup
- EDABackup


Important:

Upgrading from Event-Driven Ansible 2.4 is not supported. If you are using Event-Driven Ansible 2.4 in production, contact Red Hat before you upgrade.

## Procedure

1.  Log in to OpenShift Container Platform.
2.  Navigate to Operators> (and then)Installed Operators.
3.  Select the Ansible Automation Platform Operator installed on your project namespace.
4.  Select the **Subscriptions** tab.
5.  To upgrade to 2.6 change the channel to `stable-2.6`.
6.  This creates an InstallPlan for the user. Click Preview InstallPlan.
7.  Click Approve.
8.  Create a Custom Resource (CR) using the Ansible Automation Platform UI.

Note:
The automation controller and automation hub UIs remain until all SSO configuration is supported in the platform gateway UI.

## Results

You can confirm you have upgraded successfully by navigating to Operators> (and then)Installed Operators, here under Ansible Automation Platform you can verify the version number matches your target version.

Additionally, go to your Ansible Automation Platform Operator deployment and click All instances to verify if all instances upgraded correctly. All pods should display either a **Running** or **Completed status**, with no pods displaying an error status.
