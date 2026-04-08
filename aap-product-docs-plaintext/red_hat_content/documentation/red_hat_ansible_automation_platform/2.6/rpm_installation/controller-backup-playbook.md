# 3. Backup and restore Ansible Automation Platform
## 3.2. Back up the Ansible Automation Platform
### 3.2.1. Backup playbook




The Ansible Automation Platform installer ( `install.yml` ) includes the `backup.yml` playbook, which automates the backup and restoration of your environment. You can use this playbook to capture critical configuration data and databases for the following components:

- Platform gateway:


- The database
- The `        SECRET_KEY` file

- Automation controller:


- The database
- The `        SECRET_KEY` file
- The `        RESOURCE_SERVER`` key
- The per-host custom configuration files

- Automation hub:


- The database
- The database_fields.symmetric.key file
- The `        SECRET_KEY`` file
- The `        RESOURCE_SERVER` key
- Automation hub pulp content

- Event-Driven Ansible controller:


- The database
- The `        SECRET_KEY` file
- The `        RESOURCE_SERVER` key



