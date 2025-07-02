# 2. Ansible Automation Platform containerized installation
## 2.2. System requirements
### 2.2.2. Database requirements




Ansible Automation Platform 2.5 can work with two varieties of database:

1. Database installed with Ansible Automation Platform - This database consists of a PostgreSQL installation done as part of an Ansible Automation Platform installation using PostgreSQL packages provided by Red Hat.
1. Customer provided or configured database - This is an external database that is provided by the customer, whether on bare metal, virtual machine, container, or cloud hosted service.


Ansible Automation Platform 2.5 uses PostgreSQL 15 and requires the customer provided (external) database to have ICU support.

**Additional resources**

- For more information about the scope of coverage for each variety of database, see [Red Hat Ansible Automation Platform Database Scope of Coverage](https://access.redhat.com/articles/4010491) .
- For more information about setting up an external database, see [Setting up a customer provided (external) database](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/aap-containerized-installation#proc-setup-postgresql-ext-database-containerized) .


