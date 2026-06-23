# Configure the inventory file
## Inventory file for online installation for containerized enterprise topology

Use the example inventory file to perform an online installation for the containerized enterprise topology:

```yaml
# This is the Ansible Automation Platform enterprise installer inventory file
# Consult the docs if you are unsure what to add
# For all optional variables consult the included README.md
# or the Red Hat documentation

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

# This section is for your metrics service hosts
# -----------------------------------------------------
[automationmetrics] metrics.example.org

[redis]
gateway1.example.org
gateway2.example.org
hub1.example.org
hub2.example.org
eda1.example.org
eda2.example.org

[all:vars]

# Common variables
# -----------------------------------------------------
postgresql_admin_username=<set your own>
postgresql_admin_password=<set your own>
registry_username=<your RHN username>
registry_password=<your RHN password>

# Platform gateway
# -----------------------------------------------------
gateway_admin_password=<set your own>
gateway_pg_host=externaldb.example.org
gateway_pg_database=<set your own>
gateway_pg_username=<set your own>
gateway_pg_password=<set your own>

# Automation controller
# -----------------------------------------------------
controller_admin_password=<set your own>
controller_pg_host=externaldb.example.org
controller_pg_database=<set your own>
controller_pg_username=<set your own>
controller_pg_password=<set your own>

# Automation hub
# -----------------------------------------------------
hub_admin_password=<set your own>
hub_pg_host=externaldb.example.org
hub_pg_database=<set your own>
hub_pg_username=<set your own>
hub_pg_password=<set your own>

# Event-Driven Ansible controller
# -----------------------------------------------------
eda_admin_password=<set your own>
eda_pg_host=externaldb.example.org
eda_pg_database=<set your own>
eda_pg_username=<set your own>
eda_pg_password=<set your own>

# AAP Automation metrics service
# -----------------------------------------------------
automationmetrics_pg_host=externaldb.example.org
automationmetrics_pg_database=<set your own>
automationmetrics_pg_username=<set your own>
automationmetrics_pg_password=<set your own>
automationmetrics_controller_read_pg_host=externaldb.example.org
automationmetrics_controller_read_pg_password=<set your own>
```


Note:

Metrics service requires access to two databases:

- **`metrics_service` database** (read/write): Stores collected metrics data
- **`automationcontroller` database** (read-only): Correlates metrics with automation activity
The `ms_awx_readonly` user must be created in the external database with SELECT privileges on the `automationcontroller` database.

