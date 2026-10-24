# Configure automation dashboard during containerized installation

Enable automation dashboard data collection during the initial installation to start collecting ROI and cost analysis data without post-installation configuration.

## Before you begin

- Red Hat Ansible Automation Platform 2.7 containerized installer downloaded and extracted
- Infrastructure meets metrics service deployment requirements
- Metrics service enabled (required dependency)

## About this task

Automation dashboard data collection is enabled by default when metrics service is installed during the initial containerized installation of Red Hat Ansible Automation Platform 2.7. Dashboard data collection starts within 1 hour of installation completion, allowing you to establish a baseline for ROI analysis from the first day of platform operation. This procedure describes how to verify dashboard enablement.

## Procedure

1. Configure inventory file. Automation dashboard is enabled by default.
Edit your Ansible Automation Platform containerized installer inventory file. Ensure metrics service is configured by adding a host to the `[automationmetrics]` group.

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
```

Note:
The `[automationmetrics]` group defines which node runs metrics service. Adding a host to this group automatically enables metrics service. There is no separate `automationmetrics_enabled` variable. The host in `[automationmetrics]` does not need to be colocated with `[automationcontroller]`.

2. Run the containerized installation program.


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
2. **Database migration:** Runs `automation-metrics-init` container to create dashboard tables from `apps/dashboard_reports/migrations/`
3. **Data collection scheduling:** Configures dashboard collection tasks
Note:
The installer log does not indicate when dashboard collection is enabled. Use the following post-installation verification steps to confirm that automation dashboard is active.

3. Verify dashboard is enabled
After installation completes, verify dashboard collection is active:

1. Verify dashboard tables exist


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

2. Check metrics service logs for collection activity

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

{"timestamp": "2026-07-21T03:05:27.033Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'sync_dashboard_job_records' complete: Task sync_dashboard_job_records completed successfully"}

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

Dashboard RBAC permissions are configured automatically by the installer based on Red Hat Ansible Automation Platform roles. Previously existing Platform Admins and System Auditors can access the dashboard once enabled. The following roles have dashboard access:

- **Administrator:** Full read/write access to all dashboard data and configuration
- **System Auditor:** Read-only access to all dashboard data and visualizations
