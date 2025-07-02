# 3. Ansible Automation Platform post-upgrade steps
## 3.4. Migrating LDAP users
### 3.4.1. Key considerations




**LDAP configurations are not migrated automatically during upgrade to 2.5:** While the legacy LDAP authentication settings are carried over during the upgrade process and allow seamless initial access to the platform after upgrade, LDAP configurations must be manually migrated over to a new Ansible Automation Platform 2.5 LDAP configuration. The legacy configuration acts as a reference to preserve existing authentication capabilities and facilitate the migration process. The legacy authentication configuration should not be modified directly or used after migration is complete.

**UID collision risk:** LDAP and legacy password authenticators both use usernames as the UID. This can cause UID collisions between users or users with the same name owned by different people. Any user accounts that are not secure for auto-migration due to UID conflicts must be manually migrated to ensure proper handling. You can manually migrate these users through the API `/api/gateway/v1/authenticator_users/` before setting auto-migrations.

**Do not log in using legacy LDAP authentication if you do not have a user account in the platform prior to the upgrade:** Instead, you must [auto migrate directly to LDAP without linking accounts](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#proc-migrate-LDAP-users) .

