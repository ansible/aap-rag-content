# Configure automation dashboard during operator installation

Enable automation dashboard using declarative Custom Resource configuration to leverage operator-managed dashboard deployment.

## Before you begin

- AnsibleAutomationPlatform CR has been deployed and reconciled successfully
- Metrics service enabled in the AnsibleAutomationPlatform CR (`spec.metrics` section present with `disabled: false`)
- You are running Ansible Automaton Platform operator (`aap-operator`) and metrics service operator (`automationmetricsservice-operator`) running

## About this task

Automation dashboard data collection is enabled by default for Red Hat Ansible Automation Platform 2.7 deployments using the operator on Kubernetes or OpenShift. The operator automatically propagates the configuration to metrics service within the reconciliation cycle (typically under 2 minutes). This procedure describes how to verify dashboard enablement.

## Procedure

1. Edit the AnsibleAutomationPlatform Custom Resource
Edit your existing `AnsibleAutomationPlatform` CR .

```
kubectl edit AnsibleAutomationPlatform <aap-cr-name> -n <namespace>
```

Or, if using OpenShift:

```
oc edit AnsibleAutomationPlatform <aap-cr-name> -n <namespace>
```

| Field                   | Default | Purpose                                                                          |
| ----------------------- | ------- | -------------------------------------------------------------------------------- |
| `spec.metrics.disabled` | `false` | Enables the metrics service component. Must be`false` for dashboard to function. |
Save and exit. The Ansible Automation Platform operator automatically begins reconciliation.

2. Verify Ansible Automation Platform operator reconciliation
The Ansible Automation Platform operator reconciles the AnsibleAutomationPlatform CR. Check the Ansible Automation Platform operator logs:

```
kubectl logs -n <namespace> \
deployment/aap-gateway-operator-controller-manager | tail -20
```

Look for reconciliation activity on your Ansible Automation Platform CR name.

3. Verify metrics service pods restarted
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

4. Verify dashboard tables created


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

- Three metrics service pods running (web, tasks, scheduler)
- Six dashboard tables exist in `metrics_service` database

## Troubleshoot

**Dashboard UI returns 403 Forbidden errors**

**Symptom:** Dashboard navigation appears in AAP UI but clicking it shows authentication errors

**Cause:** Gateway has not registered metrics service for routing and authentication (known issue in early builds)
