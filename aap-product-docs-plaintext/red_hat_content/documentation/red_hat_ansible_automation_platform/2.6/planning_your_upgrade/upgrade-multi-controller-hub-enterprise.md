# 4. Infrastructure changes by deployment type
## 4.1. RPM-based deployments
### 4.1.4. Upgrading a 2.4 multi node automation controller and automation hub deployment to a 2.6 enterprise topology




You can upgrade your 2.4 multi node automation controller and automation hub deployment to a 2.6 enterprise topology. This section outlines the infrastructure changes, requirements, and an example inventory for upgrading.

#### 4.1.4.1. 2.4 infrastructure topology diagram




This diagram outlines the 2.4 infrastructure topology that Red Hat has tested with this deployment model.


<span id="idm140440487201008"></span>
**Figure 4.7. 2.4 infrastructure topology diagram**

![2.4 multi controller and hub topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/b41838ce1c18cbce6495ce4eac2fcadd/rpm-b-controller-hub-2-4.png)




#### 4.1.4.2. 2.6 infrastructure topology diagram




This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.


<span id="idm140440484560048"></span>
**Figure 4.8. 2.6 infrastructure topology diagram**

![2.6 multi controller and hub enterprise topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/1a073d50d5f416340b05c3fe41863cfe/rpm-b-controller-hub-2.6.png)




#### 4.1.4.3. Requirements for upgrading a multi automation controller node and automation hub deployment




The following table highlights the requirements for upgrading from Ansible Automation Platform version 2.4 to 2.6.

| Existing 2.4 topology | Tested 2.6 topology | Requirements for each VM |
| --- | --- | --- |
| Redundant deployment with automation controller and automation hub:

- Two automation controller VMs
- Two automation hub VMs
- One automation mesh hop node VM
- Two automation mesh execution node VMs
- One customer-provided (external) PostgreSQL 15 database
- One HA proxy load balancer in front of automation controller and automation hub | Enterprise topology:

- Two platform gateway with colocated Redis VMs
- Two automation controller VMs
- Two private automation hub with colocated Redis VMs
- Two Event-Driven Ansible controller with colocated Redis VMs
- One automation mesh hop node VM
- Two automation mesh execution node VMs
- One customer-provided (external) PostgreSQL 15 database
- One HA proxy load balancer in front of platform gateway


**Note** : Redis high availability requires 6 VMs. Redis can be colocated with automation hub, platform gateway, or Event-Driven Ansible components, but it cannot be colocated with automation controller, execution nodes, or the PostgreSQL database. | See the [RPM enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/rpm-topologies#rpm-b-env-a) section of the _Tested deployment models_ guide. |


#### 4.1.4.4. Example inventory file




The following inventory file has been updated with the necessary changes to upgrade to the 2.6 enterprise topology.

Important
If your 2.4 inventory file uses `automationhub_main_url` for a load balancer, you must remove this variable from your 2.6 inventory file. The load balancer is now expected to be configured in front of platform gateway ( `automationgateway_main_url` ).



```
# This is the RPM-based Ansible Automation Platform installer inventory file intended for upgrading from a 2.4 multi node automation controller and automation hub deployment to a 2.6 enterprise deployment.

# For all optional variables consult the Red Hat documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation

# This section is for your platform gateway hosts - NEW for 2.6 enterprise topology
# -----------------------------------------------------
[automationgateway]
gateway1.example.org
gateway2.example.org

# This section is for your automation controller hosts from your 2.4 inventory
# -----------------------------------------------------
[automationcontroller]
controller1.example.org
controller2.example.org

[automationcontroller:vars]
peers=execution_nodes

# This section is for your execution hosts from your 2.4 inventory
# -----------------------------------------------------
[execution_nodes]
hop1.example.org node_type='hop'
exec1.example.org
exec2.example.org

# This section is for your automation hub hosts from your 2.4 inventory
# -----------------------------------------------------
[automationhub]
hub1.example.org
hub2.example.org

# This section is for your Event-Driven Ansible hosts - NEW for 2.6 enterprise topology
# -----------------------------------------------------
[automationedacontroller]
eda1.example.org
eda2.example.org

# This section is for your Redis hosts - NEW for 2.6 enterprise topology
# -----------------------------------------------------
[redis]
gateway1.example.org
gateway2.example.org
hub1.example.org
hub2.example.org
eda1.example.org
eda2.example.org

[all:vars]
# Common variables from your 2.4 inventory
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

# Platform gateway - NEW for 2.6 enterprise topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
automationgateway_admin_password=&lt;set your own&gt;
automationgateway_main_url=&lt;set your own&gt; #Set to the URL of the load balancer
automationgateway_pg_host=&lt;set your own&gt;
automationgateway_pg_database=&lt;set your own&gt;
automationgateway_pg_username=&lt;set your own&gt;
automationgateway_pg_password=&lt;set your own&gt;

# Automation controller variables from your 2.4 inventory
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
admin_password=&lt;set your own&gt;
pg_host=&lt;set your own&gt;
pg_database=&lt;set your own&gt;
pg_username=&lt;set your own&gt;
pg_password=&lt;set your own&gt;

# Automation hub variables from your 2.4 inventory
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
automationhub_admin_password=&lt;set your own&gt;
automationhub_pg_host=&lt;set your own&gt;
automationhub_pg_database=&lt;set your own&gt;
automationhub_pg_username=&lt;set your own&gt;
automationhub_pg_password=&lt;set your own&gt;
# This variable is no longer used for load balancer configuration in 2.6:
# automationhub_main_url=&lt;set your own&gt;

# Event-Driven Ansible - NEW for 2.6 enterprise topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
automationedacontroller_admin_password=&lt;set your own&gt;
automationedacontroller_pg_host=&lt;set your own&gt;
automationedacontroller_pg_database=&lt;set your own&gt;
automationedacontroller_pg_username=&lt;set your own&gt;
automationedacontroller_pg_password=&lt;set your own&gt;
```

