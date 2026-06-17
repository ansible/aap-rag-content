# RPM growth topology

The RPM-based growth topology provides a smaller footprint deployment without redundancy for organizations getting started with Ansible Automation Platform.

Included are the tested infrastructure topology, system requirements, network port configurations, and an example inventory file for installation.

## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*

![RPM growth topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rpm-a-env-a.png)

Red Hat tests each VM with these requirements:

*Table 1. Virtual machine requirements*

| Requirement    | Minimum requirement |
| -------------- | ------------------- |
| <br>RAM        | <br>16 GB           |
| <br>CPUs       | <br>4               |
| <br>Local disk | <br>60 GB           |
| <br>Disk IOPS  | <br>3000            |

*Table 2. Infrastructure topology components*

| VM count | Purpose                                          | Example VM group names         |
| -------- | ------------------------------------------------ | ------------------------------ |
| <br>1    | <br>Platform gateway with colocated Redis        | <br> `automationgateway`       |
| <br>1    | <br>Automation controller                        | <br> `automationcontroller`    |
| <br>1    | <br>Private automation hub                       | <br> `automationhub`           |
| <br>1    | <br>Event-Driven Ansible                         | <br> `automationedacontroller` |
| <br>1    | <br>Automation mesh execution node               | <br> `execution_nodes`         |
| <br>1    | <br>Ansible Automation Platform managed database | <br> `database`                |

## Tested system configurations

Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:

*Table 3. Tested system configurations*

| Type                 | Description                                                                                                                           |                                                                                                                                                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription     | <br>Valid Red Hat Ansible Automation Platform subscription                                                                            |                                                                                                                                                                                                                                                      |
| <br>Operating system | <br>Red Hat Enterprise Linux 9.6 or later minor versions of Red Hat Enterprise Linux 9.                                               |                                                                                                                                                                                                                                                      |
| <br>CPU architecture | <br>x86\_64, AArch64, s390x (IBM Z), ppc64le (IBM Power)                                                                              |                                                                                                                                                                                                                                                      |
| <br> `ansible-core`  | <br>`ansible-core` version 2.16 or later                                                                                              | <br>Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments.                                                        |
| <br>Browser          | <br>A currently supported version of Mozilla Firefox or Google Chrome                                                                 |                                                                                                                                                                                                                                                      |
| <br>Database         | For Ansible Automation Platform managed databases: PostgreSQL 15For customer provided (external) databases: PostgreSQL 15, 16, or 17. | External (customer supported) databases require ICU support.External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |
| <br>IP version       | <br>IPv4, IPv6 (single-stack and dual-stack)                                                                                          |                                                                                                                                                                                                                                                      |

## Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 4. Network ports and protocols*

| Port number | Protocol | Service        | Source                    | Destination               |
| ----------- | -------- | -------------- | ------------------------- | ------------------------- |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Event-Driven Ansible  | <br>Automation hub        |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Event-Driven Ansible  | <br>Automation controller |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Automation controller | <br>Automation hub        |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation controller |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation hub        |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Event-Driven Ansible  |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Execution node        | <br>Platform gateway      |
| <br>5432    | <br>TCP  | <br>PostgreSQL | <br>Event-Driven Ansible  | <br>Database              |
| <br>5432    | <br>TCP  | <br>PostgreSQL | <br>Platform gateway      | <br>Database              |
| <br>5432    | <br>TCP  | <br>PostgreSQL | <br>Automation hub        | <br>Database              |
| <br>5432    | <br>TCP  | <br>PostgreSQL | <br>Automation controller | <br>Database              |
| <br>6379    | <br>TCP  | <br>Redis      | <br>Event-Driven Ansible  | <br>Redis node            |
| <br>6379    | <br>TCP  | <br>Redis      | <br>Platform gateway      | <br>Redis node            |
| <br>8443    | <br>TCP  | <br>HTTPS      | <br>Platform gateway      | <br>Platform gateway      |
| <br>27199   | <br>TCP  | <br>Receptor   | <br>Automation controller | <br>Execution node        |


Note:

If you change any port values by using inventory variables, refer to [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars) to review all default port values and ensure there are no port conflicts.

## Example inventory file

Use the example inventory file to perform an installation:

```yaml
# This is the Ansible Automation Platform installer inventory file intended for the RPM growth deployment topology.
# Consult the Ansible Automation Platform product documentation about this topology's tested hardware configuration.
#
# Consult the docs if you are unsure what to add
# For all optional variables consult the Ansible Automation Platform documentation

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
# -----------------------------------------------------
registry_username=<your RHN username>
registry_password=<your RHN password>

redis_mode=standalone

# Platform gateway
# -----------------------------------------------------
automationgateway_admin_password=<set your own>
automationgateway_pg_host=db.example.org
automationgateway_pg_password=<set your own>

# Automation controller
# -----------------------------------------------------
admin_password=<set your own>
pg_host=db.example.org
pg_password=<set your own>

# Automation hub
# -----------------------------------------------------
automationhub_admin_password=<set your own>
automationhub_pg_host=db.example.org
automationhub_pg_password=<set your own>

# Event-Driven Ansible controller
# -----------------------------------------------------
automationedacontroller_admin_password=<set your own>
automationedacontroller_pg_host=db.example.org
automationedacontroller_pg_password=<set your own>
```
