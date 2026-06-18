+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_cont_a_env_a"
template = "docs/aem-title.html"
title = "Container growth topology - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-assembly_overview_tested_deployment_models/", "Choose a deployment method and topology"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-ref_cont_a_env_a/aem-page/plan-ref_cont_a_env_a.html"
last_crumb = "Container growth topology"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Container growth topology"
oversized = "false"
page_slug = "plan-ref_cont_a_env_a"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-ref_cont_a_env_a"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-ref_cont_a_env_a/toc/toc.json"
type = "aem-page"
+++

# Container growth topology

The container-based growth topology provides a smaller footprint deployment without redundancy for organizations getting started with Ansible Automation Platform.

Included are the tested infrastructure topology, system requirements, network port configurations, and an example inventory file for installation.

## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*
![Container growth topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/cont-a-env-a-2_7.png)

Red Hat tests a single VM with these requirements:

*Table 1. Virtual machine requirements*

| Requirement    | Minimum requirement                                                                                                                                                                                                                                                                                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>RAM        | 16 GB minimum, 20 GB recommended32 GB required for growth topology bundled installations with `hub_seed_collections=true`. Seeding the collections can take 45 or more minutes.    Note:     Metrics service adds approximately 4 GB RAM usage (2 GB minimum).                                                                                                  |
| <br>CPUs       | <br>4                                                                                                                                                                                                                                                                                                                                                           |
| <br>Local disk | Total available disk space: 80 GB (60 GB base + 20 GB for metrics service)Installation directory: 15 GB (if on a dedicated partition)`/var/tmp` for online installations: 1 GB`/var/tmp` for offline or bundled installations: 10 GBMetrics service database: 20 GB minimumTemporary directory (defaults to `/tmp`) for offline or bundled installations: 10 GB |
| <br>Disk IOPS  | <br>3000                                                                                                                                                                                                                                                                                                                                                        |

*Table 2. Infrastructure topology components*

| Purpose                                        | Example group names                                                                                      |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| <br>All Ansible Automation Platform components | `automationgateway` `automationcontroller` `automationhub` `automationeda``automationmetrics` `database` |


 Note:

In the growth topology (all-in-one), metrics service runs on the same host as automation controller and other Ansible Automation Platform components. The installer deploys 3 metrics service containers:

- `automation-metrics-web` - REST API for metrics and dashboard data
- `automation-metrics-tasks` - dispatcherd worker for data collection
- `automation-metrics-scheduler` - APScheduler for periodic collection tasks

## Tested system configurations

Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:

*Table 3. System configuration*

| Type                 | Description                                                                                                                                                                                                                               | Notes                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription     | Valid Red Hat Ansible Automation Platform subscriptionValid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories)                                                                                      |                                                                                                                                                                                                                                                                                             |
| <br>Operating system | Red Hat Enterprise Linux 9.6 or later minor versions of Red Hat Enterprise Linux 9.Red Hat Enterprise Linux 10 or later minor versions of Red Hat Enterprise Linux 10.                                                                    |                                                                                                                                                                                                                                                                                             |
| <br>CPU architecture | <br>x86\_64, AArch64, s390x (IBM Z), ppc64le (IBM Power)                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
| <br> `ansible-core`  | RHEL 9: installation program uses`ansible-core` 2.14, Ansible Automation Platform operation uses `ansible-core 2.16`RHEL 10: installation program uses`ansible-core` 2.16, Ansible Automation Platform operation uses `ansible-core` 2.16 | The installation program uses the `ansible-core` package from the RHEL AppStream repository.Ansible Automation Platform bundles `ansible-core` 2.16 for operation, so you do not need to install it manually.                                                                               |
| <br>Browser          | <br>A currently supported version of Mozilla Firefox or Google Chrome.                                                                                                                                                                    |                                                                                                                                                                                                                                                                                             |
| <br>Database         | For Ansible Automation Platform managed databases: PostgreSQL 15.For customer provided (external) databases: PostgreSQL 15, 16, or 17.                                                                                                    | External (customer supported) databases require International Components for Unicode (ICU) support.External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |
| <br>IP version       | <br>IPv4, IPv6 (single-stack and dual-stack)                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                             |

## Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 4. Network ports and protocols*

