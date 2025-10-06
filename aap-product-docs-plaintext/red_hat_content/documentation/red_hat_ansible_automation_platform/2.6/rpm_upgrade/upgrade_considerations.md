# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.8. Automation controller and automation hub 2.4 and Event-Driven Ansible 2.6 with unified UI upgrades
### 2.8.1. Upgrade considerations




- You must maintain two separate inventory files: one for the 2.4 services and one for the 2.6 services.
- You must maintain two separate installations within this scenario: one for the 2.4 services and one for the 2.6 services.
- You must upgrade the two separate installations separately.
- To upgrade to a consistent component version topology, consider the following:


- You must manually combine the inventory file configuration from the 2.4 inventory into the 2.6 inventory and run the upgrade on the 2.6 inventory file ONLY.
- You must be using an external database for both the 2.4 inventory and 2.6 inventory.
- Customers using managed database instances for either 2.4 or 2.6 inventory must migrate to an external database first, before upgrading.



