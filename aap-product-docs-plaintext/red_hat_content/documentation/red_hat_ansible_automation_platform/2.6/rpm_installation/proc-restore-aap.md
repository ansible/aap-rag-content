# 3. Backup and restore Ansible Automation Platform
## 3.3. Restore Ansible Automation Platform
### 3.3.2. Restore the platform to its original state




Restore your environment by running the setup.sh script to recover platform data and configurations. Ensure the backup TAR file is available in the default location, or use the optional `restore_backup_file` flag to specify a custom path before starting.

**Procedure**

1. Navigate to your Ansible Automation Platform installation directory.
1. Run the ./setup.sh script following the example:


```
root@localhost:~# ./setup.sh -e 'restore_backup_file=/path/to/nondefault/backup.tar.gz' -r
```

Where: `    restore_backup_file` : Path to the TAR file used for the platform restore.




