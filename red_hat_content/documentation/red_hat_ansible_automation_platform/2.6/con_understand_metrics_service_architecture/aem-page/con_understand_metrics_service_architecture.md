+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/con_understand_metrics_service_architecture"
template = "docs/aem-title.html"
title = "Understand metrics service architecture - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/con_understand_metrics_service_architecture/aem-page/con_understand_metrics_service_architecture.html"
last_crumb = "Understand metrics service architecture"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Understand metrics service architecture"
oversized = "false"
page_slug = "con_understand_metrics_service_architecture"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/con_understand_metrics_service_architecture"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/con_understand_metrics_service_architecture/toc/toc.json"
type = "aem-page"
+++

# Understand metrics service architecture

Learn the architectural components and deployment topology of metrics service to make informed infrastructure decisions and ensure successful integration with Ansible Automation Platform.

## Metrics service overview

Metrics service is a Django-based application component of Ansible Automation Platform 2.7. It collects anonymized usage and performance data from your automation controller. The service runs as containerized workloads managed by either systemd (containerized installer) or Kubernetes (operator). It maintains its own PostgreSQL database and read-only access to the controller database.

## Default behavior in Ansible Automation Platform 2.7

Metrics service is enabled by default in Ansible Automation Platform 2.7 for both operator-based (OpenShift) and containerized installations that include automation controller. It is deployed automatically as a required component when you install automation controller.

- **Containerized installations:** [automationmetrics] inventory group is required when installing Ansible Automation Platform if automationcontroller is present in the inventory file
- **Operator installations:** Enabled when `metrics.disabled: false` is set in the AnsibleAutomationPlatform custom resource

## Key characteristics

- **Django-based application:** Built on Django framework with database migrations managed through /app/scripts/init.sh
- **Containerized deployment:** Runs as three containers (`automation-metrics-web`, `automation-metrics-tasks`, `automation-metrics-scheduler`) managed by systemd (containerized installer) or Kubernetes (operator)
- **Automatic anonymization:** Customer-defined object names are replaced with "Custom" before transmission. Only built-in object names and publicly available collection names are sent in their original form
- **Auto-configured ingress:** Establishes secure connection to Red Hat Data Ingress without manual setup
- **Read-only access:** Accesses automation controller database in read-only mode to prevent operational impact
- **Isolated database:** Maintains its own `metrics_service` database for metrics processing and storage
- **Health monitoring:** Provides health check endpoint (returns `"status": "good"` when healthy)
- **HTTP proxy support:** Supports HTTP/HTTPS proxy configuration for environments without direct internet access
- **Startup validation:** Validates required production environment variables at startup. Containers exit immediately with validation errors if required variables are missing or invalid
- **Deployment flexibility:** Supports both RHEL-based containerized deployments and OpenShift operator-based deployments with different configuration approaches

## Relationship to automation dashboard

Metrics service serves as the unified backend for automation dashboard, a Technology Preview feature in Ansible Automation Platform 2.7. When dashboard collection is enabled (`FEATURE_DASHBOARD_COLLECTION_ENABLED: true`), metrics service collects additional dashboard-specific metrics, including:

- Cost and pricing data for ROI calculations
- Automation savings metrics
- Executive reporting data


Dashboard collection is disabled by default and must be enabled separately. Dashboard collection runs on a 6-hourly schedule to minimize database impact.

## Dashboard collection feature flag

Automation dashboard data collection is controlled by the `FEATURE_DASHBOARD_COLLECTION_ENABLED` feature flag. This is an official Ansible Automation Platform feature flag that customers can configure during installation or post-installation.

**Default:** `false` (dashboard collection disabled)

**Purpose:** When enabled, metrics service collects additional dashboard-specific metrics (cost data, ROI calculations, pricing information) in addition to standard anonymized metrics.

## Architecture components

*Figure 1. Metrics service overall system architecture*
![Overall system architecture diagram for metrics service](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/metrics-service-system-architecture.png)

**Core components**

