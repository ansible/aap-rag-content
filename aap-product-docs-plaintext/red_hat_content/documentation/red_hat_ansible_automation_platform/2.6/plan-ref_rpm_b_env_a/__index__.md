# RPM enterprise topology

The RPM-based enterprise topology provides redundancy and higher compute for large volumes of automation.

Included are the tested infrastructure topology, system requirements, network port configurations, and an example inventory file for installation.

## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*

![RPM enterprise topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rpm-b-env-a.png)

Red Hat tests each VM with these requirements:

*Table 1. Virtual machine requirements*

| Requirement    | Minimum requirement |
| -------------- | ------------------- |
| <br>RAM        | <br>16 GB           |
| <br>CPUs       | <br>4               |
| <br>Local disk | <br>60 GB           |
| <br>Disk IOPS  | <br>3000            |

*Table 2. Infrastructure topology components*

| VM count | Purpose                                                                     | Example VM group names         |
| -------- | --------------------------------------------------------------------------- | ------------------------------ |
| <br>2    | <br>Platform gateway with colocated Redis                                   | <br> `automationgateway`       |
| <br>2    | <br>Automation controller                                                   | <br> `automationcontroller`    |
| <br>2    | <br>Private automation hub with colocated Redis                             | <br> `automationhub`           |
| <br>2    | <br>Event-Driven Ansible with colocated Redis                               | <br> `automationedacontroller` |
| <br>1    | <br>Automation mesh hop node                                                | <br> `execution_nodes`         |
| <br>2    | <br>Automation mesh execution node                                          | <br> `execution_nodes`         |
| <br>1    | <br>Externally managed database service                                     | <br>N/A                        |
| <br>1    | <br>HAProxy load balancer in front of platform gateway (externally managed) | <br>N/A                        |


Note:

- Redis high availability (HA) deployment requires 6 VMs. You can colocate Redis on each Ansible Automation Platform component VM except for automation controller, execution nodes, or the PostgreSQL database.
- RPM-based deployments of Ansible Automation Platform do not support external Redis.

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

| Port number | Protocol | Service        | Source                    | Destination                     |
| ----------- | -------- | -------------- | ------------------------- | ------------------------------- |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Event-Driven Ansible  | <br>Automation hub              |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Event-Driven Ansible  | <br>Automation controller       |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Automation controller | <br>Automation hub              |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>HAProxy load balancer | <br>Platform gateway            |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation controller       |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation hub              |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Event-Driven Ansible        |
| <br>80/443  | <br>TCP  | <br>HTTP/HTTPS | <br>Execution node        | <br>Platform gateway            |
| <br>5432    | <br>TCP  | <br>PostgreSQL | <br>Event-Driven Ansible  | <br>External database           |
| <br>5432    | <br>TCP  | <br>PostgreSQL | <br>Platform gateway      | <br>External database           |
| <br>5432    | <br>TCP  | <br>PostgreSQL | <br>Automation hub        | <br>External database           |
| <br>5432    | <br>TCP  | <br>PostgreSQL | <br>Automation controller | <br>External database           |
| <br>6379    | <br>TCP  | <br>Redis      | <br>Event-Driven Ansible  | <br>Redis node                  |
| <br>6379    | <br>TCP  | <br>Redis      | <br>Platform gateway      | <br>Redis node                  |
| <br>8443    | <br>TCP  | <br>HTTPS      | <br>Platform gateway      | <br>Platform gateway            |
| <br>16379   | <br>TCP  | <br>Redis      | <br>Redis node            | <br>Redis node                  |
| <br>27199   | <br>TCP  | <br>Receptor   | <br>Automation controller | <br>Hop node and execution node |
| <br>27199   | <br>TCP  | <br>Receptor   | <br>Hop node              | <br>Execution node              |


Note:

If you change any port values by using inventory variables, refer to [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars) to review all default port values and ensure there are no port conflicts.

## Example inventory file

Use the example inventory file to perform an installation:

```yaml
# This is the Ansible Automation Platform enterprise installer inventory file
# Consult the docs if you are unsure what to add
# For all optional variables consult the Red Hat documentation

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

[automationcontroller:vars]
peers=execution_nodes

# This section is for your Ansible Automation Platform execution hosts
# -----------------------------------------------------
[execution_nodes]
hop1.example.org node_type='hop'
exec1.example.org
exec2.example.org

# This section is for your automation hub hosts
# -----------------------------------------------------
[automationhub]
hub1.example.org
hub2.example.org

# This section is for your Event-Driven Ansible controller hosts
# -----------------------------------------------------
[automationedacontroller]
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
# -----------------------------------------------------
registry_username=<your RHN username>
registry_password=<your RHN password>

# Platform gateway
# -----------------------------------------------------
automationgateway_admin_password=<set your own>
automationgateway_pg_host=<set your own>
automationgateway_pg_database=<set your own>
automationgateway_pg_username=<set your own>
automationgateway_pg_password=<set your own>

# Automation controller
# -----------------------------------------------------
admin_password=<set your own>
pg_host=<set your own>
pg_database=<set your own>
pg_username=<set your own>
pg_password=<set your own>

# Automation hub
# -----------------------------------------------------
automationhub_admin_password=<set your own>
automationhub_pg_host=<set your own>
automationhub_pg_database=<set your own>
automationhub_pg_username=<set your own>
automationhub_pg_password=<set your own>

# Event-Driven Ansible controller
# -----------------------------------------------------
automationedacontroller_admin_password=<set your own>
automationedacontroller_pg_host=<set your own>
automationedacontroller_pg_database=<set your own>
automationedacontroller_pg_username=<set your own>
automationedacontroller_pg_password=<set your own>
```
