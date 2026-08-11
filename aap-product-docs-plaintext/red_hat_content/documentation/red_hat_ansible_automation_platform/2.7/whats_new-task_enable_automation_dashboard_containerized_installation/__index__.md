# Enable automation dashboard during containerized installation

Enable automation dashboard data collection during the initial installation to start collecting ROI and cost analysis data without post-installation configuration.

## Before you begin

- Red Hat Ansible Automation Platform 2.7 containerized installer downloaded and extracted
- Infrastructure meets metrics service deployment requirements
- Understanding of Technology Preview features and limitations
- Metrics service enabled (required dependency)

Important:

**Technology Preview:** Automation dashboard is a Technology Preview feature in Red Hat Ansible Automation Platform 2.7 and is disabled by default. You must explicitly enable it by adding the feature flag variable to your inventory file.

## About this task

This procedure enables automation dashboard during the initial containerized installation of Red Hat Ansible Automation Platform 2.7. By adding the dashboard feature flag directly to your inventory file, you eliminate post-installation configuration steps and enable dashboard data collection to start within 1 hour of installation completion. This approach ensures no gap in data collection, allowing you to establish a baseline for ROI analysis from the first day of platform operation and begin capturing all automation activity immediately.

## Procedure

1.  Configure inventory file for metrics service and enable dashboard collection.
Edit your Ansible Automation Platform containerized installer inventory file. Ensure metrics service is configured, and add the dashboard feature flag to the `[all:vars]` section..

```
[automationcontroller]
aap.example.com

[automationmetrics]
aap.example.com

[database]
aap.example.com

[all:vars]
postgresql_admin_username=postgres
postgresql_admin_password=''
feature_flags={'FEATURE_DASHBOARD_COLLECTION_ENABLED':True}
```

| Variable                                                          | Default                          | Purpose                                                                                                                                                                                                  |
| ----------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>`feature_flags={'FEATURE_DASHBOARD_COLLECTION_ENABLED':True}` | <br>Not set (dashboard disabled) | <br>Enables automation dashboard data collection in metrics service (Technology Preview). When enabled, metrics service collects dashboard-specific metrics (cost data, ROI calculations, pricing information) in addition to standard metrics. |
Note:
The `[automationmetrics]` group defines which node runs metrics service. Adding a host to this group automatically enables metrics service. There is no separate `automationmetrics_enabled` variable. The host in `[automationmetrics]` does not need to be colocated with `[automationcontroller]`.

Note:
The `feature_flags` variable uses INI-compatible syntax (Python dictionary format) so it can be added directly to the inventory file. No separate YAML file is required.

2.  Run the containerized installation program.


```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory ansible.containerized_installer.install
```

The installation program performs the following sequence for dashboard enablement:

1. **Metrics service installation:** Installs and configures metrics service backend
- Creates `metrics_service` database
- Creates `metrics_service` user (ALL privileges)
- Creates `ms_awx_readonly` user (SELECT-only on Controller DB)
- Deploys `automation-metrics-web`, `automation-metrics-tasks`, and `automation-metrics-scheduler` containers
2. **Dashboard feature flag configuration:** Sets `feature_flags: {'FEATURE_DASHBOARD_COLLECTION_ENABLED': True}` in metrics service container configuration file
3. **Database migration:** Runs `automation-metrics-init` container to create dashboard tables from `apps/dashboard_reports/migrations/`
4. **Data collection scheduling:** Configures dashboard collection tasks
Note:
The installer log does not indicate when dashboard collection is enabled. Use the following post-installation verification steps to confirm that automation dashboard is active.

3.  Verify dashboard is enabled
After installation completes, verify dashboard collection is active:

1.  Check metrics service container configuration


```
podman exec automation-metrics-web cat /etc/ansible-automation-platform/metrics_service/settings.yaml | grep FEATURE_DASHBOARD_COLLECTION_ENABLED
```

Expected output:

```
FEATURE_DASHBOARD_COLLECTION_ENABLED: True
```

2.  Verify dashboard tables exist


```
podman exec postgresql \
psql -h localhost -U metrics_service -d metrics_service \
-c "SELECT table_name FROM information_schema.tables WHERE table_name LIKE 'dashboard%';"
```

Expected output: Six dashboard tables:

- `dashboard_job_data` - Main record for every job in the AWX database
- `dashboard_job_data_host_summary` - Host summary records by job
- `dashboard_job_data_label` - Labels associated with jobs
- `dashboard_template_metadata` - Job template metadata
- `dashboard_subscription_cost` - Singleton for cost parameters
- `dashboard_filter_set` - Saved user filtersets

3.  Check metrics service logs for collection activity

Note:
Dashboard collection logs appear only after the first collection cycle runs. On a new installation with no historical data, the initial backfill task runs 30 seconds after metrics service starts. Regular hourly collection logs may not appear for up to 1 hour after installation.

```
podman logs --tail 50 automation-metrics-web2>&1 | grep -i dashboard
podman logs --tail 50 automation-metrics-tasks2>&1 | grep -i dashboard
podman logs --tail 50 automation-metrics-scheduler2>&1 | grep -i dashboard
```

