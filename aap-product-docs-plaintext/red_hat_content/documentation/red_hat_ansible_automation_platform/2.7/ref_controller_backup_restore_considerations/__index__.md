# Considerations for back up and restore

Consider the following points when you back up and restore your system:

Disk space
Review your disk space requirements to ensure you have enough room to backup configuration files, keys, other relevant files, and the database of the Ansible Automation Platform installation.

Important:

Database backup files can be significantly larger than the reported size because the backup process creates a logical dump that represents data differently than the live database. There is no reliable formula for predicting backup size, so ensure that you have sufficient storage available before running a backup. To reduce backup size, see the compression options described in [Back up the platform using automation installer](/documentation/en-us/red_hat_ansible_automation_platform/2.7/back_up_the_platform_using_automation_installer "Run the setup script to create a verified archive of your platform database, configurations, and secrets. This ensures your instance is captured in a compatible format for reliable restoration during a system failure or migration.").

Note:

The Ansible Automation Platform database backups are staged on each node at `/var/backups/automation-platform` through the variable `backup_dir`. You might need to mount a new volume to `/var/backups` or change the staging location with the variable `backup_dir` to prevent issues with disk space before running the `./setup.sh -b` script.

System credentials
Confirm you have the required system credentials when working with a local database or a remote database. On local systems, you might need `root` or `sudo` access, depending on how credentials are set up. On remote systems, you might need different credentials to grant you access to the remote system you are trying to backup or restore.

Version
You must always use the most recent minor version of a release to backup or restore your Ansible Automation Platform installation version. For example, if the current platform version you are on is 2.0.x, only use the latest 2.0 installer.

Backup file location
- **Default location:** If the backup file is placed in the same directory as the `./setup.sh` installer, the restore playbook locates it automatically.
- **Non-default location:** If your backup file is stored in a different directory, you must specify the path using the `restore_backup_file` extra variable when running the restore command.
