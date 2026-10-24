# Back up and restore your containerized deployment
## Restore containerized Ansible Automation Platform

Restore your container-based installation of Ansible Automation Platform from a backup, or to a different environment.

### Before you begin

- You have logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.
- You have a backup of your Ansible Automation Platform deployment. For more information, see [Back up containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-back_up_and_restore_your_containerized_deployment#backing-up-containerized-ansible-automation-platform "Perform a backup of your container-based installation of Ansible Automation Platform.").
- The target environment has a successful installation of Ansible Automation Platform with the same topology as the source environment. Note:
The restore playbook restores data to a working installation. It does not recreate platform services, secrets, or PostgreSQL connection credentials. If the target environment has not been installed or has installation errors, run the installation playbook before running the restore playbook.

- You have ensured that the administrator credentials on the target environment match the administrator credentials from the source environment.
- If restoring to a different environment with the same hostnames, you have performed a fresh installation on the target environment with the same topology as the original (source) environment.
- If your deployment uses an external PostgreSQL database, one of the following conditions is true:
* You have configured `postgresql_admin_username` and `postgresql_admin_password` in your inventory file. The restore playbook uses these credentials to grant the `CREATEDB` privilege to the application database users before the restore operation and revoke the privilege afterward.
* You have ensured that the application database users, such as `gateway_pg_username` or `controller_pg_username`, have the `CREATEDB` privilege on the external PostgreSQL instance.
Important:
If your external PostgreSQL database uses high availability or streaming replication, you must close all replica connections to the platform databases before running the restore playbook. Open replica connections prevent the restore playbook from dropping the platform databases. Consult your database provider's documentation to suspend replica synchronization and terminate active connections to the platform databases. After the restore completes, verify that replicas have resynchronized with the restored primary before restarting Ansible Automation Platform services.

### About this task

Note:

When restoring Ansible Automation Platform, use the latest installation program available at the time of the restore. Use the latest installer for the same Ansible Automation Platform version as the backup.

Restore functionality only works with the PostgreSQL versions supported by your current Ansible Automation Platform version. For more information, see [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_cont_aap_system_requirements "Use this information when planning your installation of containerized Ansible Automation Platform.").

For the lowest-risk restore outcome, upgrade the source environment to the same async release as the target before taking a backup. Restoring a backup from an earlier async release onto a later async release is possible but may encounter unexpected behavior if schema or configuration changes were introduced in the intervening releases.

### Procedure

1. Go to the installation directory on your Red Hat Enterprise Linux host.
2. Run the restore playbook for your environment:

- If you are restoring to the same environment with the same hostnames, run the `restore` playbook:

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.restore
```

The restore playbook restores the following:

* PostgreSQL databases
* Configuration files
* Data files
* Podman secrets for application credentials and encryption keys

By default, the backup directory is set to `./backups`. You can change this by using the `backup_dir` variable in your `inventory` file.

Important:
The restore playbook does not restore database connection secrets. These secrets store the connection configuration used by each component to connect to its database. Restoring them from a backup could configure services to connect to a database server from the source environment, which might not be accessible from the restored environment.

If a database connection secret is missing on an existing installation, rerun the installation playbook to recreate it:

```
$ ansible-playbook -i <path_to_inventory> ansible.containerized_installer.installcontext
```

- If you are restoring to a different environment with different hostnames, perform the following additional steps before running the `restore` playbook:
Important:
Restoring to a different environment with different hostnames is not recommended and is intended only as a workaround.
1. For each component, identify the backup file from the source environment that contains the PostgreSQL dump file. For example:

```
$ cd ansible-automation-platform-containerized-setup-<version_number>/backups
```

```
$ tar tvf gateway_env1-gateway-node1.tar.gz | grep db

-rw-r--r-- ansible/ansible 4850774 2025-06-30 11:05 aap/backups/awx.db
```

2. Copy the backup files from the source environment to the target environment.

3. Rename the backup files on the target environment to reflect the new node names. For example:

```
$ cd ansible-automation-platform-containerized-setup-<version_number>/backups
```

```
$ mv gateway_env1-gateway-node1.tar.gz gateway_env2-gateway-node1.tar.gz
```

4. For enterprise topologies, ensure that the component backup file containing the `component.db` file is listed first in its group within the inventory file. For example:

```
$ cd ansible-automation-platform-containerized-setup-<version_number>
```

```
$ ls backups/gateway*

gateway_env2-gateway-node1.tar.gz
gateway_env2-gateway-node2.tar.gz
```

```
$ tar tvf backups/gateway_env2-gateway-node1.tar.gz | grep db

-rw-r--r-- ansible/ansible 416687 2025-06-30 11:05 aap/backups/gateway.db
```

```
$ tar tvf backups/gateway_env2-gateway-node2.tar.gz | grep db
```

```
$ vi inventory

[automationgateway]
env2-gateway-node1
env2-gateway-node2
```

### What to do next

If you are using an external PostgreSQL database and manually granted the `CREATEDB` privilege to your application database users before the restore, revoke the privilege after the restore completes. Run the following command for each component, where *<username>* is the value of the corresponding `*_pg_username` variable in your inventory file:

```
ALTER USER *<username>* NOCREATEDB;
```

If you used `postgresql_admin_username` and `postgresql_admin_password` in your inventory file, the restore playbook revokes the privilege automatically and no further action is required.

