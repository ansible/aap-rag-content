+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/con_understand_automation_dashboard_architecture"
title = "Understand automation dashboard architecture - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/con_understand_automation_dashboard_architecture/aem-page/con_understand_automation_dashboard_architecture.html"
last_crumb = "Understand automation dashboard architecture"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Understand automation dashboard architecture"
oversized = "false"
page_slug = "con_understand_automation_dashboard_architecture"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/con_understand_automation_dashboard_architecture"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/con_understand_automation_dashboard_architecture/toc/toc.json"
type = "aem-page"
+++

# Understand automation dashboard architecture

This module explains the automation dashboard architecture in Red Hat Ansible Automation Platform 2.7, including its integration with metrics service, deployment options, and Technology Preview limitations.

 Important:

**Technology Preview:** Automation dashboard is a Technology Preview feature in Red Hat Ansible Automation Platform 2.7. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

Automation dashboard is disabled by default in Red Hat Ansible Automation Platform 2.7. You must explicitly enable it by using installer configuration or Custom Resource (CR) definition.

## Automation dashboard overview

Automation dashboard provides visualization, measurement, and return on investment (ROI) analysis for your Ansible automation usage. In Ansible Automation Platform 2.7, the dashboard becomes a native component of the platform. It integrates directly with the Ansible Automation Platform unified user interface (UI) and leverages metrics service as its data collection backend.

 Note:

For information on the standalone automation dashboard, see View automation job metrics with automation dashboard.

## Key characteristics (Red Hat Ansible Automation Platform 2.7 native integration)

| Characteristic           | Ansible Automation Platform 2.7 Native Dashboard                                                                                                                                              | Standalone Dashboard Utility (Ansible Automation Platform 2.6)                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Deployment               | Containerized installer or operator-based deployment as part of Ansible Automation Platform installation                                                                                      | Separate RHEL 9 host, manual installation bundle                                       |
| Backend                  | Metrics service - unified data collection service                                                                                                                                             | Standalone database, direct Controller application programming interface (API) queries |
| UI Integration           | Native Ansible Automation Platform unified UI (integrated navigation)                                                                                                                         | Separate dashboard URL                                                                 |
| Authentication           | Ansible Automation Platform Gateway role-based access control (RBAC) (Lightweight Directory Access Protocol (LDAP), Security Assertion Markup Language (SAML), OpenID Connect (OIDC) support) | OAuth tokens (clusters.yaml configuration)                                             |
| Data Collection          | 6-hourly automated collection by using metrics service                                                                                                                                        | Configurable synchronization schedule                                                  |
| Multi-Instance Support   | Single Ansible Automation Platform instance only (Technology Preview limitation)                                                                                                              | Multiple Ansible Automation Platform instances supported                               |
| Default State            | Disabled (opt-in by using feature flag)                                                                                                                                                       | N/A (separate installation)                                                            |
| Database                 | Metrics service database                                                                                                                                                                      | Standalone postgres instance                                                           |
| Historical Data Backfill | Up to 90 days from Controller DB when enabled post-installation                                                                                                                               | Configurable backfill period                                                           |

## Architecture components

*Figure 1. Automation dashboard architecture*
![Architectural diagram showing relationship between automation dashboard and metrics service](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/metrics-services-dashboard-architecture.png)

**Core components**

| Component                           | Purpose                               | Dashboard Role                                                                                                             |
| ----------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Automation dashboard UI             | Visualization and reporting interface | Displays ROI metrics, cost analysis, and usage trends collected by metrics service                                         |
| Metrics service                     | Unified data collection backend       | Collects dashboard-specific metrics (cost, pricing, ROI) when FEATURE\_DASHBOARD\_COLLECTION\_ENABLED feature flag enabled |
| Metrics service database            | Metrics storage and processing        | Once the feature flag is enabled, the data is stored in dashboard\_\* tables                                               |
| awx database                        | Controller operational data           | Source of automation usage data (accessed read-only by using ms\_awx\_readonly user)                                       |
| Ansible Automation Platform Gateway | Authentication and RBAC               | Controls dashboard access by using configurable RBAC policies                                                              |

## Metrics service as unified backend

Automation dashboard uses metrics service as its data collection and storage backend. This architecture provides:

- **Single infrastructure:** Avoids duplicate data collection mechanisms
- **Unified API:** Dashboard UI consumes data by using metrics service REST APIs
- **Shared database:** Dashboard tables coexist with standard metrics in metrics_service database
- **Consistent data model:** Same anonymization and retention policies
- **Feature flag control:** Dashboard collection enabled independently by using FEATURE_DASHBOARD_COLLECTION_ENABLED: true

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
- Top 10 users by automation usage
- Top 10 projects by savings
- Time-series data for graphs


**Filter list endpoints**

