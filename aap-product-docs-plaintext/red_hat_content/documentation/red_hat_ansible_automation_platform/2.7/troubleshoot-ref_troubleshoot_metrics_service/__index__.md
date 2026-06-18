# Troubleshoot metrics service

Diagnostic procedures and solutions for common metrics service issues to resolve problems and restore data collection.

## Diagnostic commands

```
# Container status
podman ps -a | grep automation-metrics

# Systemd unit status (user scope)
systemctl --user status automation-metrics-web.service
systemctl --user status automation-metrics-tasks.service
systemctl --user status automation-metrics-scheduler.service

# Recent logs
podman logs automation-metrics-web --tail 100
podman logs automation-metrics-tasks --tail 100
podman logs automation-metrics-scheduler --tail 100

# Init container logs (for migration issues)
podman logs automation-metrics-init

# Health endpoint check (via nginx)
# Returns HTTP 2** (e.g., 200) if ok, 50* (e.g., 503) if degraded
curl https://localhost:8450/health/ ( http://localhost:8087/health if HTTPS is disabled).

# Database connectivity
psql -h localhost -U metrics_service -d metrics_service -c "SELECT 1;"
psql -h localhost -U ms_awx_readonly -d awx -c "SELECT COUNT(*) FROM main_job LIMIT 1;"

# Verify Podman secrets (should show 4 secrets)
podman secret ls | grep automationmetrics

# Verify dashboard collection feature flag status
podman exec automation-metrics-web \
env | grep METRICS_SERVICE_FEATURE_ENABLED__DASHBOARD_COLLECTION
```

## Common issues

| Symptom                                                                                           | Possible Cause                                                                                                                                                                                                                                            | Solution                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Installation fails with:**`unable to connect to database: FATAL: database "awx" does not exist` | Separate database host topology issue. metrics service and controller databases on different hosts,`DATABASES__awx__HOST` set incorrectly. OR`controller_pg_database` set to non-default value but`automationmetrics_controller_db` not updated to match. | **Step 1:** Verify`automationmetrics_controller_read_pg_host` points to controller database host.**Step 2:** Verify`automationmetrics_controller_db` matches`controller_pg_database`.**Example fix:** If`controller_pg_database=custom_awx_db`, set`automationmetrics_controller_db=custom_awx_db`.               |
| **Installation fails:**`controller_pg_database` mismatch                                          | `controller_pg_database` set to custom value,`automationmetrics_controller_db` not set to same value                                                                                                                                                      | Set`automationmetrics_controller_db` to match`controller_pg_database` exactly.**Example:**`controller_pg_database=my_custom_awx` requires`automationmetrics_controller_db=my_custom_awx`. Default for`automationmetrics_controller_db` is`awx`, which causes mismatch if controller uses different database name. |
| Container exits immediately                                                                       | Database connection failure                                                                                                                                                                                                                               | Verify database credentials and connectivity                                                                                                                                                                                                                                                                      |
| Port conflict error (ports 8087 or 8450)                                                          | Nginx port already in use                                                                                                                                                                                                                                 | Identify conflicting process:`ss -tulpn | grep 8087`                                                                                                                                                                                                                                                              |
| Permission denied errors                                                                          | SELinux blocking container                                                                                                                                                                                                                                | Check SELinux denials:`ausearch -m avc`                                                                                                                                                                                                                                                                           |
| Connection timeout to Red Hat Data Ingress                                                        | Firewall blocking HTTPS or proxy misconfiguration                                                                                                                                                                                                         | Allow outbound port 443; verify proxy configuration if used                                                                                                                                                                                                                                                       |
| Task appears "stuck" or won't run                                                                 | PostgreSQL advisory lock left held after process crash                                                                                                                                                                                                    | metrics service uses PostgreSQL advisory locks for task concurrency control. If a process crashes (segfault, OOM-kill), the lock may remain held.**Solution:** Restart PostgreSQL or wait for lock timeout. Check for held locks:`SELECT * FROM pg_locks WHERE locktype = 'advisory';`                            |

## Service containers fail to start with validation errors

**New in Ansible Automation Platform 2.7:** Metrics service validates required production environment variables at startup to prevent misconfiguration.

**Symptom:** Service containers fail to start with log messages indicating missing or invalid environment variables.

**Cause:** Required production environment variables are not set or are incorrectly configured.

**Solution:**

1. Check container logs for validation error messages:

```
podman logs automation-metrics-web --tail 50 | grep -i "validation\|error\|required"
```

2. Verify required environment variables are set correctly:

```
podman exec automation-metrics-web env | grep METRICS_SERVICE
```

3. Common validation failures:
| Validation Error                      | Required Variable                    | Solution                                                  |
| ------------------------------------- | ------------------------------------ | --------------------------------------------------------- |
| Database host validation failed       | `METRICS_SERVICE_DB_HOST`            | Verify`automationmetrics_pg_host` is set in inventory     |
| Controller database validation failed | `METRICS_SERVICE_CONTROLLER_DB_HOST` | Verify`automationmetrics_controller_read_pg_host` is set  |
| Secret key validation failed          | `METRICS_SERVICE_SECRET_KEY`         | Verify Podman secret`automationmetrics_secret_key` exists |

4. After fixing environment variables, restart the service:

```
systemctl --user restart automation-metrics-web.service
```

## Rollup processing troubleshooting

Metrics service uses a daily rollup process to aggregate hourly metrics data. The following scenarios describe common rollup issues and solutions.

**Scenario 1: Rollup task failing**

**Symptom:** `daily_metrics_rollup` task fails or shows errors in `automation-metrics-scheduler` logs.

**Cause:** Hourly collection tasks did not complete successfully before rollup runs at 2:00 AM.

