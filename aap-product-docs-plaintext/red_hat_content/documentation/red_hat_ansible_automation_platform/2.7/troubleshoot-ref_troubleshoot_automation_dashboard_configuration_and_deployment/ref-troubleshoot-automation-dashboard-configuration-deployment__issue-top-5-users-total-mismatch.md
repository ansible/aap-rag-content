# Troubleshoot automation dashboard
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