These endpoints provide lists of available filter options for dropdown menus:

- **Organizations:** `GET /api/metrics/v1/dashboard_reports/organizations/`
- **Templates:** `GET /api/metrics/v1/dashboard_reports/templates/`
- **Projects:** `GET /api/metrics/v1/dashboard_reports/projects/`
- **Labels:** `GET /api/metrics/v1/dashboard_reports/labels/`


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
**API documentation**

For complete API schema and additional endpoints, access the OpenAPI specification:

```
curl -k -u admin:<password> \
  https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/schema/
```


 Note:

**RBAC Note:** Dashboard API access is controlled by Ansible Automation Platform Gateway RBAC policies. Users must have appropriate dashboard permissions to access these endpoints. System Auditor role provides read-only access to all dashboard data.

## Data collection architecture

**Collection schedule**

When `FEATURE_DASHBOARD_COLLECTION_ENABLED: true` is configured (containerized) or `spec.metrics_service.FEATURE_DASHBOARD_COLLECTION_ENABLED: true` (operator), metrics service collects dashboard-specific data on a 6-hourly schedule.

| Aspect           | Details                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------- |
| Frequency        | Every 6 hours (balance between data freshness and Controller database load)             |
| Configurable?    | No                                                                                      |
| Database Impact  | Minimal - read-only queries by using ms\_awx\_readonly user, optimized for low overhead |
| Topology Support | Single VM (growth topology) supported with 6-hourly collection                          |


**Dashboard collection configuration**

The following configuration variables control dashboard collection behavior:

| Variable                                                              | Default           | Purpose                                                          | User-Configurable?          |
| --------------------------------------------------------------------- | ----------------- | ---------------------------------------------------------------- | --------------------------- |
| FEATURE\_DASHBOARD\_COLLECTION\_ENABLED                               | False             | Enables/disables all dashboard data collection                   | Yes                         |
| FEATURE\_DASHBOARD\_COLLECTION\_ENABLED\_\_COLLECTION\_SCHEDULE\_CRON | "0 \*/6 \* \* \*" | Incremental data collection schedule (every 6 hours)             | No                          |
| retention\_period\_days                                               | 90                | How many days JobData records are stored (configurable per task) | Internal configuration only |


 Note:

In Technology Preview, the collection schedule is fixed at 6 hours.

**Dashboard-specific metrics collected**

- **Cost and pricing data:** Infrastructure costs for automation execution
- **ROI calculations:** Time saved, cost savings, manual effort avoided
- **Automation savings metrics:** Efficiency gains and resource optimization
- **Executive reporting data:** High-level usage trends and adoption metrics


**Detailed metrics schema:**

| Field                  | Type                | Source (AWX database table)       | Description                                                                           |
| ---------------------- | ------------------- | --------------------------------- | ------------------------------------------------------------------------------------- |
| job\_id                | int                 | main\_unifiedjob.id               | Job ID in AWX (unique)                                                                |
| template\_name         | str                 | main\_unifiedjobtemplate.name     | Job template name                                                                     |
| template\_id           | int (nullable)      | main\_unifiedjobtemplate.id       | Job template ID in AWX                                                                |
| project\_id            | int (nullable)      | main\_project.id                  | Project ID in AWX                                                                     |
| project\_name          | str (nullable)      | main\_project.name                | Project name                                                                          |
| organization\_id       | int (nullable)      | main\_organization.id             | Organization ID in AWX                                                                |
| organization\_name     | str (nullable)      | main\_organization.name           | Organization name                                                                     |
| status                 | str                 | main\_unifiedjob.status           | Status: new, pending, waiting, running, successful, failed, error, cancelled          |
| started                | datetime (nullable) | main\_unifiedjob.started          | Job start time                                                                        |
| finished               | datetime (nullable) | main\_unifiedjob.finished         | Job end time                                                                          |
| elapsed                | decimal             | main\_unifiedjob.elapsed          | Job duration in seconds                                                               |
| num\_hosts             | int                 | Calculated from main\_hostsummary | Number of hosts in a job                                                              |
| launched\_by\_id       | int (nullable)      | main\_unifiedjob.created\_by\_id  | ID of the user that started the job in AWX/Automation Controller                      |
| launched\_by\_username | str (nullable)      | auth\_user.username               | Name of the user that started the job                                                 |
| awx\_created           | datetime            | main\_unifiedjob.created          | Date created in AWX/Automation Controller                                             |
| awx\_modified          | datetime            | main\_unifiedjob.modified         | Last changed date in AWX/Automation Controller (watermark for incremental collection) |


**Related raw data tables:**