| Component                                          | Container Name                 | Purpose                                                                                                                                                                                                                    |
| -------------------------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Metrics service (web)**                          | `automation-metrics-web`       | Nginx reverse proxy + Gunicorn serving the Django application. Internal Gunicorn port: 8006. External via nginx: 8087 (HTTP) / 8450 (HTTPS). Health endpoint:/health/ (returns HTTP 2\*\* for healthy, 50\* for unhealthy) |
| **Metrics service (tasks)**                        | `automation-metrics-tasks`     | Dispatcherd async task worker for background job execution                                                                                                                                                                 |
| **Metrics service (scheduler)**                    | `automation-metrics-scheduler` | APScheduler process that triggers periodic data collection tasks                                                                                                                                                           |
| **Init container**                                 | `automation-metrics-init`      | One-shot container that runs Django database migrations and system initialization via/app/scripts/init.sh. Exits on completion.                                                                                            |
| **metrics\_service database**                      | PostgreSQL database            | Stores processed metrics data and configuration. Created with user`metrics_service` (ALL privileges)                                                                                                                       |
| **awx/automation controller database (read-only)** | PostgreSQL database            | Source of automation controller usage data. Accessed via user`ms_awx_readonly` (SELECT-only privileges on all tables in schema)                                                                                            |
| **Red Hat Data Ingress**                           | External endpoint              | Receives anonymized data from customer environments via Segment write key. Data flows through Gateway/api/metrics/ endpoint (no direct customer-facing endpoints in 2.7 GA)                                                |


**Database architecture**

| Database                      | User              | Privileges                            | Purpose                                                            |
| ----------------------------- | ----------------- | ------------------------------------- | ------------------------------------------------------------------ |
| `metrics_service`             | `metrics_service` | ALL                                   | Metrics service own data storage, schema migrations, configuration |
| **awx/automation controller** | `ms_awx_readonly` | SELECT ON ALL TABLES IN SCHEMA public | Read-only access to controller data for metrics collection         |


 Note:

The two-database model ensures metrics service cannot modify controller data. The `ms_awx_readonly` user has only SELECT privileges on the **awx/automation controller** database, preventing any writes to automation controller tables.

 Note:

When `FEATURE_DASHBOARD_COLLECTION_ENABLED: true`, the `metrics_service` database includes additional tables from apps/dashboard_reports/migrations/ for dashboard-specific data. These tables are created automatically during database migration if the feature flag is enabled.

## Database schema architecture

*Figure 2. Metrics service database scheme architecture*
![Architectural diagram for metrics service database schema (simplified)](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/metrics-service-simplified-schema.png)

**Collection phase**

1. Metrics service queries automation controller/`awx` database (read-only connection using `ms_awx_readonly` user)
2. Raw usage data extracted from the following tables: jobs, job host summaries, credentials, execution environments, controller versions, and feature flags


**What is NOT collected:**

- Event data
- Host inventory data
- Customer-defined template names, playbook names, or workflow names


 Important:

Host and inventory data collection is handled separately by the metrics-utility CLI for CCSP reports only. Metrics service does not collect this data.

## Complete task schedule

*Figure 3. Task system module*
![Architectural diagram for metrics service and automation dashboard task system module](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/automation-dashboard-task-system-module.png)

Metrics service uses three task groups controlled by feature flags:

**METRICS_COLLECTION group**

Gated by `METRICS_COLLECTION` feature flag (default: `true`). When disabled, all tasks in this group skip execution.

| Task                                                 | Schedule            | Description                                                 |
| ---------------------------------------------------- | ------------------- | ----------------------------------------------------------- |
| `collect_hourly_metrics` (job\_host\_summary)        | Every hour at XX:05 | Collects job host summary metrics from controller database  |
| `collect_hourly_metrics` (unified\_jobs)             | Every hour at XX:10 | Collects unified jobs metrics from controller database      |
| `collect_hourly_metrics` (credentials)               | Every hour at XX:15 | Collects credentials usage metrics from controller database |
| `collect_snapshot_metrics` (execution\_environments) | Daily at 1:00 AM    | Snapshot of execution environment configuration             |
| `collect_snapshot_metrics` (config)                  | Daily at 1:30 AM    | Snapshot of system configuration                            |
| `collect_snapshot_metrics` (controller\_version)     | Daily at 1:35 AM    | Snapshot of controller version information                  |
| `collect_snapshot_metrics` (table\_metadata)         | Daily at 1:40 AM    | Snapshot of database table metadata                         |
| `collect_snapshot_metrics` (feature\_flags)          | Daily at 1:45 AM    | Snapshot of feature flag states                             |
| `collect_daily_metrics` (task\_executions)           | Daily at 1:50 AM    | Pipeline health metrics (task execution observability)      |
| `daily_metrics_rollup`                               | Daily at 2:00 AM    | Aggregates hourly data into daily summaries                 |
| `cleanup_metrics_data`                               | Daily at 4:00 AM    | Purges expired data based on retention policies             |


