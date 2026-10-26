+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_understand_automation_dashboard_architecture"
title = "Understand automation dashboard architecture - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_automation_dashboard_deployment_options/", "Automation dashboard deployment options"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_understand_automation_dashboard_architecture/aem-page/install-con_understand_automation_dashboard_architecture.html"
last_crumb = "Understand automation dashboard architecture"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Understand automation dashboard architecture"
oversized = "false"
page_slug = "install-con_understand_automation_dashboard_architecture"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-con_understand_automation_dashboard_architecture"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_understand_automation_dashboard_architecture/toc/toc.json"
type = "aem-page"
+++

# Understand automation dashboard architecture

This module explains the automation dashboard architecture in Red Hat Ansible Automation Platform 2.7, including its integration with metrics service, deployment options.

## Automation dashboard overview

Automation dashboard provides visualization, measurement, and return on investment (ROI) analysis for your Ansible automation usage. In Ansible Automation Platform 2.7, the dashboard becomes a native component of the platform. It integrates directly with the Ansible Automation Platform unified user interface (UI) and leverages metrics service as its data collection backend.

Note:

For information on the standalone automation dashboard, see View automation job metrics with automation dashboard.

## Key characteristics (Red Hat Ansible Automation Platform 2.7 native integration)

| Characteristic           | Ansible Automation Platform 2.7 Native Dashboard                                                                                                                                              | Standalone Dashboard Utility (Ansible Automation Platform 2.4+)                        |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Deployment               | Containerized installer or operator-based deployment as part of Ansible Automation Platform installation                                                                                      | Separate RHEL 9 host, manual installation bundle                                       |
| Backend                  | Metrics service - unified data collection service                                                                                                                                             | Standalone database, direct Controller application programming interface (API) queries |
| UI Integration           | Native Ansible Automation Platform unified UI (integrated navigation)                                                                                                                         | Separate dashboard URL                                                                 |
| Authentication           | Ansible Automation Platform Gateway role-based access control (RBAC) (Lightweight Directory Access Protocol (LDAP), Security Assertion Markup Language (SAML), OpenID Connect (OIDC) support) | OAuth tokens (clusters.yaml configuration)                                             |
| Data Collection          | Hourly automated collection by using metrics service                                                                                                                                          | Configurable synchronization schedule                                                  |
| Multi-Instance Support   | Single Ansible Automation Platform instance only                                                                                                                                              | Multiple Ansible Automation Platform instances supported                               |
| Default State            | Enabled by default when metrics service is installed                                                                                                                                          | N/A (separate installation)                                                            |
| Database                 | Metrics service database                                                                                                                                                                      | Standalone postgres instance                                                           |
| Historical Data Backfill | Aligns with controller’s configured retention period                                                                                                                                          | Configurable backfill period                                                           |

## Architecture components

*Figure 1. Automation dashboard architecture*
![Architectural diagram showing relationship between automation dashboard and metrics service](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/metrics-services-dashboard-architecture.png)

**Core components**

| Component                           | Purpose                               | Dashboard Role                                                                       |
| ----------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------ |
| Automation dashboard UI             | Visualization and reporting interface | Displays ROI metrics, cost analysis, and usage trends collected by metrics service   |
| Metrics service                     | Unified data collection backend       | Collects dashboard-specific metrics (cost, pricing, ROI)                             |
| Metrics service database            | Metrics storage and processing        | Stores dashboard data in dashboard\_\* tables                                        |
| awx database                        | Controller operational data           | Source of automation usage data (accessed read-only by using ms\_awx\_readonly user) |
| Ansible Automation Platform Gateway | Authentication and RBAC               | Controls dashboard access by using configurable RBAC policies                        |

## Metrics service as unified backend

Automation dashboard uses metrics service as its data collection and storage backend. This architecture provides:

- **Single infrastructure:** Avoids duplicate data collection mechanisms
- **Unified API:** Dashboard UI consumes data by using metrics service REST APIs
- **Shared database:** Dashboard tables coexist with standard metrics in metrics_service database
- **Consistent data model:** Same anonymization and retention policies

