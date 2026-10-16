+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-assembly_self_service_telemetry_capture"
title = "Capture telemetry data for the Ansible self-service portal - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-assembly_self_service_telemetry_capture/", "Capture telemetry data for the Ansible self-service portal"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-assembly_self_service_telemetry_capture/aem-page/observe-assembly_self_service_telemetry_capture.html"
last_crumb = "Capture telemetry data for the Ansible self-service portal"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Capture telemetry data for the Ansible self-service portal"
oversized = "false"
page_slug = "observe-assembly_self_service_telemetry_capture"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/observe-assembly_self_service_telemetry_capture"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-assembly_self_service_telemetry_capture/toc/toc.json"
type = "aem-page"
+++

# Capture telemetry data for the Ansible self-service portal

The telemetry data collection feature helps in collecting and analyzing the telemetry data to improve your experience with Ansible automation portal. This feature is enabled by default.

## Telemetry data collected by Red Hat

Red Hat collects and analyses the following data:

- Events of page visits and clicks on links or buttons.
- System-related information, for example, locale, timezone, user agent including browser and OS details.
- Page-related information, for example, title, category, extension name, URL, path, referrer, and search parameters.
- Anonymized IP addresses, recorded as `0.0.0.0`.
- Anonymized username hashes, which are unique identifiers used solely to identify the number of unique users of the RHDH application.
- Feedback and sentiment submitted through the Ansible automation portal feedback form, including a 1-5 star rating and feedback text. Users must acknowledge that they share the feedback with Red Hat before submitting.

Note:

The feedback form is optional and disabled by default. You can enable for your users if you choose.

## Configure automation dashboard post-installation

Activate dashboard data collection with automatic historical data backfill to generate comprehensive usage and ROI reports without reinstalling the platform or losing historical automation activity data.

### Before you begin

- Red Hat Ansible Automation Platform 2.7 installed and operational
- Metrics service installed and running
- For containerized: access to the installer inventory file
- For operator: `kubectl` or `oc` access and edit permissions on the AnsibleAutomationPlatform CR

### About this task

This procedure enables automation dashboard on an existing Red Hat Ansible Automation Platform 2.7 installation without platform downtime or service disruption. When you enable dashboard collection post-installation, metrics service automatically backfills up to 90 days of historical data from the Controller database, allowing the dashboard UI to display historical trends within hours of enablement. This zero-disruption activation eliminates the need to reinstall the platform and enables hourly automated collection for ongoing dashboard metrics after backfill completion, providing comprehensive usage and ROI reports using both historical and current automation activity data.

### Procedure

Choose your deployment method and follow the corresponding procedure

- For containerized installation, follow the containerized procedure
- For operator deployment, follow the operator procedure

### Results

After completing the procedure for your deployment method, dashboard is enabled and historical data backfill begins automatically.

### Procedure (containerized installation)

Enable dashboard collection on an existing containerized deployment by updating the installer inventory and re-running the installer.

#### Procedure

1. Update inventory file
      Edit your Ansible Automation Platform containerized installer inventory file. Add a host to the [automationmetrics] group so metrics service is installed. Dashboard collection is enabled automatically with metrics service.

```
[all:vars]
postgresql_admin_username=postgres
postgresql_admin_password=''
```

2. Re-run installer
  

```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory ansible.containerized_installer.install
ansible-playbook -i inventory install.yml
```

  Note:
      There is no separate update playbook. Re-running the install playbook (`ansible.containerized_installer.install`) `install.yml` on an existing installation automatically detects the current state and applies only the necessary updates (in this case, dashboard enablement).

    Expected duration: Approximately 30 minutes for dashboard enablement on an existing installation.

    The installer detects existing Ansible Automation Platform installation and performs dashboard-specific updates:

  - Runs the `automation-metrics-init` container to create dashboard tables
  - Restarts metrics service containers — which triggers `initial_dashboard_collection` task creation

3. Monitor historical data backfill progress
      After enabling automation dashboard, metrics service backfills up to 90 days of historical data from the Controller database (if available). This process runs in the background and may take several hours depending on data volume.

  1. Check backfill status by using CLI
  

