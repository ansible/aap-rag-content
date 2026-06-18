# Background task processing for Event-Driven Ansible

In Ansible Automation Platform 2.7, Event-Driven Ansible controller uses `dispatcherd`, a PostgreSQL-based task broker, for all background task processing. Dispatcherd replaces the previous Redis-based task queue and uses the PostgreSQL pg_notify feature as its message transport.

This transition simplifies the platform architecture by eliminating Redis as an infrastructure dependency for Event-Driven Ansible controller.

`Dispatcherd` requires a connection to the same PostgreSQL instance used by the Event-Driven Ansible controller. A separate message broker, such as Redis, is no longer required.

## `Dispatcherd` worker types

`Dispatcherd` manages the following worker types to handle background operations:

- **Default worker:** Processes system tasks, including project imports, project synchronizations, analytics gathering, and resource synchronization.
- **Activation worker:** Processes rulebook activation tasks, such as container creation, process monitoring, heartbeat checks, and restart policy enforcement. In multi-node deployments, each node runs dedicated activation workers listening on node-specific queues (for example, `activation-node1`).

## Impact of service unavailability

If the task workers or the PostgreSQL database become unavailable, the following operations are disabled:

- Creating or syncing a project.
- Creating, enabling, or disabling an activation.
- Deleting or restarting an activation (unless using the **Force** option).

## Verifying worker status

To verify that the `dispatcherd` workers are active, you must run the following management command:

Bash

```
aap-eda-manage dispatcherctl alive
```
