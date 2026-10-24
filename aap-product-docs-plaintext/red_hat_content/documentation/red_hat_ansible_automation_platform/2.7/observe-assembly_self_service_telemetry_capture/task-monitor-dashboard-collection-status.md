# Capture telemetry data for the Ansible self-service portal
## Configure automation dashboard post-installation
### Monitor data collection status for automation dashboard

Monitor the status of automation dashboard data collection to verify data freshness, check sync progress, and troubleshoot stale or missing data.

#### Before you begin

- Automation dashboard is enabled and metrics service is installed.
- You have a dashboard viewer or editor role in Ansible Automation Platform.
- You have access to the Ansible Automation Platform API.

#### Procedure

1. Check the current status of dashboard data collection by sending a GET request to the collection status endpoint:


```
GET /api/metrics-service/v1/metrics-dashboard/collection-status/
```

The response includes the following fields:

| Field               | Description                                               |
| ------------------- | --------------------------------------------------------- |
| `last_run`          | Timestamp of the last completed collection cycle.         |
| `status`            | Current status:`completed`,`in_progress`, or`failed`.     |
| `duration_seconds`  | Duration of the last collection cycle in seconds.         |
| `records_processed` | Number of records processed in the last collection cycle. |
| `next_run`          | Timestamp of the next scheduled collection cycle.         |

2. If you enabled automation dashboard for the first time or after an upgrade, check the progress of the historical data backfill:


```
GET /api/metrics-service/v1/metrics-dashboard/backfill-status/
```

The response includes the following fields:

| Field                       | Description                                    |
| --------------------------- | ---------------------------------------------- |
| `backfill_status`           | Current status:`in_progress` or`completed`.    |
| `progress_percentage`       | Percentage of historical data processed.       |
| `estimated_completion_time` | Estimated time for the backfill to complete.   |
| `records_processed`         | Number of historical records processed so far. |
Note:
Initial backfill can process up to 90 days of historical data and may take several hours depending on data volume. Subsequent hourly collection cycles process only new and updated records.

3. Interpret the collection status to determine whether action is needed:
| Status        | Meaning                                                                                                           | Action                                                                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `completed`   | The last collection cycle finished successfully. Dashboard data is current within the 1-hour collection interval. | No action needed.                                                                                                                          |
| `in_progress` | A collection cycle is running. Normal duration is less than 30 minutes.                                           | No action needed. If the cycle exceeds 30 minutes, check metrics service logs for errors.                                                  |
| `failed`      | The last collection cycle encountered an error.                                                                   | Check metrics service logs for error details. Verify database connectivity between metrics service and the automation controller database. |

#### Results

Verify that data collection is operating normally by confirming all of the following:

- The `last_run` timestamp is within the last hour.
- The collection status is `completed`.
- If a backfill is in progress, the `progress_percentage` is increasing over time.