```
podman logs automation-metrics-scheduler | grep -i initial_dashboard
podman logs automation-metrics-tasks | grep -i initial_dashboard
```

        Expected log messages:

        **automation-metrics-scheduler:**

```
{"timestamp": "2026-04-22T08:53:39.627Z", "level": "INFO", "logger": "apps.tasks.cron_scheduler", "message": "Found new immediate task: initial_dashboard_collection (ID: 568) - executing now"}

        {"timestamp": "2026-04-22T08:53:39.635Z", "level": "INFO", "logger": "apps.tasks.cron_scheduler", "message": "Executing database task: initial_dashboard_collection (ID: 568)"}

        {"timestamp": "2026-04-22T08:53:39.640Z", "level": "INFO", "logger": "apps.tasks.tasks_system", "message": "Submitted task initial_dashboard_collection (ID: 568) to dispatcher queue dashboard"}

        {"timestamp": "2026-04-22T09:03:39.665Z", "level": "INFO", "logger": "apscheduler.executors.default", "message": "Running job \"DB Task: initial_dashboard_collection (trigger: date[2026-04-22 09:03:39 UTC], next run at: 2026-04-22 09:03:39 UTC)\" (scheduled at 2026-04-22 09:03:39.664342+00:00)"}
```

        **automation-metrics-tasks:**

```
{"timestamp": "2026-04-22T09:03:39.685Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'initial_dashboard_collection' running: Executing function: collect_dashboard_reports_initial_data"}

        {"timestamp": "2026-04-22T09:03:39.709Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'initial_dashboard_collection' completed: Task execution finished with status: completed"}
```

  2. Query database for backfill metadata
  

```
podman exec automation-metrics-database \
  psql -h localhost -U metrics_service -d metrics_service \
  -c "SELECT COUNT(*), MIN(finished), MAX(finished) FROM dashboard_job_data;"
```

        Expected output for successful collection:

    - `COUNT > 0` - Data has been collected
    - `MAX(finished)` close to current date - Collection is up-to-date
        If `COUNT = 0`, no data has been collected yet (backfill may still be in progress or no jobs exist in Controller).

### Procedure (operator deployment)

Enable dashboard collection on an existing operator deployment by editing the AnsibleAutomationPlatform Custom Resource.

#### Procedure

1. Edit the AnsibleAutomationPlatform Custom Resource
      Post-installation enablement on the operator uses the same CR edit as during-installation. There is no separate update playbook or process.

```
kubectl edit AnsibleAutomationPlatform <aap-cr-name> -n <namespace>
```

    Or with OpenShift:

```
oc edit AnsibleAutomationPlatform <aap-cr-name> -n <namespace>
```

    Ensure metrics service is enabled on the CR. Dashboard collection is enabled automatically when metrics service is enabled.

```
spec:
    metrics:
    disabled: false    # metrics service enabled → dashboard collection active
    name: <aap-cr-name>-metrics
  # ... rest of your existing spec unchanged
```

    Save and exit. The Ansible Automation Platform operator and automationmetricsservice operator begin reconciliation automatically.

  Note:
      There is no separate update playbook. Unlike the containerized installer, you do not re-run an install command.

2. Verify metrics service pods restarted with new configuration
      After the ConfigMap is updated, the operator restarts the metrics service pods. Confirm they are running and the pod age reflects the restart:

```
kubectl get pods -n <namespace> -l app.kubernetes.io/name=<aap-cr-name>-metrics
```

    Expected: Three pods running (metrics-web, metrics-tasks, metrics-scheduler), age matching the time since reconciliation.

3. Monitor historical data backfill progress
      After the pods restart, metrics service creates and schedules the `initial_dashboard_collection` task automatically. Monitor its progress by using the tasks pod logs:

```
# Get the tasks pod name
TASKS_POD=$(kubectl get pods -n <namespace> \
  -l app.kubernetes.io/name=<aap-cr-name>-metrics \
  --field-selector=status.phase=Running \
  -o jsonpath='{.items[?(@.metadata.name contains "tasks")].metadata.name}')

    kubectl logs -n <namespace> $TASKS_POD | grep -i initial_dashboard
```

    Or stream logs in real time:

```
kubectl logs -n <namespace> -l app.kubernetes.io/name=<aap-cr-name>-metrics \
  -c metrics-tasks -f | grep -i dashboard
```

    Example scheduler log output:

