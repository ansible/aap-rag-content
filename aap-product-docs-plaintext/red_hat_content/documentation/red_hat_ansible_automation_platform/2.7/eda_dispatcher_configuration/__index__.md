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

