# 6. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 6.7. Ansible Automation Platform post-upgrade steps
### 6.7.3. Key considerations for migrating normal users




**Previous service accounts are prefixed:** Users with accounts on multiple services in 2.4 are migrated as individual users in 2.5 and prefixed to identify the service from which they were migrated. For example, automation hub accounts are prefixed as `hub_&lt;username&gt;` . Automation controller user names do not include a prefix.

**Automation controller user accounts take precedence:** When an individual user had accounts on multiple services in 2.4, priority is given to their automation controller account during migration, so those are not renamed.

**Component level roles are retained until user migration is complete:** When users log in using an existing service account and do not perform the account linking process, only the roles for that specific service account are available. The migration process is completed once the user performs the account linking process. At that time, all roles for all services are migrated into the new platform gateway user account.

