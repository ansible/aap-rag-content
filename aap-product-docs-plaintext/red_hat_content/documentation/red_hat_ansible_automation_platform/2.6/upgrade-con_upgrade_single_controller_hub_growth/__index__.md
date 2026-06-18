# 2.4 single node automation controller and automation hub deployment to a 2.6 growth topology

Upgrade your 2.4 single-node deployment (automation controller and automation hub) to a 2.6 growth topology. Review the infrastructure changes and requirements needed to successfully plan your upgrade.

## 2.4 infrastructure topology diagram

This diagram outlines the 2.4 infrastructure topology for this deployment model.

*Figure 1. 2.4 infrastructure topology diagram*

![2.4 single controller and hub topology](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rpm-a-controller-hub-2-4.png)

## 2.6 infrastructure topology diagram

This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.

*Figure 2. 2.6 infrastructure topology diagram*

![2.6 single controller and hub growth topology](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rpm-a-controller-hub-2-6.png)

## Requirements for upgrading a single automation controller node and automation hub deployment

The following table highlights the requirements for upgrading from Ansible Automation Platform version 2.4 to 2.6.

| Existing 2.4 topology                                                                                                                                                                          | Tested 2.6 topology                                                                                                                                                                                                                                                 | Requirements for each VM       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| <br>Non-redundant deployment with automation controller and automation hub:<br>One automation controller VMOne automation hub VMOne Ansible Automation Platform managed PostgreSQL 15 database | <br>Growth topology:<br>One platform gateway with colocated Redis VMOne automation controller VMOne private automation hub VMOne Event-Driven Ansible controller VMOne automation mesh execution nodeOne Ansible Automation Platform managed PostgreSQL 15 database | <br>See *RPM growth topology*. |

## Example inventory file

The following inventory file has been updated with the necessary changes to upgrade to the 2.6 growth topology.

```yaml
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
registry_username=<your RHN username>
registry_password=<your RHN password>

# Common variables - NEW for 2.6 growth topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
redis_mode=standalone

# Platform gateway - NEW for 2.6 growth topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
automationgateway_admin_password=<set your own>
automationgateway_pg_host=db.example.org
automationgateway_pg_password=<set your own>

# Automation controller variables from your 2.4 inventory file
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
admin_password=<set your own>
pg_host=db.example.org
pg_password=<set your own>

# Automation hub - NEW for 2.6 growth topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
automationhub_admin_password=<set your own>
automationhub_pg_host=db.example.org
automationhub_pg_password=<set your own>

# Event-Driven Ansible - NEW for 2.6 growth topology
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
automationedacontroller_admin_password=<set your own>
automationedacontroller_pg_host=db.example.org
automationedacontroller_pg_password=<set your own>
```
