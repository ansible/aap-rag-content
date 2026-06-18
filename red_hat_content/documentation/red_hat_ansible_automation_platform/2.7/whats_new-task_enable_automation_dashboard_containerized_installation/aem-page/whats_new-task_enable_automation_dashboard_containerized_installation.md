+++
template = "docs/aem-title.html"
title = "Enable automation dashboard during containerized installation - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-task_enable_automation_dashboard_containerized_installation"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-task_enable_automation_dashboard_containerized_installation/aem-page/whats_new-task_enable_automation_dashboard_containerized_installation.html"
last_crumb = "Enable automation dashboard during containerized installation"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Enable automation dashboard during containerized installation"
oversized = "false"
page_slug = "whats_new-task_enable_automation_dashboard_containerized_installation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-task_enable_automation_dashboard_containerized_installation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-task_enable_automation_dashboard_containerized_installation/toc/toc.json"
type = "aem-page"
+++

# Enable automation dashboard during containerized installation

Enable automation dashboard data collection during the initial installation to start collecting ROI and cost analysis data without post-installation configuration.

## Before you begin

- Red Hat Ansible Automation Platform 2.7 containerized installer downloaded and extracted
- Infrastructure meets metrics service deployment requirements
- Understanding of Technology Preview features and limitations
- Metrics service enabled (required dependency)


Important:

**Technology Preview:** Automation dashboard is a Technology Preview feature in Red Hat Ansible Automation Platform 2.7 and is disabled by default. You must explicitly enable it by creating a feature flags file and passing it to the installer.

## About this task

This procedure enables automation dashboard during the initial containerized installation of Red Hat Ansible Automation Platform 2.7. By configuring dashboard collection in a feature flags file, you eliminate post-installation configuration steps and enable dashboard data collection to start within 6 hours of installation completion. This approach ensures no gap in data collection, allowing you to establish a baseline for ROI analysis from the first day of platform operation and begin capturing all automation activity immediately.

## Procedure

1.  Configure inventory file for metrics service.
      Edit your Ansible Automation Platform containerized installer inventory file and ensure metrics service is configured. Dashboard requires metrics service as its backend.

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
      The `[automationmetrics]` group defines which node runs metrics service. Adding a host to this group automatically enables metrics service - there is no separate `automationmetrics_enabled` variable. The host in `[automationmetrics]` does not need to be colocated with `[automationcontroller]`.

2.  Create feature flags file to enable dashboard collection.
      Create a feature_flags.yml file in your installer directory with the dashboard collection feature flag:

```
cd /path/to/aap-containerized-installer  
  echo "feature_flags:  
    FEATURE_DASHBOARD_COLLECTION_ENABLED: True" > feature_flags.yml
```
    This creates a YAML file containing:

```
feature_flags:  
    FEATURE_DASHBOARD_COLLECTION_ENABLED: True
```
  Important:
      Do not add `feature_flags` directly to the INI-formatted inventory file. YAML syntax cannot be mixed with INI syntax in the inventory file. Feature flags must be passed to the installer as a separate file using the `-e` flag in Step 3.

    | Variable                               | Default | Purpose                                                                                                                                                                                                                                     |
    | -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `FEATURE_DASHBOARD_COLLECTION_ENABLED` | `False` | Enables automation dashboard data collection in metrics service (Technology Preview). When enabled, metrics service collects dashboard-specific metrics (cost data, ROI calculations, pricing information) in addition to standard metrics. |
  Note:
      Metrics service is enabled by adding a host to the `[automationmetrics]` group (Step 1). There is no separate `automationmetrics_enabled` variable.

3.  Run the containerized installation program with feature flags
  

