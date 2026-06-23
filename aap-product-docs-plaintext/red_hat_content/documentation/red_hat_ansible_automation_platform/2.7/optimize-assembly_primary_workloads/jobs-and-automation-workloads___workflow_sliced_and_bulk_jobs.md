# Understand primary workloads for automation controller
## Jobs and automation workloads
### Workflow, sliced and bulk jobs

To enable complex automation and orchestration, use the following job types to extend standard jobs:

- Sliced jobs: Split jobs to run against slices of the inventory in parallel
- Bulk jobs: Launch multiple jobs in a single request
- Workflow jobs: Coordinate multiple job templates


These job types coordinate the launch and management of multiple underlying standard jobs. They impact job scheduling, which occurs in the control plane, but otherwise do not have significant impact on their services.

