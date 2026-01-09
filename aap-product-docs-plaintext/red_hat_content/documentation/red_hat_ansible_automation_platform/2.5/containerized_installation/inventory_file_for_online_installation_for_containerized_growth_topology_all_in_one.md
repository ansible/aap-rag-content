# 4. Preparing the containerized Ansible Automation Platform installation
## 4.6. Configuring the inventory file
### 4.6.1. Inventory file for online installation for containerized growth topology (all-in-one)




Use the example inventory file to perform an online installation for the containerized growth topology (all-in-one):

```
# This is the Ansible Automation Platform installer inventory file intended for the container growth deployment topology.
# This inventory file expects to be run from the host where Ansible Automation Platform will be installed.
# Consult the Ansible Automation Platform product documentation about this topology's tested hardware configuration.
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/container-topologies
#
# Consult the docs if you are unsure what to add
# For all optional variables consult the included README.md
# or the Ansible Automation Platform documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation

# This section is for your platform gateway hosts
# -----------------------------------------------------
[automationgateway]
aap.example.org

# This section is for your automation controller hosts
# -----------------------------------------------------
[automationcontroller]
aap.example.org

# This section is for your automation hub hosts
# -----------------------------------------------------
[automationhub]
aap.example.org

# This section is for your Event-Driven Ansible controller hosts
# -----------------------------------------------------
[automationeda]
aap.example.org

# This section is for the Ansible Automation Platform database
# -----------------------------------------------------
[database]
aap.example.org

[all:vars]
# Ansible
ansible_connection=local

# Common variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
postgresql_admin_username=postgres
postgresql_admin_password=&lt;set your own&gt;

registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

redis_mode=standalone

# Platform gateway
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
gateway_admin_password=&lt;set your own&gt;
gateway_pg_host=aap.example.org
gateway_pg_password=&lt;set your own&gt;

# Automation controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
controller_admin_password=&lt;set your own&gt;
controller_pg_host=aap.example.org
controller_pg_password=&lt;set your own&gt;
controller_percent_memory_capacity=0.5

# Automation hub
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
hub_admin_password=&lt;set your own&gt;
hub_pg_host=aap.example.org
hub_pg_password=&lt;set your own&gt;
hub_seed_collections=false

# Event-Driven Ansible controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
eda_admin_password=&lt;set your own&gt;
eda_pg_host=aap.example.org
eda_pg_password=&lt;set your own&gt;
```

-  `    ansible_connection=local` - Used for all-in-one installations where the installation program is run on the same node that hosts Ansible Automation Platform.


- If the installation program is run from a separate node, do not include `        ansible_connection=local` . In this case, use an SSH connection instead.

-  `    [database]` - This group in the inventory file defines the Ansible Automation Platform managed database.


**Additional resources**

-  [Container growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/container-topologies#infrastructure_topology_5)


