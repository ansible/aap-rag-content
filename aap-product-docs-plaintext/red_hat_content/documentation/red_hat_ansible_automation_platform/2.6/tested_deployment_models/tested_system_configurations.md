# 2. Container topologies
## 2.1. Container growth topology
### 2.1.2. Tested system configurations




Red Hat has tested these configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm140264429779536"></span>
**Table 2.3. System configuration**

| Type | Description | Notes |
| --- | --- | --- |
| Subscription | - Valid Red Hat Ansible Automation Platform subscription
- Valid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories) |  |
| Operating system | - Red Hat Enterprise Linux 9.4 or later minor versions of Red Hat Enterprise Linux 9.
- Red Hat Enterprise Linux 10 or later minor versions of Red Hat Enterprise Linux 10. |  |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  `ansible-core` | - RHEL 9: `    ansible-core` 2.14
- RHEL 10: `    ansible-core` 2.16 | - Install `    ansible-core` from the RHEL AppStream repository before running the installation program.
- Ansible Automation Platform bundles `    ansible-core` 2.16 separately for platform operation, including the control plane and built-in execution environments. |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |  |
| Database | - For Ansible Automation Platform managed databases: PostgreSQL 15.
- For customer provided (external) databases: PostgreSQL 15, 16, or 17. | - External (customer supported) databases require International Components for Unicode (ICU) support.
- External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |
| IP version | IPv4, IPv6 (single-stack and dual-stack) |  |




