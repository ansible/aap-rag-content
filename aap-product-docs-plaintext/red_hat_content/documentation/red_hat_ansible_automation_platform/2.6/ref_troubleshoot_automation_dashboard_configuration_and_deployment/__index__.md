# Troubleshoot automation dashboard configuration and deployment

Diagnose automation dashboard issues including Gateway integration failures, RBAC access problems, UI feature limitations, and data collection errors.

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

## Issue 2: System Auditor cannot access dashboard (RBAC broken)

**Symptom**

- System Auditor role users cannot see dashboard navigation item in Ansible Automation Platform UI
- Attempting to access dashboard URL directly shows access denied or 404
- Only Administrator role users can access dashboard


**Expected behavior:** System Auditor should have read-only access to dashboard

**Actual behavior:** Dashboard completely unavailable to System Auditor role

**Root cause**

Dashboard RBAC permissions not correctly registered for System Auditor role. The dashboard permission model assumes both Administrator (read/write) and System Auditor (read-only) access, but implementation only grants access to Administrators.

**Diagnostic commands**

1.      Verify user role:



```
# Check user's role assignments in AAP
# Navigate to: Access → Users → [username] → Roles
```
Confirm user has System Auditor role.

2.      Check dashboard visibility in UI:

Log in as System Auditor user and check if "Automation dashboard" appears in navigation menu.

**Solution**

**Technology Preview Limitation:**

If System Auditor access is not working in your Ansible Automation Platform 2.7 build:

1.      **Grant Administrator role temporarily:**

For users who need dashboard access during Technology Preview period:

- Navigate to Access> (and then)Users> (and then)[username]
- Add Administrator role

Warning:
This grants full admin access, not just dashboard read-only

2.      **Use dedicated dashboard admin account:**

Create a separate admin account specifically for dashboard access:

- Username: `dashboard-viewer`
- Role: Administrator
- Purpose: Dashboard viewing only

**Verification after fix**

- **Log in as System Auditor:** Use account with only System Auditor role (no Administrator role)

- **Verify dashboard visible:** "Automation dashboard" navigation item appears in Ansible Automation Platform UI

-      **Verify read-only access:**

* Can view all dashboard data
* Cannot modify cost settings
* Cannot create/modify/delete saved reports (filter sets)

Important:

**Automation dashboard access (Technology Preview):**

- **Administrator:** Full read/write access
- **System Auditor:** Not available in Technology Preview. Workaround: Grant Administrator role to users requiring dashboard access.

## Issue 3: Date range and currency selectors not working (UI features missing)

**Symptom**

- Cannot select custom date ranges in dashboard UI
- Date range selector shows only predefined options (or is missing entirely)
- Cannot change currency in dashboard settings
- All cost values display in USD only


**Root cause**

Custom date range selection and currency selector features are not implemented in Ansible Automation Platform 2.7 Technology Preview dashboard UI.

**Impact**

**Technology Preview Limitations:**

- **Date filtering:** Users can only use predefined date range options (Last 7 days, Last 30 days, Last 90 days, etc.)
- **Currency:** All cost values display in USD. Multi-currency support not available.


**Solution**

**Workaround:**

No workaround is available for Technology Preview.

Important:

**Date range filtering (Technology Preview limitation):**

In Ansible Automation Platform 2.7 Technology Preview, dashboard supports the following predefined date ranges:

- Last 7 days
- Last 30 days
- Last 90 days


Custom date range selection (choosing specific start and end dates) is not available in Technology Preview.

Important:

**Cost currency (Technology Preview limitation):**

In Ansible Automation Platform 2.7 Technology Preview, all dashboard cost values display in USD ($). Currency selection and multi-currency support are not available in Technology Preview.

## Issue 4: Duplicate saved report names allowed

**Symptom**

- Creating a saved report (filter set) with an existing name succeeds
- No warning or error message displayed
- No overwrite confirmation dialog
- Results in two different reports with identical names in the list


**Root cause**

Dashboard does not validate saved report names for uniqueness. The system allows multiple reports with the same name, relying on internal IDs to differentiate them.

