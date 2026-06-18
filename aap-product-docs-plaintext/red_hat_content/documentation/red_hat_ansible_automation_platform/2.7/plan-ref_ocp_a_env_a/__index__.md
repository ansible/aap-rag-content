# Operator growth topology

The Operator-based growth topology provides a smaller footprint deployment without redundancy for organizations getting started with Ansible Automation Platform on Red Hat OpenShift Container Platform.

Included are the tested infrastructure topology, system requirements, network port configurations, and an example custom resource file for installation.

Important:

You can only install a single instance of the Ansible Automation Platform Operator into a single namespace. Installing multiple instances in the same namespace can lead to improper operation for both Operator instances.

## Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

*Figure 1. Infrastructure topology diagram*
![Operator growth topology diagram](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ocp-a-env-a-2_7.png)

Important:

While Redis and PostgreSQL can be installed as part of the operator-based installation process, the topology diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.

Red Hat tests a Single Node OpenShift (SNO) cluster with these requirements:

*Table 1. Single Node OpenShift (SNO) cluster requirements*

| Requirement | Minimum requirement |
| ----------- | ------------------- |
| RAM         | 32 GB               |
| CPUs        | 16                  |
| Local disk  | 128 GB              |
| Disk IOPS   | 3000                |

*Table 2. Infrastructure topology components*

| Count | Component                                      |
| ----- | ---------------------------------------------- |
| <br>1 | <br>Automation controller web pod              |
| <br>1 | <br>Automation controller task pod             |
| <br>1 | <br>Automation hub web pod                     |
| <br>1 | <br>Automation hub API pod                     |
| <br>2 | <br>Automation hub content pod                 |
| <br>2 | <br>Automation hub worker pod                  |
| <br>1 | <br>Automation hub Redis pod                   |
| <br>1 | <br>Metrics service web pod                    |
| <br>1 | <br>Metrics service tasks pod                  |
| <br>1 | <br>Metrics service scheduler pod              |
| <br>1 | <br>Event-Driven Ansible API pod               |
| <br>1 | <br>Event-Driven Ansible activation worker pod |
| <br>1 | <br>Event-Driven Ansible default worker pod    |
| <br>1 | <br>Event-Driven Ansible event stream pod      |
| <br>1 | <br>Event-Driven Ansible scheduler pod         |
| <br>1 | <br>Platform gateway pod                       |
| <br>1 | <br>Database pod                               |
| <br>1 | <br>Redis pod                                  |


Note:

Metrics service is deployed automatically when the AnsibleAutomationPlatform Custom Resource (CR) includes metrics configuration. The operator creates a MetricsService CR (named `<aap-name>`-metrics) and manages three pods:

- `<aap-name>`- **metrics-web** - REST API for metrics and dashboard data
- `<aap-name>`- **metrics-tasks** - dispatcherd worker for background data collection
- `<aap-name>`- **metrics-scheduler** - APScheduler for periodic collection tasks (6-hourly schedule)


All database provisioning, secrets management, and routing configuration is handled automatically by the operators.

Note:

You can deploy multiple isolated instances of Ansible Automation Platform into the same Red Hat OpenShift Container Platform cluster. To do this, use a namespace-scoped deployment model (isolated within a namespace).

This approach allows you to use the same cluster for several deployments.

## Tested system configurations

Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:

*Table 3. Tested system configurations*

| Type                  | Description                                                                                                                           | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription      | <br>Valid Red Hat Ansible Automation Platform subscription                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <br>Red Hat OpenShift | `Version`: 4.14`num_of_control_nodes`: 1`num_of_worker_nodes`: 1                                                                      | <br>Single Node OpenShift (SNO) tested with 32 GB RAM, 16 CPUs, 128 GB disk. Metrics service adds approximately 3.5 Gi RAM request (7 Gi limit).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <br>Ansible-core      | <br>Ansible-core version 2.16 or later                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <br>Browser           | <br>A currently supported version of Mozilla Firefox or Google Chrome.                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <br>Database          | For Ansible Automation Platform managed databases: PostgreSQL 15For customer provided (external) databases: PostgreSQL 15, 16, or 17. | External (customer supported) databases require International Components for Unicode (ICU) support.External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality depends on utilities provided with PostgreSQL 15.       Warning:   <br>Operator-deployed database connection limits<br>The operator-deployed PostgreSQL database has a default `max_connections` limit of 100 and a maximum database size of 100 GB.<br>Do not use the operator-deployed database if any of the following conditions apply:   <br>You are running more than 1 replica of any component (platform gateway, automation controller, automation hub, Event-Driven Ansible, or metrics service).The automation controller capacity exceeds 100 concurrent jobs.Total database connections from all components exceed 100.Estimated 30-day database storage exceeds 100 GB.<br>If your deployment exceeds any of these limits, use an external database instead of the operator-deployed database.<br>Database storage consumption depends on your workload, including job frequency, playbook task count, output verbosity, and the number of managed hosts per job. Higher verbosity levels can increase storage consumption by 3-5x. |
| <br>IP version        | <br>IPv4, IPv6 (single-stack and dual-stack)                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Example custom resource file

