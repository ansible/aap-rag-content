+++
title = "Metrics service deployment requirements - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_metrics_service_deployment_requirements"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_understand_metrics_service_architecture/", "Understand metrics service architecture"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_metrics_service_deployment_requirements/aem-page/install-ref_metrics_service_deployment_requirements.html"
last_crumb = "Metrics service deployment requirements"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Metrics service deployment requirements"
oversized = "false"
page_slug = "install-ref_metrics_service_deployment_requirements"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_metrics_service_deployment_requirements"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_metrics_service_deployment_requirements/toc/toc.json"
type = "aem-page"
+++

# Metrics service deployment requirements

Review infrastructure requirements and prerequisites for deploying metrics service to provision appropriate resources and ensure successful deployment without capacity or compatibility issues.

## System requirements

**Supported platforms**

| Platform                        | Versions           | Notes                                                                                                                     |
| ------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **Red Hat Enterprise Linux**    | **9.2 or later**   | Required for containerized installer deployment.**RHEL 8 is NOT supported** (Ansible Automation Platform 2.7 requirement) |
| **Podman**                      | **4.6.0 or later** | Container runtime for metrics service                                                                                     |
| **PostgreSQL**                  | **15 or later**    | For`metrics_service` database and**awx/automation controller** database                                                   |
| **Ansible Automation Platform** | **2.7.0 or later** | Metrics service integrated with Ansible Automation Platform 2.7 containerized installer                                   |


Important:

Metrics service does not support RHEL 8. All Ansible Automation Platform 2.7 deployments require RHEL 9.2 or later.

**Data retention periods**

| Data Category       | Description                                                                                   | Retention Period                                                               | Cleanup Schedule      |
| ------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------- |
| Hourly metrics      | Raw metrics collected hourly from controller                                                  | 7 days                                                                         | Daily at 4:00-5:30 AM |
| Daily summaries     | Aggregated daily metrics                                                                      | 30 days                                                                        | Daily at 4:00-5:30 AM |
| Anonymized payloads | Anonymized data sent to Red Hat Data Ingress                                                  | 7 days (after successful transmission) / 30 days (unsent/pending transmission) | Daily at 4:00-5:30 AM |
| Dashboard data      | Job execution data for dashboard reporting (when`FEATURE_DASHBOARD_COLLECTION_ENABLED: true`) | 90 days                                                                        | Daily at 5:30 AM      |


Note:

Cleanup tasks run automatically daily at 4:00 AM to enforce retention policies.

## Hardware requirements

metrics service hardware requirements are the same as Gateway specifications:

| Component               | Minimum                                         | Recommended                                     | Notes                                                        |
| ----------------------- | ----------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| **CPU**                 | **2 vCPUs**                                     | **4 vCPUs**                                     | Dedicated to metrics service container                       |
| **RAM**                 | **4 GB**                                        | **8 GB**                                        | For metrics processing and database operations               |
| **Storage (database)**  | **20 GB**                                       | **40 GB+ (SSD preferred)**                      | For metrics\_service database; grows based on data retention |
| **Storage (container)** | Included in database storage                    | Included in database storage                    | For container images and temporary processing                |
| **Network bandwidth**   | Standard Ansible Automation Platform networking | Standard Ansible Automation Platform networking | For data transmission to Red Hat Data Ingress via Gateway    |


Note:

Metrics service is not required to be co-located with automation controller. It can run on any node defined in the `[automationmetrics]` inventory group. Hardware requirements can be shared (AIO Growth topology) or dedicated (Enterprise Multi-Node topology).

**Filesystem requirements**

| Path                                      | Purpose                                                                                       | Minimum Size                      |
| ----------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------- |
| /var/lib/containers                       | Container images and storage                                                                  | 10 GB (part of overall storage)   |
| `{{ aap_volumes_dir }}/automationmetrics` | Host-side volume mount (maps to/var/lib/ansible-automation-platform/metrics inside container) | 5 GB (part of overall storage)    |
| /var/lib/postgresql (or custom path)      | PostgreSQL data directory for metrics\_service database                                       | 20 GB minimum, 40 GB+ recommended |

## Network requirements

