# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.7. Automation controller and automation hub 2.4 and Event-Driven Ansible 2.6 with unified UI upgrades
### 2.7.2. Using migration path for 2.4 instances with managed databases




Migrate Ansible Automation Platform 2.4 instances with managed databases to 2.6 by upgrading automation controller and automation hub before enabling unified UI and Event-Driven Ansible.

**Prerequisites**

- An inventory from 2.4 for automation controller and automation hub and a 2.6 inventory for the unified UI (platform gateway) and Event-Driven Ansible. You must merge both inventories into a single 2.6 inventory file before running the upgrade. The platform gateway host must be included in the inventory for the installation program to run successfully.


Important
Ensure you have upgraded to the latest version of Ansible Automation Platform 2.4 before merging inventories and running the 2.6 upgrade.



**Procedure**

-  **For standalone node managed database**


- Convert the database node to an external one, removing it from the inventory. The PostgreSQL node will continue working and will not lose the Ansible Automation Platform-provided setup, but you are responsible for managing its configuration afterward.

-  **For collocated managed database**


1. Back up
1. Restore with standalone managed database node instead of collocated
1. Unmanaged standalone database