**ANONYMIZATION group**

Gated by `ANONYMIZED_DATA_COLLECTION` feature flag (default: `true`). When disabled, anonymization and transmission skip execution.

| Task                          | Schedule         | Description                                            |
| ----------------------------- | ---------------- | ------------------------------------------------------ |
| `daily_anonymize_and_prepare` | Daily at 3:00 AM | Anonymizes collected data and transmits to Segment.com |


**SYSTEM group**

Always enabled regardless of feature flag state. System maintenance tasks continue even when all collection is disabled.

| Task                | Schedule         | Description                                     |
| ------------------- | ---------------- | ----------------------------------------------- |
| `cleanup_old_tasks` | Daily at 5:00 AM | Purges old task execution records from database |
| `hello_world`       | Every hour       | Health check heartbeat for monitoring           |


**Task dependencies**

Tasks are scheduled in dependency order:

1. **Hourly collection** (XX:05, XX:10, XX:15) - provides raw data
2. **Daily snapshots** (1:00 AM - 1:50 AM) - supplements hourly data
3. **Daily rollup** (2:00 AM) - aggregates hourly data (depends on hourly collectors completing)
4. **Anonymization** (3:00 AM) - anonymizes aggregated data (depends on rollup completing)
5. **Cleanup** (4:00 AM, 5:00 AM) - purges old data (runs after rollup/anonymization to avoid race conditions)


 Important:

If hourly collectors fail, daily rollup will have incomplete data. Always verify hourly collection completed before troubleshooting rollup issues.

 Note:

To ensure the readonly user can access tables created in the future, we recommend setting the following default privileges: `ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO ms_awx_readonly;`

## Anonymization phase

No personal data leaves the customer environment. Only publicly available collection names (for example from Galaxy) and built-in object names (such as built-in credential types and execution environments) are transmitted.

**Anonymization method:** Statistics and counts only

Metrics service transmits only aggregated statistics, counts, and built-in/public object names. Customer-defined object names are never transmitted. For example, if you have 3 custom credentials, metrics service sends the count "3" but does not send the credential names.

**What data is sent:**

- **Job statistics:** Aggregated job execution data grouped by job type, launch type, and version (success/failure counts, duration statistics, timestamps). Job template names are NOT included.
- **Job host summary statistics:** Aggregated job execution results per host (success/failure counts, execution performance metrics).
- **Credential type statistics:** Built-in credential type names (e.g., "Machine", "Source Control", "Vault") and count of customer-defined credentials (e.g., "3 custom credentials"). Customer-defined credential names are NOT sent.
- **Execution environment statistics:** Built-in EE names (e.g., "ee-minimal-rhel9", "ee-supported-rhel9") and count of customer-defined EEs (e.g., "5 custom EEs"). Customer-defined EE names are NOT sent.
- **Collection statistics:** Public collection names from Galaxy or Red Hat Certified Collections (e.g., "ansible.builtin", "ansible.posix") and count of customer-defined collections. Customer-defined collection names are NOT sent.
- **Project SCM types:** Source control management types for projects (e.g., Git, SVN).
- **Organization counts:** Total number of organizations configured.
- **Version information:** Controller version, Ansible core version, installed collection versions.
- **Warnings and deprecations:** Statistics on deprecation warnings encountered.
- **Feature flag states:** Boolean status of enabled/disabled feature flags.


**What data is NOT sent:**

- **Job template names** (not collected at all)
- **Customer-defined credential names** (only counts transmitted, e.g., "3 custom credentials")
- **Customer-defined execution environment names** (only counts transmitted, e.g., "5 custom EEs")
- **Customer-defined collection names** (only counts transmitted)
- **Event data** (removed from metrics service in February 2026)
- **Host inventory data** (not queried by metrics service; handled separately by metrics-utility CLI for CCSP reports only)
- **Playbook names** (customer-defined content)
- **Variable names and values** (customer-defined content)
- **Workflow template names** (customer-defined content)


 Important:

Customer-defined object names are never transmitted. Metrics service sends only counts (e.g., "3 custom credentials") and statistics (e.g., "50 jobs executed"). There is no way to identify which specific custom objects belong to which customer, and no individual object names can be recovered from the transmitted data.

