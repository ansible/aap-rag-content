# Understand metrics service architecture
## Complete task schedule

*Figure 3. Task system module*
![Architectural diagram for metrics service and automation dashboard task system module](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/automation-dashboard-task-system-module.png)

Metrics service uses three task groups:

**METRICS_COLLECTION group**

Gated by `METRICS_COLLECTION` feature flag (default: `true`). When disabled, all tasks in this group skip execution.

| Task                                                 | Schedule            | Description                                                                        |
| ---------------------------------------------------- | ------------------- | ---------------------------------------------------------------------------------- |
| `collect_hourly_metrics` (job\_host\_summary)        | Every hour at XX:05 | Collects job host summary metrics from controller database                         |
| `collect_hourly_metrics` (unified\_jobs)             | Every hour at XX:10 | Collects unified jobs metrics from controller database                             |
| `collect_hourly_metrics` (credentials)               | Every hour at XX:15 | Collects credentials usage metrics from controller database                        |
| `collect_hourly_metrics` (main\_jobevent\_service)   | Every hour at XX:20 | Collects collection, module, and role usage from job events in controller database |
| `collect_snapshot_metrics` (execution\_environments) | Daily at 1:00 AM    | Snapshot of execution environment configuration                                    |
| `collect_snapshot_metrics` (config)                  | Daily at 1:30 AM    | Snapshot of system configuration                                                   |
| `collect_snapshot_metrics` (controller\_version)     | Daily at 1:35 AM    | Snapshot of controller version information                                         |
| `collect_snapshot_metrics` (table\_metadata)         | Daily at 1:40 AM    | Snapshot of database table metadata                                                |
| `collect_snapshot_metrics` (feature\_flags)          | Daily at 1:45 AM    | Snapshot of feature flag states                                                    |
| `collect_daily_metrics` (task\_executions)           | Daily at 1:50 AM    | Pipeline health metrics (task execution observability)                             |
| `daily_metrics_rollup`                               | Daily at 2:00 AM    | Aggregates hourly data into daily summaries                                        |
| `cleanup_metrics_data`                               | Daily at 4:00 AM    | Purges expired data based on retention policies                                    |

**ANONYMIZATION group**

Gated by `ANONYMIZED_DATA_COLLECTION` feature flag (default: `true`). When disabled, anonymization and transmission skip execution.

| Task                          | Schedule         | Description                                            |
| ----------------------------- | ---------------- | ------------------------------------------------------ |
| `daily_anonymize_and_prepare` | Daily at 3:00 AM | Anonymizes collected data and transmits to Segment.com |

**SYSTEM group**

Always enabled regardless of feature flag state. System maintenance tasks continue even when all collection is disabled.

| Task                | Schedule         | Description                                     |
| ------------------- | ---------------- | ----------------------------------------------- |
| `cleanup_old_tasks` | Daily at 5:00 AM | Purges old task execution records from database |
| `hello_world`       | Every hour       | Health check heartbeat for monitoring           |

**Task dependencies**

Tasks are scheduled in dependency order:

1. **Hourly collection** (XX:05, XX:10, XX:15, XX:20) - provides raw data
2. **Daily snapshots** (1:00 AM - 1:50 AM) - supplements hourly data
3. **Daily rollup** (2:00 AM) - aggregates hourly data (depends on hourly collectors completing)
4. **Anonymization** (3:00 AM) - anonymizes aggregated data (depends on rollup completing)
5. **Cleanup** (4:00 AM, 5:00 AM) - purges old data (runs after rollup/anonymization to avoid race conditions)

Important:

If hourly collectors fail, daily rollup will have incomplete data. Always verify hourly collection completed before troubleshooting rollup issues.

Note:

To ensure the readonly user can access tables created in the future, we recommend setting the following default privileges: `ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO ms_awx_readonly;`

