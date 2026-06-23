# Enable automation dashboard post-installation
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