Example successful collection output (`automation-metrics-tasks`):

```
{"timestamp": "2026-07-21T03:05:26.953Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'sync_dashboard_job_records' start: Starting sync_dashboard_job_records task"}

{"timestamp": "2026-07-21T03:05:26.953Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'sync_dashboard_jobs_2026-07-21T02:00:00+00:00_0' running: Executing function: sync_dashboard_job_records"}

{"timestamp": "2026-07-21T03:05:26.991Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'sync_dashboard_job_records' processing: Syncing 3 dashboard job records for 2026-07-21T02:00:00+00:00"}

{"timestamp": "2026-07-21T03:05:26.999Z", "level": "INFO", "logger": "apps.dashboard_reports.models", "message": "Created JobData Job 21 - Template: Cleanup Job Details - Status: successful"}

{"timestamp": "2026-07-21T03:05:27.003Z", "level": "INFO", "logger": "apps.dashboard_reports.models", "message": "Created new TemplateMetadata 'Metadata for example-template (ID: 8)' from AWX data."}

{"timestamp": "2026-07-21T03:05:27.009Z", "level": "INFO", "logger": "apps.dashboard_reports.models", "message": "Created JobData Job 22 - Template: example-template - Status: successful"}

{"timestamp": "2026-07-21T03:05:27.014Z", "level": "INFO", "logger": "apps.dashboard_reports.models", "message": "Created JobData Job 23 - Template: example-template - Status: successful"}

{"timestamp": "2026-07-21T03:05:27.020Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'sync_dashboard_job_records' completed: Synced 3 job records for 2026-07-21T02:00:00+00:00"}

{"timestamp": "2026-07-21T03:05:27.033Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'sync_dashboard_job_records' complete: Task sync_dashboard_job_records completed successfully"} jellyfin

{"timestamp": "2026-07-21T03:05:27.033Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'sync_dashboard_jobs_2026-07-21T02:00:00+00:00_0' completed: Task execution finished with status: completed"}

{"timestamp": "2026-07-21T03:10:26.954Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'sync_dashboard_host_summaries' start: Starting sync_dashboard_host_summaries task"}
```

Example scheduling output (`automation-metrics-scheduler`):

```
{"timestamp": "2026-07-21T13:05:26.866Z", "level": "INFO", "logger": "apps.tasks.cron_scheduler", "message": "Found new immediate task: sync_dashboard_jobs_2026-07-21T12:00:00+00:00_0 (ID: 170) - executing now"}

{"timestamp": "2026-07-21T13:05:26.907Z", "level": "INFO", "logger": "apps.tasks.cron_scheduler", "message": "Executing database task: sync_dashboard_jobs_2026-07-21T12:00:00+00:00_0 (ID: 170)"}

{"timestamp": "2026-07-21T13:05:26.946Z", "level": "INFO", "logger": "apps.tasks.tasks_system", "message": "Submitted task sync_dashboard_jobs_2026-07-21T12:00:00+00:00_0 (ID: 170) to dispatcher queue dashboard"}
```

**Common warning and error messages**

If dashboard collection encounters issues, you may see these log messages:

**Errors:**

- `Error collecting jobs: <reason>`
- `Error creating/updating JobData for job <id>: <reason>`
- `Error during cleanup of old JobData records: <reason>`
- `cleanup_dashboard_reports_old_data: retention_period_days=<value> is not a valid integer; aborting cleanup`
**Warnings:**

- `Warning: Failed to close AWX DB connection in _collect_data()`
- `retention_period_days=<n> is negative ... clamping to 0`
- `Race condition creating TemplateMetadata for '<name>'; fetching existing record.`

## Results

Dashboard is successfully enabled when:

- `podman exec automation-metrics-web cat /etc/ansible-automation-platform/metrics_service/settings.yaml | grep FEATURE_ENABLED` shows `FEATURE_ENABLED: {'DASHBOARD_COLLECTION': True}`
- Six dashboard tables exist in `metrics_service` database
- Metrics service logs show dashboard collection tasks scheduled
- Dashboard UI accessible in Ansible Automation Platform unified UI (after first collection cycle completes)

## What to do next

**What happens next**

After installation, the dashboard enablement sequence is:

1. **30 seconds after metrics service starts:** Initial backfill task (`initial_dashboard_collection`) begins
2. **Backfill in progress:** Metrics service collects up to 90 days of historical data from Controller database (if available)
3. **Backfill completes:** Dashboard UI displays collected data
4. **Regular collection starts:** 1-hour collection schedule (`daily_dashboard_collection`) begins running

**Time to first data:**

- **New installations with no historical jobs:** Dashboard data appears within minutes after backfill completes
- **Installations with substantial Controller history:** The backfill process involves retrieving and storing historical records. The duration of this task is contingent upon the volume of data currently residing in the automation controller database.

Note:

Dashboard RBAC permissions are configured automatically by the installer based on Red Hat Ansible Automation Platform roles. Only Administrators have full access. Other roles do not have access to the automation dashboard.
