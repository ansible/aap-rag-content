# Configure an external (customer provided) PostgreSQL database

Set up an external (customer provided) PostgreSQL database for containerized Ansible Automation Platform to use your own database infrastructure.

There are two possible scenarios for setting up an external database:

1. An external database with PostgreSQL admin credentials
2. An external database without PostgreSQL admin credentials


Important:

- When using an external database with Ansible Automation Platform, you must create and support that database. Ensure that you clear your external database when uninstalling Ansible Automation Platform.
- Red Hat Ansible Automation Platform requires customer provided (external) database to have International Components for Unicode (ICU) support.
- During configuration of an external database, you must check the external database coverage. For more information, see *Red Hat Ansible Automation Platform Database Scope of Coverage* in the related information section.
- Metrics service requires two database connections: a dedicated `metrics_service` database (read/write) and read-only access to the automation controller database using the `ms_awx_readonly` user. You must create both before installation.
- The `[database]` group in your inventory file defines the Ansible Automation Platform managed database. When using an externally managed database, do not include the `[database]` group in your inventory file.

