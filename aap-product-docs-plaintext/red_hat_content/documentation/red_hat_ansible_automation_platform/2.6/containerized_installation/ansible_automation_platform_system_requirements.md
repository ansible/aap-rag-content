# 4. Preparing the containerized Ansible Automation Platform installation
## 4.2. System requirements
### 4.2.2. Ansible Automation Platform system requirements

Your system must meet the following minimum system requirements to install and run Red Hat Ansible Automation Platform.

**Table 4.1. System configuration**

| Type | Description | Notes |
| --- | --- | --- |
| <br>  Subscription | <br>  Valid Red Hat Ansible Automation Platform subscription   Valid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories) |  |
| <br>  Operating system | <br>  Red Hat Enterprise Linux 9.4 or later minor versions of Red Hat Enterprise Linux 9.   Red Hat Enterprise Linux 10 or later minor versions of Red Hat Enterprise Linux 10. |  |
| <br>  CPU architecture | <br>  x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
| <br> `ansible-core` | <br>  RHEL 9: `ansible-core` 2.14   RHEL 10: `ansible-core` 2.16 | <br>  Install `ansible-core` from the RHEL AppStream repository before running the installation program.   Ansible Automation Platform bundles `ansible-core` 2.16 separately for platform operation, including the control plane and built-in execution environments. |
| <br>  Browser | <br>  A currently supported version of Mozilla Firefox or Google Chrome. |  |
| <br>  Database | <br>  For Ansible Automation Platform managed databases: PostgreSQL 15.   For customer provided (external) databases: PostgreSQL 15, 16, or 17. | <br>  External (customer supported) databases require International Components for Unicode (ICU) support.   External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |
| <br>  IP version | <br>  IPv4, IPv6 (single-stack and dual-stack) |  |

Each virtual machine (VM) has the following system requirements:

**Table 4.2. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| <br>  RAM | <br>  16 GB   32 GB required for growth topology bundled installations with `hub_seed_collections=true`. Seeding the collections can take 45 or more minutes. |
| <br>  CPUs | <br>  4 |
| <br>  Local disk | <br>  Total available disk space: 60 GB   Installation directory: 15 GB (if on a dedicated partition) `/var/tmp` for online installations: 1 GB `/var/tmp` for offline or bundled installations: 3 GB   Temporary directory (defaults to `/tmp`) for offline or bundled installations: 10GB |
| <br>  Disk IOPS | <br>  3000 |

