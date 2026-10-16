# Troubleshoot automation dashboard
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

