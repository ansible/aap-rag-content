# 5. Advanced containerized deployment
## 5.6. Configuring an external (customer provided) PostgreSQL database




Set up an external (customer provided) PostgreSQL database for containerized Ansible Automation Platform to use your own database infrastructure.

There are two possible scenarios for setting up an external database:

1. An external database with PostgreSQL admin credentials
1. An external database without PostgreSQL admin credentials


Important
- When using an external database with Ansible Automation Platform, you must create and support that database. Ensure that you clear your external database when uninstalling Ansible Automation Platform.
- Red Hat Ansible Automation Platform requires customer provided (external) database to have ICU support.
- During configuration of an external database, you must check the external database coverage. For more information, see [Red Hat Ansible Automation Platform Database Scope of Coverage](https://access.redhat.com/articles/4010491) .




