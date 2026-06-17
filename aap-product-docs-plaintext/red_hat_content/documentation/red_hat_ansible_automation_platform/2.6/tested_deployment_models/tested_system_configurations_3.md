# 3. Operator topologies
## 3.1. Operator growth topology
### 3.1.2. Tested system configurations

Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:

**Table 3.2. Tested system configurations**

| Type | Description | Notes |
| --- | --- | --- |
| <br>  Subscription | <br>  Valid Red Hat Ansible Automation Platform subscription |  |
| <br>  Red Hat OpenShift | <br> `Version`: 4.14 `num_of_control_nodes`: 1 `num_of_worker_nodes`: 1 |  |
| <br>  Ansible-core | <br>  Ansible-core version 2.16 or later |  |
| <br>  Browser | <br>  A currently supported version of Mozilla Firefox or Google Chrome. |  |
| <br>  Database | <br>  For Ansible Automation Platform managed databases: PostgreSQL 15   For customer provided (external) databases: PostgreSQL 15, 16, or 17. | <br>  External (customer supported) databases require International Components for Unicode (ICU) support.   External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality depends on utilities provided with PostgreSQL 15.       Operator-deployed database connection and storage limits   <br>  The operator-deployed PostgreSQL database has a default `max_connections` limit of 100 and a maximum database size of 100 GB. <br>  Do not use the operator-deployed database if any of the following conditions apply:    <br>  You are running more than 1 replica of any component (platform gateway, automation controller, automation hub, or Event-Driven Ansible).   The automation controller capacity exceeds 100 concurrent jobs.   Total database connections from all components exceed 100.   Estimated 30-day database storage exceeds 100 GB. <br>  If your deployment exceeds any of these limits, use an external database instead of the operator-deployed database. <br>  Database storage consumption depends on your workload, including job frequency, playbook task count, output verbosity, and the number of managed hosts per job. Higher verbosity levels can increase storage consumption by 3-5x. |
| <br>  IP version | <br>  IPv4, IPv6 (single-stack and dual-stack) |  |

