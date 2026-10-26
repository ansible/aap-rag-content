# Troubleshoot metrics service
## Partial event data collection

**Symptom**: Collection/module usage statistics appear incomplete or show fewer entries than expected.

**Cause**: When `JOBEVENT_ROW_LIMIT`, `JOBEVENT_JOB_LIMIT`, or built-in time-budget cap is reached, the collector stops processing and marks the collection as partial. The `HourlyMetricsCollection` record is stored with whatever data was collected. Uncollected events from that cycle are skipped permanently - partial collections are NOT retried for the same time window. The next hourly run collects events only from jobs that finished during the new hourly window.

**Resolution**: If more complete per-cycle collection is required, increase the limit values. Partial collections are included in the daily rollup with whatever data was collected, so no data gaps occur in the daily summary - but per-cycle granularity may be reduced.

