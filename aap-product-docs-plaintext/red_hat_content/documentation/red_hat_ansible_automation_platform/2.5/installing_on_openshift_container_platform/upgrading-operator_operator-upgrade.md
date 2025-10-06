# 8. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 8.5. Upgrading the Ansible Automation Platform Operator




To upgrade to the latest version of Ansible Automation Platform Operator on OpenShift Container Platform, you can use the following procedure:

Note
If you are on version 2.4, it is recommended to skip 2.5 and upgrade straight to version 2.5.

If you upgraded from 2.4 to 2.5, you must migrate your authentication methods and users before upgrading to 2.6 as that legacy authenticator functionality was removed.



**Prerequisites**

- Read the [Release notes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/release_notes) for 2.5
- [Optional] You need to deploy all of your Red Hat Ansible Automation Platform services (automation controller, automation hub, Event-Driven Ansible) to the same, single namespace before upgrading to 2.5 (only for existing deployments). For more information see, [Migrating from one namespace to another](https://access.redhat.com/solutions/7092056) .
- Review the [Backup and recovery for operator environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/backup_and_recovery_for_operator_environments) guide and backup your services:


- AutomationControllerBackup
- AutomationHubBackup
- EDABackup



Important
Upgrading from Event-Driven Ansible 2.4 is not supported. If you are using Event-Driven Ansible 2.4 in production, contact Red Hat before you upgrade.



**Procedure**

1. Log in to OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select the Ansible Automation Platform Operator installed on your project namespace.
1. Select the **Subscriptions** tab.
1. Change the channel from stable-2.4 to stable-2.5. An InstallPlan is created for the user.
1. ClickPreview InstallPlan.
1. ClickApprove.
1. Create a Custom Resource (CR) using the Ansible Automation Platform UI. The automation controller and automation hub UIs remain until all SSO configuration is supported in the platform gateway UI.


**Additional resources**

-  [Configuring the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#configure-aap-operator_operator-platform-doc)


