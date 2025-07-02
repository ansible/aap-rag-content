# 2. RPM topologies
## 2.1. RPM growth topology
### 2.1.4. Example inventory file




Use the example inventory file to perform an installation for this topology:

```
# This is the Ansible Automation Platform installer inventory file intended for the RPM growth deployment topology.
# Consult the Ansible Automation Platform product documentation about this topology's tested hardware configuration.
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/rpm-topologies
#
# Consult the docs if you are unsure what to add
# For all optional variables consult the Ansible Automation Platform documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation


# This section is for your platform gateway hosts
# -----------------------------------------------------
[automationgateway]
gateway.example.org

# This section is for your automation controller hosts
# -----------------------------------------------------
[automationcontroller]
controller.example.org

[automationcontroller:vars]
peers=execution_nodes

# This section is for your Ansible Automation Platform execution hosts
# -----------------------------------------------------
[execution_nodes]
exec.example.org

# This section is for your automation hub hosts
# -----------------------------------------------------
[automationhub]
hub.example.org

# This section is for your Event-Driven Ansible controller hosts
# -----------------------------------------------------
[automationedacontroller]
eda.example.org

# This section is for the Ansible Automation Platform database
# -----------------------------------------------------
[database]
db.example.org

[all:vars]

# Common variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

redis_mode=standalone

# Platform gateway
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
automationgateway_admin_password=&lt;set your own&gt;
automationgateway_pg_host=db.example.org
automationgateway_pg_password=&lt;set your own&gt;

# Automation controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#controller-variables
# -----------------------------------------------------
admin_password=&lt;set your own&gt;
pg_host=db.example.org
pg_password=&lt;set your own&gt;

# Automation hub
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#hub-variables
# -----------------------------------------------------
automationhub_admin_password=&lt;set your own&gt;
automationhub_pg_host=db.example.org
automationhub_pg_password=&lt;set your own&gt;

# Event-Driven Ansible controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
automationedacontroller_admin_password=&lt;set your own&gt;
automationedacontroller_pg_host=db.example.org
automationedacontroller_pg_password=&lt;set your own&gt;
```

