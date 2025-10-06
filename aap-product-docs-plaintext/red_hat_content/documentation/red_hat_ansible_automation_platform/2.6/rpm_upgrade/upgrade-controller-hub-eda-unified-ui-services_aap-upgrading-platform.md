# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.8. Automation controller and automation hub 2.4 and Event-Driven Ansible 2.6 with unified UI upgrades
### 2.8.3. Using Migration path for 2.4 services with 2.6 services




If you installed Ansible Automation Platform 2.6 to use Event-Driven Ansible in a supported scenario, you can upgrade your Ansible Automation Platform 2.4 automation controller and automation hub to Ansible Automation Platform 2.6 by following the procedure in this section.

**Prerequisites**

- An inventory from 2.4 for automation controller and automation hub and a 2.6 inventory for unified UI (platform gateway) and Event-Driven Ansible. You must run upgrades on 2.4 services (using the inventory file to specify only automation controller and automation hub VMs) to get them to the initial version of Ansible Automation Platform 2.6 first. When all the services are at the same version, run an upgrade (using a complete inventory file) on all the services to go to the latest version of Ansible Automation Platform 2.6.


Important
DO NOT upgrade Event-Driven Ansible and the unified UI (platform gateway) to the latest version of Ansible Automation Platform 2.6 without first upgrading the individual services (automation controller and automation hub) to the initial version of Ansible Automation Platform 2.6.



- Ensure you have upgraded to the latest version of Ansible Automation Platform 2.4 before upgrading your Red Hat Ansible Automation Platform.


**Procedure**

1. Merge 2.4 inventory data into the 2.6 inventory.

The example below shows the inventory file for automation controller and automation hub for 2.4 and the inventory file for Event-Driven Ansible and the unified UI (platform gateway) for 2.6, respectively, as the starting point, and what the merged inventory looks like.

**Inventory files from 2.4**


```
[automationcontroller]    controller-1    controller-2        [automationhub]    hub-1    hub-2        [all:vars]    # Here we have the admin passwd, db credentials, etc.
```

**Inventory files from 2.6**


```
[edacontroller]    eda-1    eda-2        [gateway]    gw-1    gw-2        [all:vars]    # Here we have admin passwd, db credentials etc.
```

**Merged Inventory**


```
[automationcontroller]    controller-1    controller-2        [automationhub]    hub-1    hub-2        [edacontroller]    eda-1    eda-2        [gateway]    gw-1    gw-2        [all:vars]    # Here we have admin passwd, db credentials etc from both inventories above
```


1. Run `    setup.sh`

The installer upgrades automation controller and automation hub from 2.4 to Ansible Automation Platform 2.6, latest Event-Driven Ansible, and the unified UI (platform gateway) from the fresh install of 2.6 to the latest version of 2.6, and connects automation controller and automation hub properly with the unified UI (platform gateway) node to initialize the unified experience.




**Verification**

- Verify that everything has upgraded to 2.6 and is working properly in one of two ways:


- Perform an SSH to automation controller and Event-Driven Ansible.
- In the unified UI, navigate toHelp→Aboutto verify the RPM versions are at 2.6.




<span id="idm140548203611184"></span>
