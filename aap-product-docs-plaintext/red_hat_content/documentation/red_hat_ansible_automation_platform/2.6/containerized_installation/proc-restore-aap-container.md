# 9. Maintaining containerized Ansible Automation Platform
## 9.3. Restoring containerized Ansible Automation Platform




Restore your container-based installation of Ansible Automation Platform from a backup, or to a different environment.

Note
When restoring Ansible Automation Platform, use the latest installation program available at the time of the restore. For example, if you are restoring a backup taken from version `2.6-1` , use the latest `2.6-x` installation program available at the time of the restore.

Restore functionality only works with the PostgreSQL versions supported by your current Ansible Automation Platform version. For more information, see [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/preparing-containerized-installation#system-requirements) .



**Prerequisites**

- You have logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.
- You have a backup of your Ansible Automation Platform deployment. For more information, see [Backing up container-based Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/maintaining-containerized-aap#backing-up-containerized-ansible-automation-platform) .
- If restoring to a different environment with the same hostnames, you have performed a fresh installation on the target environment with the same topology as the original (source) environment.
- You have ensured that the administrator credentials on the target environment match the administrator credentials from the source environment.


**Procedure**

1. Go to the installation directory on your Red Hat Enterprise Linux host.
1. Perform the relevant restoration steps:


- If you are restoring to the same environment with the same hostnames, run the `        restore` playbook:


```
$ ansible-playbook -i &lt;path_to_inventory&gt; ansible.containerized_installer.restore
```

This restores the important data deployed by the containerized installer such as:


- PostgreSQL databases
- Configuration files
- Data files

By default, the backup directory is set to `            ./backups` . You can change this by using the `            backup_dir` variable in your `            inventory` file.



- If you are restoring to a different environment with different hostnames, perform the following additional steps before running the `        restore` playbook:

Important
Restoring to a different environment with different hostnames is not recommended and is intended only as a workaround.




1. For each component, identify the backup file from the source environment that contains the PostgreSQL dump file.

For example:


```
$ cd ansible-automation-platform-containerized-setup-&lt;version_number&gt;/backups
```


```
$ tar tvf gateway_env1-gateway-node1.tar.gz | grep db                        -rw-r--r-- ansible/ansible 4850774 2025-06-30 11:05 aap/backups/awx.db
```


1. Copy the backup files from the source environment to the target environment.
1. Rename the backup files on the target environment to reflect the new node names.

For example:


```
$ cd ansible-automation-platform-containerized-setup-&lt;version_number&gt;/backups
```


```
$ mv gateway_env1-gateway-node1.tar.gz gateway_env2-gateway-node1.tar.gz
```


1. For enterprise topologies, ensure that the component backup file containing the `            component.db` file is listed first in its group within the inventory file.

For example:


```
$ cd ansible-automation-platform-containerized-setup-&lt;version_number&gt;
```


```
$ ls backups/gateway*                        gateway_env2-gateway-node1.tar.gz            gateway_env2-gateway-node2.tar.gz
```


```
$ tar tvf backups/gateway_env2-gateway-node1.tar.gz | grep db                        -rw-r--r-- ansible/ansible 416687 2025-06-30 11:05 aap/backups/gateway.db
```


```
$ tar tvf backups/gateway_env2-gateway-node2.tar.gz | grep db
```


```
$ vi inventory                        [automationgateway]            env2-gateway-node1            env2-gateway-node2
```






