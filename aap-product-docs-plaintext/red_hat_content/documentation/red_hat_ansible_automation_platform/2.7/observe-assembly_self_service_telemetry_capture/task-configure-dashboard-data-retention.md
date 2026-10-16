# Capture telemetry data for the Ansible self-service portal
## Configure automation dashboard post-installation
### Configure data retention for automation dashboard

Configure how long automation dashboard retains job execution data to balance your reporting needs with storage capacity.

#### Before you begin

- You have the Platform Administrator role in Ansible Automation Platform.
- Metrics service is installed on your Ansible Automation Platform 2.7 deployment.
- You have access to the Ansible Automation Platform API.
- You know your organization's data retention requirements (for example, compliance frameworks or reporting needs).

#### About this task

Dashboard data retention is controlled by the `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` setting, which determines whether dashboard data follows the automation controller's retention period or uses an independent retention period.

| Setting                                          | Value          | Behavior                                                                                                                                                                     |
| ------------------------------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` | True (default) | Dashboard data retention matches the automation controller retention period. When controller data is purged, corresponding dashboard records are also deleted.               |
| `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` | False          | Dashboard uses an independent retention period configured through`retention_days` in the metrics service settings API. Default and recommended: 90 days. Range: 90-730 days. |

Warning:

When dashboard retention syncs with the controller setting (`DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION: True`, the default), any data in the metrics service database older than the controller retention period will be deleted. Verify your controller retention period before enabling dashboard collection. If the controller retention period is shorter than the dashboard's previous retention period (default: 90 days), enabling this sync will permanently delete dashboard data older than the controller retention period.

#### Procedure

1. Determine your retention requirements.
Consider the following when choosing a retention period:

| Consideration           | Guidance                                                                                                                                                              |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compliance requirements | Some compliance frameworks require specific retention periods (for example, SOC 2 requires 1 year, HIPAA requires up to 7 years). Check your organizational policies. |
| Reporting needs         | Year-over-year comparisons require at least 13 months of data. Quarterly trend reports require at least 4 months.                                                     |
| Storage capacity        | Longer retention periods require more database storage.                                                                                                               |
Note:
The default retention period is 90 days. The maximum configurable retention period is 730 days (2 years).

2. Choose your retention mode.
- **Use controller-synced retention (default):** If the automation controller retention period meets your dashboard reporting needs, no action is required. Dashboard data retention automatically follows the controller setting.
- **Set an independent retention period:** If you need a different retention period for dashboard data, disable controller sync by setting `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` to `false`. See the following substeps.
For containerized installations, add the following to your inventory file:

```
automationmetrics_extra_settings='[{"setting": "DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION", "value": "false"}]'
```

For operator installations, add the following to your AnsibleAutomationPlatform custom resource:

```
spec:
metrics:
extra_settings:
- setting: DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION
value: "false"
```

3. If you chose to set an independent retention period, configure the retention period by using the metrics service settings API:


```
curl -X PATCH \
https://<aap-host>/api/metrics-service/v1/settings/ \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"retention_days": 365}'
```

Replace the following values:

- `<aap-host>`: Your Ansible Automation Platform hostname.
- `<token>`: A valid API token with Platform Administrator permissions.
- `365`: Your desired retention period in days (90-730).

4. Verify that the retention period is set correctly:


```
curl -X GET \
https://<aap-host>/api/metrics-service/v1/settings/ \
-H "Authorization: Bearer <token>"
```

In the response, verify that `retention_days` matches your configured value and check the `cleanup_schedule` field.

Note:
The retention cleanup task runs weekly on Sundays at 2:00 AM UTC. Data older than the configured retention period is deleted during cleanup.

5. **Optional:** To delete expired data immediately rather than waiting for the weekly cleanup schedule, trigger a manual cleanup:


```
curl -X POST \
https://<aap-host>/api/metrics-service/v1/metrics-dashboard/cleanup/ \
-H "Authorization: Bearer <token>"
```

Use manual cleanup when:

- You reduced the retention period and need to reclaim storage immediately.
- You need to verify that cleanup is working correctly.

#### Results

Verify that data retention is configured correctly by confirming the following:

- The `retention_days` value in the settings API response matches your configured retention period.
- The cleanup schedule shows the expected run time (default: Sundays at 2:00 AM UTC).
- The date range available in the dashboard UI reflects the configured retention period.

#### What to do next

Important:

If you are upgrading from a previous release, the default retention behavior change may affect existing data. If the automation controller retention period is shorter than the dashboard's previous retention period (default: 90 days), any dashboard data older than the controller retention period will be deleted after the upgrade. To preserve existing dashboard data, set `DASHBOARD_COLLECTION__USE_CONTROLLER_RETENTION` to `false` in your inventory file before upgrading.