## Transmission phase

1. Anonymized data packaged for transmission
2. Secure HTTPS connection established to Red Hat Data Ingress endpoint using **Segment** (a third-party data pipeline service)
3. Data transmitted through the Gateway /api/metrics/ endpoint (no direct customer-facing endpoints in 2.7 GA)
4. Transmission status logged in `metrics_service` database
5. HTTP/HTTPS proxy supported for environments without direct internet access


 Note:

Segment is a third-party data pipeline service that securely routes anonymized metrics from your environment to Red Hat analytics infrastructure. The Segment write key is pre-configured during installation.

**Message size handling**

Metrics service splits anonymized data deterministically into separate messages. If any message exceeds 32 KB, the service splits it further. This ensures reliable transmission of large datasets without message size errors.

## Deployment topology options

**AIO Growth (All-in-One) topology**

A single host runs all Ansible Automation Platform components, including metrics service. The `[automationmetrics]` inventory group points to the same host as `[automationcontroller]`.

Characteristics:

- All components share the same host
- Simplest deployment for small to medium environments
- Metrics service, controller, and databases on one node
- Suitable for development, testing, or small production environments


**Enterprise / Multi-Node topology**

Metrics service runs on a dedicated node or alongside Gateway. Key design decision: metrics service is NOT required to be co-located with automation controller. You define which node hosts metrics service by using the `[automationmetrics]` inventory group.

Characteristics:

- Flexible topology: metrics service can run on any node
- Scaled independently from controller
- Metrics processing isolated from automation execution
- Suitable for large-scale production environments

## Deployment method comparison

Metrics service supports two deployment methods with different configuration complexity and automation levels:

| Aspect                       | Containerized Installer                                                      | Operator (OpenShift)                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Deployment method**        | Ansible role (`automationmetrics`) in containerized installation program     | Kubernetes operator (`automation-metrics-operator`) managed by AAP gateway operator        |
| **Configuration complexity** | Manual: requires inventory file edits, database passwords, network variables | Automatic: single CR field (`metrics.disabled: false`)                                     |
| **Database provisioning**    | Administrator provisions databases and configures credentials in inventory   | Operator automatically provisions databases and manages credentials via Kubernetes secrets |
| **Container management**     | Podman with systemd user-scope units                                         | Kubernetes deployments managed by operator                                                 |
| **Network configuration**    | Manual firewall rules, port configuration in inventory                       | Automatic Kubernetes services and Envoy routing through gateway                            |
| **OAuth integration**        | Manual configuration if needed                                               | Automatic integration with platform gateway OAuth                                          |
| **Upgrades**                 | Re-run installer with updated inventory                                      | Operator handles upgrades automatically via CR updates                                     |
| **Backup/restore**           | Manual playbook execution                                                    | Operator-managed backup/restore via AutomationMetricsBackup CR (when available)            |


 Tip:

For OpenShift deployments, use the operator method for simplified configuration and automatic lifecycle management. For RHEL-based containerized deployments, use the containerized installer method.

## Containerized installer deployment details

Metrics service is deployed through the `automationmetrics` Ansible role included in the Ansible Automation Platform 2.7 containerized installation program:

- **Container runtime:** Podman with host networking mode (rootless, user namespace)
- **Service management:** Three systemd user-scope units: `automation-metrics-web.service`, `automation-metrics-tasks.service`, `automation-metrics-scheduler.service`
- **Data persistence:** Host volumes mounted from `{{ aap_volumes_dir }}/automationmetrics` into container path /var/lib/ansible-automation-platform/metrics
- **Secrets management:** Four Podman secrets: `automationmetrics_pg_password`, `automationmetrics_controller_read_pg_password`, `automationmetrics_secret_key`, `automationmetrics_resource_server`
- **Firewall integration:** Ports 8087/tcp (HTTP) and 8450/tcp (HTTPS) opened in configured firewall zone (default: public)


**Configuration requirements:**

- Hosts must be added to `[automationmetrics]` inventory group
- Database connection variables must be configured (`automationmetrics_pg_host`, `automationmetrics_pg_password`, etc.)
- Read-only controller database user must be provisioned manually or by installer
- Segment write key must be provided for data transmission

## Operator-based deployment details

