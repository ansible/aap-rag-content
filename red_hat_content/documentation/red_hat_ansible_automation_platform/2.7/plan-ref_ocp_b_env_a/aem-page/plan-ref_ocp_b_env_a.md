+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_ocp_b_env_a"
title = "Operator enterprise topology - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-assembly_overview_tested_deployment_models/", "Choose a deployment method and topology"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-ref_ocp_b_env_a/aem-page/plan-ref_ocp_b_env_a.html"
last_crumb = "Operator enterprise topology"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Operator enterprise topology"
oversized = "false"
page_slug = "plan-ref_ocp_b_env_a"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-ref_ocp_b_env_a"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-ref_ocp_b_env_a/toc/toc.json"
type = "aem-page"
+++

# Operator enterprise topology

The Operator-based enterprise topology provides redundancy and higher compute for large volumes of automation on Red Hat OpenShift Container Platform.

The Ansible Automation Platform Service on AWS is an example of an OpenShift Operator based enterprise topology.

Included are the tested infrastructure topology, system requirements, network port configurations, and an example custom resource file for installation.

 Important:

You can only install a single instance of the Ansible Automation Platform Operator into a single namespace. Installing multiple instances in the same namespace can lead to improper operation for both Operator instances.

## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*
![Operator enterprise topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ocp-b-env-a-2_7.png)

 Important:

While Redis and PostgreSQL can be installed as part of the operator-based installation process, the topology diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.

This infrastructure topology describes an OpenShift Cluster with 3 primary nodes and 2 worker nodes.

Red Hat tests each OpenShift Worker node with these requirements:

*Table 1. OpenShift Worker node requirements*

| Requirement | Minimum requirement |
| ----------- | ------------------- |
| RAM         | 16 GB               |
| CPUs        | 4                   |
| Local disk  | 128 GB              |
| Disk IOPS   | 3000                |

*Table 2. Infrastructure topology components*

| Count   | Component                                                          |
| ------- | ------------------------------------------------------------------ |
| <br>1   | <br>Automation controller web pod                                  |
| <br>1   | <br>Automation controller task pod                                 |
| <br>1   | <br>Automation hub web pod                                         |
| <br>1   | <br>Automation hub API pod                                         |
| <br>2   | <br>Automation hub content pod                                     |
| <br>2   | <br>Automation hub worker pod                                      |
| <br>1   | <br>Automation hub Redis pod                                       |
| <br>1   | <br>Event-Driven Ansible API pod                                   |
| <br>2   | <br>Event-Driven Ansible activation worker pod                     |
| <br>2   | <br>Event-Driven Ansible default worker pod                        |
| <br>2   | <br>Event-Driven Ansible event stream pod                          |
| <br>1   | <br>Event-Driven Ansible scheduler pod                             |
| <br>1   | <br>Platform gateway pod                                           |
| <br>1   | <br>Metrics service web pod                                        |
| <br>1   | <br>Metrics service tasks pod                                      |
| <br>1   | <br>Metrics service scheduler pod                                  |
| <br>2   | <br>Mesh ingress pod                                               |
| <br>N/A | <br>Externally managed database service                            |
| <br>N/A | <br>Externally managed Redis                                       |
| <br>N/A | <br>Externally managed object storage service (for automation hub) |

## Tested system configurations

Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:

*Table 3. Tested system configurations*

| Type                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription                 | <br>Valid Red Hat Ansible Automation Platform subscription                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <br>Red Hat OpenShift            | Red Hat OpenShift on AWS Hosted Control Planes 4.15.16     2 worker nodes in different availability zones (AZs) at t3.xlarge                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <br>Ansible-core                 | <br>Ansible-core version 2.16 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <br>Browser                      | <br>A currently supported version of Mozilla Firefox or Google Chrome.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <br>AWS RDS PostgreSQL service   | engine: "postgres"engine\_version: 15"parameter\_group\_name: "default.postgres15"allocated\_storage: 20max\_allocated\_storage: 1000storage\_type: "gp2"storage\_encrypted: trueinstance\_class: "db.t4g.small"multi\_az: truebackup\_retention\_period: 5database: must have International Components for Unicode (ICU) supportdatabases required: `automationcontroller`, `automationhub`, `automationeda`, `metrics_service`       Note:   <br>Minimum external database requirements<br>The external database must meet these minimum requirements:<br>4 vCPUs16 GB RAMmax\_connections: 1024 (minimum). You might need more connections when scaling replicas.200 GB storage on a volume capable of at least 3000 IOPS.<br>Database storage consumption depends on your workload, including job frequency, playbook task count, output verbosity, and the number of managed hosts per job. Start with a 200 GB baseline and monitor actual usage after deployment. Configure automated cleanup jobs to prevent unbounded database growth.<br>These requirements ensure adequate database performance for the enterprise topology workload profile. |
| <br>**Metrics service database** | Database: `metrics_service`User: metrics database user with CREATEDB roleStorage: 40 GB minimum (plan for 100 GB with data growth)Connections: 100 connections minimum<br>Read-only access to `automationcontroller` database:<br>User: `ms_awx_readonly` with SELECT on all tables in public schemaRequires ALTER DEFAULT PRIVILEGES for future tables                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <br>AWS Memcached Service        | engine: "redis"engine\_version: "6.2"auto\_minor\_version\_upgrade: "false"node\_type: "cache.t3.micro"parameter\_group\_name: "default.redis6.x.cluster.on"transit\_encryption\_enabled: "true"num\_node\_groups: 2replicas\_per\_node\_group: 1automatic\_failover\_enabled: true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <br>s3 storage                   | <br>HTTPS only accessible through AWS Role assigned to automation hub SA at runtime by using AWS Pod Identity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <br>IP version                   | <br>IPv4, IPv6 (single-stack and dual-stack)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |


 Note:

