# 4. RPM topologies
## 4.1. RPM growth topology
### 4.1.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm140627605006512"></span>
**Table 4.3. Tested system configurations**

| Type | Description |  |
| --- | --- | --- |
| Subscription | Valid Red Hat Ansible Automation Platform subscription |  |
| Operating system | Red Hat Enterprise Linux 9.4 or later minor versions of Red Hat Enterprise Linux 9. |  |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  `ansible-core` |  `ansible-core` version 2.16 or later | Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments. |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome |  |
| Database | - For Ansible Automation Platform managed databases: PostgreSQL 15
- For customer provided (external) databases: PostgreSQL 15, 16, or 17. | - External (customer supported) databases require ICU support.
- External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |




