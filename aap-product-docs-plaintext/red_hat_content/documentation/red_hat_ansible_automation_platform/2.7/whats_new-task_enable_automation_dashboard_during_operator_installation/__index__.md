# Enable automation dashboard during operator installation

Enable automation dashboard using declarative Custom Resource configuration to leverage operator-managed dashboard deployment with automatic feature flag propagation to metrics service.

## Before you begin

- AnsibleAutomationPlatform CR has been deployed and reconciled successfully
- Metrics service enabled in the AnsibleAutomationPlatform CR (`spec.metrics` section present with `disabled: false`)
- You are running Ansible Automaton Platform operator (`aap-operator`) and metrics service operator (`automationmetricsservice-operator`) running
- Understanding of Technology Preview features and limitations


Important:

**Technology Preview:** Automation dashboard is a Technology Preview feature in Red Hat Ansible Automation Platform 2.7 and is disabled by default. You must explicitly enable it by setting `spec.feature_flags.FEATURE_DASHBOARD_COLLECTION_ENABLED: true` in your AnsibleAutomationPlatform Custom Resource.

## About this task

This procedure enables automation dashboard for Red Hat Ansible Automation Platform 2.7 deployments using the operator on Kubernetes or OpenShift. By configuring the AnsibleAutomationPlatform Custom Resource with the dashboard feature flag, the operator automatically propagates the configuration to metrics service within the reconciliation cycle (typically under 2 minutes). This declarative approach eliminates manual pod configuration and enables version-controlled, GitOps-compatible dashboard state management with 100% operator-managed deployment.

## Procedure

1.  Edit the AnsibleAutomationPlatform Custom Resource
Edit your existing `AnsibleAutomationPlatform` CR to enable the dashboard collection feature flag. The feature flag is set at the top level of `spec`, not inside `spec.metrics`.

```
kubectl edit AnsibleAutomationPlatform <aap-cr-name> -n <namespace>
```
Or, if using OpenShift:

```
oc edit AnsibleAutomationPlatform <aap-cr-name> -n <namespace>
```
Add or update the `feature_flags` section:

```
spec:
feature_flags:
FEATURE_DASHBOARD_COLLECTION_ENABLED: true   # ADD THIS
metrics:
disabled: false
name: <aap-cr-name>-metrics
# ... rest of your existing spec unchanged
```
| Field                                                     | Default          | Purpose                                                                              |
| --------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------ |
| `spec.feature_flags.FEATURE_DASHBOARD_COLLECTION_ENABLED` | `false` (absent) | Enables automation dashboard data collection in metrics service (Technology Preview) |
| `spec.metrics.disabled`                                   | `false`          | Enables the metrics service component. Must be`false` for dashboard to function.     |
Note:
`spec.feature_flags` is a top-level spec field on the AnsibleAutomationPlatform CR. Do not nest it under `spec.metrics`.

Save and exit. The Ansible Automation Platform operator automatically begins reconciliation.

2.  Verify Ansible Automation Platform operator reconciliation
The Ansible Automation Platform operator reconciles the AnsibleAutomationPlatform CR and propagates `FEATURE_DASHBOARD_COLLECTION_ENABLED` to the MetricsService CR. Check the Ansible Automation Platform operator logs:

```
kubectl logs -n <namespace> \
deployment/aap-gateway-operator-controller-manager | tail -20
```
Look for reconciliation activity on your Ansible Automation Platform CR name.

3.  Verify the feature flag reached the metrics service
**Expected output:**

```
METRICS_SERVICE_FEATURE_DASHBOARD_COLLECTION_ENABLED: '@bool True'
```
If this key is absent, the operator has not yet reconciled. Wait 1–2 minutes and re-check.

Note:
The `@bool True` prefix is Dynaconf syntax for boolean values. This is expected and correct.

You can also verify by using the pod environment directly:

```
METRICS_POD=$(kubectl get pods -n <namespace> \
-l app.kubernetes.io/component=metrics-service \
--field-selector=status.phase=Running \
-o jsonpath='{.items[0].metadata.name}')

kubectl exec -n <namespace> $METRICS_POD -- \
env | grep DASHBOARD
```
**Expected output:**

```
METRICS_SERVICE_FEATURE_DASHBOARD_COLLECTION_ENABLED=@bool True
```

4.  Verify metrics service pods restarted
After the ConfigMap is updated, the metrics service pods restart automatically to pick up the new environment variable. Confirm three pods are running:

```
kubectl get pods -n <namespace> | grep metrics
```
**Expected output (on three running pods):**

```
<aap-cr-name>-metrics-web-<hash>        1/1   Running   0   <age>
<aap-cr-name>-metrics-tasks-<hash>      1/1   Running   0   <age>
<aap-cr-name>-metrics-scheduler-<hash>  1/1   Running   0   <age>
```
Note:
There is no separate settings.yaml file in the operator deployment. All metrics service configuration is managed by using the `<name>-metrics-env-properties` ConfigMap.

5.  Verify dashboard tables created


```
# Get database pod
DB_POD=$(kubectl get pods -n <namespace> | grep postgres | awk '{print $1}')

# Check dashboard tables exist
kubectl exec -n <namespace> $DB_POD -- \
psql -U metrics_service -d metrics_service \
-c "SELECT table_name FROM information_schema.tables WHERE table_name LIKE 'dashboard%';"
```
**Expected output:** Six dashboard tables:

- `dashboard_job_data`
- `dashboard_job_data_host_summary`
- `dashboard_job_data_label`
- `dashboard_template_metadata`
- `dashboard_subscription_cost`
- `dashboard_filter_set`

## Results

Dashboard is successfully enabled when:

- `spec.feature_flags.FEATURE_DASHBOARD_COLLECTION_ENABLED: true` is present in the AnsibleAutomationPlatform CR
- `<name>-metrics-env-properties` ConfigMap contains `METRICS_SERVICE_FEATURE_DASHBOARD_COLLECTION_ENABLED: '@bool True'`
- Three metrics service pods running (web, tasks, scheduler)
- Six dashboard tables exist in `metrics_service` database

## Troubleshoot

**Issue: Feature flag not appearing in ConfigMap**

**Symptom:** After editing the Ansible Automation Platform CR, `METRICS_SERVICE_FEATURE_DASHBOARD_COLLECTION_ENABLED` does not appear in the ConfigMap.

**Solution:**

1.      Confirm the change was applied to the Ansible Automation Platform CR:



```
kubectl get AnsibleAutomationPlatform <aap-cr-name> \
-n <namespace> -o yaml | grep -A3 feature_flags
```
Verify `FEATURE_DASHBOARD_COLLECTION_ENABLED: true` is present under `spec.feature_flags`.

2.      Check Ansible Automation Platform operator logs for reconciliation errors:



```
kubectl logs -n <namespace> \
deployment/aap-gateway-operator-controller-manager | grep -i error
```

3.      Check automationmetricsservice operator logs:



```
kubectl logs -n <namespace> \
deployment/automationmetricsservice-operator-controller-manager | tail -30
```

**Dashboard UI returns 403 Forbidden errors**

**Symptom:** Dashboard navigation appears in AAP UI but clicking it shows authentication errors

**Cause:** Gateway has not registered metrics service for routing and authentication (known issue in early builds)