Metrics service is deployed through the `automation-metrics-operator` running on OpenShift. The AAP gateway operator manages the metrics operator lifecycle:

- **Container runtime:** Kubernetes pods managed by operator deployments
- **Service management:** Three Kubernetes deployments: `metrics-api`, `metrics-tasks`, `metrics-scheduler`
- **Data persistence:** Kubernetes persistent volumes managed by operator
- **Secrets management:** Kubernetes secrets automatically created and managed by operator (database credentials, OAuth tokens, Segment write key)
- **Network integration:** Kubernetes services and Envoy routing through platform gateway
- **Database provisioning:** Operator automatically creates and configures both `metrics_service` database and read-only controller database user


**Configuration simplicity:**

- Single CR field: `spec.metrics.disabled: false` in AnsibleAutomationPlatform CR
- Zero manual database configuration required
- Zero manual network configuration required
- Automatic OAuth integration with platform gateway
- Operator handles all credential rotation and secret management


**Operator-managed resources:**

- **MetricsService CR:** Created as `<aap-name>-automationmetricsservice` in same namespace as AnsibleAutomationPlatform CR
- **Database:** PostgreSQL database for metrics service, automatically provisioned with credentials stored in Kubernetes secrets
- **Read-only user:** Automatically created in controller database with SELECT privileges
- **Services:** Kubernetes Service resources for metrics API, tasks, and scheduler pods
- **Routes/Ingress:** Traffic routing through platform gateway Envoy proxy (no direct external endpoints)


 Important:

In AAP 2.7, the operator removes ownerReferences from the MetricsService CR. This means the CR is not automatically deleted when you set `metrics.disabled: true`. You must manually delete the CR if you want to fully remove metrics service from your cluster.

 Note:

In standard operator deployments, database provisioning is fully automatic. The operator creates all required databases and users. This includes the metrics service database and the read-only user for the controller database.

**Externally managed databases:** If you use a fully externally managed database such as RDS or Cloud SQL, you must manually provision databases and configure credentials before deploying metrics service. See the related information for external database configuration procedures.

## Network architecture

**Required network connectivity**

| Source                                                                | Destination                        | Protocol/Port     | Purpose                                                          |
| --------------------------------------------------------------------- | ---------------------------------- | ----------------- | ---------------------------------------------------------------- |
| `automation-metrics-tasks` /`automation-metrics-scheduler` containers | Automation controller database     | PostgreSQL (5432) | Read-only data collection via`ms_awx_readonly` user              |
| `automation-metrics-tasks` /`automation-metrics-scheduler` containers | `metrics_service` database         | PostgreSQL (5432) | Read-write metrics storage via`metrics_service` user             |
| `automation-metrics-tasks` container                                  | Red Hat Data Ingress (via Segment) | HTTPS (443)       | Anonymized data transmission authenticated via Segment write key |
| Monitoring systems (optional)                                         | `automation-metrics-web` container | HTTP (8087)       | Health check endpoint at/health/ via nginx                       |


**Firewall requirements**

- **Protocol:** HTTPS (TLS 1.2 or higher); supported TLS versions: TLSv1.2, TLSv1.3
- **Direction:** Outbound from metrics service container to Red Hat Data Ingress
- **Nginx ports:** 8087/tcp (HTTP) and 8450/tcp (HTTPS) opened in firewall (default zone: public)
- **Internal Gunicorn port:** 8006 (localhost only, not opened in firewall)
- **Proxy support:** HTTP/HTTPS proxy configuration supported via standard environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`)

## Naming conventions

| Element                  | Value                                        |
| ------------------------ | -------------------------------------------- |
| Role name                | `automationmetrics`                          |
| Inventory group          | `[automationmetrics]`                        |
| Web container            | `automation-metrics-web`                     |
| Tasks container          | `automation-metrics-tasks`                   |
| Scheduler container      | `automation-metrics-scheduler`               |
| Init container           | `automation-metrics-init`                    |
| Variable prefix          | `automationmetrics_`                         |
| Gunicorn port (internal) | `8006` (localhost only)                      |
| Nginx HTTP port          | `8087`                                       |
| Nginx HTTPS port         | `8450`                                       |
| Health endpoint          | http://localhost:8087/health/                |
| Host volume path         | `{{ aap_volumes_dir }}/automationmetrics`    |
| Container data path      | /var/lib/ansible-automation-platform/metrics |
