# 2. Ansible Automation Platform containerized installation
## 2.10. Backing up containerized Ansible Automation Platform




Perform a backup of your container-based installation of Ansible Automation Platform.

**Prerequisites**

You have done the following:


- Logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.


**Procedure**

1. Go to the Red Hat Ansible Automation Platform installation directory on your Red Hat Enterprise Linux host.
1. To control compression of the backup artifacts before they are sent to the host running the backup operation, you can use the following variables in your inventory file:


1. For control of compression for filesystem related backup files:


```
# For global control of compression for filesystem related backup files        use_archive_compression=true                # For component-level control of compression for filesystem related backup files        #controller_use_archive_compression=true        #eda_use_archive_compression=true        #gateway_use_archive_compression=true        #hub_use_archive_compression=true        #pcp_use_archive_compression=true        #postgresql_use_archive_compression=true        #receptor_use_archive_compression=true        #redis_use_archive_compression=true
```


1. For control of compression for database related backup files:


```
# For global control of compression for database related backup files        use_db_compression=true                # For component-level control of compression for database related backup files        #controller_use_db_compression=true        #eda_use_db_compression=true        #hub_use_db_compression=true        #gateway_use_db_compression=true
```



1. Run the `    backup` playbook:


```
$ ansible-playbook -i &lt;path_to_inventory&gt; ansible.containerized_installer.backup
```




This backs up the important data deployed by the containerized installer such as:

- PostgreSQL databases
- Configuration files
- Data files


By default, the backup directory is set to `./backups` . You can change this by using the `backup_dir` variable in your `inventory` file.

