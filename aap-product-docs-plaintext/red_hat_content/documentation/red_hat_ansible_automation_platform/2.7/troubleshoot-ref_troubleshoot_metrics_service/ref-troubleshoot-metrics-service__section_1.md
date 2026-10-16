# Troubleshoot metrics service
## Troubleshoot events collector

**Events collector timeout or slow performance**

**Symptom**: The `main_jobevent_service` task shows `failure` status or takes longer than expected in the `/api/v1/tasks/` output.

**Cause**: Large deployments with high job volumes can exceed the 3600-second task timeout when processing job events. The stuck-task detector marks timed-out tasks as failed.

**Resolution:**

- Check the current limit settings:
* `JOBEVENT_ROW_LIMIT` (default: 200,000) - controls maximum rows processed per cycle
* `JOBEVENT_JOB_LIMIT` (default: 1,000) - controls maximum jobs processed per cycle
- Reduce the limits to lower values to decrease processing time. The collector has a built-in time-budget check that stops processing early and marks the collection as partial (not failed) if it risks exceeding the timeout.
- Verify the collector completes within the hourly window by querying the tasks API:

```
curl
https://<gateway-route>/api/metrics/v1/tasks/?name=main_jobevent_services&limit=5 \
-H "Authorization: Bearer <token>"
```

Note:

A collection cycle that completes within the hourly window but takes an extended time (for example, 50 minutes) still indicates a problem. Long-running SQL queries consume database resources that affect automation controller performance. If the `main_jobevent_service` task regularly takes more than a few minutes to complete, reduce `JOBEVENT_ROW_LIMIT` and `JOBEVENT_JOB_LIMIT` to lower values even if the task is not timing out.

