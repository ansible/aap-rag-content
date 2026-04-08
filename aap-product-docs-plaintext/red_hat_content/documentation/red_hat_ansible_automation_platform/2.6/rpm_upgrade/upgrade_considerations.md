# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.7. Automation controller and automation hub 2.4 and Event-Driven Ansible 2.6 with unified UI upgrades
### 2.7.1. Upgrade considerations




- You must have two inventory files as a starting point: one for the 2.4 services and one for the 2.6 services.
- Before running the upgrade, you must merge the 2.4 inventory into the 2.6 inventory. The platform gateway host must be included in the inventory for the installation program to run successfully.
- Run the upgrade on the merged 2.6 inventory file only.
- You must be using an external database for both the 2.4 inventory and 2.6 inventory.
- Customers using managed database instances for either 2.4 or 2.6 inventory must migrate to an external database first, before upgrading.


