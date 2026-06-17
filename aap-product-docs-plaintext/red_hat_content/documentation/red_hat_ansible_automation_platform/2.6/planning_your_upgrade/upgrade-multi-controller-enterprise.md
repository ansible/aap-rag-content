# 4. Infrastructure changes by deployment type
## 4.1. RPM-based deployments
### 4.1.3. Upgrading a 2.4 multi node automation controller deployment to a 2.6 enterprise topology

Upgrade your 2.4 multi-node automation controller setup to a 2.6 enterprise topology. Review the required infrastructure changes and requirements needed to successfully plan the upgrade.

#### 4.1.3.1. 2.4 infrastructure topology diagram

This diagram outlines the 2.4 infrastructure topology for this deployment model.

**Figure 4.5. 2.4 infrastructure topology diagram**

![2.4 multi controller topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/dae45b79ec5c3b275a7884b5e80d6a14/rpm-b-controller-2-4.png)

#### 4.1.3.2. 2.6 infrastructure topology diagram

This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.

**Figure 4.6. 2.6 infrastructure topology diagram**

![2.6 multi controller enterprise topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/b3751f9a7f990673c57748eab57cc559/rpm-b-controller-2.6.png)

#### 4.1.3.3. Requirements for upgrading a multi automation controller node deployment

The following table highlights the requirements for upgrading from Ansible Automation Platform version 2.4 to 2.6.

| Existing 2.4 topology | Tested 2.6 topology | Requirements for each VM |
| --- | --- | --- |
| <br>  Redundant automation controller-only deployment:    <br>  Two automation controller VMs   One automation mesh hop node VM   Two automation mesh execution node VMs   One customer-provided (external) PostgreSQL 15 database   One HA proxy load balancer in front of automation controller | <br>  Enterprise topology:    <br>  Two platform gateway with colocated Redis VMs   Two automation controller VMs   Two private automation hub with colocated Redis VMs   Two Event-Driven Ansible controller with colocated Redis VMs   One automation mesh hop node VM   Two automation mesh execution node VMs   One customer-provided (external) PostgreSQL 15 database   One HA proxy load balancer in front of platform gateway <br> **Note**: Redis high availability requires 6 VMs. Redis can be colocated with automation hub, platform gateway, or Event-Driven Ansible components, but it cannot be colocated with automation controller, execution nodes, or the PostgreSQL database. | <br>  See the [RPM enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/rpm-topologies#rpm-b-env-a) section of the *Tested deployment models* guide. |

#### 4.1.3.4. Example inventory file

The following inventory file has been updated with the necessary changes to upgrade to the 2.6 enterprise topology.

# This is the RPM-based Ansible Automation Platform installer inventory file intended for upgrading from a 2.4 multi node automation controller deployment to a 2.6 enterprise deployment.

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

# This section is for your automation hub hosts - NEW for 2.6 enterprise topology
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
registry_username=<your RHN username>
registry_password=<your RHN password>

# Platform gateway - NEW for 2.6 enterprise topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
automationgateway_admin_password=<set your own>
automationgateway_main_url=<set your own> #Set to the URL of the load balancer
automationgateway_pg_host=<set your own>
automationgateway_pg_database=<set your own>
automationgateway_pg_username=<set your own>
automationgateway_pg_password=<set your own>

# Automation controller variables from your 2.4 inventory
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
admin_password=<set your own>
pg_host=<set your own>
pg_database=<set your own>
pg_username=<set your own>
pg_password=<set your own>

# Automation hub - NEW for 2.6 enterprise topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
automationhub_admin_password=<set your own>
automationhub_pg_host=<set your own>
automationhub_pg_database=<set your own>
automationhub_pg_username=<set your own>
automationhub_pg_password=<set your own>

# Event-Driven Ansible - NEW for 2.6 enterprise topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
automationedacontroller_admin_password=<set your own>
automationedacontroller_pg_host=<set your own>
automationedacontroller_pg_database=<set your own>
automationedacontroller_pg_username=<set your own>
automationedacontroller_pg_password=<set your own>

