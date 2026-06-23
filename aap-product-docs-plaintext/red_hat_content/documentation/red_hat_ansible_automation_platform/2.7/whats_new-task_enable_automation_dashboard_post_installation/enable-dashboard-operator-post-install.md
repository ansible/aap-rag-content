# Enable automation dashboard post-installation
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