**Impact**

User confusion when multiple reports have the same name. Users must open each report to see its filter configuration to determine which is which.

**Solution**

**Workaround:**

Use unique, descriptive names for all saved reports. Include identifying information in the name.

**Best practices:**

- **Good:** "Q1-2026-Production-Org", "Weekly-Template-Usage", "EMEA-Region-ROI"
- **Avoid:** "Test Report", "My Report", "Dashboard" (too generic, likely to duplicate)


**Recommended naming convention:**

```
[Purpose]-[Timeframe/Scope]-[Date Created]

Examples:
- Compliance-Audit-Last-90-Days-2026-04-27
- Executive-Summary-Q1-2026
- Development-Org-Weekly-Usage
```
**Managing duplicate names**

If you have multiple reports with the same name:

1.      **Identify each report:**

- Open each report with duplicate name
- Note the filter configuration
- Determine purpose/owner

2.      **Rename to unique names:**

- Update each report with descriptive unique name
- Save changes

3.      **Delete unwanted duplicates:**

- Remove any obsolete or test reports

**Verification**

Expected behavior:

- Attempting to save report with existing name triggers warning
- User can choose to overwrite or rename
- System prevents unintentional duplicates

## General dashboard troubleshooting

**Dashboard shows no data**

**Possible causes:**

1.      Collection not running:

- Verify metrics service containers running
- Check logs for collection activity

2.      No historical data in Controller:

- New Ansible Automation Platform installation with no jobs run yet
- Controller database recently purged
- Solution: Run some jobs and wait for next collection cycle (6 hours)

3.      Gateway integration broken:

See [Issue 1: Dashboard returns 403 Forbidden errors (Gateway integration failure)](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/ref_troubleshoot_automation_dashboard_configuration_and_deployment#ref-troubleshoot-automation-dashboard-configuration-deployment__issue-gateway-403-forbidden)

4.      RBAC access denied:

See [Issue 2: System Auditor cannot access dashboard (RBAC broken)](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/ref_troubleshoot_automation_dashboard_configuration_and_deployment#ref-troubleshoot-automation-dashboard-configuration-deployment__issue-system-auditor-rbac)

Diagnostic steps:

- Verify data exists in database
- Check metrics service logs for errors
- Verify user has appropriate role
- Test API access directly (bypass UI)


**Dashboard performance is slow**

**Possible causes:**

1.      Large dataset:

- 90 days of data with high job volume
- Complex filter queries

2.      Database performance:

- Metrics service DB colocated with Controller DB (Tech Preview)
- Resource constraints

3.      Network latency:

- Slow connection to Ansible Automation Platform

Solutions:

1.      Reduce date range:

- Use shorter predefined ranges (Last 7 days vs Last 90 days)

2.      Add filters:

- Filter by specific organization, project, or template
- Reduces dataset size

3.      Check database resources:

- Monitor CPU/memory usage during dashboard queries
- Consider separate database for metrics service in GA

Dashboard UI not appearing in navigation

Possible causes:

1.      Feature not enabled:

- Dashboard collection flag not set
- Metrics service not installed

2.      User role insufficient:

- User lacks Administrator or System Auditor role

3.      UI cache:

- Browser cache showing old navigation

**Solutions:**

1.      Verify enablement:

- Check settings.yaml for `FEATURE_DASHBOARD_COLLECTION_ENABLED: true`

2.      Verify user role:

- Ensure user has Administrator role
- NOTE: System Auditor is not working

3.      Clear browser cache:

- Hard refresh (Ctrl+F5) or clear cache completely

## Getting help

If dashboard issues persist:

1.      **Collect diagnostic information:**

- Ansible Automation Platform version and build number
- Deployment type (operator/containerized)
- Metrics service logs (last 100 lines)
- Gateway logs (last 100 lines)
- Dashboard configuration (inventory file or CR)
- Specific error messages

2.      **Contact Red Hat Support:**

- Provide diagnostic information
- Reference relevant Jira ticket if applicable
- Specify Technology Preview status