## Metrics service REST API endpoints

The dashboard UI consumes data by using the following metrics service REST API endpoints:

| Endpoint                                                | Method                | Purpose                                          |
| ------------------------------------------------------- | --------------------- | ------------------------------------------------ |
| /api/metrics/v1/dashboard\_reports/report/              | GET                   | Paginated data list aggregated by templates      |
| /api/metrics/v1/dashboard\_reports/report/details/      | GET                   | Summary, graphical data, top user/project data   |
| /api/metrics/v1/dashboard\_reports/organizations/       | GET                   | Organization dropdown filter (from AWX database) |
| /api/metrics/v1/dashboard\_reports/templates/           | GET                   | Job template dropdown filter (from AWX database) |
| /api/metrics/v1/dashboard\_reports/projects/            | GET                   | Project dropdown filter (from AWX database)      |
| /api/metrics/v1/dashboard\_reports/labels/              | GET                   | Label dropdown filter (from AWX database)        |
| /api/metrics/v1/dashboard\_reports/subscription\_costs/ | GET/PATCH             | Cost parameters (singleton)                      |
| /api/metrics/v1/dashboard\_reports/template\_metadata/  | GET/PATCH             | Manual/automated effort time metadata            |
| /api/metrics/v1/dashboard\_reports/filter\_sets/        | GET/POST/PATCH/DELETE | Saved filterset configurations                   |

## Dashboard API quick reference

The automation dashboard provides REST APIs for programmatic access to dashboard data. These APIs are consumed by the dashboard UI and can also be accessed directly for custom reporting and integrations.

**Base URL:** `https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/`

**Authentication:** All dashboard API endpoints require authentication by using Ansible Automation Platform credentials and are subject to RBAC enforcement through the Ansible Automation Platform Gateway.

**Report endpoint**

**Endpoint:** `/api/metrics/v1/dashboard_reports/report/`

**Method:** GET

**Purpose:** Retrieve paginated dashboard data aggregated by job templates

**Required Query Parameters:**

| Parameter | Type   | Description                      | Valid Values                                   |
| --------- | ------ | -------------------------------- | ---------------------------------------------- |
| period    | string | Time period for data aggregation | last\_30\_days, last\_60\_days, last\_90\_days |

**Optional Filter Query Parameters:**

| Parameter    | Type    | Description               | Example         |
| ------------ | ------- | ------------------------- | --------------- |
| organization | integer | Filter by organization ID | ?organization=3 |
| template     | integer | Filter by job template ID | ?template=5     |
| project      | integer | Filter by project ID      | ?project=10     |
| label        | integer | Filter by label ID        | ?label=2        |

Important:

Filter parameter names are singular (organization, not organizations). Multiple filters can be combined using multiple query parameters of the same name (for example, ?organization=3&organization=5).

**Example Requests:**

```
# Get all dashboard data for last 90 days
curl -k -u admin:<password> \
  "https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/report/?period=last_90_days"

# Filter by specific organization
curl -k -u admin:<password> \
  "https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/report/?period=last_90_days&organization=3"

# Combine multiple filters
curl -k -u admin:<password> \
  "https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/report/?period=last_60_days&organization=3&project=10"

# Filter by multiple organizations
curl -k -u admin:<password> \
  "https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/report/?period=last_90_days&organization=3&organization=5"
```

**Response:** Paginated JSON response containing job template aggregations with:

- Cost and savings calculations
- ROI metrics
- Job execution statistics
- Time saved calculations

Note:

The jobs table includes a sortable Time Savings column showing the difference between configured manual effort time and automated elapsed time, calculated per template.

**Report details endpoint**

**Endpoint:** `/api/metrics/v1/dashboard_reports/report/details/`

**Method:** GET

**Purpose:** Retrieve summary statistics, graphical data, and top user/project information

