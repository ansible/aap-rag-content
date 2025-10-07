# 3. Operator topologies
## 3.1. Operator growth topology
### 3.1.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm140627607215296"></span>
**Table 3.2. Tested system configurations**

| Type | Description | Notes |
| --- | --- | --- |
| Subscription | Valid Red Hat Ansible Automation Platform subscription |  |
| Red Hat OpenShift | - Version: 4.14
- num_of_control_nodes: 1
- num_of_worker_nodes: 1 |  |
| Ansible-core | Ansible-core version 2.16 or later |  |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |  |
| Database | - For Ansible Automation Platform managed databases: PostgreSQL 15
- For customer provided (external) databases: PostgreSQL 15, 16, or 17. | - External (customer supported) databases require ICU support.
- External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |




