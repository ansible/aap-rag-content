# 3. Container topologies
## 3.1. Container growth topology
### 3.1.2. Tested system configurations




Red Hat has tested the following configurations to install and run Red Hat Ansible Automation Platform:


<span id="idm139849916191872"></span>
**Table 3.3. System configuration**

| Type | Description | Notes |
| --- | --- | --- |
| Subscription | - Valid Red Hat Ansible Automation Platform subscription
- Valid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories) |  |
| Operating system | - Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9.
- Red Hat Enterprise Linux 10 or later minor versions of Red Hat Enterprise Linux 10 for enterprise topologies. |  |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  `ansible-core` | - For the installation: `    ansible-core` version 2.14.
- For Ansible Automation Platform operation: `    ansible-core` version 2.16. | - The installation program uses the `    ansible-core` 2.14 package from the RHEL 9 AppStream repository.
- Ansible Automation Platform bundles `    ansible-core` version 2.16 for its operation, so you do not need to install it manually. |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |  |
| Database | PostgreSQL 15 | External (customer supported) databases require ICU support. |




