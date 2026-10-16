# Overview
## Expected behavior during upgrade

During an operator upgrade, expect the following behavior:

- **Brief service interruptions** occur as component pods restart. The duration depends on the size of your deployment and the number of components being upgraded.
- **Component pods restart in sequence**, not all at once. You may see a mix of old and new pods running during the rollout.
- **Running jobs in automation controller** may be interrupted if a controller pod restarts during execution. Schedule upgrades during a maintenance window to avoid disruption to active automation.
- **Database migrations** run automatically as part of the component startup process. For large databases, this can extend the time before a component becomes fully available.
- **Custom resource status** fields update throughout the process. The upgrade is complete when all CRs report a healthy status and all pods show a `Running` or `Completed` state.