Use this example custom resource (CR) to add your Ansible Automation Platform instance to your project:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: <aap instance name>
spec:
eda:
automation_server_ssl_verify: 'no'
hub:
storage_type: 's3'
object_storage_s3_secret: '<name of the Secret resource holding s3 configuration>'
metrics:
disabled: false
```

## Metrics service configuration

`spec.metrics.disabled: false` - Enables metrics service deployment (default: false, meaning enabled)

- Setting `disabled: true` will prevent metrics service deployment
- The operator automatically creates a MetricsService CR named `<aap-name>`-metrics

## Metrics service automatic provisioning

The operator handles all metrics service deployment details automatically:

**Database provisioning**

The operator automatically creates:

- `metrics_service` database with full permissions for the `metrics_service` user
- `ms_awx_readonly` user in the automation controller database with SELECT-only permissions
- All database connection secrets as Kubernetes secrets


No manual database setup required for operator deployments with managed databases.

**Secrets management**

The operator creates and manages these Kubernetes secrets:

- `<aap-name>`- `automationmetrics-pg-password` - Metrics database credentials
- `<aap-name>`- `automationmetrics-controller-read-pg-password` - Read-only controller database credentials
- `<aap-name>`- `automationmetrics-secret-key` - Django secret key
- `<aap-name>`- `automationmetrics-resource-server` - Resource server configuration


**Gateway routing**

The operator configures Envoy routing through platform gateway:

- Dashboard requests route to `/api/metrics/` endpoint
- Internal communication between gateway and metrics service web pod
- No external exposure of metrics service (access only through gateway)


**ConfigMap**

Configuration is managed via ConfigMap:

- `<aap-name>`- `metrics-env-properties` - Contains all metrics service environment variables including feature flags

## External database configuration

When using an external database (not operator-managed), you must manually provision the metrics service databases before deployment.

**Create metrics_service database:**

```
CREATE DATABASE metrics_service
WITH ENCODING='UTF8'
LC_COLLATE='en_US.UTF-8'
LC_CTYPE='en_US.UTF-8'
TEMPLATE=template0;

CREATE USER metrics_service WITH PASSWORD '<secure_password>';
GRANT ALL PRIVILEGES ON DATABASE metrics_service TO metrics_service;
\c metrics_service
GRANT ALL ON SCHEMA public TO metrics_service;
```
**Create read-only user for controller database:**

```
CREATE USER ms_awx_readonly WITH PASSWORD '<readonly_password>';
\c awx  -- Connect to controller database
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ms_awx_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO ms_awx_readonly;
```
**Configure external database in CR:**

```
spec:
metrics:
disabled: false
postgres_configuration_secret: <secret-name-with-db-credentials>
```

## Nonfunctional requirements

Ansible Automation Platform’s performance characteristics and capacity depend on its resource allocation and configuration. With OpenShift, each Ansible Automation Platform component deploys as a pod. You can specify resource requests and limits for each pod.

Use the Ansible Automation Platform Custom Resource (CR) to configure resource allocation for OpenShift installations. Each configurable item has default settings. These settings are the minimum requirements for an installation, but might not meet your production workload needs.

By default, each component’s deployments use minimum resource requests but no resource limits. OpenShift only schedules pods with available resource requests, but the pods can consume unlimited RAM or CPU as long as the OpenShift worker node itself is not under node pressure.

In the Operator growth topology, Ansible Automation Platform runs on a Single Node OpenShift (SNO) with 32 GB RAM, 16 CPUs, 128 GB local disk, and 3000 IOPS. This is not a shared environment, so Ansible Automation Platform pods have full access to all of the compute resources of the OpenShift SNO. In this scenario, the capacity calculation for automation controller task pods comes from the underlying OpenShift Container Platform node that runs the pod. It does not have access to the entire node. This capacity calculation influences how many concurrent jobs automation controller can run.

OpenShift manages storage distinctly from VMs. This impacts how automation hub stores its artifacts. In the Operator growth topology, the topology uses S3 storage because automation hub requires a `ReadWriteMany` type storage, which is not a default storage type in OpenShift.

## Network ports

Red Hat Ansible Automation Platform uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.

*Table 4. Network ports and protocols*

| Port number | Protocol       | Service      | Source                                   | Destination                              |
| ----------- | -------------- | ------------ | ---------------------------------------- | ---------------------------------------- |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor | <br>Execution node                       | <br>OpenShift Container Platform ingress |
| <br>80/443  | <br>HTTP/HTTPS | <br>Receptor | <br>Hop node                             | <br>OpenShift Container Platform ingress |
| <br>80/443  | <br>HTTP/HTTPS | <br>Platform | <br>Customer clients                     | <br>OpenShift Container Platform ingress |
| <br>27199   | <br>TCP        | <br>Receptor | <br>OpenShift Container Platform cluster | <br>Execution node                       |
| <br>27199   | <br>TCP        | <br>Receptor | <br>OpenShift Container Platform cluster | <br>Hop node                             |


Note:

Metrics service communication in operator deployments:

- Platform gateway routes dashboard requests to metrics service via internal Kubernetes service
- Metrics service connects to PostgreSQL via Kubernetes service (port 5432)
- All communication is internal to the OpenShift cluster
- No additional external ports required for metrics service
