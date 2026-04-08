# 3. Backup and restore Ansible Automation Platform
## 3.3. Restore Ansible Automation Platform
### 3.3.1. Restore playbook




Automation controller includes playbooks to backup and restore your installation.

In addition to the `install.yml` file included with your `setup.sh` setup playbook, there are also `restore.yml` files.

The restore backup restores the backed up files and data to a freshly installed and working second instance of automation controller.

When restoring your system, installation program checks to see that the backup file exists before beginning the restoration. If the backup file is not available, your restoration fails.

Note
Make sure that your automation controller hosts are properly set up with SSH keys, user or pass variables in the hosts file, and that the user has `sudo` access.



