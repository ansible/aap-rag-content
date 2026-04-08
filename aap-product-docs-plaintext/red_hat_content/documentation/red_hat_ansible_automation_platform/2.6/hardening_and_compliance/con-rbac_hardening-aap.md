# 2. Hardening Ansible Automation Platform
## 2.4. Day two operations
### 2.4.1. RBAC considerations




As an administrator, you can use the _Role-Based Access Controls_ (RBAC) built into the platform gateway to delegate access to server inventories, organizations, and more. Administrators can also centralize the management of various credentials, enabling end users to use a needed secret without ever exposing that secret to the end user. RBAC controls allow Ansible Automation Platform to help you increase security and streamline management.

RBAC is the practice of granting roles to users or teams. RBAC is easiest to think of in terms of Roles which define precisely who or what can see, change, or delete an “object” for which a specific capability is being set.

There are a few main concepts that you should become familiar with regarding Ansible Automation Platform’s RBAC design–roles, resources, and users. Users can be members of a role, which gives them certain access to any resources associated with that role, or any resources associated with “descendant” roles.

A role is essentially a collection of capabilities. Users are granted access to these capabilities and automation controller’s resources through the roles to which they are assigned or through roles inherited through the role hierarchy.

Roles associate a group of capabilities with a group of users. All capabilities are derived from membership within a role. Users receive capabilities only through the roles to which they are assigned or through roles they inherit through the role hierarchy. All members of a role have all capabilities granted to that role. Within an organization, roles are relatively stable, while users and capabilities are both numerous and may change rapidly. Users can have many roles.

For further detail on Role Hierarchy, access inheritance, Built in Roles, permissions, personas, Role Creation, and so on see [Managing access with Role-Based access controls](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access) .

The following is an example of an organization with roles and resource permissions:


<span id="idm140601137934096"></span>
**Figure 2.2. RBAC role scopes within automation controller**

![Reference architecture for an example of an organization with roles and resource permissions.](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Hardening_and_compliance-en-US/images/7243b4cac93a882c6112555ade6a3891/aap_ref_arch_2.4.1.png)




User access is based on managing permissions to system objects (users, groups, namespaces) rather than by assigning permissions individually to specific users. You can assign permissions to the groups you create. You can then assign users to these groups. This means that each user in a group has the permissions assigned to that group.

Teams created in automation hub can range from system administrators responsible for governing internal collections, configuring user access, and repository management to groups with access to organize and upload internally developed content to automation hub.

View-only access can be enabled for further lockdown of the private automation hub. By enabling view-only access, you can grant access for users to view collections or namespaces on your private automation hub without the need for them to log in. View-only access allows you to share content with unauthorized users while restricting their ability to only view or download source code, without permissions to edit anything on your private automation hub. Enable view-only access for your private automation hub by editing the inventory file found on your Red Hat Ansible Automation Platform installer.

#### 2.4.1.1. Protecting sensitive data with no_log




If you save Ansible output to a log, you expose any secret data in your Ansible output, such as passwords and usernames. To keep sensitive values out of your logs, mark tasks that expose them with the `no_log: true` attribute.

However, the `no_log` attribute does not affect debugging output, so be careful not to debug playbooks in a production environment.

#### 2.4.1.2. Disaster recovery and continuity of operations




Taking regular backups of Ansible Automation Platform is a critical part of disaster recovery planning. Both backups and restores are performed using the installation program, so these actions should be performed from the dedicated installation host. Refer to [Back up and restore](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/controller-backup-and-restore) for further details on how to perform these operations.

An important aspect of backups is that they contain a copy of the database as well as the secret key used to decrypt credentials stored in the database, so the backup files should be stored in a secure encrypted location. Otherwise, credentials stored in the backup file may be at risk of being disclosed. Access to backups should be limited only to Ansible Automation Platform administrators who have root shell access to the infrastructure nodes and the dedicated installation host.

The two main reasons an Ansible Automation Platform administrator needs to back up their Ansible Automation Platform environment are:

- To save a copy of the data from your Ansible Automation Platform environment, so you can restore it if needed.
- To use the backup to restore the environment into a different set of servers if you’re creating a new Ansible Automation Platform cluster or preparing for an upgrade.


In all cases, the recommended and safest process is to always use the same versions of PostgreSQL and Ansible Automation Platform to back up and restore the environment.

#### 2.4.1.3. Rotate the datatbase secret key




Using some redundancy on the system is highly recommended. If the secrets system is down, the automation controller cannot fetch the information and can fail in a way that would be recoverable once the service is restored.

If you believe the SECRET_KEY automation controller generated for you has been compromised and has to be regenerated, you can run a tool from the installation program that behaves much like the automation controller backup and restore tool.

To generate a new secret key, perform the following steps:

**Procedure**

1. Backup your Ansible Automation Platform database. For more information on backing up your database, see [Back up and restore](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/controller-backup-and-restore) .
1. Using the inventory from your install (same inventory with which you run backups/restores), run `    setup.sh -k` .


**Result**

A backup copy of the previous key is saved in `/etc/tower/` .


