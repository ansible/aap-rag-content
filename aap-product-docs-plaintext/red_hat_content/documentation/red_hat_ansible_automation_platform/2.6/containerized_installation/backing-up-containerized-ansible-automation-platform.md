# 2. Ansible Automation Platform containerized installation
## 2.10. Backing up containerized Ansible Automation Platform




Perform a backup of your container-based installation of Ansible Automation Platform.

Note
When backing up Ansible Automation Platform, use the installation program that matches your currently installed version of Ansible Automation Platform.

Backup functionality only works with the PostgreSQL versions supported by your current Ansible Automation Platform version. For more information, see [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/aap-containerized-installation#system-requirements) .



**Prerequisites**

- You have logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.


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

1. By default, the backup directory is set to `    ./backups` . You can change this by using the `    backup_dir` variable in your `    inventory` file.


**Next steps**

To customize the backup, use the following variables in your `inventory` file.


- Change the backup destination directory from the default `    ./backups` by using the `    backup_dir` variable.
- Exclude paths that contain duplicated data, such as snapshot subdirectories, by using the `    hub_data_path_exclude` variable. For instance, to exclude a .snapshots subdirectory, specify hub_data_path_exclude=[' **/.snapshots/** '] in your inventory file.


- Alternatively, you can use the command-line interface with the `        -e` flag to pass this variable at runtime:


```
$ ansible-playbook -i inventory ansible.containerized_installer.backup -e hub_data_path_exclude="['*/.snapshots/*']"
```





