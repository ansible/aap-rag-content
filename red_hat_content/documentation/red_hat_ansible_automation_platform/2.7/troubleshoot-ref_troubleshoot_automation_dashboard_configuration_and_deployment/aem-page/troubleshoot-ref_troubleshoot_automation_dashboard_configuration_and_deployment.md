+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_automation_dashboard_configuration_and_deployment"
template = "docs/aem-title.html"
title = "Troubleshoot automation dashboard - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_automation_dashboard_configuration_and_deployment/", "Troubleshoot automation dashboard"]]
category = "Troubleshoot"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_automation_dashboard_configuration_and_deployment/aem-page/troubleshoot-ref_troubleshoot_automation_dashboard_configuration_and_deployment.html"
last_crumb = "Troubleshoot automation dashboard"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Troubleshoot automation dashboard"
oversized = "false"
page_slug = "troubleshoot-ref_troubleshoot_automation_dashboard_configuration_and_deployment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_automation_dashboard_configuration_and_deployment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_automation_dashboard_configuration_and_deployment/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot automation dashboard

Diagnose automation dashboard issues where job counts, user totals, or cost configuration values differ from expected results.

## Issue 1: Job counts differ between the automation dashboard and the Controller

**Symptom**

- Successful or Failed job counts on the automation dashboard do not match the counts shown on the Controller Jobs page.
- The dashboard count is typically lower than or equal to the Controller count for the same time period, because the dashboard counts only a subset of job types.

The automation dashboard and the Controller use different methods to count jobs. The dashboard collects and reports only playbook run jobs with a terminal status of successful or failed.

The dashboard excludes the following job types from its counts:

- Inventory sync jobs
- Project update jobs
- System and maintenance jobs (such as `cleanup_jobs` and `cleanup_activitystream`)
- Workflow parent jobs
- Jobs with a non-terminal status (running, pending, waiting, canceled, error)

The Controller Jobs page displays all job types by default. When you apply filters on the Controller, the API processes the filtered query differently than the dashboard collection query, which can produce minor count differences.

**Root cause**

The dashboard collection layer and the Controller API apply different filtering and counting logic. The dashboard counts jobs at collection time using the metrics-utility collector, while the Controller counts jobs at query time using the Unified Jobs API. These two code paths can produce slightly different results, especially for:

- Workflow child jobs (jobs spawned as nodes inside a workflow run)
- Jobs that completed during a collection cycle boundary
- Filtered queries where the Controller API applies RBAC scoping

**Diagnostic steps**

1. Filter the Controller Jobs page to Status = Successful and Type = Playbook Run.

2. Compare this filtered count to the dashboard Successful jobs count for the same date range.

3. Check if the discrepancy is consistent or intermittent:

  - A consistent 2x difference indicates workflow child jobs are being double-counted. Contact Red Hat Support.
  - A difference of 1-2 jobs is expected and does not indicate a data integrity issue.

4. Check metrics service collection logs for errors:

```
# Operator deployment
kubectl logs -n ansible-automation-platform <metrics-web-pod> | grep -i "collection"

    # Containerized deployment
podman logs automation-metrics-tasks | grep -i "collection"
```

**Solution**

- To compare job counts accurately, filter the Controller Jobs page to Status = Successful (or Failed) and Type = Playbook Run before comparing to the dashboard.
- Small discrepancies (1-2 jobs) between the dashboard and the filtered Controller count are expected and do not indicate a data integrity issue.
- If you see a consistent large discrepancy (2x or more), contact Red Hat Support.

## Issue 2: Top 5 users total does not match the successful and failed job totals

**Symptom**

- The sum of jobs displayed in the Top 5 users widget is lower than the combined Successful and Failed job counts on the dashboard summary cards.
- Users expect the per-user totals to add up to the overall totals.

The Top 5 users widget counts only jobs attributed to individual user accounts. The Successful and Failed summary cards count all jobs regardless of how they were launched.

The following job types are included in the summary card totals but are not attributed to individual users in the Top 5 users widget:

- Scheduled jobs
- Callback jobs
- System-initiated jobs

This is expected behavior.

**Root cause**

Scheduled, callback, and system-initiated jobs run without a specific user context. The dashboard attributes these jobs to the overall totals but cannot assign them to an individual user in the Top 5 users breakdown.

**Solution**

No action is required. The difference between the Top 5 users total and the summary card totals reflects jobs that were not launched by an individual user.

To reconcile the totals:

1. Note the Successful plus Failed total from the summary cards.
2. Note the sum of all jobs in the Top 5 users widget.
3. The difference represents scheduled, callback, and system-initiated jobs that are not attributed to individual users.

## Issue 3: Default manual execution time does not reflect actual job running time

**Symptom**

- The Time taken to manually execute (min) value does not reflect actual job running time and does not change as more jobs run or as job execution data changes.
- New job templates receive a default of 1 minute, consistent with the standalone automation dashboard Utility.
- ROI and cost savings calculations appear inaccurate because the manual execution time can be stale or underestimated.

When the dashboard discovers a new job template during data collection, it sets a system-generated manual execution time. However, the current logic applies a value only when the field is empty. After any value is stored, the dashboard does not recalculate it, so the value persists even when later job execution data changes significantly.

This is most visible when historical job data is removed by retention cleanup while the template metadata remains. The system-generated value can persist with no remaining job data to justify it.

**Root cause**

The `time_taken_manually_execute_minutes` value is recalculated only when the field is empty (`None`). Once a system-generated value is stored, subsequent job runs and retention cleanup do not update it, so the value can drift from actual job execution time.

**Solution**

Manually update the Time taken to manually execute (min) value for each job template to reflect the actual time required to perform the equivalent task manually.

1. Navigate to the automation dashboard.
2. Locate the job template in the jobs table.
3. Update the Time taken to manually execute (min) value to an appropriate estimate.

A common estimation method is to set the manual execution time to 2 times the automated running time, reflecting the additional overhead of manual SSH access, command entry, error checking, and host-by-host execution.

## Getting help

If dashboard issues persist:

1. **Collect diagnostic information:**

  - Ansible Automation Platform version and build number
  - Deployment type (operator/containerized)
  - Metrics service logs (last 100 lines)
  - Gateway logs (last 100 lines)
  - Dashboard configuration (inventory file or CR)
  - Specific error messages

2. **Contact Red Hat Support:**

  - Provide diagnostic information
  - Reference relevant Jira ticket if applicable
  - Specify Technology Preview status
