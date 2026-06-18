# Configure the inventory file

You can control the installation of Ansible Automation Platform with inventory files. Inventory files define the host details, certificate details, and component-specific settings needed to customize the installation.

Example inventory files are available in this document that you can copy and change to get started.

Important:

The inventory file requirements differ based on your installation type:

- **Online installation**: Requires the `registry_username` and `registry_password` variables to authenticate and pull container images from Red Hat registries during installation.
- **Disconnected (bundled) installation**: Does not require `registry_username` or `registry_password` because all container images are pre-packaged in the bundle. Instead, requires the `bundle_install=true` and `bundle_dir` variables.


The following inventory file examples are for online installations. For disconnected installation inventory requirements, see [Perform a disconnected installation](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_aap_containerized_disconnected_installation#perform-disconnected-installation "A disconnected installation installs containerized Ansible Automation Platform without requiring network access to external registries.").

Important:

The `[automationmetrics]` inventory group is required in Ansible Automation Platform 2.7 when `[automationcontroller]` is present. The installer will fail preflight checks if this group is missing.

Metrics service must be deployed on a dedicated host in containerized deployments.

Additionally, growth topology and enterprise topology inventory files are available in the following locations:

- In the downloaded installation program package:
* The default inventory file, named `inventory`, is for the enterprise topology pattern.
* To deploy the growth topology (all-in-one) pattern, use the `inventory-growth` file instead.
- In [Container growth topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_cont_a_env_a "The container-based growth topology provides a smaller footprint deployment without redundancy for organizations getting started with Ansible Automation Platform.") and [Container enterprise topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_cont_b_env_a "The container-based enterprise topology provides redundancy and higher compute for large volumes of automation.") in *Tested deployment models*.


To use the example inventory files, replace the `< >` placeholders with your specific variables, and update the host names.

Refer to the `README.md` file in the installation directory or [Inventory file variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_inventory_file_vars "The following tables contain information about the variables used in Ansible Automation Platform’s installation inventory files.") for more information about optional and required variables.

Important:

Metrics service is a required component in Ansible Automation Platform 2.7. When you include the `[automationcontroller]` inventory group, you must also include the `[automationmetrics]` inventory group. The installer will fail if `[automationcontroller]` is present without `[automationmetrics]`.

In containerized deployments, metrics service must be deployed on a dedicated host. Do not co-locate metrics service with other Ansible Automation Platform components.

## Inventory file for online installation for containerized growth topology (all-in-one)

Use the example inventory file to perform an online installation for the containerized growth topology (all-in-one):

```yaml
# This is the Ansible Automation Platform installer inventory file intended for the container growth deployment topology.
# This inventory file expects to be run from the host where Ansible Automation Platform will be installed.
# Consult the Ansible Automation Platform product documentation about this topology's tested hardware configuration.
#
# Consult the docs if you are unsure what to add
# For all optional variables consult the included README.md
# or the Ansible Automation Platform documentation

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

# This section is for your metrics service hosts
# -----------------------------------------------------
[automationmetrics]
aap.example.org

# This section is for the Ansible Automation Platform database
# -----------------------------------------------------
[database]
aap.example.org

[all:vars]

# Ansible
ansible_connection=local

# Common variables
# -----------------------------------------------------
postgresql_admin_username=postgres
postgresql_admin_password=<set your own>

registry_username=<your RHN username>
registry_password=<your RHN password>

redis_mode=standalone

# Platform gateway
# -----------------------------------------------------
gateway_admin_password=<set your own>
gateway_pg_host=aap.example.org
gateway_pg_password=<set your own>

# Automation controller
# -----------------------------------------------------
controller_admin_password=<set your own>
controller_pg_host=aap.example.org
controller_pg_password=<set your own>
controller_percent_memory_capacity=0.5

# Automation hub
# -----------------------------------------------------
hub_admin_password=<set your own>
hub_pg_host=aap.example.org
hub_pg_password=<set your own>
hub_seed_collections=false

# Event-Driven Ansible controller
# -----------------------------------------------------
eda_admin_password=<set your own>
eda_pg_host=aap.example.org
eda_pg_password=<set your own>

# AAP Automation metrics service
# -----------------------------------------------------
automationmetrics_pg_host=aap.example.org
automationmetrics_pg_password=<set your own>
automationmetrics_controller_read_pg_host=aap.example.org
automationmetrics_controller_read_pg_password=<set your own>
```


- `ansible_connection=local` - Used for all-in-one installations where the installation program is run on the same node that hosts Ansible Automation Platform.   * If the installation program is run from a separate node, do not include `ansible_connection=local`. In this case, use an SSH connection instead.
- `[database]` - This group in the inventory file defines the Ansible Automation Platform managed database.

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

## Tips for building inventories

When building inventories for Ansible automation, consider the following best practices to ensure efficient and effective management of your hosts.

- Ensure that group names are meaningful and unique.
- Group names are also case sensitive.
- Do not use spaces, hyphens, or preceding numbers (use `floor_19`, not `19th_floor`) in group names.
- Group hosts in your inventory logically according to their What, Where, and When:
* What: Group hosts according to the topology, for example: db, web, leaf, spine, metrics.
* Where: Group hosts by geographic location, for example: data center, region, floor, building.
* When: Group hosts by stage, for example: development, test, staging, production.
- Metrics service must be included when automation controller is present. In containerized deployments, use a dedicated host for metrics service (separate from controller, hub, gateway, and EDA).