**Explanation:** The rollup task depends on hourly data being available. If hourly collectors (`collect_hourly_metrics`) fail or are delayed, the rollup cannot aggregate incomplete data.

**Solution:**

1. Verify hourly collection tasks completed successfully:

```
podman exec automation-metrics-web \
psql -h localhost -U metrics_service -d metrics_service -c \
"SELECT name, status, started, finished FROM dynamic_tasks_taskexecution
WHERE name LIKE 'collect_hourly_metrics%'
ORDER BY started DESC LIMIT 24;"
```
Expected output: All hourly tasks should show `status = 'success'` for the past 24 hours.

2. Check scheduler logs for task execution order:

```
podman logs automation-metrics-scheduler --tail 100 | grep -E "collect_hourly_metrics|daily_metrics_rollup"
```

3. If hourly tasks are failing, investigate root cause (database connectivity, controller database access, query timeouts).

4. After fixing hourly collection, manually trigger rollup:

```
podman exec automation-metrics-web metrics-service tasks create \
--name "manual-rollup" \
--function daily_metrics_rollup
```

**Scenario 2: cleanup_metrics_data running before rollup completes**

**Symptom:** Rollup produces incomplete results or missing data for recent periods.

**Cause:** Data cleanup task (`cleanup_metrics_data` at 4:00 AM) runs before rollup completes, purging hourly data that rollup still needs.

**Explanation:** This should not happen given the schedule (rollup at 2:00 AM, cleanup at 4:00 AM), but can occur if rollup is delayed or takes longer than 2 hours due to large data volumes.

**Solution:**

1. Check rollup task duration:

```
podman exec automation-metrics-web \
psql -h localhost -U metrics_service -d metrics_service -c \
"SELECT name, started, finished, (finished - started) AS duration
FROM dynamic_tasks_taskexecution
WHERE name = 'daily_metrics_rollup'
ORDER BY started DESC LIMIT 7;"
```

2. If rollup consistently takes >2 hours, adjust cleanup schedule by setting later execution time (contact Red Hat Support for guidance on modifying task schedules).

3. Verify data retention settings allow sufficient overlap:

```
podman exec automation-metrics-web env | grep RETENTION
```
Expected: Hourly data retained for 7 days (default), giving rollup sufficient time to process even if delayed.

**Scenario 3: Stuck task auto-detection and reset (NEW GA feature)**

**New in Ansible Automation Platform 2.7:** The scheduler automatically detects and resets tasks stuck in `running` state beyond their timeout.

**Feature behavior:**

- Scheduler periodically checks for tasks in `running` state longer than configured timeout
- Automatically resets stuck tasks to allow retry on next schedule
- Logs stuck task detection and reset actions in `automation-metrics-scheduler` container logs


**How to monitor automatic stuck task recovery:**

1. Check scheduler logs for stuck task detection:

```
podman logs automation-metrics-scheduler | grep -i "stuck\|timeout\|reset"
```
Expected output: Log messages indicating stuck task detection and automatic reset.

2. Query task execution history to see reset tasks:

```
podman exec automation-metrics-web \
psql -h localhost -U metrics_service -d metrics_service -c \
"SELECT name, status, started, finished
FROM dynamic_tasks_taskexecution
WHERE status = 'timeout' OR status = 'reset'
ORDER BY started DESC LIMIT 10;"
```

**When manual intervention is still needed:**

Automatic recovery handles transient issues (network timeouts, temporary database locks). Manual intervention is required when:

- Same task repeatedly gets stuck (indicates underlying infrastructure issue)
- Task execution observability metrics show declining success rates
- Database queries from metrics service are slow (check controller database performance)


**Scenario 4: Task execution observability**

**New in Ansible Automation Platform 2.7:** `collect_daily_metrics` task with `task_executions` service provides pipeline health metrics.

**Purpose:** Monitor the health and performance of the metrics collection pipeline itself (meta-metrics).

**What is collected:**

- Task success rates for all collectors (hourly, daily, rollup, anonymization)
- Task execution timing and duration
- Task error counts and types
- Collection throughput metrics


**How to access pipeline health metrics:**

1. Query task execution observability data:

```
podman exec automation-metrics-web \
psql -h localhost -U metrics_service -d metrics_service -c \
"SELECT * FROM task_executions ORDER BY collected_at DESC LIMIT 10;"
```

2. Identify declining success rates:

```
podman exec automation-metrics-web \
psql -h localhost -U metrics_service -d metrics_service -c \
"SELECT name,
COUNT(*) FILTER (WHERE status = 'success') AS success_count,
COUNT(*) FILTER (WHERE status = 'failure') AS failure_count,
ROUND(100.0 * COUNT(*) FILTER (WHERE status = 'success') / COUNT(*), 2) AS success_rate
FROM dynamic_tasks_taskexecution
WHERE started > NOW() - INTERVAL '7 days'
GROUP BY name
ORDER BY success_rate ASC;"
```
Expected: Success rates >95% for all tasks. Rates <90% indicate infrastructure issues requiring investigation.

3. Monitor task duration trends:

```
podman exec automation-metrics-web \
psql -h localhost -U metrics_service -d metrics_service -c \
"SELECT name,
AVG(EXTRACT(EPOCH FROM (finished - started))) AS avg_duration_seconds,
MAX(EXTRACT(EPOCH FROM (finished - started))) AS max_duration_seconds
FROM dynamic_tasks_taskexecution
WHERE started > NOW() - INTERVAL '7 days' AND status = 'success'
GROUP BY name
ORDER BY avg_duration_seconds DESC;"
```

Use pipeline health metrics to:

- Detect performance degradation early (increasing task durations)
- Identify which collectors are failing most frequently
- Validate infrastructure changes (e.g., database upgrades) haven't impacted collection
