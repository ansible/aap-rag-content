# 5. Migrating Red Hat Ansible Automation Platform to Red Hat Ansible Automation Platform Operator
## 5.2. Preparing for migration
### 5.2.1. Migrating to Ansible Automation Platform Operator




**Prerequisites**

To migrate Ansible Automation Platform deployment to Ansible Automation Platform Operator, you must have the following:


- Secret key secret
- Postgresql configuration
- Role-based Access Control for the namespaces on the new OpenShift cluster
- The new OpenShift cluster must be able to connect to the previous PostgreSQL database


Note
You can store the secret key information in the inventory file before the initial Red Hat Ansible Automation Platform installation. If you are unable to remember your secret key or have trouble locating your inventory file, contact [Ansible support](https://access.redhat.com/) through the Red Hat Customer portal.



Before migrating your data from Ansible Automation Platform 2.4, you must back up your data for loss prevention.

**Procedure**

1. Log in to your current deployment project.
1. Run `    $ ./setup.sh -b` to create a backup of your current data or deployment.


