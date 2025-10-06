# 4. Infrastructure changes by deployment type
## 4.1. RPM-based deployments
### 4.1.2. Upgrading a 2.4 single node automation controller and automation hub deployment to a 2.6 growth topology




You can upgrade your 2.4 single node automation controller and automation hub deployment to a 2.6 growth topology. This section outlines the infrastructure changes, requirements, and an example inventory for upgrading.

#### 4.1.2.1. 2.4 infrastructure topology diagram




This diagram outlines the 2.4 infrastructure topology for this deployment model.


<span id="idm140440485343008"></span>
**Figure 4.3. 2.4 infrastructure topology diagram**

![2.4 single controller and hub topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/f6dd26e553109a3bae6119cd1a996f06/rpm-a-controller-hub-2-4.png)




#### 4.1.2.2. 2.6 infrastructure topology diagram




This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.


<span id="idm140440485190816"></span>
**Figure 4.4. 2.6 infrastructure topology diagram**

![2.6 single controller and hub growth topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/349e4be26d5082fc249d738fe99596bf/rpm-a-controller-hub-2.6.png)




#### 4.1.2.3. Requirements for upgrading a single automation controller node and automation hub deployment




The following table highlights the requirements for upgrading from Ansible Automation Platform version 2.4 to 2.6.

| Existing 2.4 topology | Tested 2.6 topology | Requirements for each VM |
| --- | --- | --- |
| Non-redundant deployment with automation controller and automation hub:

- One automation controller VM
- One automation hub VM
- One Ansible Automation Platform managed PostgreSQL 15 database | Growth topology:

- One platform gateway with colocated Redis VM
- One automation controller VM
- One private automation hub VM
- One Event-Driven Ansible controller VM
- One automation mesh execution node
- One Ansible Automation Platform managed PostgreSQL 15 database | See the [RPM growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/rpm-topologies#rpm-a-env-a) section of the _Tested deployment models_ guide. |


#### 4.1.2.4. Example inventory file




The following inventory file has been updated with the necessary changes to upgrade to the 2.6 growth topology.

```
# This is the RPM-based Ansible Automation Platform installer inventory file intended for upgrading from a 2.4 single automation controller and automation hub deployment to a 2.6 growth deployment.

# Consult the Ansible Automation Platform product documentation about this topology's tested hardware configuration.
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/rpm-topologies
# For all optional variables consult the Ansible Automation Platform documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation

# This section is for your platform gateway hosts - NEW for 2.6 growth topology
# -----------------------------------------------------
[automationgateway]
gateway.example.org

# This section is for your automation controller hosts from your 2.4 inventory
# -----------------------------------------------------
[automationcontroller]
controller.example.org

[automationcontroller:vars]
peers=execution_nodes

# This section is for your execution hosts - NEW for 2.6 growth topology
# -----------------------------------------------------
[execution_nodes]
exec.example.org

# This section is for your automation hub hosts from your 2.4 inventory
# -----------------------------------------------------
[automationhub]
hub.example.org

# This section is for your Event-Driven Ansible hosts - NEW for 2.6 growth topology
# -----------------------------------------------------
[automationedacontroller]
eda.example.org

# This section is for the Ansible Automation Platform database from your 2.4 inventory file
# -----------------------------------------------------
[database]
db.example.org

[all:vars]

# Common variables from your 2.4 inventory file
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

# Common variables - NEW for 2.6 growth topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
redis_mode=standalone

# Platform gateway - NEW for 2.6 growth topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
automationgateway_admin_password=&lt;set your own&gt;
automationgateway_pg_host=db.example.org
automationgateway_pg_password=&lt;set your own&gt;

# Automation controller variables from your 2.4 inventory file
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
admin_password=&lt;set your own&gt;
pg_host=db.example.org
pg_password=&lt;set your own&gt;

# Automation hub - NEW for 2.6 growth topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
automationhub_admin_password=&lt;set your own&gt;
automationhub_pg_host=db.example.org
automationhub_pg_password=&lt;set your own&gt;

# Event-Driven Ansible - NEW for 2.6 growth topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
automationedacontroller_admin_password=&lt;set your own&gt;
automationedacontroller_pg_host=db.example.org
automationedacontroller_pg_password=&lt;set your own&gt;
```