| Connection                                  | Protocol   | Port           | Direction | Purpose                                                 |
| ------------------------------------------- | ---------- | -------------- | --------- | ------------------------------------------------------- |
| metrics service → Controller database       | PostgreSQL | 5432 (default) | Outbound  | Read-only data collection                               |
| metrics service → metrics\_service database | PostgreSQL | 5432 (default) | Outbound  | Metrics storage and retrieval                           |
| metrics service → Gateway                   | HTTPS      | 443            | Outbound  | Anonymized data transmission to`/api/metrics/` endpoint |
| Monitoring → metrics service (optional)     | HTTP       | 8087           | Inbound   | Health check endpoint at`/health/` via nginx            |


**Proxy Support:** metrics service supports HTTP/HTTPS proxy configuration via standard environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`).

## Database requirements

| Database                      | User              | Privileges                                      | Purpose                                                                  |
| ----------------------------- | ----------------- | ----------------------------------------------- | ------------------------------------------------------------------------ |
| `metrics_service`             | `metrics_service` | ALL                                             | metrics service's own data storage, Django migrations, schema management |
| **awx/automation controller** | `ms_awx_readonly` | **GRANT SELECT ON ALL TABLES IN SCHEMA public** | Read-only access to controller data for metrics collection               |


**PostgreSQL Version:** 15 or later (both databases)

Note:

The `ms_awx_readonly` user requires SELECT privileges on all tables in the public schema of the **awx/automation controller** database. This is configured automatically by the installer.

## Performance impact and capacity planning

**Validated performance characteristics**

Metrics service is designed for minimal impact on automation controller operations:

| Metric                            | Measured Impact  | Notes                                                              |
| --------------------------------- | ---------------- | ------------------------------------------------------------------ |
| **Controller performance impact** | <5%              | Peak impact during hourly collection (XX:05, XX:10, XX:15)         |
| **Peak memory usage**             | 300-500 MB       | During active collection with chunked processing                   |
| **Local storage usage**           | <1 GB per cycle  | Includes hourly, daily, and anonymized data before cleanup         |
| **Database query performance**    | Read-only access | No write impact on controller database                             |
| **Network bandwidth**             | Minimal          | Anonymized payloads transmitted daily (varies by environment size) |


**Collection strategy**:

- Hourly micro-batches with chunked processing (1000 rows per batch)
- Read-only database access prevents controller impact
- Scheduled during low-usage periods (1:00 AM - 5:00 AM for daily tasks)


**Data retention (local to metrics service database)**

| Data Category          | Retention Period                 | Storage Impact                                |
| ---------------------- | -------------------------------- | --------------------------------------------- |
| Hourly collection data | 7 days                           | Primary storage consumer                      |
| Daily summaries        | 30 days                          | Aggregated, smaller than hourly               |
| Anonymized payloads    | 7 days                           | Compressed before transmission                |
| Dashboard report data  | 90 days (when dashboard enabled) | Largest storage consumer if dashboard enabled |


All data is purged automatically by `cleanup_metrics_data` task (daily at 4:00 AM).

## Capacity planning guidelines

**When to scale metrics service resources**

| Condition                                          | Recommended Action                                      |
| -------------------------------------------------- | ------------------------------------------------------- |
| Hourly collection duration exceeds 10 minutes      | Add 2 vCPUs or optimize database queries                |
| Memory usage sustained above 80% (>6.4 GB of 8 GB) | Add 4 GB RAM                                            |
| Database size exceeds 10 GB                        | Increase storage OR reduce retention periods            |
| Task execution failures increase                   | Check database performance, verify network connectivity |


**Storage growth estimates** (without dashboard):

- Small environment (1000 jobs/day): ~50-100 MB/day
- Medium environment (5000 jobs/day): ~200-300 MB/day
- Large environment (20,000 jobs/day): ~500-800 MB/day


**Storage growth with dashboard enabled** (90-day retention):

- Multiply above estimates by 3-4x due to additional dashboard data collection

## Disconnected environments

Metrics service handles disconnected environments gracefully:

**If Segment.com is unreachable:**

- Service retries transmission 3 times per scheduled run
- Logs failure and waits for next cycle (no retry storms)
- No impact on automation controller operations when disconnected
- Local collection continues normally


**When connectivity is restored:**

- Next scheduled anonymization/transmission cycle resumes
- Only most recent anonymized payload is sent (older payloads are purged per retention policy)
- No backlog buildup or resource exhaustion


**Recommendation for disconnected environments:** Disable `ANONYMIZED_DATA_COLLECTION` feature flag if permanent disconnection is expected. This prevents log noise from failed transmission attempts while allowing local collection to continue.
