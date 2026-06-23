# Troubleshoot automation dashboard configuration and deployment
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

See [Issue 1: Dashboard returns 403 Forbidden errors (Gateway integration failure)](/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-ref_troubleshoot_automation_dashboard_configuration_and_deployment#ref-troubleshoot-automation-dashboard-configuration-deployment__issue-gateway-403-forbidden)

4.      RBAC access denied:

See [Issue 2: System Auditor cannot access dashboard (RBAC broken)](/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-ref_troubleshoot_automation_dashboard_configuration_and_deployment#ref-troubleshoot-automation-dashboard-configuration-deployment__issue-system-auditor-rbac)

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

