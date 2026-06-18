# Dispatcherd configuration

`Dispatcherd` uses PostgreSQL's pg_notify as its message transport to coordinate background task processing for Event-Driven Ansible controller. The following environment variables control how `dispatcherd` connects to PostgreSQL, identifies worker queues, and manages health checks.

For single-node deployments, the default values are sufficient and no additional configuration is required. `Dispatcherd` automatically connects to the same PostgreSQL instance used by Event-Driven Ansible controller.

For multi-node deployments, you must configure queue names to ensure that each node runs its own activation workers and that workloads are distributed across nodes. See the **Multi-node deployments** for details.

*Table 1. Dispatcherd environment variables*

| Variable                                    | Description                                                                                                                                                               | Default                         |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `EDA_PG_NOTIFY_DSN_SERVER`                  | The PostgreSQL connection string for the pg\_notify broker. Must point to the same PostgreSQL instance used by the Event-Driven Ansible controller.                       | Application database connection |
| `EDA_RULEBOOK_QUEUE_NAME`                   | The base queue name for the activation worker on the current node.                                                                                                        | `activation`                    |
| `EDA_RULEBOOK_WORKER_QUEUES`                | A comma-separated list of all activation worker queue names across the deployment. Required for multi-node deployments (for example, activation-node1, activation-node2). | Empty (single-node)             |
| `EDA_DISPATCHERD_QUEUE_HEALTHCHECK_TIMEOUT` | The amount of time, in seconds, to wait when checking worker health.                                                                                                      | `3`                             |

## Worker services

Each Event-Driven Ansible controller deployment requires at least one default worker and one activation worker. Use the following commands to initialize these services:

```
aap-eda-manage dispatcherd --worker-class DefaultWorker
aap-eda-manage dispatcherd --worker-class ActivationWorker
```

## Multi-node deployments

In multi-node deployments, each node runs its own activation workers with a unique queue name. You must set `EDA_RULEBOOK_QUEUE_NAME` to a node-specific value on each node and set `EDA_RULEBOOK_WORKER_QUEUES` to the full list of all node queue names across the deployment. This ensures the Event-Driven Ansible controller can distribute activation workloads and route operations to the correct node.

## Deprecated Redis variables

The following Redis-related variables are no longer used by the Event-Driven Ansible controller in Ansible Automation Platform 2.7. You can safely remove these from your inventory files:

- `EDA_MQ_HOST`
- `EDA_MQ_PORT`
- `EDA_MQ_USER`
- `EDA_MQ_USER_PASSWORD`
- `EDA_MQ_CLIENT_CERT_PATH`
- `EDA_MQ_CLIENT_KEY_PATH`
- `EDA_MQ_CLIENT_CACERT_PATH`