```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory ansible.containerized_installer.install -e @feature_flags.yml
```
    The `-e @feature_flags.yml` flag passes the feature flags file to the installer as extra variables.

    The installation program performs the following sequence for dashboard enablement:

  1. **Metrics service installation:** Installs and configures metrics service backend
    - Creates `metrics_service` database
    - Creates `metrics_service` user (ALL privileges)
    - Creates `ms_awx_readonly` user (SELECT-only on Controller DB)
    - Deploys `automation-metrics-web`, `automation-metrics-tasks`, and `automation-metrics-scheduler` containers
  2. **Dashboard feature flag configuration:** Sets `feature_flags: {'FEATURE_DASHBOARD_COLLECTION_ENABLED': True}` in metrics service container configuration file
  3. **Database migration:** Runs `automation-metrics-init` container to create dashboard tables from apps/dashboard_reports/migrations/
  4. **Data collection scheduling:** Configures dashboard collection tasks
  Note:
      The installer log does not indicate when dashboard collection is enabled. Use the following post-installation verification steps to confirm that automation dashboard is active.

4.  Verify dashboard is enabled
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
            Dashboard collection logs appear only after the first collection cycle runs. On a new installation with no historical data, the initial backfill task runs 30 seconds after metrics service starts. Regular 6-hourly collection logs may not appear for up to 6 hours after installation.

```
podman logs automation-metrics-web --tail 50 | grep -i dashboard
podman logs automation-metrics-tasks --tail 50 | grep -i dashboard
podman logs automation-metrics-scheduler --tail 50 | grep -i dashboard
```
        Example successful collection output (`automation-metrics-tasks`):

```
{"timestamp": "2026-04-23T12:03:00.066Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'daily_dashboard_collection (Execution 2026-04-23 12:03:00)' completed: Task execution finished with status: completed"}

        {"timestamp": "2026-04-23T12:04:00.028Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'collect_dashboard_reports_data' start: Starting collect_dashboard_reports_data task"}

        {"timestamp": "2026-04-23T12:04:00.034Z", "level": "INFO", "logger": "apps.tasks.utils", "message": "Task 'collect_dashboard_reports_data' processing: Collecting dashboard data for: 2026-04-23T02:51:58.295245+00:00 to 2026-04-23T12:04:00.033289+00:00"}

        {"timestamp": "2026-04-23T12:04:00.048Z", "level": "INFO", "logger": "apps.dashboard_reports.models", "message": "Updated JobData Job 250 - Template: example-template - Status: successful"}

        {"timestamp": "2026-04-23T12:04:00.055Z", "level": "INFO", "logger": "apps.dashboard_reports.models", "message": "Updated 16 JobHostSummary records for JobData Job 250 - Template: example-template - Status: successful"}
```
        Example scheduling output (`automation-metrics-scheduler`):

```
{"timestamp": "2026-04-23T12:05:00.024Z", "level": "INFO", "logger": "apps.tasks.tasks_system", "message": "Submitted task daily_dashboard_collection (Execution 2026-04-23 12:05:00) (ID: 2314) to dispatcher queue dashboard"}

        {"timestamp": "2026-04-23T12:05:00.024Z", "level": "INFO", "logger": "apps.tasks.cron_scheduler", "message": "Recurring task daily_dashboard_collection (ID: 571) remains as template for future executions"}

        {"timestamp": "2026-04-23T12:06:00.014Z", "level": "INFO", "logger": "apps.tasks.cron_scheduler", "message": "Created execution record for recurring task: daily_dashboard_collection → daily_dashboard_collection (Execution 2026-04-23 12:06:00) (ID: 2315)"}
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
4. **Regular collection starts:** 6-hourly collection schedule (`daily_dashboard_collection`) begins running


**Time to first data:**

- **New installations with no historical jobs:** Dashboard data appears within minutes after backfill completes
- **Installations with substantial Controller history:** The backfill process involves retrieving and storing historical records. The duration of this task is contingent upon the volume of data currently residing in the automation controller database.


Note:

Dashboard RBAC permissions are configured automatically by the installer based on Red Hat Ansible Automation Platform roles. Only Administrators have full access. Other roles do not have access to the automation dashboard.