**Query Parameters:** Same as /report/ endpoint (period required, filters optional)

**Example Request:**

```
curl -k -u admin:<password> \
  "https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/report/details/?period=last_90_days"
```

**Response:** JSON response containing:

- Summary statistics (total jobs, total savings, total time saved)
- Top 5 users by automation usage
  Note:
  Jobs triggered by schedules, webhooks, or maintenance tasks do not have an associated user ID. These jobs are included in total job counts but excluded from the Top 5 Users card.

- Top 5 projects by savings
- Time-series data for graphs

**Filter list endpoints**

These endpoints provide lists of available filter options for dropdown menus:

- **Organizations:** `GET /api/metrics/v1/dashboard_reports/organizations/`
- **Templates:** `GET /api/metrics/v1/dashboard_reports/templates/`
- **Projects:** `GET /api/metrics/v1/dashboard_reports/projects/`
- **Labels:** `GET /api/metrics/v1/dashboard_reports/labels/`

Note:

When duplicate label names exist across organizations, the label filter includes the organization name for disambiguation (for example, "Production (EMEA Org)" and "Production (APAC Org)").

Note:

These endpoints return the complete list of available filter values from the Controller database.

**Cost configuration endpoint**

**Endpoint:** `/api/metrics/v1/dashboard_reports/subscription_costs/`

**Methods:** GET (retrieve), PATCH (update)

**Purpose:** Configure cost parameters for ROI calculations

**Example - Retrieve cost parameters:**

```
curl -k -u admin:<password> \
  https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/subscription_costs/
```

**Example - Update cost parameters:**

```
curl -k -X PATCH -u admin:<password> \
  https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/subscription_costs/ \
  -H "Content-Type: application/json" \
  -d '{
    "infrastructure_cost_per_hour": 2.50,
    "currency": "USD"
  }'
```

Note:

The `infrastructure_cost_per_hour` field accepts values between $0 and $1,000. Values exceeding $1,000 are rejected to prevent unreasonable cost calculations.

The maximum value for infrastructure_cost_per_hour is $1,000.00. The automation dashboard UI prevents entry of values exceeding this limit. This cap applies to the dashboard UI only and does not affect API requests.

**API documentation**

For complete API schema and additional endpoints, access the OpenAPI specification:

```
curl -k -u admin:<password> \
  https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/schema/
```

Note:

**RBAC Note:** Dashboard API access is controlled by Ansible Automation Platform Gateway RBAC policies. Users must have appropriate dashboard permissions to access these endpoints. Previously existing Platform Admins and System Auditors can access the dashboard once enabled. The following roles have dashboard access:

- **Administrator:** Full read/write access to all dashboard data and configuration
- **System Auditor:** Read-only access to all dashboard data

## Template metadata endpoint

Use the template metadata endpoint to configure manual effort time estimates for ROI calculations.

**Endpoint**: `/api/metrics/v1/dashboard_reports/template_metadata/`

**Methods**: GET (retrieve all template metadata), PATCH (update an individual template)

The default `time_taken_to_manually_execute` value is **1 minute** (60 seconds) for all templates. This default applies to any template where an administrator has not explicitly configured a manual effort time.

To update the manual effort time for a specific template, send a PATCH request:

```
PATCH /api/metrics/v1/dashboard_reports/template_metadata/<template_id>/
```

```
{
    "time_taken_to_manually_execute": 300
}
```

This example sets the manual effort time to 5 minutes (300 seconds) for the specified template.

## Data collection architecture

**Collection schedule**

Metrics service collects dashboard-specific data on an hourly schedule.

| Aspect           | Details                                                                                |
| ---------------- | -------------------------------------------------------------------------------------- |
| Frequency        | Every hour (balance between data freshness and Controller database load)               |
| Configurable?    | No                                                                                     |
| Database Impact  | Minimal - read-only queries by using`ms_awx_readonly` user, optimized for low overhead |
| Topology Support | Single VM (growth topology) supported with hourly collection                           |

