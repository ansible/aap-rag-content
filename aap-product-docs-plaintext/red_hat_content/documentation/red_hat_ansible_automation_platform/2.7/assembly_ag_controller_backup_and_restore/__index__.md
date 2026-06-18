# Backup and restore overview

You can backup and restore your system by using the Ansible Automation Platform setup playbook.

Note:

When backing up Ansible Automation Platform, use the installation program that matches your currently installed version of Ansible Automation Platform.

When restoring Ansible Automation Platform, use the latest installation program available at the time of the restore. For example, if you are restoring a backup taken from version `2.6-1`, use the latest `2.6-x` installation program available at the time of the restore.

Backup and restore functionality only works with the PostgreSQL versions supported by your current Ansible Automation Platform version. For more information, see **System requirements** in *Planning your installation*.

The Ansible Automation Platform setup playbook is invoked as `setup.sh` from the path where you unpacked the platform installer tar file. It uses the same inventory file used by the install playbook. The setup script takes the following arguments for backing up and restoring:

- `-b`: Perform a database backup rather than an installation.
- `-r`: Perform a database restore rather than an installation.


As the root user, call `setup.sh` with the appropriate parameters and the Ansible Automation Platform backup or restored as configured:

```
root@localhost:~# ./setup.sh -b
root@localhost:~# ./setup.sh -r
```
Backup files are created on the same path that `setup.sh` script exists. You can change it by specifying the following `EXTRA_VARS`:

```
root@localhost:~# ./setup.sh -e 'backup_dest=/path/to/backup_dir/' -b
```
A default restore path is used unless you provide `EXTRA_VARS` with a non-default path, as shown in the following example:

```
root@localhost:~# ./setup.sh -e 'restore_backup_file=/path/to/nondefault/backup.tar.gz' -r
```
Optionally, you can override the inventory file used by passing it as an argument to the setup script:

```
setup.sh -i <inventory file>
```
