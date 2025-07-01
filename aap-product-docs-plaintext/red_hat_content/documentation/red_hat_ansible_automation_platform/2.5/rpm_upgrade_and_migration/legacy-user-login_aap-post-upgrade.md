# 3. Ansible Automation Platform post-upgrade steps
## 3.4. Migrating LDAP users
### 3.4.2. Legacy user login and account linking




Users can log in using their legacy accounts by selecting “I have a <component> account” and entering their credentials (username and password). If the login is successful, they may be prompted to link their account with another component account for example, automation hub and automation controller. If the login credentials are the same for both automation hub and automation controller, account linking is automatically done for that user.

After successful account linking, user accounts from both components are merged into a `gateway:legacy external password` authenticator. If user accounts are not automatically merged into the `gateway:legacy external password` authenticator, you must auto migrate directly to LDAP without linking accounts.

For more information about account linking, see [Linking your accounts](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade#account-linking_aap-post-upgrade) .