| Field             | Type           | Source (AWX database table) | Description                                                    |
| ----------------- | -------------- | --------------------------- | -------------------------------------------------------------- |
| host\_summary\_id | int            | main\_hostsummary.id        | Host summary ID in AWX/Automation Controller                   |
| host\_id          | int (nullable) | main\_host.id               | Host ID in AWX/Automation Controller                           |
| host\_name        | str            | main\_host.name             | Host name                                                      |
| label\_id         | int            | main\_label.id              | Label ID in AWX/Automation Controller (for filtering purposes) |

## Database architecture

**Technology Preview database approach**

In Ansible Automation Platform 2.7 Technology Preview, the metrics service database may be colocated with the Controller database on the same postgres instance. The 6-hourly collection schedule minimizes performance impact on Controller database operations.

| Phase                                                  | Database Architecture                                                                | Notes                                                               |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Technology Preview (Ansible Automation Platform 2.7.0) | Metrics service DB may be colocated with Controller DB on the same postgres instance | 6-hourly collection minimizes impact; performance monitoring active |
| General Availability (2.7 async release)               | Database architecture evaluated based on Technology Preview data                     |                                                                     |

## Deployment topology

**Single-instance limitation (Technology Preview)**

The integrated dashboard in Ansible Automation Platform 2.7 Technology Preview displays data for the local Ansible Automation Platform instance only. Multi-instance support (connecting multiple Ansible Automation Platform deployments to a single dashboard) is not available with the Ansible Automation Platform integration.

| Deployment Scenario                                                 | Technology Preview Support | Current Workaround                                              |
| ------------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------- |
| Single Ansible Automation Platform instance                         | Fully supported            | N/A                                                             |
| Multiple Ansible Automation Platform instances (different versions) | Not supported              | Use standalone dashboard utility for multi-instance aggregation |
| Multiple Ansible Automation Platform instances (same version)       | Not supported              | Use standalone dashboard utility for multi-instance aggregation |


 Note:

If you need to aggregate data across multiple Ansible Automation Platform instances, continue using the standalone automation dashboard utility (Ansible Automation Platform 2.6 approach).

## Feature flag architecture

Dashboard collection is controlled by a feature flag that enables or disables data collection when metrics service is installed.

**Containerized installation method**

Create a feature flags variables file (for example, feature_flags.yml) with the following information:

```
feature_flags:
  FEATURE_DASHBOARD_COLLECTION_ENABLED: True
```
Then pass the file to the installer using the -e flag:

```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory ansible.containerized_installer.install -e @feature_flags.yml
```
**Operator deployment**

```
spec:
  feature_flags:
    FEATURE_DASHBOARD_COLLECTION_ENABLED: true
```
This maps to the internal metrics service configuration:

```
# In metrics service settings.yaml
FEATURE_ENABLED:
  FEATURE_DASHBOARD_COLLECTION_ENABLED: true

# or in metrics service environment
env | grep DASHBOARD
METRICS_SERVICE_FEATURE_DASHBOARD_COLLECTION_ENABLED=true
```
**Feature flag behavior**

| Feature Flag State | Behavior                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| false (default)    | Dashboard collection tasks not scheduled; no dashboard data collected; UI may show empty state or be disabled      |
| true               | Dashboard collection tasks run on 6-hourly schedule; dashboard-specific metrics collected; dashboard UI accessible |

## Dependency: Metrics service required

Automation dashboard requires metrics service to be configured and available.

If metrics service is not configured (no host in [automationmetrics] group for containerized, or no MetricsService CR for operator), dashboard configuration settings are ignored. The dashboard collection feature flag (FEATURE_DASHBOARD_COLLECTION_ENABLED: True) has no effect without metrics service enabled.

 Warning:

There is currently no installer preflight validation for this dependency. If metrics service is not configured, dashboard settings are ignored during installation.

**Dependency Behavior:**

- **Dashboard requires metrics service:** Dashboard collection cannot function without metrics service backend
- **Metrics service is independent:** Metrics service operates with or without dashboard enabled
- **Configuration relationship:** If metrics service is not configured, dashboard settings are ignored

## Performance characteristics

**Collection impact on Controller database**

The 6-hourly collection schedule minimizes impact on the Controller (AWX) database:

| Metric                 | Specification                                          |
| ---------------------- | ------------------------------------------------------ |
| Collection frequency   | Every 6 hours                                          |
| Database access        | Read-only by using ms\_awx\_readonly user              |
| Query optimization     | Incremental data collection (only new/updated records) |
| Topology support       | Single VM (growth topology) supported                  |
| Expected CPU impact    | < 5% during collection (lasts ~5-10 minutes)           |
| Expected memory impact | < 500MB temporary increase during collection           |

## Technology Preview to GA migration

**What to expect**

- **Feature flag may change:** GA enables dashboard by default
- **Backup before upgrade:** Always back up metrics_service database before upgrading from Technology Preview to GA
