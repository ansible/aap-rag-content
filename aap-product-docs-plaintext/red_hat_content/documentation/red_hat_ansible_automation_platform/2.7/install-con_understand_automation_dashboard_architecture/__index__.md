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

