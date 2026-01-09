# 4. Preparing the containerized Ansible Automation Platform installation
## 4.2. System requirements
### 4.2.3. Database requirements




Ansible Automation Platform can work with two varieties of database:

1. Database installed with Ansible Automation Platform - This database consists of a PostgreSQL installation done as part of an Ansible Automation Platform installation using PostgreSQL packages that Red Hat provides.
1. Customer provided or configured database - This is an external database that the customer provides, whether on bare metal, virtual machine, container, or cloud hosted service.


Ansible Automation Platform requires a customer provided (external) database to have International Components for Unicode (ICU) support.

**Additional resources**

-  [Red Hat Ansible Automation Platform Database Scope of Coverage](https://access.redhat.com/articles/4010491)
-  [Setting up a customer provided (external) database](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/advanced-configuration-containerized#setting-up-a-customer-provided-external-database)
-  [Collation Support](https://www.postgresql.org/docs/current/collation.html)


