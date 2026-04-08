# Chapter 3. Backup and restore Ansible Automation Platform




You can protect your Ansible Automation Platform environment by backing up the database, configuration files, and keys. Use the `./setup.sh` script or playbooks to create compressed artifacts. This ensures a recovery path for single nodes or clusters, including restores, to secondary instances.

Note
Use the installation program matching your current Ansible Automation Platform version for backups, and always use the latest available version for restores. Ensure your PostgreSQL version is supported by checking the [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/platform-system-requirements) in _Planning your installation_ .



