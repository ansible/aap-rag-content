+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-task_enable_automation_dashboard_post_installation"
title = "Enable automation dashboard post-installation - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-task_enable_automation_dashboard_post_installation/aem-page/whats_new-task_enable_automation_dashboard_post_installation.html"
last_crumb = "Enable automation dashboard post-installation"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Enable automation dashboard post-installation"
oversized = "false"
page_slug = "whats_new-task_enable_automation_dashboard_post_installation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-task_enable_automation_dashboard_post_installation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-task_enable_automation_dashboard_post_installation/toc/toc.json"
type = "aem-page"
+++

# Enable automation dashboard post-installation

Activate dashboard data collection with automatic historical data backfill to generate comprehensive usage and ROI reports without reinstalling the platform or losing historical automation activity data.

## Before you begin

- Red Hat Ansible Automation Platform 2.7 installed and operational
- Metrics service installed and running
- For containerized: access to the installer inventory file
- For operator: `kubectl` or `oc` access and edit permissions on the AnsibleAutomationPlatform CR


Important:

**Technology Preview:** Automation dashboard is a Technology Preview feature in Red Hat Ansible Automation Platform 2.7. Enabling it post-installation triggers up to 90 days of historical data backfill from Controller database. Monitor data collection logs to know when complete dashboard data is available.

## About this task

This procedure enables automation dashboard on an existing Red Hat Ansible Automation Platform 2.7 installation without platform downtime or service disruption. When you enable dashboard collection post-installation, metrics service automatically backfills up to 90 days of historical data from the Controller database, allowing the dashboard UI to display historical trends within hours of enablement. This zero-disruption activation eliminates the need to reinstall the platform and enables 6-hourly automated collection for ongoing dashboard metrics after backfill completion, providing comprehensive usage and ROI reports using both historical and current automation activity data.

## Procedure

 Choose your deployment method and follow the corresponding procedure

- For containerized installation, follow the containerized procedure
- For operator deployment, follow the operator procedure

## Results

After completing the procedure for your deployment method, dashboard is enabled and historical data backfill begins automatically.

## Procedure (containerized installation)

### Procedure

1.  Update inventory file
      Edit your Ansible Automation Platform containerized installer inventory file to add the dashboard collection variable:

```
[all:vars]
postgresql_admin_username=postgres
postgresql_admin_password=''

    # Enable automation dashboard data collection (Technology Preview)
feature_flags:
  FEATURE_DASHBOARD_COLLECTION_ENABLED: true
```

2.  Re-run installer
  

```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory install.yml
```
  Note:
      There is no separate update playbook. Re-running install.yml on an existing installation automatically detects the current state and applies only the necessary updates (in this case, dashboard enablement).

    Expected duration: Approximately 30 minutes for dashboard enablement on an existing installation.

    The installer detects existing Ansible Automation Platform installation and performs dashboard-specific updates:

  - Updates metrics service container settings with `FEATURE_ENABLED: {'DASHBOARD_COLLECTION': True}`
  - Runs the `automation-metrics-init` container to create dashboard tables
  - Restarts metrics service containers — which triggers `initial_dashboard_collection` task creation

3.  Monitor historical data backfill progress
      After enabling automation dashboard, metrics service backfills up to 90 days of historical data from the Controller database (if available). This process runs in the background and may take several hours depending on data volume.

  1.  Check backfill status by using CLI
  

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

  2.  Query database for backfill metadata
  

```
podman exec automation-metrics-database \
  psql -h localhost -U metrics_service -d metrics_service \
  -c "SELECT COUNT(*), MIN(finished), MAX(finished) FROM dashboard_job_data;"
```
        Expected output for successful collection:

    - `COUNT > 0` - Data has been collected
    - `MAX(finished)` close to current date - Collection is up-to-date
        If `COUNT = 0`, no data has been collected yet (backfill may still be in progress or no jobs exist in Controller).

## Procedure (operator deployment)

### Procedure

1.  Edit the AnsibleAutomationPlatform Custom Resource
      Post-installation enablement on the operator uses the same CR edit as during-installation. There is no separate update playbook or process.

```
kubectl edit AnsibleAutomationPlatform <aap-cr-name> -n <namespace>
```
    Or with OpenShift:

```
oc edit AnsibleAutomationPlatform <aap-cr-name> -n <namespace>
```
    Add `spec.feature_flags.FEATURE_DASHBOARD_COLLECTION_ENABLED: true`:

```
spec:
  feature_flags:
    FEATURE_DASHBOARD_COLLECTION_ENABLED: true   # ADD THIS
  metrics:
    disabled: false
    name: <aap-cr-name>-metrics
  # ... rest of your existing spec unchanged
```
    Save and exit. The Ansible Automation Platform operator and automationmetricsservice operator begin reconciliation automatically.

  Note:
      There is no separate update playbook. Unlike the containerized installer, you do not re-run an install command.

2.  Verify the feature flag reached metrics service
      After reconciliation (typically 1–2 minutes), confirm the feature flag appears in the metrics service ConfigMap:

```
kubectl get cm <aap-cr-name>-metrics-env-properties \
  -n <namespace> -o yaml | grep DASHBOARD
```
    Expected output:

```
METRICS_SERVICE_FEATURE_DASHBOARD_COLLECTION_ENABLED: '@bool True'
```

3.  Verify metrics service pods restarted with new configuration
      After the ConfigMap is updated, the operator restarts the metrics service pods. Confirm they are running and the pod age reflects the restart:

```
kubectl get pods -n <namespace> -l app.kubernetes.io/name=<aap-cr-name>-metrics
```
    Expected: Three pods running (metrics-web, metrics-tasks, metrics-scheduler), age matching the time since reconciliation.

4.  Monitor historical data backfill progress
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

5.  Query database for backfill status
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

## Historical data backfill details

Understand how automation dashboard backfills historical data after post-installation enablement by learning the backfill scope, behavior, performance impact, and duration estimates for dashboard data collection.

### Backfill scope and behavior

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

### Backfill process control

The backfill process runs to completion automatically and cannot be paused or resumed. Once initiated, it continues until all available data within the 90-day window is collected. If metrics service is restarted during backfill, the process resumes from the last successful checkpoint.

### Performance impact and duration

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

## Difference between automation dashboard enablement during-installation and post-installation

Use this reference when choosing between during-installation and post-installation dashboard enablement to compare historical data collection, downtime requirements, and time to availability.

### Comparison of enablement approaches

| Aspect               | During Installation                        | Post-Installation                                   |
| -------------------- | ------------------------------------------ | --------------------------------------------------- |
| When to use          | New Ansible Automation Platform deployment | Existing Ansible Automation Platform installation   |
| Historical data      | No historical data (new installation)      | Up to 90 days backfilled                            |
| Downtime             | Part of initial installation               | None (container restart only)                       |
| Time to dashboard    | Immediate after first collection (6 hours) | Available after backfill completes (hours to 1 day) |
| Configuration effort | One-time during install                    | Update inventory/CR and re-run installer            |

### Decision criteria

**Choose during-installation enablement when:**

- Deploying a new Ansible Automation Platform environment
- No historical data needed (starting fresh)
- You want dashboard available immediately after first collection cycle
- Installation downtime is already planned


**Choose post-installation enablement when:**

- Ansible Automation Platform is already in production
- You need historical data from existing automation jobs
- Zero downtime is required
- You want to evaluate dashboard with real historical trends
