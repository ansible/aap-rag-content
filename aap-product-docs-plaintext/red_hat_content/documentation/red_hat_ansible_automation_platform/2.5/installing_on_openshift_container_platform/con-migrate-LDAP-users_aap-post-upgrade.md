# 8. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 8.7. Ansible Automation Platform post-upgrade steps
### 8.7.6. Migrating LDAP users




As a platform administrator upgrading from Ansible Automation Platform 2.4 to 2.5, you must migrate your LDAP user accounts if you want to continue using LDAP authentication capabilities after the upgrade. Follow the steps in this procedure to ensure the smoothest possible LDAP user migration.

There are two primary scenarios for migrating users from legacy authentication systems to LDAP-based authentication:

1. Legacy user login and account linking
1. Migration to LDAP without account linking


#### 8.7.6.1. Key considerations




**LDAP configurations are not migrated automatically during upgrade to 2.5:** While the legacy LDAP authentication settings are carried over during the upgrade process and allow seamless initial access to the platform after upgrade, LDAP configurations must be manually migrated over to a new Ansible Automation Platform 2.5 LDAP configuration. The legacy configuration acts as a reference to preserve existing authentication capabilities and facilitate the migration process. The legacy authentication configuration should not be modified directly or used after migration is complete.

**UID collision risk:** LDAP and legacy password authenticators both use usernames as the UID. This can cause UID collisions between users or users with the same name owned by different people. Any user accounts that are not secure for auto-migration due to UID conflicts must be manually migrated to ensure proper handling. You can manually migrate these users through the API `/api/gateway/v1/authenticator_users/` before setting auto-migrations.

**Do not log in using legacy LDAP authentication if you do not have a user account in the platform prior to the upgrade:** Instead, you must [auto migrate directly to LDAP without linking accounts](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#proc-migrate-LDAP-users) .

#### 8.7.6.2. Legacy user login and account linking




Users can log in using their legacy accounts by selecting “I have a <component> account” and entering their credentials (username and password). If the login is successful, they may be prompted to link their account with another component account for example, automation hub and automation controller. If the login credentials are the same for both automation hub and automation controller, account linking is automatically done for that user.

After successful account linking, user accounts from both components are merged into a `gateway:legacy external password` authenticator. If user accounts are not automatically merged into the `gateway:legacy external password` authenticator, you must auto migrate directly to LDAP without linking accounts.

For more information about account linking, see [Linking your accounts](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade#account-linking_aap-post-upgrade) .

#### 8.7.6.3. Migrating LDAP users without account linking




If a user is unable to link their accounts because there is no linking option for their automation hub account, you must immediately configure the auto-migrate feature on all legacy password authenticators to target the new gateway LDAP authenticator.

Then, when a user logs in, the platform gateway will automatically migrate the user to the LDAP authenticator if a matching UID is found.

**Prerequisites**

- Verify that all legacy accounts are properly linked and merged before proceeding with auto-migration.
- Verify that there are no UID collisions or ensure they are manually migrated before proceeding with auto-migration.


**Procedure**

1. Log in to the Ansible Automation Platform UI.
1. Set up a new LDAP authentication method in the platform gateway following the steps in [Configuring LDAP authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-configure-authentication#controller-set-up-LDAP) . This will be the configuration that you will migrate your previous LDAP users to.

Note
Ansible Automation Platform 2.4 LDAP configurations are renamed during the upgrade process and are displayed in the **Authentication Methods** list view prefixed to indicate that it is a legacy configuration, for example, `    &lt;controller/hub/eda&gt;: legacy_password` . The **Authentication type** is listed as **Legacy password** . These configurations can not be modified.




1. Select the legacy LDAP authenticator from the **Auto migrate users from** list. This is the legacy authenticator you want to use for migrating users to your platform gateway LDAP authenticator.


Once you set up the auto migrate functionality, you should be able to login with LDAP in the platform gateway and any matching accounts from the legacy 2.4 LDAP authenticator will automatically be linked.

