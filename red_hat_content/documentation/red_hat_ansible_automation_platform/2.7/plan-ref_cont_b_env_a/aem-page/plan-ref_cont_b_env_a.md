+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_cont_b_env_a"
title = "Container enterprise topology - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-assembly_overview_tested_deployment_models/", "Choose a deployment method and topology"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-ref_cont_b_env_a/aem-page/plan-ref_cont_b_env_a.html"
last_crumb = "Container enterprise topology"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Container enterprise topology"
oversized = "false"
page_slug = "plan-ref_cont_b_env_a"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-ref_cont_b_env_a"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-ref_cont_b_env_a/toc/toc.json"
type = "aem-page"
+++

# Container enterprise topology

The container-based enterprise topology provides redundancy and higher compute for large volumes of automation.

Included are the tested infrastructure topology, system requirements, network port configurations, and an example inventory file for installation.

## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*
![Container enterprise topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/cont-b-env-a-2_7.png)

Red Hat tests each VM with these requirements:

*Table 1. Virtual machine requirements*

| Requirement    | Minimum requirement                                                                                                                                                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>RAM        | <br>16 GB                                                                                                                                                                                                                                                                     |
| <br>CPUs       | <br>4                                                                                                                                                                                                                                                                         |
| <br>Local disk | Total available disk space: 60 GBInstallation directory: 15 GB (if on a dedicated partition)`/var/tmp` for online installations: 1 GB`/var/tmp` for offline or bundled installations: 3 GBTemporary directory (defaults to `/tmp`) for offline or bundled installations: 10GB |
| <br>Disk IOPS  | <br>3000                                                                                                                                                                                                                                                                      |


 Note:

Metrics service node requirements:

- **RAM:** 16 GB (4 GB minimum, 8 GB recommended for high-volume environments)
- **CPUs:** 4 (2 minimum)
- **Local disk:** 40 GB (20 GB minimum)
- **Disk IOPS:** 3000

*Table 2. Infrastructure topology components*

| VM count | Purpose                                                                     | Example VM group names      |
| -------- | --------------------------------------------------------------------------- | --------------------------- |
| <br>2    | <br>Platform gateway with colocated Redis                                   | <br> `automationgateway`    |
| <br>2    | <br>Automation controller                                                   | <br> `automationcontroller` |
| <br>1    | <br>Metrics service                                                         | <br>`automationmetrics`     |
| <br>2    | <br>Private automation hub with colocated Redis                             | <br> `automationhub`        |
| <br>2    | <br>Event-Driven Ansible with colocated Redis                               | <br> `automationeda`        |
| <br>1    | <br>Automation mesh hop node                                                | <br> `execution_nodes`      |
| <br>2    | <br>Automation mesh execution node                                          | <br> `execution_nodes`      |
| <br>1    | <br>Externally managed database service                                     | <br>N/A                     |
| <br>1    | <br>HAProxy load balancer in front of platform gateway (externally managed) | <br>N/A                     |


 Note:

- 6 VMs are required for a Redis high availability (HA) compatible deployment. When installing Ansible Automation Platform with the containerized installer, Redis can be colocated on any Ansible Automation Platform component VMs of your choice except for execution nodes or the PostgreSQL database. They might also be assigned VMs specifically for Redis use.
- External Redis is not supported for containerized Ansible Automation Platform.

## Tested system configurations

Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:

*Table 3. System configuration*

| Type                 | Description                                                                                                                                                                                                                                   | Notes                                                                                                                                                                                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription     | Valid Red Hat Ansible Automation Platform subscriptionValid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories)                                                                                          |                                                                                                                                                                                                                                                                                             |
| <br>Operating system | Red Hat Enterprise Linux 9.6 or later minor versions of Red Hat Enterprise Linux 9.Red Hat Enterprise Linux 10 or later minor versions of Red Hat Enterprise Linux 10.                                                                        |                                                                                                                                                                                                                                                                                             |
| <br>CPU architecture | <br>x86\_64, AArch64, s390x (IBM Z), ppc64le (IBM Power)                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                             |
| <br> `ansible-core`  | RHEL 9: installation program uses `ansible-core` 2.14, Ansible Automation Platform operation uses `ansible-core` 2.16.RHEL 10: installation program uses `ansible-core` 2.16, Ansible Automation Platform operation uses `ansible-core` 2.16. | The installation program uses the `ansible-core` package from the RHEL AppStream repository.Ansible Automation Platform bundles `ansible-core` 2.16 for operation, so you do not need to install it manually.                                                                               |
| <br>Browser          | <br>A currently supported version of Mozilla Firefox or Google Chrome.                                                                                                                                                                        |                                                                                                                                                                                                                                                                                             |
| <br>Database         | For Ansible Automation Platform managed databases: PostgreSQL 15.For customer provided (external) databases: PostgreSQL 15, 16, or 17.                                                                                                        | External (customer supported) databases require International Components for Unicode (ICU) support.External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |
| <br>IP version       | <br>IPv4, IPv6 (single-stack and dual-stack)                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |

## Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 4. Network ports and protocols*