**Dashboard collection configuration**

The following configuration variables control dashboard collection behavior:

| Variable                                         | Default | Purpose                                                                                                                                                                     | User-Configurable?                          |
| ------------------------------------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| `retention_period_days`                          | `90`    | How many days JobData records are stored. Applies only when`DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` is false. When false, the dashboard uses its own setting.       | Internal configuration only                 |
| `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` | `True`  | When true, the dashboard data retention period aligns with the automation controller retention period. When false, the dashboard uses its own`retention_period_days` value. | Yes (via`automationmetrics_extra_settings`) |

**Dashboard-specific metrics collected**

Note:

Dashboard counts playbook jobs only. Sync, cleanup, and maintenance jobs are excluded from all job counts and ROI calculations. Only successful and failed outcomes are counted — canceled and error job outcomes are not tracked by the dashboard. If you compare dashboard job counts to automation controller job counts, they will differ because the dashboard excludes non-automation jobs and non-terminal outcomes.

- **Cost and pricing data:** Infrastructure costs for automation execution
- **ROI calculations:** Time saved, cost savings, manual effort avoided. Time saved is calculated per template as manual effort time (default: 1 minute) minus automated elapsed time
- **Automation savings metrics:** Efficiency gains and resource optimization
- **Executive reporting data:** High-level usage trends and adoption metrics

**Detailed metrics schema:**

| Field                  | Type                | Source (AWX database table)       | Description                                                                                                                                                                   |
| ---------------------- | ------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| job\_id                | int                 | main\_unifiedjob.id               | Job ID in AWX (unique)                                                                                                                                                        |
| template\_name         | str                 | main\_unifiedjobtemplate.name     | Job template name                                                                                                                                                             |
| template\_id           | int (nullable)      | main\_unifiedjobtemplate.id       | Job template ID in AWX                                                                                                                                                        |
| project\_id            | int (nullable)      | main\_project.id                  | Project ID in AWX                                                                                                                                                             |
| project\_name          | str (nullable)      | main\_project.name                | Project name                                                                                                                                                                  |
| organization\_id       | int (nullable)      | main\_organization.id             | Organization ID in AWX                                                                                                                                                        |
| organization\_name     | str (nullable)      | main\_organization.name           | Organization name                                                                                                                                                             |
| status                 | str                 | main\_unifiedjob.status           | Status: new, pending, waiting, running, successful, failed, error, cancelled                                                                                                  |
| started                | datetime (nullable) | main\_unifiedjob.started          | Job start time                                                                                                                                                                |
| finished               | datetime (nullable) | main\_unifiedjob.finished         | Job end time                                                                                                                                                                  |
| elapsed                | decimal             | main\_unifiedjob.elapsed          | Job duration in seconds                                                                                                                                                       |
| time\_saved            | decimal (nullable)  | Calculated                        | Time saved per job in seconds (manual effort time minus automated elapsed time). Calculated per template, not per host. Null if template has no manual effort time configured |
| num\_hosts             | int                 | Calculated from main\_hostsummary | Number of hosts in a job                                                                                                                                                      |
| launched\_by\_id       | int (nullable)      | main\_unifiedjob.created\_by\_id  | ID of the user that started the job in AWX/Automation Controller                                                                                                              |
| launched\_by\_username | str (nullable)      | auth\_user.username               | Name of the user that started the job                                                                                                                                         |
| awx\_created           | datetime            | main\_unifiedjob.created          | Date created in AWX/Automation Controller                                                                                                                                     |
| awx\_modified          | datetime            | main\_unifiedjob.modified         | Last changed date in AWX/Automation Controller (watermark for incremental collection)                                                                                         |

**Related raw data tables:**