| Port number   | Protocol | Service        | Source                    | Destination                                                                                           | Description                                                                                                                                                               |
| ------------- | -------- | -------------- | ------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Event-Driven Ansible  | <br>Automation hub                                                                                    | <br>Pull container decision environments                                                                                                                                  |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Event-Driven Ansible  | <br>Automation controller                                                                             | <br>Launch automation controller jobs                                                                                                                                     |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Automation controller | <br>Automation hub                                                                                    | <br>Pull collections and execution environment images                                                                                                                     |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation controller                                                                             | <br>Platform gateway to automation controller communication                                                                                                               |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation hub                                                                                    | <br>Platform gateway to automation hub communication                                                                                                                      |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Event-Driven Ansible                                                                              | <br>Platform gateway to Event-Driven Ansible communication                                                                                                                |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Event-Driven Ansible  | <br>Database                                                                                          | <br>Event-Driven Ansible database access                                                                                                                                  |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Platform gateway      | <br>Database                                                                                          | <br>Platform gateway database access                                                                                                                                      |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Automation hub        | <br>Database                                                                                          | <br>Automation hub database access                                                                                                                                        |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Automation controller | <br>Database                                                                                          | <br>Automation controller database access                                                                                                                                 |
| <br>6379      | <br>TCP  | <br>Redis      | <br>Event-Driven Ansible  | <br>Redis container                                                                                   | <br>Job launching and data storage for Event-Driven Ansible                                                                                                               |
| <br>6379      | <br>TCP  | <br>Redis      | <br>Platform gateway      | <br>Redis container                                                                                   | <br>Data storage and retrieval for platform gateway services                                                                                                              |
| <br>8443      | <br>TCP  | <br>HTTPS      | <br>Platform gateway      | <br>Platform gateway                                                                                  | <br>Internal gateway NGINX communication                                                                                                                                  |
| <br>27199     | <br>TCP  | <br>Receptor   | <br>Automation controller | <br>Execution container                                                                               | <br>Mesh nodes connect directly to controllers. Allows two-way communication for job distribution.                                                                        |
| <br>8080/8443 | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation controller                                                                             | <br>Automation controller NGINX ports. You can configure these ports with the following inventory variables: `controller_nginx_http_port`, `controller_nginx_https_port`. |
| <br>8081/8444 | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation hub                                                                                    | <br>Automation hub NGINX ports. You can configure these ports with the following inventory variables: `hub_nginx_http_port`, `hub_nginx_https_port`.                      |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Metrics service API (internal, routes dashboard requires from hub UI)                             | <br>                                                                                                                                                                      |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Metrics service       | <br>Metrics service database access (`metrics_service` database: read/write, awx database: read-only) | <br>                                                                                                                                                                      |
| <br>8082/8445 | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Event-Driven Ansible                                                                              | <br>Event-Driven Ansible NGINX ports. You can configure these ports with the following inventory variables: `eda_nginx_http_port`, `eda_nginx_https_port`.                |
| <br>8083/8446 | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Platform gateway                                                                                  | <br>Platform gateway NGINX ports. You can configure these ports with the following inventory variables: `gateway_nginx_http_port`, `gateway_nginx_https_port`.            |


 Note:

If you change any port values by using inventory variables, refer to [Inventory file variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_inventory_file_vars "The following tables contain information about the variables used in Ansible Automation Platform’s installation inventory files.") to review all default port values and ensure there are no port conflicts.

## Example inventory file

Use the example inventory file to perform an installation:

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

# Metrics service
# ----------------------------------------------------- automationmetrics_pg_host=aap.example.org
automationmetrics_pg_password=<set your own>
```
SSH keys are only required when installing on remote hosts. If doing a self contained local VM based installation, you can use `ansible_connection=local`.

## Metrics service database

The growth topology uses a managed PostgreSQL database that includes the metrics_service database alongside other AAP component databases.

**Databases created**

- `gateway` - Platform gateway data
- `awx` - Automation controller data
- `pulp` - Automation hub data
- `eda` - Event-Driven Ansible data
- `metrics_service` - Metrics service data storage (20 GB minimum)


**Database users**

- `metrics_service` - Full access to metrics_service database
- `ms_awx_readonly` - Read-only access to awx database for metrics collection


 Note:

The installer automatically creates both databases and users. No manual database provisioning is required for growth topology.