| Port number   | Protocol | Service        | Source                    | Destination                     | Description                                                                                                                                                               |
| ------------- | -------- | -------------- | ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Event-Driven Ansible  | <br>Automation hub              | <br>Pull container decision environments                                                                                                                                  |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Event-Driven Ansible  | <br>Automation controller       | <br>Launch automation controller jobs                                                                                                                                     |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Automation controller | <br>Automation hub              | <br>Pull collections and execution environment images                                                                                                                     |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>HAProxy load balancer | <br>Platform gateway            | <br>External load balancer access                                                                                                                                         |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation controller       | <br>Platform gateway to automation controller communication                                                                                                               |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation hub              | <br>Platform gateway to automation hub communication                                                                                                                      |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Metrics service             | <br>Platform gateway to metrics service communication (internal routing for dashboard)                                                                                    |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Metrics service       | <br>External database           | <br>Metrics service database access (dual-database: `metrics_service` read/write + awx read-only)                                                                         |
| <br>80/443    | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Event-Driven Ansible        | <br>Platform gateway to Event-Driven Ansible communication                                                                                                                |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Event-Driven Ansible  | <br>External database           | <br>Event-Driven Ansible database access                                                                                                                                  |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Platform gateway      | <br>External database           | <br>Platform gateway database access                                                                                                                                      |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Automation hub        | <br>External database           | <br>Automation hub database access                                                                                                                                        |
| <br>5432      | <br>TCP  | <br>PostgreSQL | <br>Automation controller | <br>External database           | <br>Automation controller database access                                                                                                                                 |
| <br>6379      | <br>TCP  | <br>Redis      | <br>Event-Driven Ansible  | <br>Redis node                  | <br>Job launching and data storage for Event-Driven Ansible                                                                                                               |
| <br>6379      | <br>TCP  | <br>Redis      | <br>Platform gateway      | <br>Redis node                  | <br>Data storage and retrieval for platform gateway services                                                                                                              |
| <br>16379     | <br>TCP  | <br>Redis      | <br>Redis node            | <br>Redis node                  | <br>Redis cluster bus communication                                                                                                                                       |
| <br>27199     | <br>TCP  | <br>Receptor   | <br>Automation controller | <br>Hop node and execution node | <br>Mesh nodes connect directly to controllers. Allows two-way communication for job distribution.                                                                        |
| <br>27199     | <br>TCP  | <br>Receptor   | <br>Hop node              | <br>Execution node              | <br>Mesh nodes connect through hop nodes. Allows two-way communication in either direction.                                                                               |
| <br>8080/8443 | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation controller       | <br>Automation controller NGINX ports. You can configure these ports with the following inventory variables: `controller_nginx_http_port`, `controller_nginx_https_port`. |
| <br>8081/8444 | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Automation hub              | <br>Automation hub NGINX ports. You can configure these ports with the following inventory variables: `hub_nginx_http_port`, `hub_nginx_https_port`.                      |
| <br>8082/8445 | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Event-Driven Ansible        | <br>Event-Driven Ansible NGINX ports. You can configure these ports with the following inventory variables: `eda_nginx_http_port`, `eda_nginx_https_port`.                |
| <br>8083/8446 | <br>TCP  | <br>HTTP/HTTPS | <br>Platform gateway      | <br>Platform gateway            | <br>Platform gateway NGINX ports. You can configure these ports with the following inventory variables: `gateway_nginx_http_port`, `gateway_nginx_https_port`.            |


 Note:

If you change any port values by using inventory variables, refer to [Inventory file variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_inventory_file_vars "The following tables contain information about the variables used in Ansible Automation Platform’s installation inventory files.") to review all default port values and ensure there are no port conflicts.

## Example inventory file

Use the example inventory file to perform an installation:

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

# Metrics Service
# -----------------------------------------------------
automationmetrics_pg_host=externaldb.example.org
automationmetrics_pg_database=metrics_service
automationmetrics_pg_username=metrics_service
automationmetrics_pg_password=<set your own>

# Read-only access to controller database for data collection
automationmetrics_controller_read_pg_host=externaldb.example.org
automationmetrics_controller_read_pg_database=<controller database name>
automationmetrics_controller_read_pg_username=ms_awx_readonly
automationmetrics_controller_read_pg_password=<set your own>
```

## Metrics service database architecture

The enterprise topology uses an externally managed PostgreSQL database service. Metrics service requires provisioning of two database configurations:

**Database 1: `metrics_service` (read/write)**

Purpose: Store metrics data, dashboard calculations, anonymized payloads

Database configuration:

```
CREATE DATABASE metrics_service
  WITH ENCODING='UTF8'
       LC_COLLATE='en_US.UTF-8'
       LC_CTYPE='en_US.UTF-8'
       TEMPLATE=template0;

CREATE USER metrics_service WITH PASSWORD '<secure_password>';
GRANT ALL PRIVILEGES ON DATABASE metrics_service TO metrics_service;
```
Storage requirements:

- Minimum: 20 GB
- Recommended: 40 GB
- High-volume (>20,000 jobs/day): 60-80 GB


**Database 2: awx (read-only access)**

Purpose: Collect automation job data for metrics calculation

User configuration:

```
CREATE USER ms_awx_readonly WITH PASSWORD '<readonly_password>';
\c awx  -- Connect to automation controller database
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ms_awx_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT ON TABLES TO ms_awx_readonly;
```
Security model:

- `ms_awx_readonly` user has SELECT-only privileges
- Prevents metrics service from modifying automation controller operations
- Read-only access ensures separation of concerns


**External database storage allocation**

Update your external PostgreSQL database storage to accommodate metrics service:

*Table 5. External database storage allocation*

| Database          | Purpose               | Storage allocation |
| ----------------- | --------------------- | ------------------ |
| `gateway`         | Platform gateway      | 20 GB              |
| `awx`             | Automation controller | 80 GB              |
| `metrics_service` | Metrics service       | 40 GB              |
| `pulp`            | Automation hub        | 60 GB              |
| `eda`             | Event-Driven Ansible  | 20 GB              |
| Total             | All components        | 220 GB             |


 Note:

Database storage consumption varies based on job frequency, playbook complexity, and retention policies. Monitor actual usage after deployment and adjust accordingly.
