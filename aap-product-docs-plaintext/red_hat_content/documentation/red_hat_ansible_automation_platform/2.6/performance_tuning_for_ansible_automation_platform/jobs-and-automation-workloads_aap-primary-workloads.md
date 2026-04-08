# 1. Types of workloads
## 1.3. Primary workloads for automation controller
### 1.3.2. Jobs and automation workloads




Jobs are the primary workload for automation controller and are run on the execution plane. They include the following job types:

- Standard jobs
- Workflow, sliced, and bulk jobs
- System jobs


#### 1.3.2.1. Standard jobs




Standard jobs involve the execution of an Ansible Playbook from a Project against a set of hosts from an Inventory. Jobs are initiated by a control node, which then streams, processes, and stores job results.

A performance sensitive part of this is the processing of the playbook output. The output is captured and serialized into job events by the automation controller. A single Ansible task running against a host typically produces multiple job events (for example: task start, host-specific details, and task completion).

Event volume varies significantly with the playbook’s configured verbosity level. For example, a simple debug task that prints `Hello World` on one host might produce 6 job events at verbosity 1, increasing to 34 job events at verbosity 3.

The dispatcher and the callback receiver collaborate to process, transmit, and store job events. These actions contribute to the platform’s storage and processing usage. Job events are processed on the control plane and stored in the database. The dispatcher processes job events, and the callback receiver stores them.

#### 1.3.2.2. Workflow, Sliced and Bulk jobs




To enable complex automation and orchestration, use the following job types to extend standard jobs:

- Sliced jobs: Split jobs to run against slices of the inventory in parallel
- Bulk jobs: Launch multiple jobs in a single request
- Workflow jobs: Coordinate multiple job templates


These job types coordinate the launch and management of multiple underlying standard jobs. They impact job scheduling, which occurs in the control plane, but otherwise do not have significant impact on their services.

#### 1.3.2.3. System jobs




System jobs involve internal maintenance tasks, such as clean up of old job event data. The execution frequency of system jobs is managed by schedules. System jobs run on the control plane, because they run management commands that interact with the database. These workloads involve key platform activities. Reducing the frequency of system jobs or increasing the number of days of data for jobs to retain can degrade database performance. In general, we recommend retaining as few days of data as possible and leveraging the external logging features for long term audit data storage. Storing more data in the database can make expensive queries that scan large tables more costly for the database.

