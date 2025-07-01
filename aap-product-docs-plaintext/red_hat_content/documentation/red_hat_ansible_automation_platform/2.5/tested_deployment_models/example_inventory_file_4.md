# 2. RPM topologies
## 2.4. RPM mixed enterprise topology
### 2.4.4. Example inventory file




Use the example inventory file to perform an installation for this topology:

```
# This is the Ansible Automation Platform mixed enterprise installer inventory file
# Consult the docs if you are unsure what to add
# For all optional variables consult the Red Hat documentation:
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation

# This section is for your platform gateway hosts
# -----------------------------------------------------
[automationgateway]
gateway1.example.org
gateway2.example.org
gateway3.example.org

# This section is for your Event-Driven Ansible controller hosts
# -----------------------------------------------------
[automationedacontroller]
eda1.example.org
eda2.example.org
eda3.example.org

[redis]
gateway1.example.org
gateway2.example.org
gateway3.example.org
eda1.example.org
eda2.example.org
eda3.example.org

[all:vars]
# Common variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#general-variables
# -----------------------------------------------------
registry_username=&lt;your RHN username&gt;
registry_password=&lt;your RHN password&gt;

# Platform gateway
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#platform-gateway-variables
# -----------------------------------------------------
automationgateway_admin_password=&lt;set your own&gt;
automationgateway_pg_host=&lt;set your own&gt;
automationgateway_pg_database=&lt;set your own&gt;
automationgateway_pg_username=&lt;set your own&gt;
automationgateway_pg_password=&lt;set your own&gt;

# Event-Driven Ansible controller
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#event-driven-ansible-variables
# -----------------------------------------------------
automationedacontroller_admin_password=&lt;set your own&gt;
automationedacontroller_pg_host=&lt;set your own&gt;
automationedacontroller_pg_database=&lt;set your own&gt;
automationedacontroller_pg_username=&lt;set your own&gt;
automationedacontroller_pg_password=&lt;set your own&gt;
```

