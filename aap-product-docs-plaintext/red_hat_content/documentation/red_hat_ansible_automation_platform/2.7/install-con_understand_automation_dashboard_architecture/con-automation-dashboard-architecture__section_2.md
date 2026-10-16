# Understand automation dashboard architecture
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
