# Troubleshoot automation dashboard configuration and deployment
## Issue 1: Dashboard returns 403 Forbidden errors (Gateway integration failure)

**Symptom**

- Dashboard navigation item appears in Ansible Automation Platform unified UI
- Clicking dashboard link shows authentication errors
- Browser console shows: `HTTP 403 Forbidden: {"detail":"Authentication credentials were not provided."}`
- Metrics service API endpoints return "no healthy upstream" errors


After enabling `FEATURE_DASHBOARD_COLLECTION_ENABLED: true` on the Ansible Automation Platform CR (operator deployment), the Gateway did NOT automatically register the metrics service. The dashboard UI navigation appeared, but accessing it resulted in 403 Forbidden errors because:

- No metrics service type/cluster/node/service route created in Gateway
- JWT authentication chain (`ANSIBLE_BASE_JWT_KEY`, resource server URL, `service_id`) not configured between Gateway and metrics service
- MetricsService operator did not set `METRICS_SERVICE_FEATURE_DASHBOARD_COLLECTION_ENABLED` env var from the CR


**Root cause**

Gateway has not registered metrics service for routing and authentication. The dashboard feature flag enables dashboard collection in metrics service, but does not automatically configure Gateway to route dashboard API calls.

**Diagnostic commands**

1.      Check if metrics service is running:



```
# Operator deployment
kubectl get pods -n ansible-automation-platform | grep metrics

# Containerized deployment
podman ps | grep automation-metrics
```
Expected: 3 metrics service pods/containers running (web, tasks, scheduler)

2.      Check metrics service logs for JWT authentication errors:



```
# Operator deployment
kubectl logs -n ansible-automation-platform <metrics-web-pod> | grep -i "ANSIBLE_BASE_JWT_KEY"

# Containerized deployment
podman logs automation-metrics-web | grep -i "ANSIBLE_BASE_JWT_KEY"
```
Error indicating Gateway not configured:



```
ansible_base.jwt_consumer.common.cert Failed to get the setting ANSIBLE_BASE_JWT_KEY
```

3.      Check Gateway logs for routing errors:



```
# Operator deployment
kubectl logs -n ansible-automation-platform <gateway-pod> | grep -i metrics

# Look for errors accessing /api/metrics/v1/dashboard_reports/
```
Error indicating no upstream registered:



```
no healthy upstream
```

4.      Check metrics service environment variables:



```
# Operator deployment
kubectl exec <metrics-web-pod> -n ansible-automation-platform -- env | grep -A2 DASHBOARD_COLLECTION

# Containerized deployment
cat /etc/ansible-automation-platform/metrics_service/settings.yaml | grep DASHBOARD
```
Expected output:



```
# Operator deployment
METRICS_SERVICE_FEATURE_DASHBOARD_COLLECTION_ENABLED=true

# Containerized deployment
FEATURE_ENABLED: {'DASHBOARD_COLLECTION': True}
```
If missing or set to `false`:

The MetricsService operator did not properly propagate the `FEATURE_DASHBOARD_COLLECTION_ENABLED: true` setting from the Ansible Automation Platform CR to the metrics service container environment.

This indicates:

- Dashboard collection does not run (even if Gateway is configured)
- CR setting not applied correctly
- Operator may need restart or CR re-application

**Solution**

**For operator deployments (primary affected scenario):**

1.      Verify operator version supports Gateway integration:



```
kubectl get pods -n ansible-automation-platform | grep aap-operator
```
Ensure operator version is `aap-operator.v2.7.0-0.1776445599` or later.

2.      Check Ansible Automation Platform CR feature flag:



```
kubectl get AnsibleAutomationPlatform aap -n aap -o yaml | grep -A5 feature_flags
```
Verify:



```
feature_flags:
FEATURE_DASHBOARD_COLLECTION_ENABLED: true
```

3.      Verify Gateway pod restarted after feature flag enabled:



```
kubectl get pods -n ansible-automation-platform | grep gateway
```
Check pod AGE. This should restart after the CR update.

4.      If Gateway registration still failing:

Contact Red Hat Support for manual Gateway registration procedure. Manual registration requires:

- Creating service type, cluster, node, and service entries in Gateway database
- Configuring JWT authentication chain
- Setting `METRICS_SERVICE_RESOURCE_SERVER__URL` environment variable in metrics service pod

**For containerized deployments:**

Gateway registration should be automatic. If you encounter this issue:

- Verify Gateway and metrics service containers are running
- Check Gateway configuration includes metrics service routes
- Contact Red Hat Support - this issue primarily affects operator deployments


**Verification after fix**

- **Access dashboard UI:** Navigate to Ansible Automation Platform UI → Automation dashboard

- **Verify no authentication errors:** Dashboard should load without 403 Forbidden errors

-      **Check metrics service API accessible:**



```
# From a machine with access to AAP
curl -k -u admin:<password> https://<AAP-FQDN>/api/metrics/v1/dashboard_reports/collection_status/
```
Expected: JSON response (not 403 error)

