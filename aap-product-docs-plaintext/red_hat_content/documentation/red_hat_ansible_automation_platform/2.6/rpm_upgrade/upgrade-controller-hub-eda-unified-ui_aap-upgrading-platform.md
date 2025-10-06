# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.8. Automation controller and automation hub 2.4 and Event-Driven Ansible 2.6 with unified UI upgrades
### 2.8.2. Using migration path for 2.4 instances with managed databases




Use this procedure if you have migration path for 2.4 instances with managed databases.

**Prerequisites**

- An inventory from 2.4 for automation controller and automation hub and a 2.6 inventory for unified UI (platform gateway) and Event-Driven Ansible. You must run upgrades on 2.4 services (using the inventory file to specify only automation controller and automation hub VMs) to get them to the initial version of Ansible Automation Platform 2.6 first. When all the services are at the same version, run an upgrade (using a complete inventory file) on all the services to go to the latest version of Ansible Automation Platform 2.6.


Important
DO NOT upgrade Event-Driven Ansible and the unified UI (platform gateway) to the latest version of Ansible Automation Platform 2.6 without first upgrading the individual services (automation controller and automation hub) to the initial version of Ansible Automation Platform 2.6.



- Ensure you have upgraded to the latest version of Ansible Automation Platform 2.4 before upgrading your Red Hat Ansible Automation Platform.


**Procedure**

-  **For standalone node managed database**


- Convert the database node to an external one, removing it from the inventory. The PostgreSQL node will continue working and will not lose the Ansible Automation Platform-provided setup, but you are responsible for managing its configuration afterward.

-  **For collocated managed database**


1. Back up
1. Restore with standalone managed database node instead of collocated
1. Unmanaged standalone database



