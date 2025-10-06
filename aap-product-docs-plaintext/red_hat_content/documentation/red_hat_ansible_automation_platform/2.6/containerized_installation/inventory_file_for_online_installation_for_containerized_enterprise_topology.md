# 2. Ansible Automation Platform containerized installation
## 2.6. Configuring the inventory file
### 2.6.2. Inventory file for online installation for containerized enterprise topology




Use the example inventory file to perform an online installation for the containerized enterprise topology:

```
# This is the Ansible Automation Platform enterprise installer inventory file
# Consult the docs if you are unsure what to add
# For all optional variables consult the included README.md
# or the Red Hat documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation

# This section is for your platform gateway hosts
# -----------------------------------------------------
[automationgateway]
gateway1.example.org
gateway2.example.org

# This section is for your automation controller hosts
# -----------------------------------------------------
[automationcontroller]
controller1.example.org
controller2.example.org

# This section is for your Ansible Automation Platform execution hosts
# -----------------------------------------------------
[execution_nodes]
hop1.example.org receptor_type='hop'
exec1.example.org
exec2.example.org

# This section is for your automation hub hosts
# -----------------------------------------------------
[automationhub]
hub1.example.org
hub2.example.org

# This section is for your Event-Driven Ansible controller hosts
# -----------------------------------------------------
[automationeda]
eda1.example.org
eda2.example.org

[redis]
gateway1.example.org
gateway2.example.org
hub1.example.org
hub2.example.org
eda1.example.org
eda2.example.org

[all:vars]

# Common variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
postgresql_admin_username=&lt;set your own&gt;
postgresql_admin_password=&lt;set your own&gt;
registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

# Platform gateway
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
gateway_admin_password=&lt;set your own&gt;
gateway_pg_host=externaldb.example.org
gateway_pg_database=&lt;set your own&gt;
gateway_pg_username=&lt;set your own&gt;
gateway_pg_password=&lt;set your own&gt;

# Automation controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
controller_admin_password=&lt;set your own&gt;
controller_pg_host=externaldb.example.org
controller_pg_database=&lt;set your own&gt;
controller_pg_username=&lt;set your own&gt;
controller_pg_password=&lt;set your own&gt;

# Automation hub
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
hub_admin_password=&lt;set your own&gt;
hub_pg_host=externaldb.example.org
hub_pg_database=&lt;set your own&gt;
hub_pg_username=&lt;set your own&gt;
hub_pg_password=&lt;set your own&gt;

# Event-Driven Ansible controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
eda_admin_password=&lt;set your own&gt;
eda_pg_host=externaldb.example.org
eda_pg_database=&lt;set your own&gt;
eda_pg_username=&lt;set your own&gt;
eda_pg_password=&lt;set your own&gt;
```

**Additional resources**

-  [Container enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/container-topologies#infrastructure_topology_6)
-  [Caching and queueing system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/ha-redis_planning)


