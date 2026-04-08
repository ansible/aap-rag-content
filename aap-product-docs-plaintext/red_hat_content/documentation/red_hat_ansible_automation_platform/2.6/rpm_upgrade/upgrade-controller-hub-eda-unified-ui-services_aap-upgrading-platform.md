# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.7. Automation controller and automation hub 2.4 and Event-Driven Ansible 2.6 with unified UI upgrades
### 2.7.3. Using Migration path for 2.4 services with 2.6 services




If you installed Ansible Automation Platform 2.6 to use Event-Driven Ansible in a supported scenario, you can upgrade your Ansible Automation Platform 2.4 automation controller and automation hub to Ansible Automation Platform 2.6 by following this procedure.

**Prerequisites**

- An inventory from 2.4 for automation controller and automation hub and a 2.6 inventory for the unified UI (platform gateway) and Event-Driven Ansible. You must merge both inventories into a single 2.6 inventory file before running the upgrade. The platform gateway host must be included in the inventory for the installation program to run successfully.


Important
Ensure you have upgraded to the latest version of Ansible Automation Platform 2.4 before merging inventories and running the 2.6 upgrade.



**Procedure**

1. Merge 2.4 inventory data into the 2.6 inventory.

The example below shows the inventory file for automation controller and automation hub for 2.4 and the inventory file for Event-Driven Ansible and the unified UI (platform gateway) for 2.6, respectively, as the starting point, and what the merged inventory looks like.

**Inventory files from 2.4**


```
[automationcontroller]    controller-1    controller-2        [automationhub]    hub-1    hub-2        [all:vars]    # Here we have the admin passwd, db credentials, etc.
```

**Inventory files from 2.6**


```
[automationedacontroller]    eda-1    eda-2        [automationgateway]    gw-1    gw-2        [all:vars]    # Here we have admin passwd, db credentials etc.
```

**Merged Inventory**


```
[automationcontroller]    controller-1    controller-2        [automationhub]    hub-1    hub-2        [automationedacontroller]    eda-1    eda-2        [automationgateway]    gw-1    gw-2        [all:vars]    # Here we have admin passwd, db credentials etc from both inventories above
```


1. Run `    setup.sh`

The installation program upgrades all services to the latest version of Ansible Automation Platform 2.6 and connects them to the unified UI (platform gateway).




**Verification**

- Verify that everything has upgraded to 2.6 and is working properly in one of two ways:


- Perform an SSH to automation controller and Event-Driven Ansible.
- In the unified UI, go toHelp→Aboutto verify the RPM versions are at 2.6.



