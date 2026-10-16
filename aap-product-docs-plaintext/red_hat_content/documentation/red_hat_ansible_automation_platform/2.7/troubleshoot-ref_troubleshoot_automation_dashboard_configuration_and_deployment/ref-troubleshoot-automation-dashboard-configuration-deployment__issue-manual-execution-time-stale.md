# Troubleshoot automation dashboard
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

