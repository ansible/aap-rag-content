# 2. Upgrading to Red Hat Ansible Automation Platform 2.5
## 2.2. Ansible Automation Platform upgrade planning




Before you begin the upgrade process, review the following considerations to plan and prepare your Ansible Automation Platform deployment:

- See [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/platform-system-requirements) in the Planning your installation guide to ensure you have the topologies that fit your use case.

Note
2.4 to 2.5 upgrades now include [Platform gateway](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ref-aap-components#con-about-platform-gateway_planning) . Ensure you review the 2.5 [Network ports and protocols](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ref-network-ports-protocols_planning) for architectural changes.



Important
When upgrading from Ansible Automation Platform 2.4 to 2.5, the API endpoints for the automation controller, automation hub, and Event-Driven Ansible controller are all available for use. These APIs are being deprecated and will be disabled in an upcoming release. This grace period is to allow for migration to the new APIs put in place with the platform gateway.




- Verify that you have a valid subscription before upgrading from a previous version of Ansible Automation Platform. Existing subscriptions are carried over during the upgrade process.
- Ensure you have a backup of an Ansible Automation Platform 2.4 environment before upgrading in case any issues occur. See [Backup and restore](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-backup-and-restore) and [Backup and recovery for operator environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/backup_and_recovery_for_operator_environments) for the specific topology of the environment.
- Ensure you capture your inventory or instance group details before upgrading.
- Ensure you have upgraded to the latest version of Ansible Automation Platform 2.4 before upgrading your Red Hat Ansible Automation Platform.
- Upgrade from Event-Driven Ansible 2.4 to 2.5 is not supported. Database migrations between Event-Driven Ansible 2.4 and Event-Driven Ansible 2.5 are not compatible. If you are upgrading from Ansible Automation Platform 2.4 to 2.5 and you have deployed Event-Driven Ansible, you must first remove the Event-Driven Ansible 2.4 database and then upgrade your platform to 2.5. For information about the procedure, see [Removing Event-Driven Ansible 2.4 database](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#proc-removing-eda-db_aap-upgrading-platform) .
- If you are currently running Event-Driven Ansible controller 2.5, it is recommended that you disable all Event-Driven Ansible activations before upgrading to ensure that only new activations run after the upgrade process is complete. For more information, see [automation controller and automation hub 2.4 and Event-Driven Ansible 2.5 with unified UI upgrades](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#upgrade-controller-hub-eda-unified-ui_aap-upgrading-platform) .
- Automation controller OAuth applications on the platform UI are not supported for 2.4 to 2.5 migration. See this [Knowledgebase article](https://access.redhat.com/solutions/7091987) for more information. To learn how to recreate your OAuth applications, see [Applications](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication#assembly-controller-applications) in the Access management and authentication guide.
- During the upgrade process, user accounts from the individual services are migrated. If there are accounts from multiple services, they must be linked to access the unified platform. See [Account linking](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_upgrade_and_migration/index#account-linking_aap-post-upgrade) for details.
- Ansible Automation Platform 2.5 offers a centralized Redis instance in both [standalone](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ha-redis_planning#gw-single-node-redis_planning) and [clustered](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ha-redis_planning#gw-clustered-redis_planning) topologies. For information on how to configure Redis, see [Configuring Redis](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-scenario#redis-config-enterprise-topology_platform-install-scenario) in the RPM installation guide.
- When upgrading from Ansible Automation Platform 2.4 to 2.5, connections to the platform gateway URL might fail on the platform gateway UI if you are using the automation controller behind a load balancer. The following error message is displayed: `    Error connecting to Controller API`

To resolve this issue, for each controller host, add the platform gateway URL as a trusted source in the `    CSRF_TRUSTED_ORIGIN` setting in the **settings.py** file for each controller host. You must then restart each controller host so that the URL changes are implemented. For more information, see _Upgrading_ in [Troubleshooting Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/troubleshooting_ansible_automation_platform) .




**Additional resources**

-  [Attaching a subscription](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/assembly-gateway-licensing#proc-attaching-subscriptions)
-  [Backup and recovery](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/backup_and_recovery_for_operator_environments/index)
-  [Clustering](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-clustering)
-  [Planning your installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/index)