```
{"timestamp": "2026-05-12T10:39:42.308Z", "level": "INFO", "logger": "apps.tasks.cron_scheduler", "message": "Found new immediate task: initial_dashboard_collection (ID: 52) - executing now"}
{"timestamp": "2026-05-12T10:39:42.309Z", "level": "INFO", "logger": "apps.tasks.cron_scheduler", "message": "Executing database task: initial_dashboard_collection (ID: 52)"}
{"timestamp": "2026-05-12T10:39:42.310Z", "level": "INFO", "logger": "apps.tasks.tasks_system", "message": "Submitted task initial_dashboard_collection (ID: 52) to dispatcher queue dashboard"}
```

    Example tasks worker log output:

```
{"timestamp": "2026-05-12T10:39:45.685Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'initial_dashboard_collection' running: Executing function: collect_dashboard_reports_initial_data"}
{"timestamp": "2026-05-12T10:39:45.709Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'collect_dashboard_reports_initial_data' processing: Collecting dashboard data for: 2026-02-11T00:00:00+00:00 to 2026-05-12T10:39:45+00:00"}
{"timestamp": "2026-05-12T10:39:45.720Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'collect_dashboard_reports_initial_data' processing: Synced batch of 1000 jobs (total so far: 1000, cursor id: 12500)"}
{"timestamp": "2026-05-12T10:39:52.034Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'initial_dashboard_collection' completed: Task execution finished with status: completed"}
```

  Note:
      Backfill collects in cursor-paginated batches. Each batch log line shows progress. For large datasets, many batch lines appear before the completion message.

4. Query database for backfill status
      Get the postgres pod name using the `app.kubernetes.io/component=database` label:

```
DB_POD=$(kubectl get pods -n <namespace> \
  -l app.kubernetes.io/component=database,app.kubernetes.io/part-of=<aap-cr-name> \
  -o jsonpath='{.items[0].metadata.name}')

    kubectl exec -n <namespace> $DB_POD -- \
  psql -U metricsservice -d metricsservice \
  -c "SELECT COUNT(*), MIN(finished), MAX(finished) FROM dashboard_job_data;"
```

    Expected output for successful collection:

  - `COUNT > 0` — data has been collected
  - `MAX(finished)` close to current date — collection is up to date
    If `COUNT = 0`, backfill may still be in progress or the Controller has no completed jobs yet.

    Dashboard data retention follows automation controller data retention settings by default (USE_CONTROLLER_RETENTION: True). No separate retention configuration is required for the automation dashboard.

    The retention_period_days setting (default: 90 days) applies when USE_CONTROLLER_RETENTION is disabled.

### Configure data retention for automation dashboard

Configure how long automation dashboard retains job execution data to balance your reporting needs with storage capacity.

#### Before you begin

- You have the Platform Administrator role in Ansible Automation Platform.
- Metrics service is installed on your Ansible Automation Platform 2.7 deployment.
- You have access to the Ansible Automation Platform API.
- You know your organization's data retention requirements (for example, compliance frameworks or reporting needs).

#### About this task

Dashboard data retention is controlled by the `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` setting, which determines whether dashboard data follows the automation controller's retention period or uses an independent retention period.

| Setting                                          | Value          | Behavior                                                                                                                                                                     |
| ------------------------------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` | True (default) | Dashboard data retention matches the automation controller retention period. When controller data is purged, corresponding dashboard records are also deleted.               |
| `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` | False          | Dashboard uses an independent retention period configured through`retention_days` in the metrics service settings API. Default and recommended: 90 days. Range: 90-730 days. |

Warning:

When dashboard retention syncs with the controller setting (`DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION: True`, the default), any data in the metrics service database older than the controller retention period will be deleted. Verify your controller retention period before enabling dashboard collection. If the controller retention period is shorter than the dashboard's previous retention period (default: 90 days), enabling this sync will permanently delete dashboard data older than the controller retention period.

#### Procedure

1. Determine your retention requirements.
      Consider the following when choosing a retention period:

    | Consideration           | Guidance                                                                                                                                                              |
    | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Compliance requirements | Some compliance frameworks require specific retention periods (for example, SOC 2 requires 1 year, HIPAA requires up to 7 years). Check your organizational policies. |
    | Reporting needs         | Year-over-year comparisons require at least 13 months of data. Quarterly trend reports require at least 4 months.                                                     |
    | Storage capacity        | Longer retention periods require more database storage.                                                                                                               |
  Note:
  The default retention period is 90 days. The maximum configurable retention period is 730 days (2 years).

2. Choose your retention mode.
  - **Use controller-synced retention (default):** If the automation controller retention period meets your dashboard reporting needs, no action is required. Dashboard data retention automatically follows the controller setting.
  - **Set an independent retention period:** If you need a different retention period for dashboard data, disable controller sync by setting `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` to `false`. See the following substeps.
      For containerized installations, add the following to your inventory file:

```
automationmetrics_extra_settings='[{"setting": "DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION", "value": "false"}]'
```

    For operator installations, add the following to your AnsibleAutomationPlatform custom resource:

```
spec:
  metrics:
    extra_settings:
      - setting: DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION
        value: "false"
