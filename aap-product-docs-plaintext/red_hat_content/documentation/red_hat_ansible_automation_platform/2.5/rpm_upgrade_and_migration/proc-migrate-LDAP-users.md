# 3. Ansible Automation Platform post-upgrade steps
## 3.6. Migrating LDAP users
### 3.6.3. Migrating LDAP users without account linking




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


<span id="idm139969191273120"></span>
