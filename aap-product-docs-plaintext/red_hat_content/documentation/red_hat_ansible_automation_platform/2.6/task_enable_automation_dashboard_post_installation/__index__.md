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
