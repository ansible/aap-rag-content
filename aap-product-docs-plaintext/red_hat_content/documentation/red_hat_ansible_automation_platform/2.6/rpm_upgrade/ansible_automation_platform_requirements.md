# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.1. Upgrade prerequisites
### 2.1.1. Ansible Automation Platform requirements




- Verify that you have a valid subscription before upgrading from a previous version of Ansible Automation Platform. Existing subscriptions are carried over during the upgrade process.
- Review [Planning your upgrade](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade) to understand the upgrade requirements and scenarios, and [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models) for the RPM topologies and infrastructure.


- Inspect all existing SAML authenticators in your automation controller environment before upgrading from Ansible Automation Platform 2.4 to 2.6. Encrypted private keys for SAML configurations are not supported in Ansible Automation Platform 2.6. For more information, see the [Authentication type: SAML](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-authentication-movement-2.4-to-2.6#upgrade-saml-auth) section in the _Planning your upgrade_ guide.

- Ensure that you are on Ansible Automation Platform 2.4 or 2.5 before upgrading to 2.6. You can only upgrade from Ansible Automation Platform 2.4 or 2.5 to 2.6.
- Upgrade to the latest version of Ansible Automation Platform 2.4 or 2.5 before upgrading to Red Hat Ansible Automation Platform 2.6.

Important

- When upgrading from Ansible Automation Platform 2.4 to 2.6, the API endpoints for the automation controller, automation hub, and Event-Driven Ansible controller are all available for use. These APIs are being deprecated and will be disabled in an upcoming release. This grace period is to allow for migration to the new APIs put in place with the platform gateway.
- If you upgraded from Ansible Automation Platform 2.4 to 2.5, you must migrate your authentication methods and users before upgrading to 2.6 as that legacy authenticator functionality was removed. For information about migrating users, see [Migrating Single Sign-On (SSO) users](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade#con-migrate-SAML-users_aap-post-upgrade) in _RPM Upgrade and Migration guide_ for 2.5.



- Back up your Ansible Automation Platform environment before upgrading in case any issues occur. See [Back up the platform using automation installer](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/controller-backup-and-restore#backup-using-automation-installer) and [Backup and recovery for operator environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/backup_and_recovery_for_operator_environments) for the specific topology of the environment.
- Capture your inventory or instance group details before upgrading.
- Review the platform gateway requirements:


- Ansible Automation Platform 2.4 to 2.6 upgrades include the [platform gateway](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/ref-aap-components#con-about-platform-gateway_planning) . Ensure you review the 2.6 [Network ports and protocols](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/network-ports-protocols_planning) for architectural changes.
- Platform gateway has a number of associated inventory file variables, some of which are required. For details of the new and changed variables for 2.6, see [Appendix A. Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars) .
- When upgrading from Ansible Automation Platform 2.4 to 2.6, connections to the platform gateway URL might fail on the platform gateway UI if you are using the automation controller behind a load balancer. The following error message is displayed: `        Error connecting to Controller API`

To resolve this issue, for each automation controller host, add the platform gateway URL as a trusted source in the `        CSRF_TRUSTED_ORIGIN` setting in the **settings.py** file for each automation controller host. You must then restart each automation controller host so that the URL changes are implemented. For more information, see _Upgrading_ in [Troubleshooting Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/troubleshooting_ansible_automation_platform) .



- Review the [centralized Redis](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/ha-redis_planning#gw-centralized-redis_planning) instance offered by Ansible Automation Platform for both standalone and clustered topologies.


- Ansible Automation Platform 2.6 offers a centralized Redis instance in both [standalone](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/ha-redis_planning#gw-single-node-redis_planning) and [clustered](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/ha-redis_planning#gw-clustered-redis_planning) topologies. For information on how to configure Redis, see [Configuring Redis](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/assembly-platform-install-scenario#redis-config-enterprise-topology_platform-install-scenario) in the RPM installation guide.
- 6 VMs are required for a Redis high availability (HA) compatible deployment. Redis can be colocated on each Ansible Automation Platform component VM except for automation controller, execution nodes, or the PostgreSQL database.
- External Redis is not supported for RPM-based deployments of Ansible Automation Platform.

- Limitation:


- Upgrade of Event-Driven Ansible 2.5 to 2.6 is supported, but upgrade from Event-Driven Ansible 2.4 to 2.6 is not supported. Database migrations between Event-Driven Ansible 2.4 and Event-Driven Ansible 2.6 are not compatible. If you are upgrading from Ansible Automation Platform 2.4 to 2.6 and you deployed Event-Driven Ansible, you must first remove the Event-Driven Ansible 2.4 database and then upgrade your platform to 2.6. For information about the procedure, see [Removing Event-Driven Ansible 2.4 database](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_upgrade/index#proc-removing-eda-db_aap-upgrading-platform) .



