# 4. RPM topologies
## 4.1. RPM growth topology
### 4.1.2. Tested system configurations

Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:

**Table 4.3. Tested system configurations**

| Type | Description |  |
| --- | --- | --- |
| <br>  Subscription | <br>  Valid Red Hat Ansible Automation Platform subscription |  |
| <br>  Operating system | <br>  Red Hat Enterprise Linux 9.4 or later minor versions of Red Hat Enterprise Linux 9. |  |
| <br>  CPU architecture | <br>  x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
| <br> `ansible-core` | <br> `ansible-core` version 2.16 or later | <br>  Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments. |
| <br>  Browser | <br>  A currently supported version of Mozilla Firefox or Google Chrome |  |
| <br>  Database | <br>  For Ansible Automation Platform managed databases: PostgreSQL 15   For customer provided (external) databases: PostgreSQL 15, 16, or 17. | <br>  External (customer supported) databases require International Components for Unicode (ICU) support.   External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |
| <br>  IP version | <br>  IPv4, IPv6 (single-stack and dual-stack) |  |

