# Troubleshoot metrics service
## Cannot disable events collector individually

**Symptom**: You want to disable only the events collector without disabling other metrics collection.

**Cause**: There is no dedicated feature flag for the events collector. It runs as part of the `METRICS_COLLECTION` task group.

**Workaround**: Set both `JOBEVENT_ROW_LIMIT` and `JOBEVENT_JOB_LIMIT` to `1`. This effectively disables event collection by limiting processing to a negligible amount, while leaving all other metrics collection active.