| Field             | Type           | Source (AWX database table) | Description                                                    |
| ----------------- | -------------- | --------------------------- | -------------------------------------------------------------- |
| host\_summary\_id | int            | main\_hostsummary.id        | Host summary ID in AWX/Automation Controller                   |
| host\_id          | int (nullable) | main\_host.id               | Host ID in AWX/Automation Controller                           |
| host\_name        | str            | main\_host.name             | Host name                                                      |
| label\_id         | int            | main\_label.id              | Label ID in AWX/Automation Controller (for filtering purposes) |

## Database architecture

The metrics service database may be colocated with the Controller database on the same postgres instance. The hourly collection schedule minimizes performance impact on Controller database operations. By default, dashboard data retention aligns with the automation controller retention period (DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION: True). This ensures the dashboard data lifecycle matches controller data availability. When controller data is purged, corresponding dashboard records are also cleaned up, preventing stale data in dashboard reports. To use an independent retention period for dashboard data, set DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION to false using automationmetrics_extra_settings in your inventory file.

Important:

If you are upgrading from a previous release, this default behavior change may affect existing data. If the automation controller retention period is shorter than the dashboard's previous retention period (default: 90 days), any dashboard data older than the controller retention period will be deleted after the upgrade. To preserve existing dashboard data, set DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION to false in your inventory file before upgrading.

## Deployment topology

**Single-instance limitation**

The integrated dashboard displays data for the local Ansible Automation Platform instance only. Multi-instance support (connecting multiple Ansible Automation Platform deployments to a single dashboard) is not available with the Ansible Automation Platform 2.7 integration.

| Deployment Scenario                                                 | Support         | Current Workaround                                              |
| ------------------------------------------------------------------- | --------------- | --------------------------------------------------------------- |
| Single Ansible Automation Platform instance                         | Fully supported | N/A                                                             |
| Multiple Ansible Automation Platform instances (different versions) | Not supported   | Use standalone dashboard utility for multi-instance aggregation |
| Multiple Ansible Automation Platform instances (same version)       | Not supported   | Use standalone dashboard utility for multi-instance aggregation |

Note:

If you need to aggregate data across multiple Ansible Automation Platform instances, use the standalone automation dashboard utility. For a comparison of the integrated dashboard and the standalone utility, see Automation dashboard deployment options.

## Dependency: Metrics service required

Automation dashboard requires metrics service to be configured and available.

If metrics service is not configured (no host in [automationmetrics] group for containerized, or no MetricsService CR for operator), dashboard configuration settings are ignored.

Warning:

There is currently no installer preflight validation for this dependency. If metrics service is not configured, dashboard settings are ignored during installation.

**Dependency Behavior:**

- **Dashboard requires metrics service:** Dashboard data collection cannot function without metrics service backend
- **Metrics service is independent:** Metrics service operates with or without dashboard enabled
- **Configuration relationship:** If metrics service is not configured, dashboard settings are ignored

## Performance characteristics

Performance validated across Containerized Ansible Automation Platform and OpenShift Ansible Automation Platform deployments with data scales from 9,100 to 100,100 jobs.

| Metric                       | SLO          | Measured (worst case)                        |
| ---------------------------- | ------------ | -------------------------------------------- |
| Dashboard page load time     | < 5 seconds  | < 1 second                                   |
| API response time            | < 5 seconds  | < 250 milliseconds                           |
| CSV export (100K rows)       | < 60 seconds | < 1 second                                   |
| Collection cycle duration    | < 1 hour     | < 15 minutes (initial backfill at 100k jobs) |
| Subsequent hourly collection | < 1 hour     | < 11 seconds                                 |

**Collection impact on Controller database**

The hourly collection schedule minimizes impact on the Controller (AWX) database:

| Metric                 | Specification                                          |
| ---------------------- | ------------------------------------------------------ |
| Collection frequency   | Every hour                                             |
| Database access        | Read-only by using ms\_awx\_readonly user              |
| Query optimization     | Incremental data collection (only new/updated records) |
| Topology support       | Single VM (growth topology) supported                  |
| Expected CPU impact    | < 5% during collection (lasts ~5-10 minutes)           |
| Expected memory impact | < 500MB temporary increase during collection           |
