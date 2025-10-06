# 2. RPM topologies
## 2.2. RPM enterprise topology
### 2.2.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm139984997451600"></span>
**Table 2.7. Tested system configurations**

| Type | Description |  |
| --- | --- | --- |
| Subscription | Valid Red Hat Ansible Automation Platform subscription |  |
| Operating system | - Red Hat Enterprise Linux 8.8 or later minor versions of Red Hat Enterprise Linux 8.
- Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9. |  |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  `ansible-core` |  `ansible-core` version 2.16 or later | Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments. |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome |  |
| Database | PostgreSQL 15 | External (customer supported) databases require ICU support. |