```

3. If you chose to set an independent retention period, configure the retention period by using the metrics service settings API:
  

```
curl -X PATCH \
  https://<aap-host>/api/metrics-service/v1/settings/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"retention_days": 365}'
```

    Replace the following values:

  - `<aap-host>`: Your Ansible Automation Platform hostname.
  - `<token>`: A valid API token with Platform Administrator permissions.
  - `365`: Your desired retention period in days (90-730).

4. Verify that the retention period is set correctly:
  

```
curl -X GET \
  https://<aap-host>/api/metrics-service/v1/settings/ \
  -H "Authorization: Bearer <token>"
```

    In the response, verify that `retention_days` matches your configured value and check the `cleanup_schedule` field.

  Note:
  The retention cleanup task runs weekly on Sundays at 2:00 AM UTC. Data older than the configured retention period is deleted during cleanup.

5. **Optional:** To delete expired data immediately rather than waiting for the weekly cleanup schedule, trigger a manual cleanup:
  

```
curl -X POST \
  https://<aap-host>/api/metrics-service/v1/metrics-dashboard/cleanup/ \
  -H "Authorization: Bearer <token>"
```

    Use manual cleanup when:

  - You reduced the retention period and need to reclaim storage immediately.
  - You need to verify that cleanup is working correctly.

#### Results

Verify that data retention is configured correctly by confirming the following:

- The `retention_days` value in the settings API response matches your configured retention period.
- The cleanup schedule shows the expected run time (default: Sundays at 2:00 AM UTC).
- The date range available in the dashboard UI reflects the configured retention period.

#### What to do next

Important:

If you are upgrading from a previous release, the default retention behavior change may affect existing data. If the automation controller retention period is shorter than the dashboard's previous retention period (default: 90 days), any dashboard data older than the controller retention period will be deleted after the upgrade. To preserve existing dashboard data, set `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` to `false` in your inventory file before upgrading.

### Monitor data collection status for automation dashboard

Monitor the status of automation dashboard data collection to verify data freshness, check sync progress, and troubleshoot stale or missing data.

#### Before you begin

- Automation dashboard is enabled and metrics service is installed.
- You have a dashboard viewer or editor role in Ansible Automation Platform.
- You have access to the Ansible Automation Platform API.

#### Procedure

1. Check the current status of dashboard data collection by sending a GET request to the collection status endpoint:
  

```
GET /api/metrics-service/v1/metrics-dashboard/collection-status/
```

    The response includes the following fields:

    | Field               | Description                                               |
    | ------------------- | --------------------------------------------------------- |
    | `last_run`          | Timestamp of the last completed collection cycle.         |
    | `status`            | Current status:`completed`,`in_progress`, or`failed`.     |
    | `duration_seconds`  | Duration of the last collection cycle in seconds.         |
    | `records_processed` | Number of records processed in the last collection cycle. |
    | `next_run`          | Timestamp of the next scheduled collection cycle.         |

2. If you enabled automation dashboard for the first time or after an upgrade, check the progress of the historical data backfill:
  

```
GET /api/metrics-service/v1/metrics-dashboard/backfill-status/
```

    The response includes the following fields:

    | Field                       | Description                                    |
    | --------------------------- | ---------------------------------------------- |
    | `backfill_status`           | Current status:`in_progress` or`completed`.    |
    | `progress_percentage`       | Percentage of historical data processed.       |
    | `estimated_completion_time` | Estimated time for the backfill to complete.   |
    | `records_processed`         | Number of historical records processed so far. |
  Note:
  Initial backfill can process up to 90 days of historical data and may take several hours depending on data volume. Subsequent hourly collection cycles process only new and updated records.

3. Interpret the collection status to determine whether action is needed:
    | Status        | Meaning                                                                                                           | Action                                                                                                                                     |
    | ------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
    | `completed`   | The last collection cycle finished successfully. Dashboard data is current within the 1-hour collection interval. | No action needed.                                                                                                                          |
    | `in_progress` | A collection cycle is running. Normal duration is less than 30 minutes.                                           | No action needed. If the cycle exceeds 30 minutes, check metrics service logs for errors.                                                  |
    | `failed`      | The last collection cycle encountered an error.                                                                   | Check metrics service logs for error details. Verify database connectivity between metrics service and the automation controller database. |

#### Results

Verify that data collection is operating normally by confirming all of the following:

- The `last_run` timestamp is within the last hour.
- The collection status is `completed`.
- If a backfill is in progress, the `progress_percentage` is increasing over time.

### Export automation dashboard data to CSV

Export dashboard data to CSV format to share automation cost savings data with stakeholders or analyze data using external tools.

#### Before you begin

- Automation dashboard must contain data for the selected time period.
- You must have access to view the automation dashboard.

#### About this task

Use this procedure when:

- Creating executive reports on automation ROI
- Analyzing automation trends in spreadsheet software
- Archiving automation performance data for compliance
- Sharing automation metrics with finance or business teams

The automation dashboard provides three CSV export formats, each serving different analysis needs:

- **Summary**: Detailed job execution data including costs, time savings, and host counts
- **ROI**: Return on investment metrics showing cost savings percentages and automation value
- **Trends**: Time-series data tracking job execution patterns over the selected period

#### Procedure

1. From the navigation panel, select Automation Analytics> (and then)Automation Dashboard.
2. Set your desired date range using the period selector in the toolbar.
  
  Note:
      The CSV export includes only the data displayed for your selected time period.

3. Click Export as CSV above the main table.
4. Select the export type:
  - Select Summary for detailed execution metrics.
  - Select ROI for cost savings analysis.
  - Select Trends for time-series performance data.

#### Results

Your browser downloads a CSV file containing the selected automation dashboard data.

**Export button is disabled:** The CSV export button is disabled when the dashboard table contains no data. Verify that:

- Your selected date range includes automation job executions.
- Your user account has permissions to view automation dashboard data.
- Automation jobs have completed during the selected period.

### Filter automation dashboard by date range

Use the date range selector to filter dashboard data and analyze automation performance over a specific time period.

#### Before you begin

- Automation dashboard must be configured and collecting data.
- You must have access to view the automation dashboard.

#### About this task

Use this procedure when:

- Comparing automation metrics across different time periods
- Analyzing automation performance for a specific project phase
- Creating reports for quarterly or monthly business reviews
- Investigating automation issues during a known time window

The automation dashboard provides preset date ranges for common analysis periods, plus a custom option for specific date windows:

- **Last 7 days**: Weekly automation performance (default)
- **Last 14 days**: Bi-weekly trends
- **Last 30 days**: Monthly performance
- **Last 60 days**: Quarterly snapshots
- **Last 90 days**: Long-term trend analysis
- **Custom**: Specific date range for targeted analysis

Note:

The custom date range defaults to the last 7 days (today minus 7 days).

#### Procedure

1. From the navigation panel, select Automation Analytics> (and then)Automation Dashboard.
2. From the period selector in the toolbar, select your desired time range:
  - For preset ranges, select Last 7 days, Last 14 days, Last 30 days, Last 60 days, or Last 90 days.
  - For a specific date window, select Custom and continue to step 3.
3. If you selected Custom, configure your date range:
  1. In the From calendar picker, select the start date for your analysis period.
            You can click a date in the calendar or type a date in YYYY-MM-DD format.

  2. In the To calendar picker, select the end date for your analysis period.
            The To field defaults to the current date. You can click a date in the calendar or type a date in YYYY-MM-DD format.

#### Results

The automation dashboard updates to display data only for the selected date range. All metrics, charts, and export functions reflect this filtered view.

To verify the filter applied correctly:

- The period selector in the toolbar displays your selected date range.
- Dashboard metrics update to reflect only the filtered time period.
- The CSV export button (if enabled) exports data for the selected range only.

**Custom date range not applying:** Verify that dates are in valid YYYY-MM-DD format. The dashboard does not send requests to the backend until both the From and To dates are in valid format.

**No data displays for selected range:** Verify that automation jobs executed during your selected date range. If no jobs ran during the period, the dashboard displays an empty table.

### Historical data backfill details

Understand how automation dashboard backfills historical data after post-installation enablement by learning the backfill scope, behavior, performance impact, and duration estimates for dashboard data collection.

#### Backfill scope and behavior

**How backfill works:**

When you enable dashboard post-installation, metrics service initiates a historical data backfill using the following logic:

- **Starting point:** 90 days before current time (`since = now - 90 days`)
- **End point:** Current time (`until = now`)
- **Data query:** Requests all jobs in Controller (AWX) database between `since` and `until`
- **Collection:** Collects whatever data exists in that timeframe

Important:

90 days is the starting point, not a minimum or maximum requirement. Metrics service collects all available data within the 90-day window.

**Examples:**

| Controller Data Available                | Data Collected | Result                                               |
| ---------------------------------------- | -------------- | ---------------------------------------------------- |
| 90+ days of job history                  | 90 days        | Backfill collects maximum (90 days from since point) |
| 30 days of job history                   | 30 days        | Backfill collects all available data (no error)      |
| 0 days of job history (new installation) | 0 jobs         | Backfill completes successfully with`job_count: 0`   |

**Key points:**

- Less than 90 days of data is not an error - backfill collects what exists
- Backfill does not fail if Controller has less than 90 days of data
- New installations with no historical jobs complete backfill immediately (within minutes)

#### Backfill process control

The backfill process runs to completion automatically and cannot be paused or resumed. Once initiated, it continues until all available data within the 90-day window is collected. If metrics service is restarted during backfill, the process resumes from the last successful checkpoint.

#### Performance impact and duration

| Aspect             | Details                                                                                |
| ------------------ | -------------------------------------------------------------------------------------- |
| Data Source        | Controller (awx) database by using`ms_readonly` user (read-only access)                |
| Performance Impact | Minimal - backfill uses same read-only queries as regular collection, spread over time |
| Duration           | Varies based on data volume; typically completes within 24 hours for large datasets    |
| Automatic          | Yes - no manual intervention required after enablement                                 |

**Estimated completion times:**

| Data Volume (Controller Jobs) | Estimated Backfill Duration |
| ----------------------------- | --------------------------- |
| < 10,000 jobs                 | Under 5 minutes             |
| 10,000 - 50,000 jobs          | 5–20 minutes                |
| 50,000 - 100,000 jobs         | 20–45 minutes               |
| > 100,000 jobs                | 45 minutes–2 hours          |

Note:

These duration figures are estimates. Actual duration depends on job complexity, number of hosts per job, database performance, and system load.

## Disable telemetry data collection

You can disable and enable the telemetry data collection feature for Ansible automation portal by updating the Helm chart for your OpenShift Container Platform project.

### Procedure

1. Log in to the OpenShift Container Platform console and open the project for Ansible automation portal in the **Developer** perspective.
2. Navigate to **Helm**.
3. Click the **More actions ⋮** icon for your Ansible automation portal Helm chart and select Upgrade.
4. Select YAML view.
5. Locate the `redhat-developer-hub.global.dynamic.plugins` section of the Helm chart.
6. To disable telemetry data collection, add the following lines to the `redhat-developer-hub.global.dynamic.plugins` section.
  

```
redhat-developer-hub:
  global:
    # ...
    dynamic:
      plugins:
        - disabled: true
          package: >-
            ./dynamic-plugins/dist/backstage-community-plugin-analytics-provider-segment
```

    To re-enable telemetry data collection, delete these lines.

7. Click Upgrade to apply the changes to the Helm chart and restart the pod.