**Minimum external database requirements**

The external database must meet these minimum requirements:

- 4 vCPUs
- 16 GB RAM
- `max_connections`: 1024 (minimum). You might need more connections when scaling replicas.
- 200 GB storage on a volume capable of at least 3000 IOPS.
- Support for 4 separate databases: `automationcontroller`, `automationhub`, `automationeda`, `metrics_service`
- Cross-database permissions: `metrics_service` database requires `ms_awx_readonly` user with SELECT privileges on `automationcontroller` database

Database storage consumption depends on your workload, including job frequency, playbook task count, output verbosity, and the number of managed hosts per job. Start with a 200 GB baseline and monitor actual usage after deployment. Configure automated cleanup jobs to prevent unbounded database growth. These requirements ensure adequate database performance for the enterprise topology workload profile.

## Example custom resource file

For example CR files, see the [ocp-b.env-a](https://github.com/ansible/test-topologies/blob/aap-2.5/ocp-b.env-a/README.md) directory in the `test-topologies` GitHub repository.

The following example shows an AnsibleAutomationPlatform custom resource configured for enterprise topology with external databases.

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: aap
  namespace: aap
spec:
  controller:
    postgres_configuration_secret: <controller-db-secret>

  hub:
    storage_type: s3
    object_storage_s3_secret: <s3-secret>

  eda:
    automation_server_ssl_verify: "no"

  metrics:
    database:
      database_secret: aap-metrics-postgres-configuration
      externally_managed: true
    ms_awx_readonly_user_secret: aap-metrics-read-token
    ms_awx_readonly_user:
      externally_managed: true
```

## Nonfunctional requirements

Ansible Automation Platform’s performance characteristics and capacity depend on its resource allocation and configuration. With OpenShift, each Ansible Automation Platform component deploys as a pod. You can specify resource requests and limits for each pod.

Use the Ansible Automation Platform custom resource to configure resource allocation for OpenShift installations. Each configurable item has default settings. These settings are the exact configuration used in this reference deployment architecture. This configuration assumes deployment and management by an Enterprise IT organization for production purposes.

By default, each component’s deployments use minimum resource requests but no resource limits. OpenShift only schedules pods with available resource requests. However, pods can consume unlimited RAM or CPU as long as the OpenShift worker node is not under node pressure.

In the Operator enterprise topology, Ansible Automation Platform runs on a Red Hat OpenShift on AWS (ROSA) Hosted Control Plane (HCP) cluster. The cluster has 2 t3.xlarge worker nodes spread across 2 AWS availability zones within a single region. This is not a shared environment so Ansible Automation Platform pods have full access to all compute resources of the ROSA HCP cluster.

The capacity calculation for automation controller task pods comes from the underlying HCP worker node running the pod. It does not have access to the CPU or memory resources of the entire node. This capacity calculation influences how many concurrent jobs automation controller can run.

OpenShift manages storage distinctly from VMs. This impacts how automation hub stores its artifacts. In the Operator enterprise topology, automation hub uses S3 storage. automation hub requires `ReadWriteMany` type storage, which is not a default storage type in OpenShift.

This topology specifies externally provided Redis, PostgreSQL, and object storage for automation hub. This provides additional scalability and reliability features for the Ansible Automation Platform deployment. These features include specialized backup, restore, and replication services, as well as scalable storage.

## Metrics service resource allocation

 Note:

Resource allocation can be configured in the AnsibleAutomationPlatform custom resource. If using external databases, configure database secrets before setting resource allocation.

In enterprise topology, metrics service runs as 3 pods with the following resource recommendations:

*Table 4. Metrics service resource allocation*

| Pod               | CPU Request | Memory Request | CPU Limit | Memory Limit | Replicas           |
| ----------------- | ----------- | -------------- | --------- | ------------ | ------------------ |
| metrics-web       | 500m        | 2 Gi           | 1000m     | 4 Gi         | 1-2                |
| metrics-tasks     | 500m        | 2 Gi           | 1000m     | 4 Gi         | 1                  |
| metrics-scheduler | 500m        | 2 Gi           | 1000m     | 4 Gi         | 1 (must not scale) |


**Scaling considerations:**

- **metrics-web pod:** Can be scaled to 2 replicas for high availability and load distribution
- **metrics-tasks pod:** Can not be scaled past 1 replica
- **metrics-scheduler pod:** Must remain at 1 replica to prevent duplicate scheduled tasks


Configure pod resource requests and limits in the AnsibleAutomationPlatform CR:

```
spec:
  metrics:
    disabled: false
    web:
      replicas: 2
      resource_requirements:
        requests:
          cpu: 500m
          memory: 2Gi
        limits:
          cpu: 1000m
          memory: 4Gi
    task:
      replicas: 2
      resource_requirements:
        requests:
          cpu: 500m
          memory: 2Gi
        limits:
          cpu: 1000m
          memory: 4Gi
    scheduler:
      replicas: 1  # Must be 1
      resource_requirements:
        requests:
          cpu: 100m
          memory: 512Mi
        limits:
          cpu: 200m
          memory: 1Gi
```


 Note:

For enterprise deployments, configure pod anti-affinity to spread metrics service pods across different worker nodes:

```
spec:
  metrics:
    web:
      topology_spread_constraints:
        - maxSkew: 1
          topologyKey: kubernetes.io/hostname
          whenUnsatisfiable: PreferNoSchedule
```

## Metrics service automatic provisioning

When you create an AnsibleAutomationPlatform custom resource with metrics service enabled, the operator automatically provisions:

**1. MetricsService custom resource**

- Defines the metrics service deployment (web, tasks, and scheduler pods)
- Configures database connection secrets
- Sets resource limits and replicas


**2. Database configuration**

- Reads customer-provided database secrets (external database scenario) or creates managed database credentials
- Creates Kubernetes Secrets for both database connections:
  * `<instance>`-automationmetricsservice-postgres-configuration - metrics service database
  * `<instance>`-automationmetricsservice-awx-postgres-configuration - automation controller read-only credentials
- Database connectivity is verified at pod start time by an init container in the web pod, which polls until `manage.py check --database default` succeeds. The AWX read-only connection is validated at application runtime, not during operator reconciliation.


**3. Service routing**

- Creates a Kubernetes Service (`<instance>`-automationmetricsservice-service) on port 8000, targeting the web pod on port 8080
- Registers the metrics service with the platform gateway (Envoy) at `/api/metrics/`, making the API accessible through the standard Ansible Automation Platform gateway URL


**4. Backup integration**

- Backup resources are not created automatically during provisioning. They are created on-demand when you trigger a backup by applying an AnsibleAutomationPlatformBackup custom resource. The operator then creates a MetricsServiceBackup CR, which provisions a PersistentVolumeClaim for backup staging and runs a `pg_dump` of the metrics database.


**Validation**

After operator reconciliation completes, verify metrics service provisioning:

```
# Check MetricsService CR status
oc get metricsservice -n <namespace>

# Verify all 3 pods are running
oc get pods -n <namespace> | grep automationmetricsservice
```
Expected output:

```
<aap-name>-automationmetricsservice-web-xxxxx         1/1  Running
<aap-name>-automationmetricsservice-tasks-xxxxx       1/1  Running
<aap-name>-automationmetricsservice-scheduler-xxxxx   1/1  Running
```

```
# Check web pod init container logs for database readiness
oc logs <aap-name>-automationmetricsservice-web-xxxxx -c wait-for-db -n <namespace>
# Should show: "Database is ready"

# Verify the service exists and is on the correct port
oc get svc -n <namespace> | grep automationmetricsservice
# Expected: <aap-name>-automationmetricsservice-service   ClusterIP   ...   8000/TCP
```

## Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 5. Network ports and protocols*

| Port number | Protocol       | Service            | Source                                   | Destination                                                                                     |
| ----------- | -------------- | ------------------ | ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| <br>80/443  | <br>HTTP/HTTPS | <br>Object storage | <br>OpenShift Container Platform cluster | <br>External object storage service                                                             |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor       | <br>Execution node                       | <br>OpenShift Container Platform ingress                                                        |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor       | <br>Hop node                             | <br>OpenShift Container Platform ingress                                                        |
| <br>5432    | <br>TCP        | <br>PostgreSQL     | <br>OpenShift Container Platform cluster | <br>External database service                                                                   |
| <br>5432    | <br>TCP        | <br>PostgreSQL     | <br>OpenShift Container Platform cluster | <br>External database service (`metrics_service` database)                                      |
| <br>5432    | <br>TCP        | <br>PostgreSQL     | <br>OpenShift Container Platform cluster | <br>External database service (`automationcontroller` database - read-only for metrics service) |
| <br>6379    | <br>TCP        | <br>Redis          | <br>OpenShift Container Platform cluster | <br>External Redis service                                                                      |
| <br>27199   | <br>TCP        | <br>Receptor       | <br>OpenShift Container Platform cluster | <br>Execution node                                                                              |
| <br>27199   | <br>TCP        | <br>Receptor       | <br>OpenShift Container Platform cluster | <br>Hop node                                                                                    |


 Note:

Metrics service pods communicate internally within the OpenShift cluster via the platform gateway. The `/api/metrics/` path is routed through the standard Ansible Automation Platform gateway and does not require a separate external ingress. Metrics service requires outbound connectivity on port 5432 to both the `metrics_service` database and the `automationcontroller` database (read-only).
